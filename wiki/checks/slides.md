# N7 內容檢查紀錄：教學簡報

依 [CLAUDE.md](../../CLAUDE.md) 的 R11（每個論點都能在 Wiki 裡找到）、R12（專有名詞第一次出現時有解釋）。
檢查對象：[slides/content.md](../../slides/content.md)

## 第 1 次執行｜❌ 不通過

### 自動檢查（`scripts/check_slides.py`）

- R11-a（來源必須在該頁的 Wiki 清單內）：✅
- R11-b（數字必須出現在該頁的 Wiki 頁面中）：✅ 所有數字都找得到
- R12：❌ 24 項
  - 第 1、2 頁：Transformer、BERT、GPT-3、T5、ViT、Encoder-Decoder、Attention 出現時沒有解釋
  - 第 7 頁：Self-Attention 在第 8 頁才解釋，第 7 頁就先用了；O(1)／O(n) 沒有解釋
  - 沒解釋的專有名詞：BLEU（第 6 頁）、梯度（第 8 頁）、FFN、d_model、d_ff（第 10 頁）、GLUE、NLP（第 12 頁）、CNN（第 15 頁）、子詞（第 3 頁）
  - 其中 BLEU（第 7、9 頁）和 CNN（第 18 頁）是**檢查程式的 bug**：R12 只要求「第一次出現時」解釋，程式卻要求每次出現都解釋 → 修正程式

### 人工逐頁比對

| 頁 | 檢查的論點 | 對應的 Wiki 句子 | 結果 |
|---|---|---|---|
| 1 | 時間軸 6 篇論文與年份 | `index.md` 各論文名稱與一行摘要 | ✅ |
| 2 | 家族樹 | `architecture-variants.md` 家族樹 | ✅ |
| 3 | 神經網路只能處理數字；token 不一定是完整單字；512 維；30,000、`[UNK]`；`play` + `##ing` | `embedding.md` 是什麼、Token、BERT 段 | ✅ |
| 4 | 定義、公式、`[2.0, 1.0, 0.1]` 例子 | `softmax.md` 是什麼、公式、計算例子 | ✅ |
| 5 | RNN 逐字讀、隱藏狀態是摘要；固定長度向量；瓶頸 | `rnn.md` 是什麼；`encoder-decoder.md` 早期做法、問題 | ✅ |
| 6 | 每字保留向量；三步驟；the man → l' homme；26.75／17.82；50 字以上不退步 | `attention.md` 算法、軟對齊；`bahdanau-2014.md` 主要結果 | ✅ |
| 7 | RNN 無法平行；只用 attention；28.4；8 張 P100、12 小時 | `rnn.md` 限制；`transformer.md` 是什麼、優點；`vaswani-2017.md` 主要結果 | ✅ |
| 8 | Q／K／V 定義；公式；√d_k 原因；遮罩 −∞；demo 數字 | `self-attention.md` 各段、計算例子、遮罩 | ✅ |
| 9 | 8 個頭、64 維；不同頭學不同任務；低 0.9；sin／cos；學出來的差不多 | `multi-head-attention.md`；`positional-encoding.md` | ✅ |
| 10 | 資料流程 4 步；Encoder／Decoder 子層；殘差、LayerNorm；參數表 | `transformer.md` 資料流程、每一層、基本設定 | ✅ |
| 11 | 遮罩是主要差別；三種遮罩；四種架構；Encoder-Decoder 最好 | `architecture-variants.md` | ✅ |
| 12 | 雙向；預訓練 → 微調；15%、80/10/10；my dog is hairy；`[CLS]`；GLUE 80.5；只看左邊變差 | `bert.md`、`masked-language-model.md`、`pretraining-finetuning.md`、`devlin-2018.md` | ✅ |
| 13 | 1,750 億、自迴歸；Decoder 推論；三種 shot；算術例子與結果；0.8%、進位；單向代價 | `gpt-3.md`、`in-context-learning.md`、`brown-2020.md` | ✅ |
| 14 | 任務前綴例子；Encoder-Decoder；**span corruption 的描述**；110 億、18／24 | `text-to-text.md`、`t5.md`、`raffel-2019.md` | ❌ span corruption 的具體做法寫在 `masked-language-model.md`，`t5.md` 只有一句「詳見 MLM」，而這頁的 Wiki 清單沒有 MLM 頁 → **R11 不通過**（自動檢查抓不到，因為標註的〈t5〉確實在清單內，只是內容不在那頁） |
| 15 | patch、N = HW/P²、196；分類 token；歸納偏置；ImageNet 130 萬；1,400 萬～3 億；結論 | `vit.md`、`patch-embedding.md`、`inductive-bias.md`、`dosovitskiy-2020.md` | ✅ |
| 16 | GPT-3、BERT（3,600）、T5、ViT 的規模發現；極限 | `scaling.md` 各段 | ✅ |
| 17 | 比較表；兩種 mask；兩種 few-shot | `architecture-variants.md`、`masked-language-model.md`、`in-context-learning.md` | ✅ |
| 18 | 3 題答案 | 第 7、11～13、15 頁 | ✅ |

### 要補的知識（N7 → N3）

- 第 12 頁要解釋 GLUE，但 **Wiki 裡沒有 GLUE 的定義**。依規則不能直接寫進簡報 → 回到 N3，在 `papers/devlin-2018.md` 補上：「GLUE 是一組多樣的自然語言理解任務所組成的測驗集」（Devlin §4.1 原文："a collection of diverse natural language understanding tasks"），再跑 lint ✅

## 修正（回到 N6，第 1 次重試）

| 頁 | 修正 |
|---|---|
| 1 | 時間軸改成每個模型附一行說明；把「Encoder」「微調」「克漏字」改成白話或標註「第 5 頁說明」 |
| 2 | 問題 ① 改成不使用術語的問法；家族樹加上 Encoder／Decoder 的一句說明 |
| 3 | 「子詞」補上「把單字切成較小的片段」（`embedding.md`） |
| 6 | BLEU 補上「翻譯品質指標，越高越好」（`bahdanau-2014.md`） |
| 7 | 拿掉 O(1)／O(n) 和 Self-Attention，改用 `transformer.md` 優點與 `rnn.md` 限制的白話說法 |
| 8 | 拿掉「梯度」，只保留「模型會很難學習」；補上 d_k 是 Key 的維度 |
| 10 | FFN、d_model、d_ff、h、N 都補上 `transformer.md` 表格中的說明 |
| 12 | GLUE 補上定義（先補進 Wiki）；「NLP 任務」改成「任務」 |
| 14 | Wiki 清單加入 `masked-language-model`（大綱同步修改，`check_outline.py` 重跑 ✅），並補上 span corruption 的例子 |
| 15 | CNN 補上「卷積網路，當時圖片辨識的主流」、ResNet 補上「一種 CNN」（`dosovitskiy-2020.md`） |

## 第 2 次執行｜✅ 通過

- 自動檢查：R11、R12 全部通過
- 人工比對：第 14 頁的 span corruption 現在對應到 `masked-language-model.md`「T5 的變化」一節 ✅；其他修改過的句子都已對照上表的 Wiki 來源 ✅
- 新增的白話說明都能在 Wiki 中找到原句，沒有新加入 Wiki 以外的解釋（記取論文 6 的教訓）
