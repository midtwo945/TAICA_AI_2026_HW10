"""N5 大綱檢查：自動檢查 slides/outline.md 是否符合 R7、R8。

R7：每頁簡報至少對應 1 個 Wiki 頁面（連結必須存在）
R8：清單中所有收錄的論文都有用到
（R9 先備順序、R10 使用者確認，由人工檢查）

用法：python scripts/check_outline.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTLINE = ROOT / "slides" / "outline.md"
PAPERS = sorted(p.name for p in (ROOT / "wiki" / "papers").glob("*.md"))
ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")


def main():
    errs = []
    used_papers = set()
    used_pages = set()
    slides = 0
    for line in OUTLINE.read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        slides += 1
        n = m.group(1)
        wiki_cell = line.rstrip("|").split("|")[-1]
        targets = LINK_RE.findall(wiki_cell)
        if not targets:
            errs.append(f"R7 第 {n} 頁沒有對應的 Wiki 頁面")
        for t in targets:
            dest = (OUTLINE.parent / t).resolve()
            if not dest.exists():
                errs.append(f"R7 第 {n} 頁的連結不存在：{t}")
                continue
            used_pages.add(dest)
            if dest.parent.name == "papers":
                used_papers.add(dest.name)

    for p in PAPERS:
        if p not in used_papers:
            errs.append(f"R8 論文沒有被任何一頁使用：{p}")

    all_pages = {p.resolve() for d in ("papers", "concepts", "models") for p in (ROOT / "wiki" / d).glob("*.md")}
    unused = sorted(p.relative_to(ROOT / "wiki").as_posix() for p in all_pages - used_pages)

    print(f"大綱共 {slides} 頁；使用 {len(used_pages & all_pages)}／{len(all_pages)} 個 Wiki 頁面")
    print(f"論文使用：{len(used_papers)}／{len(PAPERS)}")
    for e in errs:
        print("❌", e)
    for u in unused:
        print("⚠️ 提醒：大綱沒有用到", u)
    print("✅ R7、R8 通過" if not errs else f"❌ {len(errs)} 項不通過")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
