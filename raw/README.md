# 原始資料（raw/）

LLM Wiki 的原始資料層：6 篇論文，全部來自 arXiv。

因著作權考量，**PDF 與轉出的全文不上傳到 GitHub**。執行下面的指令即可重新下載並轉成文字檔（需要 `curl` 與 `pdftotext`）：

```bash
bash scripts/fetch_raw.sh
```

| 檔名 | 論文 | arXiv |
|---|---|---|
| `bahdanau-2014` | Neural Machine Translation by Jointly Learning to Align and Translate | https://arxiv.org/abs/1409.0473 |
| `vaswani-2017` | Attention Is All You Need | https://arxiv.org/abs/1706.03762 |
| `devlin-2018` | BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding | https://arxiv.org/abs/1810.04805 |
| `raffel-2019` | Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer | https://arxiv.org/abs/1910.10683 |
| `brown-2020` | Language Models are Few-Shot Learners | https://arxiv.org/abs/2005.14165 |
| `dosovitskiy-2020` | An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale | https://arxiv.org/abs/2010.11929 |

轉檔方式：單欄論文（bahdanau、vaswani）用 `pdftotext -layout`；雙欄論文用 `pdftotext`（依閱讀順序），原因見 `wiki/log.md` 論文 3 的 N1 紀錄。
