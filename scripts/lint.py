"""N4 Lint 檢查：自動檢查 Wiki 是否符合 CLAUDE.md 的 R3、R4、R5、R18。

R6（矛盾要標出）無法自動判斷，由 AI 在 N4 人工檢查並寫進 log。

用法：python scripts/lint.py
結束碼：0 = 全部通過，1 = 有不通過項目
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
PAGE_DIRS = ["papers", "concepts", "models"]
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
CITE = "〔出處"


def pages():
    for d in PAGE_DIRS:
        yield from sorted((WIKI / d).glob("*.md"))


def rel(p):
    return p.relative_to(WIKI).as_posix()


def blocks(text):
    """把頁面切成區塊：('code', 行) 或 ('text', 行)。空行分隔區塊，code fence 整段視為一塊。"""
    out, cur, in_code = [], [], False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            if in_code:
                cur.append(line)
                out.append(("code", cur))
                cur, in_code = [], False
            else:
                if cur:
                    out.append(("text", cur))
                cur, in_code = [line], True
            continue
        if in_code:
            cur.append(line)
        elif line.strip() == "":
            if cur:
                out.append(("text", cur))
            cur = []
        else:
            cur.append(line)
    if cur:
        out.append(("code" if in_code else "text", cur))
    return out


def is_list(lines):
    return all(re.match(r"\s*([-*]|\d+\.)\s", l) or l.startswith("  ") for l in lines)


def check_r3(path, text):
    """R3：每個段落都標註出處。
    例外：標題、頁首 blockquote、code block；
    緊接在「有出處的段落」後面的清單或 code 視為該段落的延伸。"""
    errs = []
    prev_cited = False
    for kind, lines in blocks(text):
        joined = "\n".join(lines)
        if kind == "code":
            continue  # code 不影響 prev_cited，讓後面的變數說明清單仍可沿用前段出處
        if lines[0].startswith("#") and len(lines) == 1:
            prev_cited = False
            continue
        if lines[0].startswith(">"):
            continue
        if CITE in joined:
            prev_cited = True
            continue
        if is_list(lines) and prev_cited:
            continue
        errs.append(f"R3 段落缺少出處：{rel(path)}「{lines[0][:30]}…」")
        prev_cited = False
    return errs


def check_r18(path, text):
    lines = [l for l in text.splitlines() if l.strip()]
    if len(lines) < 2 or not lines[0].startswith("# ") or not lines[1].startswith(">"):
        return [f"R18 頁首格式錯誤（第一行要是標題、第二行要是 blockquote）：{rel(path)}"]
    missing = [k for k in ("**類型**", "**出處**", "**相關**") if k not in lines[1]]
    return [f"R18 頁首缺少 {'、'.join(missing)}：{rel(path)}"] if missing else []


def links(path, text):
    for target in LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        yield target, (path.parent / target.split("#")[0]).resolve()


def main():
    errs, warns = [], []
    all_pages = list(pages())
    inbound = {p.resolve(): set() for p in all_pages}

    for p in all_pages:
        text = p.read_text(encoding="utf-8")
        errs += check_r18(p, text)
        errs += check_r3(p, text)
        for target, dest in links(p, text):
            if not dest.exists():
                errs.append(f"R4 失效連結：{rel(p)} → {target}")
            elif dest in inbound and dest != p.resolve():
                inbound[dest].add(rel(p))

    # R4 也檢查 index.md
    index = WIKI / "index.md"
    index_text = index.read_text(encoding="utf-8")
    listed = set()
    for target, dest in links(index, index_text):
        if not dest.exists():
            errs.append(f"R4 失效連結：index.md → {target}")
        listed.add(dest)

    for p in all_pages:
        if not inbound[p.resolve()]:
            errs.append(f"R5 孤兒頁面（沒有其他頁面連到它）：{rel(p)}")
        if p.resolve() not in listed:
            warns.append(f"提醒：index.md 沒有列出 {rel(p)}")

    print(f"檢查 {len(all_pages)} 個頁面")
    for e in errs:
        print("❌", e)
    for w in warns:
        print("⚠️", w)
    print("R6（矛盾標註）需人工檢查")
    print("✅ 全部通過" if not errs else f"❌ {len(errs)} 項不通過")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
