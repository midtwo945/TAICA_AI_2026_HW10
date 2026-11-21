#!/usr/bin/env bash
# N1 取得資料：重新下載 6 篇論文並轉成文字檔（raw/ 不上傳 GitHub）
set -euo pipefail
cd "$(dirname "$0")/../raw"
while read -r name id layout; do
  curl -sSL -A "Mozilla/5.0" -o "$name.pdf" "https://arxiv.org/pdf/$id"
  if [ "$layout" = "layout" ]; then pdftotext -layout "$name.pdf" "$name.txt"; else pdftotext "$name.pdf" "$name.txt"; fi
  echo "$name: $(wc -w < "$name.txt") words"
done <<'LIST'
bahdanau-2014 1409.0473 layout
vaswani-2017 1706.03762 layout
devlin-2018 1810.04805 reading
raffel-2019 1910.10683 reading
brown-2020 2005.14165 reading
dosovitskiy-2020 2010.11929 reading
LIST
