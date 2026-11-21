# LLM Wiki 規則（Schema）

主題：**Transformer 論文與其應用變化**
本檔是 AI 維護 Wiki 時必須遵守的規則。所有規則由使用者設計，AI 不確定時必須先問使用者，不得自行決定。

## 資料夾

| 路徑 | 用途 |
|---|---|
| `raw/` | 原始論文（PDF 與轉出的文字檔），只讀不改；不上傳 GitHub，用 `scripts/fetch_raw.sh` 重新下載 |
| `wiki/index.md` | 所有 Wiki 頁面的目錄，每頁一行摘要 |
| `wiki/checks/` | N3.5 原文比對紀錄，每篇論文一個檔案 |
| `wiki/log.md` | 每個節點每次執行的紀錄（通過／不通過、原因） |
| `wiki/papers/` | 論文頁：每篇論文一頁 |
| `wiki/concepts/` | 概念頁：例如 Attention、Positional Encoding |
| `wiki/models/` | 模型頁：例如 Transformer、BERT、GPT-3 |
| `slides/` | 教學 HTML 簡報 |
| `docs/` | Graph 設計說明、反思 |

## 論文清單

| # | 論文 | 狀態 |
|---|---|---|
| 1 | Bahdanau et al. 2014, Neural Machine Translation by Jointly Learning to Align and Translate | 必收 |
| 2 | Vaswani et al. 2017, Attention Is All You Need | 必收 |
| 3 | Devlin et al. 2018, BERT | 必收 |
| 4 | Brown et al. 2020, Language Models are Few-Shot Learners (GPT-3) | 必收 |
| 5 | Raffel et al. 2019, T5 | 必收 |
| 6 | Dosovitskiy et al. 2020, ViT | 收錄（使用者授權 AI 決定，2026-11-21） |

長篇論文只 ingest 架構與核心概念章節，實驗細節跳過。

## Graph

```
【階段一：建 Wiki】每篇論文跑一次
 N1 取得資料 → N2 討論 → N3 寫入 Wiki → N3.5 原文比對 → N4 Lint 檢查 → 還有論文？是 → N1；否 → 階段二
【階段二：做簡報】
 N5 規劃大綱 → N6 產生內容 → N7 內容檢查 → N8 產生 HTML → N9 瀏覽檢查 → N10 發布
 N7 發現 Wiki 缺少知識 → 回到 N3 補寫 Wiki
```

## 檢查規則

### 階段一
- **R1**（N1）連結有效，而且能讀到全文。不通過：改找 arXiv 其他版本，仍失敗就問使用者。
- **R2**（N2）AI 提出「重點、要新增／更新的頁面、與現有 Wiki 的衝突」，由使用者確認同意後才能進 N3。不同意：依意見修改，回到 N2。
- **R20**（N3.5，2026-11-21 使用者核准新增）這次新增或修改的每個段落，都要回原文找到對應的句子，記下「段落 → 原文句子」的對照（存在 `wiki/checks/<論文>.md`，log 中附連結）。找不到對應句子的內容要刪掉或改寫。不通過：回到 N3 修正。
- **R3**（N4）每個段落都標註出處。標題、頁首、code block 除外；緊接在有出處段落後面的清單視為該段落的延伸。
- **R4**（N4）沒有失效的連結。
- **R5**（N4）沒有孤兒頁面（至少有一個頁面連到它；index.md 不算）。
- **R6**（N4）與舊頁面矛盾時要明確標出，不得直接覆蓋。
- N4 的 R3、R4、R5、R18 由 `scripts/lint.py` 自動檢查；R6 由 AI 人工檢查。
- N4 不通過：回到 N3 修正，最多重試 2 次，仍失敗就問使用者。

### 階段二
- **R7**（N5）每頁簡報至少對應 1 個 Wiki 頁面。
- **R8**（N5）清單中所有收錄的論文都有用到。
- **R9**（N5）先備概念排在前面。
- **R10**（N5）大綱由使用者確認。
- **R11**（N7）每個論點都能在 Wiki 裡找到。
- **R12**（N7）專有名詞第一次出現時有解釋。
- N7 不通過：內容寫錯 → 回到 N6（最多 2 次）；Wiki 沒有這個知識 → 回到 N3 補寫 Wiki，不准直接寫進簡報。
- **R13**（N9）能正常翻頁。
- **R14**（N9）文字沒有超出畫面。
- **R15**（N9）手機也能看。
- N9 不通過：回到 N8 修正。
- **R16**（N10）推送到 GitHub 前要經過使用者同意。

## Wiki 頁面規則
- **R17** 頁面分三類：論文頁、概念頁、模型頁。
- **R18** 每頁開頭固定標註：類型、出處論文、相關頁面。格式：

  ```markdown
  # 頁面標題

  > **類型**：概念 ｜ **出處**：[Bahdanau 2014](../papers/bahdanau-2014.md) ｜ **相關**：[Attention](attention.md)
  ```
- **R19** 頁面之間使用一般的相對路徑 Markdown 連結（可在 GitHub 上點擊）。
- 段落出處標註格式：段落結尾加 `〔出處：[Bahdanau 2014 §3](../papers/bahdanau-2014.md)〕`。
- 論文頁的出處標註指向原文：`〔出處：§3.1，[原文](https://arxiv.org/abs/1409.0473)〕`（2026-11-21 使用者決定：原文 PDF 不公開上傳，連結改指 arXiv）。
- 檔名使用小寫英文加連字號，例如 `self-attention.md`。

## log.md 格式

每次節點執行追加一筆：

```markdown
### [日期 時間] N4 Lint 檢查｜論文 1｜❌ 不通過（第 1 次）
- R5：`concepts/rnn.md` 是孤兒頁面
- 處理：回到 N3，在 `models/rnn-encoder-decoder.md` 加上連結
```
