"""N7 內容檢查：自動檢查 slides/content.md 是否符合 R11、R12 中可機械判斷的部分。

R11-a：每個要點標註的〈來源〉，必須是該頁「Wiki：」清單裡的頁面（只能用大綱指定的頁面）
R11-b：每個要點裡的數字，都必須出現在該頁指定的 Wiki 頁面中（抓「數字寫錯／自己編」）
R12  ：TERMS 清單中的術語，第一次出現的那一頁必須以 **粗體** 標出（表示有解釋），
       或已在更早的頁面解釋過；JARGON 清單中的詞第一次出現時，必須在同一行附上解釋（括號或冒號）

論點的「意思」是否和 Wiki 一致，無法自動判斷，由 AI 逐頁人工比對並寫進 checks/slides.md。

用法：python scripts/check_slides.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "slides" / "content.md"
WIKI = ROOT / "wiki"

# 必須在第一次出現時解釋的核心術語
TERMS = ["Token", "Embedding", "Softmax", "RNN", "Encoder-Decoder", "Attention", "軟對齊",
         "Transformer", "Self-Attention", "Query", "Key", "Value", "遮罩", "Multi-Head Attention",
         "Positional Encoding", "殘差連接", "LayerNorm", "全可見", "因果", "BERT", "預訓練 → 微調",
         "Masked Language Model", "GPT-3", "自迴歸語言模型", "In-context Learning", "Text-to-Text",
         "T5", "ViT", "patch", "歸納偏置"]
# 出現時必須在同一行附上解釋的專有名詞（評估指標、資料集、架構縮寫等）
JARGON = ["BLEU", "GLUE", "CNN", "FFN", "d_model", "d_ff", "O(1)", "O(n)", "梯度", "NLP", "子詞"]

SLIDE_RE = re.compile(r"^## (\d+)｜(.+)$")
TAG_RE = re.compile(r"〈([^〉]+)〉")
NUM_RE = re.compile(r"(?<![\w.])(\d[\d,]*(?:\.\d+)?)")


def page_path(name):
    name = name.strip()
    if name == "index":
        return WIKI / "index.md"
    return WIKI / f"{name}.md"


def norm(s):
    return s.replace(",", "").replace("，", "")


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


def main():
    errs = []
    slides = parse()
    explained = set()
    for s in slides:
        pages = [page_path(w) for w in s["wiki"]]
        for p in pages:
            if not p.exists():
                errs.append(f"第 {s['n']} 頁：Wiki 清單中的頁面不存在 {p.name}")
        short = {w.split("/")[-1] for w in s["wiki"]}
        wiki_text = norm("\n".join(p.read_text(encoding="utf-8") for p in pages if p.exists()))

        for line in s["lines"]:
            # R11-a：〈來源〉必須在清單內（「第 N 頁」是頁面互相參照，不算）
            for tag in TAG_RE.findall(line):
                for t in re.split(r"[、,]", tag):
                    t = t.strip()
                    if t and not t.startswith("第") and t not in short:
                        errs.append(f"R11 第 {s['n']} 頁：來源〈{t}〉不在本頁的 Wiki 清單 {sorted(short)} 中")
            # R11-b：數字必須出現在本頁 Wiki 中
            body = TAG_RE.sub("", line)
            body = re.sub(r"^\s*(\d+\.|[-|])\s*", "", body)  # 去掉清單編號
            for num in NUM_RE.findall(body):
                n = norm(num)
                if len(n.replace(".", "")) <= 1:
                    continue  # 單一位數（例如 1 個頭、Q1）太常見，不檢查
                if n not in wiki_text:
                    errs.append(f"R11 第 {s['n']} 頁：數字 {num} 在本頁的 Wiki 頁面中找不到")

        text = "\n".join(s["lines"])
        # R12：核心術語
        for term in TERMS:
            if term in explained:
                continue
            if f"**{term}**" in text or f"**{term}（" in text:
                explained.add(term)
            elif re.search(re.escape(term), text):
                errs.append(f"R12 第 {s['n']} 頁：「{term}」第一次出現，但沒有以粗體解釋")
                explained.add(term)  # 只報一次
        # R12：專有名詞第一次出現時，必須在同一行附上解釋
        for line in s["lines"]:
            for j in JARGON:
                if j in line and j not in explained:
                    explained.add(j)
                    after = line.split(j, 1)[1]
                    if not re.match(r"\s*[（(：:]", after):
                        errs.append(f"R12 第 {s['n']} 頁：「{j}」第一次出現，沒有在同一行附上解釋")

    print(f"檢查 {len(slides)} 頁")
    for e in errs:
        print("❌", e)
    print("✅ R11、R12（自動部分）通過" if not errs else f"❌ {len(errs)} 項不通過")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
