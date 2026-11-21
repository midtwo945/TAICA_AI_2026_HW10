# 簡報大綱（N5 產出，待使用者確認 R10）

主題：**Transformer：從一篇翻譯論文，到 BERT、GPT-3、T5、ViT**
目標讀者：沒學過 Transformer 的人（作業最低要求：看得懂基本概念）
每頁的「Wiki」欄是該頁內容**唯一**允許使用的來源（N6 只能用這些頁面寫）。

## 第一部分：開場

| # | 標題 | 這頁要教會什麼 | Wiki |
|---|---|---|---|
| 1 | Transformer：一個架構，撐起整個 AI 時代 | 主題、6 篇論文的時間軸 | [index](../wiki/index.md)、[Vaswani 2017](../wiki/papers/vaswani-2017.md) |
| 2 | 這堂課的地圖 | 學完能回答的 3 個問題；家族樹預告 | [Transformer 架構家族](../wiki/concepts/architecture-variants.md) |

## 第二部分：先備知識

| # | 標題 | 這頁要教會什麼 | Wiki |
|---|---|---|---|
| 3 | 電腦怎麼讀字？Token 與 Embedding | 字要先切成 token、再變成向量 | [Embedding](../wiki/concepts/embedding.md) |
| 4 | Softmax：把分數變成權重 | 分數 → 加總為 1 的權重；`[2.0, 1.0, 0.1]` 例子 | [Softmax](../wiki/concepts/softmax.md) |

## 第三部分：Attention 的誕生

| # | 標題 | 這頁要教會什麼 | Wiki |
|---|---|---|---|
| 5 | 起點：RNN 翻譯模型的瓶頸 | RNN 逐字讀；整句壓成一個向量，長句會變差 | [RNN](../wiki/concepts/rnn.md)、[Encoder-Decoder](../wiki/concepts/encoder-decoder.md)、[Bahdanau 2014](../wiki/papers/bahdanau-2014.md) |
| 6 | Attention：翻譯每個字時回頭看原文 | 算分數 → softmax → 加權平均；軟對齊的例子 | [Attention](../wiki/concepts/attention.md)、[Bahdanau 2014](../wiki/papers/bahdanau-2014.md) |

## 第四部分：Transformer

| # | 標題 | 這頁要教會什麼 | Wiki |
|---|---|---|---|
| 7 | Attention Is All You Need | 拿掉 RNN、只用 attention；為什麼更快 | [Vaswani 2017](../wiki/papers/vaswani-2017.md)、[Transformer](../wiki/models/transformer.md)、[RNN](../wiki/concepts/rnn.md) |
| 8 | Self-Attention：Q、K、V | 公式與 3 個字的計算例子；遮罩 | [Self-Attention](../wiki/concepts/self-attention.md)、[Softmax](../wiki/concepts/softmax.md) |
| 9 | Multi-Head 與 Positional Encoding | 多個頭看不同面向；沒有 RNN 要補位置 | [Multi-Head Attention](../wiki/concepts/multi-head-attention.md)、[Positional Encoding](../wiki/concepts/positional-encoding.md) |
| 10 | Transformer 全貌 | Encoder／Decoder 各 6 層的資料流程 | [Transformer](../wiki/models/transformer.md) |

## 第五部分：應用變化

| # | 標題 | 這頁要教會什麼 | Wiki |
|---|---|---|---|
| 11 | 一個遮罩，分出整個家族 | 三種遮罩 → 四種架構 | [Transformer 架構家族](../wiki/concepts/architecture-variants.md)、[Raffel 2019](../wiki/papers/raffel-2019.md) |
| 12 | BERT：只用 Encoder，做克漏字 | 雙向；MLM（15%、80/10/10）；預訓練 → 微調 | [BERT](../wiki/models/bert.md)、[Masked Language Model](../wiki/concepts/masked-language-model.md)、[預訓練與微調](../wiki/concepts/pretraining-finetuning.md)、[Devlin 2018](../wiki/papers/devlin-2018.md) |
| 13 | GPT-3：只用 Decoder，給範例就會做 | 自迴歸語言模型；zero／one／few-shot；算術例子 | [GPT-3](../wiki/models/gpt-3.md)、[In-context Learning](../wiki/concepts/in-context-learning.md)、[語言模型](../wiki/concepts/language-model.md)、[Brown 2020](../wiki/papers/brown-2020.md) |
| 14 | T5：一切都是文字轉文字 | 任務前綴；span corruption；Encoder-Decoder 勝出 | [T5](../wiki/models/t5.md)、[Text-to-Text](../wiki/concepts/text-to-text.md)、[Masked Language Model](../wiki/concepts/masked-language-model.md)、[Raffel 2019](../wiki/papers/raffel-2019.md) |
| 15 | ViT：一張圖值 16×16 個字 | 圖片切 patch；資料多才贏 CNN | [ViT](../wiki/models/vit.md)、[Patch Embedding](../wiki/concepts/patch-embedding.md)、[歸納偏置](../wiki/concepts/inductive-bias.md)、[Dosovitskiy 2020](../wiki/papers/dosovitskiy-2020.md) |

## 第六部分：總結

| # | 標題 | 這頁要教會什麼 | Wiki |
|---|---|---|---|
| 16 | 共同主題：越大越強 | BERT、GPT-3、T5、ViT 都看到規模的效果，以及極限 | [規模化](../wiki/concepts/scaling.md) |
| 17 | 總整理與常見誤會 | 5 個模型比較表；兩種 mask、兩種 few-shot | [Transformer 架構家族](../wiki/concepts/architecture-variants.md)、[Masked Language Model](../wiki/concepts/masked-language-model.md)、[In-context Learning](../wiki/concepts/in-context-learning.md) |
| 18 | 小測驗與參考資料 | 3 題自我檢查；6 篇論文連結 | [index](../wiki/index.md) |
