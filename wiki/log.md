# 執行紀錄（log）

每個節點每次執行都追加一筆紀錄。規則見 [CLAUDE.md](../CLAUDE.md)。

---

### [2026-11-21] 初始化
- 建立資料夾結構與規則檔 CLAUDE.md（R1～R19，由使用者確認草稿 B 版）
- 論文 1～5 必收，論文 6（ViT）待確認

### [2026-11-21] N1 取得資料｜論文 1（Bahdanau 2014）｜✅ 通過
- 來源：https://arxiv.org/abs/1409.0473 （v7，ICLR 2015）
- 存檔：`raw/bahdanau-2014.pdf`、`raw/bahdanau-2014.txt`（pdftotext 轉出，約 8,200 字）
- R1：連結有效，可讀到全文（含 §1～§7 與附錄）
- 備註：轉檔後部分符號遺失（α、→、←、∈ 等數學符號變成亂碼），引用公式時要對照 PDF

### [2026-11-21] N2 討論｜論文 1｜⏳ 等待使用者確認
- AI 已提出提案，等待使用者回覆

### [2026-11-21] N2 討論｜論文 1｜✅ 通過
- 使用者回覆「你決定就好」，授權 AI 決定提案中的 4 個問題：
  1. softmax 獨立成頁 → 是（Transformer 也會用到）
  2. RNNsearch 建模型頁 → 否，寫在論文頁
  3. 實驗細節 → 只保留關鍵 BLEU 數字與長句結果
  4. 論文 6（ViT）→ 收錄（多 1 篇緩衝，也讓簡報能講「跨到圖片」）

### [2026-11-21] N3 寫入 Wiki｜論文 1
- 新增：`papers/bahdanau-2014.md`、`concepts/encoder-decoder.md`、`concepts/rnn.md`、`concepts/attention.md`、`concepts/softmax.md`
- 更新：`index.md`
- **寫入時自我核對發現 1 個錯誤**：`softmax.md` 把「Decoder 輸出用 softmax」標成附錄 A.2.2，回原文核對後實際在 A.1.1，已修正
  - 這類「出處章節標錯」lint 程式抓不到（連結本身有效），只能回原文比對 → 之後每篇都要做出處抽查
- 規則補充（AI 決定）：論文頁的出處指向 `raw/` 原文；R3 允許「緊接有出處段落的清單」沿用出處

### [2026-11-21] N4 Lint 檢查｜論文 1｜✅ 通過（第 1 次）
- 新增 `scripts/lint.py` 自動檢查 R3、R4、R5、R18
- 先放一個故意寫錯的測試頁，確認程式能抓到 R3、R4、R5、R18 四種錯誤，再刪除測試頁
- 正式執行：5 個頁面全部通過
- R6：第一篇，沒有舊頁面可衝突

### [2026-11-21] N1 取得資料｜論文 2（Vaswani 2017）｜✅ 通過
- 來源：https://arxiv.org/abs/1706.03762 （NIPS 2017）
- 存檔：`raw/vaswani-2017.pdf`、`raw/vaswani-2017.txt`（約 6,100 字）
- R1：連結有效，可讀到全文

### [2026-11-21] N2 討論｜論文 2｜⏳ 等待使用者確認
- 讀論文時發現 **原文自相矛盾**：英翻法 BLEU 在摘要與表 2 是 41.8，§6.1 內文卻寫 41.0 → 列入提案，請使用者決定（R6）
- 讀論文時發現 **舊頁面出處錯誤**：`attention.md` 寫「加法式 attention」並標出處為 Bahdanau 附錄 A.1.2，但 Bahdanau 原文沒有用 additive 這個詞；這個說法其實出自 Vaswani §3.2.1 → 列入提案修正

### [2026-11-21] N2 討論｜論文 2｜✅ 通過
- 使用者回覆「照提案通過」
- R6 處理：英翻法 BLEU 採用摘要與表 2 的 41.8，並在論文頁保留「§6.1 寫 41.0」的矛盾紀錄

### [2026-11-21] N3 寫入 Wiki｜論文 2
- 新增：`papers/vaswani-2017.md`、`models/transformer.md`、`concepts/self-attention.md`、`concepts/multi-head-attention.md`、`concepts/positional-encoding.md`、`concepts/embedding.md`
- 更新：`rnn.md`（無法平行計算）、`encoder-decoder.md`（Transformer 版本）、`attention.md`（內積版本、修正 additive 出處）、`softmax.md`（√d_k、−∞ 遮罩）、`index.md`
- 計算例子（self-attention 權重、遮罩、內積變異數）全部用 Python 實際計算，不由 AI 心算
- **寫入時自我核對發現 3 個問題**：
  1. `multi-head-attention.md` 寫「1 個頭比 8 個頭差」，原文 §6.2 是「比**最佳設定**差 0.9 BLEU」→ 改成原文說法（AI 改寫時語意跑掉）
  2. 同頁自行加了「一個頭看文法、另一個頭看語意」的例子，原文沒有這樣分工的說法 → 改成原文的描述（AI 自行補充例子）
  3. Positional Encoding 的波長範圍，轉檔時 π 符號遺失，無法從文字檔確認 → **不寫入**，不憑記憶補
- 修正論文 1 留下的錯誤：`attention.md` 的「additive」說法改標出處為 Vaswani §3.2.1

### [2026-11-21] N4 Lint 檢查｜論文 2｜✅ 通過（第 1 次）
- `scripts/lint.py`：11 個頁面全部通過 R3、R4、R5、R18
- R6 人工檢查：論文 1、2 對 attention 的描述沒有衝突（Vaswani 明確把 Bahdanau 的版本歸為 additive attention，與 Wiki 一致）；論文 2 內部的 41.8／41.0 矛盾已標註
- **觀察**：到目前為止 lint 全部一次通過，但 N3 自我核對已經抓到 4 個內容錯誤（論文 1 的 1 個、論文 2 的 3 個）。lint 只檢查格式，抓不到「內容與原文不符」

### [2026-11-21] N1 取得資料｜論文 3（Devlin 2018，BERT）｜✅ 通過
- 來源：https://arxiv.org/abs/1810.04805
- 存檔：`raw/devlin-2018.pdf`、`raw/devlin-2018.txt`（約 10,100 字）
- R1：可讀到全文。**第一次轉檔用 `-layout` 時左右兩欄交錯混在一起**，無法閱讀 → 改用預設模式（依閱讀順序）重新轉檔後正常
  - 論文 1、2 是單欄排版所以沒遇到；之後的論文一律先用閱讀順序模式

### [2026-11-21] N2 討論｜論文 3｜⏳ 等待使用者確認
- 發現術語衝突：BERT 的「mask」（把輸入字遮住讓模型猜）與 Wiki 現有 `self-attention.md` 的「遮罩」（禁止看後面的字）是兩件不同的事 → 列入提案
- 發現術語用法差異：BERT 註 4 說雙向版本常被稱為「Transformer encoder」、只看左邊的版本常被稱為「Transformer decoder」，但 `transformer.md` 中的 Decoder 還包含 Encoder-Decoder Attention，兩者不完全相同 → 列入提案

### [2026-11-21] N2 討論｜論文 3｜✅ 通過
- 使用者回覆「兩個都通過」：論文 3 提案通過，並**核准新增節點 N3.5 與規則 R20**

### [2026-11-21] 🔧 Graph 修改：新增 N3.5 原文比對（R20）
- 原因：論文 1、2 的 N4 lint 全部一次通過，但 N3 已出現 5 個內容錯誤（其中 1 個到下一篇論文才發現）。lint 只檢查格式，抓不到「內容與原文不符」
- 做法：N3 寫完後、N4 之前，逐段回原文找對應句子，紀錄存在 `wiki/checks/`
- 更新 `CLAUDE.md` 的 Graph 與規則

### [2026-11-21] N3 寫入 Wiki｜論文 3
- 新增：`papers/devlin-2018.md`、`models/bert.md`、`concepts/pretraining-finetuning.md`、`concepts/masked-language-model.md`、`concepts/language-model.md`
- 更新：`embedding.md`（三種 embedding）、`self-attention.md`（雙向 vs. 只看左邊、兩種 mask）、`transformer.md`（encoder-only／decoder-only 用語）、`index.md`
- R6 處理：兩個術語衝突（兩種 mask；Transformer decoder 的用法）都在相關頁面加上 ⚠️ 說明

### [2026-11-21] N3.5 原文比對｜論文 3｜❌ 不通過 → 修正後 ✅
- 完整紀錄：[checks/devlin-2018.md](checks/devlin-2018.md)
- 檢查 44 段，3 段找不到對應原文：
  1. `language-model.md`「語言模型是預測下一個字」→ Devlin 全文沒有這個說法，改引 Bahdanau 式 (2)（AI 自己的知識）
  2. `embedding.md`「## 表示接在前一個片段後面」→ 原文沒解釋，刪除（AI 自己的知識）
  3. `bert.md`「問答找答案位置」標成 §3.2 → 實際在 §4.2、圖 1（出處標錯）
- **N3.5 第一次實際執行就抓到 3 個錯誤**；這 3 個錯誤 lint 都會通過

### [2026-11-21] N4 Lint 檢查｜論文 3｜✅ 通過（第 1 次）
- 16 個頁面全部通過；R6 已人工處理（見 N3）

### [2026-11-21] N1 取得資料｜論文 4（Brown 2020，GPT-3）｜✅ 通過
- 來源：https://arxiv.org/abs/2005.14165
- 存檔：`raw/brown-2020.pdf`、`raw/brown-2020.txt`（約 37,900 字，最長的一篇）
- R1：可讀到全文；依 CLAUDE.md「長篇只 ingest 架構與核心概念」，只精讀 §1、§2、§3.9.1、§5、§8

### [2026-11-21] N2 討論｜論文 4｜⏳ 等待使用者確認
- **用 Python 驗算表 2.1 發現原文數字不一致**：依 Transformer 的設計，頭數 × 每頭維度應等於 d_model
  - GPT-3 XL（1.3B）：24 × 128 = 3072，但表中 d_model = 2048
  - GPT-3 13B：40 × 128 = 5120，但表中 d_model = 5140
  - 其他 6 個尺寸都一致 → 列入提案（R6）
- 發現推論問題：GPT-3 原文沒有直接寫「只用 Decoder」，只寫「autoregressive」和「與 GPT-2 相同架構」→ 列入提案，請使用者決定能否寫成推論

### [2026-11-21] N2 討論｜論文 4｜✅ 通過
- 使用者回覆「照預設通過」：
  1. 表 2.1 數字不一致 → 照原文抄錄並加 ⚠️，不自行修改
  2. 「GPT-3 只用 Decoder」→ 可寫，但必須明確標成推論
  3. §6 社會影響 → 不另建頁，只在論文頁用一句話帶過偏見問題

### [2026-11-21] N3 寫入 Wiki｜論文 4
- 新增：`papers/brown-2020.md`、`models/gpt-3.md`、`concepts/in-context-learning.md`、`concepts/scaling.md`
- 更新：`language-model.md`、`pretraining-finetuning.md`、`transformer.md`、`index.md`
- 圖 2.1 的翻譯範例是圖片、轉檔後沒有文字 → 不憑記憶引用，改用 §3.9.1 文字中的算術範例

### [2026-11-21] N3.5 原文比對｜論文 4｜❌ 不通過 → 修正後 ✅
- 完整紀錄：[checks/brown-2020.md](checks/brown-2020.md)
- 檢查 41 段，**8 段找不到對應**（比論文 3 的 3 段多）：
  - 4 段 **把 Wiki 既有用語套到新論文**：「由左到右」是 BERT 論文對 GPT 的描述，GPT-3 原文從沒用過 left-to-right
  - 2 段 AI 憑記憶補充（NeurIPS 2020、「運算量」）
  - 1 段數字改寫失真（10～100 → 幾個到幾十個）
  - 1 段出處標錯章節
- **新觀察**：Wiki 越大，AI 越容易把舊頁面的說法帶進新論文的描述（「交叉污染」）。這類錯誤在 N2 討論時就埋下了：我在 N2 提案寫「由左到右預測下一個 token」，使用者通過後，N3 就照著寫了

### [2026-11-21] N4 Lint 檢查｜論文 4｜✅ 通過（第 1 次）
- 20 個頁面全部通過；R6 的兩件事（表 2.1 數字、Decoder 推論）已在頁面中標註

### [2026-11-21] N1 取得資料｜論文 5（Raffel 2019，T5）｜✅ 通過
- 來源：https://arxiv.org/abs/1910.10683 （arXiv 2019；正式發表於 JMLR 第 21 卷，2020）
- 存檔：`raw/raffel-2019.pdf`、`raw/raffel-2019.txt`（約 32,300 字）
- R1：可讀到全文；只精讀 §1、§2、§3.1、§3.2、§3.7、§4.1

### [2026-11-21] N2 討論｜論文 5｜⏳ 等待使用者確認
- **新論文推翻了舊頁面的一個說法（R6）**：`gpt-3.md` 寫「頭數 × 每頭維度**應該**等於 d_model」。但 T5 的 3B（32 × 128 = 4096 ≠ 1024）和 11B（128 × 128 = 16384 ≠ 1024）也不相等，而且是刻意的設計。Vaswani 只是「選擇」讓兩者相等，不是規定 → GPT-3 表 2.1 的不一致不一定是錯誤，舊頁面的「應該」說太重了（Python 驗算 T5 5 個尺寸）
- 發現架構差異：T5 把 LayerNorm 放在子層的**輸入**，Vaswani 是放在殘差相加**之後** → 列入提案

### [2026-11-21] N2 討論｜論文 5｜✅ 通過
- 使用者回覆「照預設通過」：
  1. 修正 `gpt-3.md` 的「應該等於 d_model」→ 改為「Vaswani 的選擇，不是必要條件」
  2. LayerNorm 位置差異 → 標註為設計變化，不判斷優劣
  3. 年份用 2019，頁首註明 JMLR 2020

### [2026-11-21] N3 寫入 Wiki｜論文 5
- 新增：`papers/raffel-2019.md`、`models/t5.md`、`concepts/text-to-text.md`、`concepts/architecture-variants.md`（Transformer 家族總覽）
- 更新：`masked-language-model.md`（denoising、span corruption）、`self-attention.md`（三種遮罩名稱）、`positional-encoding.md`（相對位置）、`pretraining-finetuning.md`（transfer learning、微調方式）、`scaling.md`、`embedding.md`、`gpt-3.md`（**修正舊說法**、補 T5 的 decoder-only 描述）、`transformer.md`、`index.md`
- R6：**第一次發生「新論文推翻 Wiki 舊說法」**——`gpt-3.md` 原本說「頭數 × 每頭維度應該等於 d_model」，T5 的 3B／11B 證明這不是規定。依 R6 不直接覆蓋，而是在頁面留下修正紀錄

### [2026-11-21] N3.5 原文比對｜論文 5｜❌ 不通過 → 修正後 ✅
- 完整紀錄：[checks/raffel-2019.md](checks/raffel-2019.md)
- 檢查 47 段，1 段找不到對應：T5-Small 的 d_kv 是 AI 自行填補的表格空格 → 改成「原文未列出」
- 錯誤數從 8 → 1。這次 N3 寫作前先把要引用的段落讀完，寫的時候就以 R20 為標準

### [2026-11-21] N4 Lint 檢查｜論文 5｜✅ 通過（第 1 次）
- 24 個頁面全部通過

### [2026-11-21] N1 取得資料｜論文 6（Dosovitskiy 2020，ViT）｜✅ 通過
- 來源：https://arxiv.org/abs/2010.11929 （ICLR 2021）
- 存檔：`raw/dosovitskiy-2020.pdf`、`raw/dosovitskiy-2020.txt`（約 10,500 字）
- R1：可讀到全文；精讀 §1～§5（附錄略過）

### [2026-11-21] N2 討論｜論文 6｜⏳ 等待使用者確認
- **術語衝突（R6）**：ViT 的「few-shot」是指「凍結模型、用少量圖片做線性迴歸」，和 GPT-3 的「few-shot」（在輸入中給範例、不更新參數）完全不同 → 列入提案
- ViT 和 T5 一樣把 LayerNorm 放在每個區塊之前，與 Vaswani 不同 → 沿用論文 5 的處理方式（標註為設計變化）

### [2026-11-21] N2 討論｜論文 6｜✅ 通過
- 使用者回覆「照預設通過」：兩種 few-shot 都加 ⚠️；224×224 例子標為假設；混合架構只簡述

### [2026-11-21] N3 寫入 Wiki｜論文 6
- 新增：`papers/dosovitskiy-2020.md`、`models/vit.md`、`concepts/patch-embedding.md`、`concepts/inductive-bias.md`
- 更新：`architecture-variants.md`（ViT、家族樹）、`positional-encoding.md`、`masked-language-model.md`、`scaling.md`、`pretraining-finetuning.md`、`transformer.md`、`vaswani-2017.md`（展望 → ViT）、`in-context-learning.md`（⚠️ 兩種 few-shot）、`index.md`

### [2026-11-21] N3.5 原文比對｜論文 6｜❌ 不通過 → 修正後 ✅
- 完整紀錄：[checks/dosovitskiy-2020.md](checks/dosovitskiy-2020.md)
- 檢查 38 段，6 段找不到對應，其中 4 段是 **AI 為了讓讀者看懂而加的白話解釋**（「不重疊」、「平移等變性」的說明、標題解讀、「查詢 embedding 表」）
- 觀察：**教學用的補充說明，正是最容易超出原文的地方**。這對階段二很重要：簡報比 Wiki 更需要白話，N6／N7 要特別注意

### [2026-11-21] N4 Lint 檢查｜論文 6｜❌ 不通過（第 1 次）
- R3：`papers/dosovitskiy-2020.md`「詳見 [ViT]。」單獨成段、沒有出處
- 處理：回到 N3，把這句併入前一段

### [2026-11-21] N4 Lint 檢查｜論文 6｜✅ 通過（第 2 次）
- 28 個頁面全部通過
- **這是 lint 第一次抓到錯誤**（6 篇論文共 7 次執行）

### [2026-11-21] ✅ 階段一完成
- 6 篇論文、28 個 Wiki 頁面（6 論文頁、17 概念頁、5 模型頁）
- N3.5 共抓到 18 個內容錯誤（論文 3～6：3、8、1、6）；N3 自我核對另抓到 5 個（論文 1、2）
- N4 lint 共抓到 1 個格式錯誤

### [2026-11-21] N5 規劃大綱｜⏳ 等待使用者確認（R10）
- 查詢 `index.md` 與各頁，產出 [slides/outline.md](../slides/outline.md)：18 頁、6 個部分
- 新增 `scripts/check_outline.py` 自動檢查 R7、R8
- R7 ✅ 每頁至少對應 1 個 Wiki 頁面，且連結都存在
- R8 ✅ 6 篇論文都有用到；28 個 Wiki 頁面全部被用到
- R9（人工）✅ 先備順序：Embedding、Softmax（第 3、4 頁）→ RNN（5）→ Attention（6）→ Self-Attention（8）→ 家族（11）→ 各模型（12～15）
- 待使用者決定：頁數（原預估 12～15，實際 18）、是否加互動 demo

### [2026-11-21] N5 規劃大綱｜✅ 通過
- 使用者回覆「照預設通過」：維持 18 頁；每頁底部標註 Wiki 來源；第 8 頁做 1 個遮罩切換 demo；單一 HTML 檔

### [2026-11-21] N6 產生內容
- 產出 [slides/content.md](../slides/content.md)：18 頁，每個要點標註〈來源 Wiki 頁〉

### [2026-11-21] N7 內容檢查｜❌ 不通過（第 1 次）
- 完整紀錄：[checks/slides.md](checks/slides.md)
- 新增 `scripts/check_slides.py`：自動檢查來源是否在清單內、數字是否出現在 Wiki、術語是否在第一次出現時解釋
- 自動檢查：R11 ✅；**R12 ❌ 24 項**（沒解釋的術語，例如 BLEU、O(n)、GLUE、CNN、d_model）
  - 其中 3 項是檢查程式的 bug（要求每次出現都解釋），已修正程式
- 人工比對：**R11 ❌ 1 項**，第 14 頁的 span corruption 內容來自 MLM 頁，但該頁的 Wiki 清單沒有 MLM（自動檢查抓不到）
- **N7 → N3（Wiki 缺少知識）**：Wiki 沒有 GLUE 的定義 → 先在 `devlin-2018.md` 補寫並回原文核對（Devlin §4.1），lint ✅，再寫進簡報
- 處理：回到 N6 修正；大綱第 14 頁加入 MLM 頁（`check_outline.py` 重跑 ✅）

### [2026-11-21] N7 內容檢查｜✅ 通過（第 2 次）
- 自動 R11、R12 全部通過；人工比對修改過的句子都有 Wiki 來源

### [2026-11-21] N8 產生 HTML
- 新增 `scripts/build_slides.py` ＋ `scripts/slides_template.html`：把 `content.md` **機械式轉換**成 `slides/index.html`
- 設計理由：N8 不讓 AI 重寫內容，HTML 只能出現 N7 檢查過的文字；每頁底部自動列出 Wiki 來源並連到 GitHub
- 第 8 頁 demo 的數字直接從 `content.md` 解析；第 18 頁的論文連結從 `wiki/papers/*.md` 讀取

### [2026-11-21] N9 瀏覽檢查｜❌ 不通過（第 1 次）
- 在內建瀏覽器用 JavaScript 逐頁檢查（1024×768）
- R13 ❌：模擬按 → 鍵沒有翻頁。原因是鍵盤處理程式對 `document` 呼叫 `.closest()` 而出錯。（說明：這是測試把事件直接送到 document 才觸發的；真人按鍵的事件目標是 body，可能不會遇到，但程式確實不夠穩，仍然修正）
- R14 ❌：第 8 頁（說明 + demo）超出畫面 118px
- 處理：回到 N8，修正鍵盤程式；有 demo 的頁面改成左右兩欄

### [2026-11-21] N9 瀏覽檢查｜✅ 通過（第 2 次）
- R13 ✅：→、空白鍵、← 都能正確翻頁；遮罩 demo 切換後第一列變成 `1, 0, 0`
- R14 ✅：1024×768、1280×720、1366×768、1920×1080 四種尺寸，18 頁都沒有超出畫面、沒有水平捲軸
- R15 ✅：手機 375×812 沒有水平溢出；第 1、8、17、18 頁內容較多，可在卡片內上下捲動

### [2026-11-21] 🔧 紀錄更正
- 撰寫反思時重新計算：「階段一完成」那筆寫「N3 自我核對另抓到 5 個（論文 1、2）」有誤，正確是 **4 個**（softmax 出處、additive 出處、0.9 改寫失真、自行補充的例子）。π 那一項是「刻意不寫入」，不是錯誤
- 依 R6 精神不直接改舊紀錄，在此更正：N3 源頭的內容錯誤共 **22 個**（4 + 18）

### [2026-11-21] 撰寫說明文件
- `docs/workflow.md`：最終版 graph（Mermaid）、節點表、重複執行與檢查點、設計理由、修改紀錄
- `docs/reflection.md`：各節點錯誤統計與三個反思問題的回答

### [2026-11-21] N10 發布｜⏳ 等待使用者同意（R16）
- 遠端 repo 目前只有 1 個 Initial commit（README.md 只有標題），可以在它之上新增 commit，不需要強制覆蓋
- 待使用者決定：`raw/` 的論文 PDF 與全文文字檔（約 16 MB）是否公開上傳（著作權考量）

### [2026-11-21] N10 發布｜✅ 推送完成（R16：使用者回覆「改連 arXiv 再推」）
- 使用者決定：論文 PDF 與全文不公開上傳 → Wiki 中 79 個原文連結改指 arXiv；新增 `raw/README.md`、`scripts/fetch_raw.sh`（可重新下載）、`.gitignore`
- 改完後重跑：lint ✅、check_outline ✅、check_slides ✅、build_slides（18 頁）
- 在遠端的 Initial commit 之上新增 commit `22e9367`，fast-forward 推送，沒有強制覆蓋；遠端共 50 個檔案、0 個 PDF
- GitHub Pages 尚未開啟（網址目前回 404），需由使用者在 repo 的 Settings → Pages 開啟

### [2026-11-21] N9 瀏覽檢查（補檢查）｜❌ 發現遺漏
- 使用者回報：網站「長得不對」
- 原因：GitHub Pages 的 **根網址**（Settings 裡的「Visit site」）沒有首頁，GitHub 直接把 README 轉成純文件頁；流程圖顯示成 Mermaid 原始碼，`wiki/checks/` 這類資料夾連結在 Pages 上是 404
- N9 先前只檢查了 `/slides/`，**沒檢查使用者實際會先打開的根網址** → 檢查範圍漏了
- 處理：新增根目錄 `index.html` 首頁（主按鈕連到簡報、作業 6 項的入口連到 GitHub 上可正常顯示的頁面、流程圖直接用 HTML 畫）；README 開頭加上首頁與簡報網址
- 本機預覽：1280×800、手機 375×812 都沒有水平溢出，首頁的簡報連結正常

### [2026-11-21] N9 瀏覽檢查（補檢查）｜❌ 發現遺漏 → N8 修正
- 使用者回報：簡報頁無法回到首頁
- 原因：新增首頁後，簡報（`scripts/slides_template.html`）沒有連回首頁的按鈕，只能用瀏覽器的上一頁
- 處理（回 N8）：模板左上角加上「← 首頁」連結（`../`），列印時隱藏；重跑 build_slides（18 頁）、check_slides ✅
- 本機預覽：桌面版點擊後回到首頁；手機 375×812 按鈕正常顯示，不擋住內容
