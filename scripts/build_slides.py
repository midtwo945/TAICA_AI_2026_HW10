"""N8 產生 HTML：把 slides/content.md 機械式轉成 slides/index.html。

設計理由：N8 不讓 AI 重新撰寫內容，只做格式轉換，
所以 HTML 不會出現 N7 沒檢查過的文字（內容只有 content.md 一個來源）。

- 每頁底部自動列出該頁的 Wiki 來源，連到 GitHub 上的 Wiki 頁面
- 第 8 頁的遮罩 demo 數字，直接從 content.md 的 demo 要點解析出來
- 第 18 頁的論文連結，從 wiki/papers/*.md 頁首的 arXiv 連結讀取

用法：python scripts/build_slides.py
"""

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "slides" / "content.md"
OUT = ROOT / "slides" / "index.html"
REPO = "https://github.com/midtwo945/TAICA_AI_2026_HW10/blob/main/"

SLIDE_RE = re.compile(r"^## (\d+)｜(.+)$")
TAG_RE = re.compile(r"\s*〈[^〉]+〉")

SECTIONS = {1: "開場", 3: "先備知識", 5: "Attention 的誕生", 7: "Transformer",
            11: "應用變化", 16: "總結"}


def inline(s):
    s = html.escape(TAG_RE.sub("", s), quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    return s


def page_title(path):
    first = path.read_text(encoding="utf-8").splitlines()[0]
    return first.lstrip("# ").split("（")[0].split("：")[0].strip()


def wiki_links(names):
    out = []
    for n in names:
        p = ROOT / "wiki" / ("index.md" if n == "index" else f"{n}.md")
        label = "Wiki 目錄" if n == "index" else page_title(p)
        out.append(f'<a href="{REPO}wiki/{"index" if n == "index" else n}.md" target="_blank" rel="noopener">{html.escape(label)}</a>')
    return "、".join(out)


def paper_refs():
    items = []
    for p in sorted((ROOT / "wiki" / "papers").glob("*.md")):
        text = p.read_text(encoding="utf-8")
        title = text.splitlines()[0].lstrip("# ")
        m = re.search(r"\[(arXiv:[^\]]+)\]\((https://arxiv\.org/abs/[^)]+)\)", text)
        items.append((title, m.group(1), m.group(2)) if m else (title, "", ""))
    order = ["bahdanau", "vaswani", "devlin", "raffel", "brown", "dosovitskiy"]
    items.sort(key=lambda x: next(i for i, k in enumerate(order) if k in x[0].lower()))
    return "".join(
        f'<li><a href="{u}" target="_blank" rel="noopener">{html.escape(t)}</a> <span class="muted">{a}</span></li>'
        for t, a, u in items)


def parse():
    slides, cur = [], None
    for line in CONTENT.read_text(encoding="utf-8").splitlines():
        m = SLIDE_RE.match(line)
        if m:
            cur = {"n": int(m.group(1)), "title": m.group(2), "wiki": [], "lines": []}
            slides.append(cur)
        elif cur and line.startswith("Wiki："):
            cur["wiki"] = [w.strip() for w in line[5:].split("、")]
        elif cur and line.strip() and not line.startswith("---"):
            cur["lines"].append(line)
    return slides


def demo_widget(lines):
    """從 demo 的兩行要點解析權重：『無遮罩：字 1 `[..]`；…』『有遮罩：…』"""
    data = {}
    for l in lines:
        key = "off" if "無遮罩" in l else "on"
        data[key] = [[float(x) for x in g.split(",")] for g in re.findall(r"`\[([^\]]+)\]`", l)]
    rows = []
    for mode in ("off", "on"):
        trs = []
        for i, w in enumerate(data[mode]):
            cells = "".join(
                f'<td style="--w:{v}"><span>{v:g}</span></td>' for v in w)
            trs.append(f"<tr><th>字 {i + 1}</th>{cells}</tr>")
        rows.append(f'<tbody data-mode="{mode}"{" hidden" if mode == "on" else ""}>{"".join(trs)}</tbody>')
    return f'''<div class="demo">
  <div class="demo-head">
    <span>每一列：這個字對各個字的 attention 權重（每列加總為 1）</span>
    <label class="switch"><input type="checkbox" id="maskToggle"><span>加上遮罩</span></label>
  </div>
  <table class="heat"><thead><tr><th></th><th>看字 1</th><th>看字 2</th><th>看字 3</th></tr></thead>{"".join(rows)}</table>
  <p class="muted small">簡化版：Q = K = V = 每個字的向量，d_k = 2。數字由 Python 計算，取自 Wiki。</p>
</div>'''


def render_body(s):
    lines = s["lines"]
    out, i = [], 0
    subtitle = ""
    while i < len(lines):
        l = lines[i]
        if l.startswith("- 副標："):
            subtitle = inline(l[5:])
            i += 1
            continue
        if l.startswith("- 互動 demo"):
            j = i + 1
            sub = []
            while j < len(lines) and lines[j].startswith("  "):
                sub.append(lines[j]); j += 1
            out.append(("li", inline(l[2:].split("：")[0] + "：切換有／無遮罩，看權重怎麼變"), demo_widget(sub)))
            i = j
            continue
        if l.startswith("- "):
            text = inline(l[2:])
            j = i + 1
            sub, table = [], []
            while j < len(lines) and lines[j].startswith("  "):
                sl = lines[j].strip()
                if sl.startswith("|"):
                    table.append(sl)
                elif sl:
                    sub.append(sl)
                j += 1
            extra = ""
            if sub:
                ordered = all(re.match(r"\d+\.", x) for x in sub)
                tag = "ol" if ordered else "ul"
                items = "".join(f"<li>{inline(re.sub(r'^(\d+\.|-)\s*', '', x))}</li>" for x in sub)
                extra += f"<{tag}>{items}</{tag}>"
            if table:
                rows = [r for r in table if not re.match(r"^\|[-| ]+\|$", r)]
                head = [c.strip() for c in rows[0].strip("|").split("|")]
                body = [[c.strip() for c in r.strip("|").split("|")] for r in rows[1:]]
                extra += "<table class=\"cmp\"><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
                extra += "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body) + "</tbody></table>"
            out.append(("li", text, extra))
            i = j
            continue
        i += 1
    return subtitle, out


def render_slide(s, total):
    subtitle, items = render_body(s)
    n = s["n"]
    if n == 1:
        lis = "".join(f"<li>{t}{x}</li>" for _, t, x in items)
        body = f'<p class="subtitle">{subtitle}</p><ul class="timeline-list">{lis}</ul>'
        cls = "title-slide"
    elif n == 18:
        qs, rest = [], []
        for _, t, x in items:
            if t.startswith("Q"):
                q, a = t.split("→", 1)
                qs.append(f"<details><summary>{q.strip()}</summary><p>{a.strip()}</p></details>")
            else:
                rest.append(t)
        body = ('<div class="quiz">' + "".join(qs) + '</div><h3>參考資料</h3><ol class="refs">'
                + paper_refs() + f'<li><a href="{REPO}wiki/index.md" target="_blank" rel="noopener">本主題的 LLM Wiki（28 頁）</a></li></ol>')
        cls = ""
    elif any('class="demo"' in x for _, _, x in items):
        # 有互動 demo 的頁面：左邊說明、右邊 demo，避免超出畫面（N9 第 1 次的修正）
        demo = next(x for _, _, x in items if 'class="demo"' in x)
        lis = "".join(f"<li>{t}</li>" if 'class="demo"' in x else f"<li>{t}{x}</li>" for _, t, x in items)
        body = f'<div class="two-col"><ul>{lis}</ul>{demo}</div>'
        cls = ""
    else:
        body = "<ul>" + "".join(f"<li>{t}{x}</li>" for _, t, x in items) + "</ul>"
        cls = ""
    section = next((v for k, v in sorted(SECTIONS.items(), reverse=True) if n >= k), "")
    return f'''<section class="slide {cls}" id="s{n}" aria-label="第 {n} 頁">
  <header><span class="kicker">{section}</span><span class="num">{n} / {total}</span></header>
  <h2>{inline(s["title"])}</h2>
  <div class="body">{body}</div>
  <footer class="src">📖 Wiki：{wiki_links(s["wiki"])}</footer>
</section>'''


TEMPLATE = (ROOT / "scripts" / "slides_template.html").read_text(encoding="utf-8")


def main():
    slides = parse()
    html_slides = "\n".join(render_slide(s, len(slides)) for s in slides)
    OUT.write_text(TEMPLATE.replace("<!--SLIDES-->", html_slides), encoding="utf-8")
    print(f"已產生 {OUT.relative_to(ROOT)}：{len(slides)} 頁")


if __name__ == "__main__":
    main()
