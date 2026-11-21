# GPT-3

> **類型**：模型 ｜ **出處**：[Brown 2020](../papers/brown-2020.md)、[Devlin 2018](../papers/devlin-2018.md)、[Raffel 2019](../papers/raffel-2019.md) ｜ **相關**：[Transformer 架構家族](../concepts/architecture-variants.md)、[Transformer](transformer.md)、[BERT](bert.md)、[In-context Learning](../concepts/in-context-learning.md)、[規模化](../concepts/scaling.md)、[語言模型](../concepts/language-model.md)

## 是什麼

GPT-3 是一個 1,750 億參數的**自迴歸[語言模型](../concepts/language-model.md)**，使用時只要讓它「預測接下來的內容」。它的模型和架構與 GPT-2 相同，只在 Transformer 的各層交替使用一般的 attention 和局部的稀疏 attention。〔出處：[Brown 2020 摘要、§1、§2.1](../papers/brown-2020.md)〕

## 屬於哪一種 Transformer

GPT-3 原文沒有直接寫「只用 Decoder」。以下是**推論**：[Devlin 2018](../papers/devlin-2018.md) 描述 OpenAI GPT 是「由左到右的 Transformer」，並指出這種只看左邊的版本常被稱為「Transformer decoder」；GPT-3 又沿用 GPT 系列（GPT-2）的架構，而且是自迴歸模型。因此可以把 GPT-3 歸類為「只用由左到右的 Decoder」的模型，和只用 Encoder 的 [BERT](bert.md) 相對。〔出處：推論自 [Devlin 2018 §3 註 4、附錄 A.4](../papers/devlin-2018.md) 與 [Brown 2020 摘要、§2.1](../papers/brown-2020.md)〕

[T5](t5.md) 的論文也支持這個歸類方式：它指出沒有 Encoder 的 Transformer decoder 可以當作語言模型使用，並把語言模型稱為「decoder-only」架構。不過 T5 論文並沒有直接討論 GPT-3。〔出處：[Raffel 2019 §3.2.1、§4.1](../papers/raffel-2019.md)〕

## 模型大小（節錄）

| 名稱 | 參數量 | 層數 | d_model | 頭數 | 每頭維度 |
|---|---|---|---|---|---|
| GPT-3 Small | 1.25 億 | 12 | 768 | 12 | 64 |
| GPT-3 XL | 13 億 | 24 | 2048 ⚠️ | 24 | 128 |
| GPT-3 13B | 130 億 | 40 | 5140 ⚠️ | 40 | 128 |
| GPT-3 175B（GPT-3） | 1,750 億 | 96 | 12288 | 96 | 128 |
〔出處：[Brown 2020 表 2.1](../papers/brown-2020.md)〕

⚠️ **原文數字與其他尺寸的規律不同（R6，2026-11-21 修正）**：原始 [Transformer](transformer.md) **選擇**讓每個頭的維度等於 d_model 除以頭數（512 / 8 = 64），所以「頭數 × 每頭維度 = d_model」。用 Python 驗算表 2.1 的 8 個尺寸，有 6 個符合這個規律，但 XL（24 × 128 = 3072 ≠ 2048）和 13B（40 × 128 = 5120 ≠ 5140）不符合。〔出處：[Brown 2020 表 2.1](../papers/brown-2020.md)、[Vaswani 2017 §3.2.2](../papers/vaswani-2017.md)，以 Python 驗算〕

不過，這不一定是錯誤：[T5](t5.md) 的 3B 和 11B 也刻意讓兩者不相等（例如 32 × 128 = 4096，d_model 卻是 1024），可見這只是一種設計選擇，不是必要條件。GPT-3 原文沒有說明這兩個尺寸的原因，本 Wiki 照原文抄錄，不自行修改。〔出處：[Raffel 2019 §3.7](../papers/raffel-2019.md)、[Brown 2020 表 2.1](../papers/brown-2020.md)，以 Python 驗算〕

> 修正紀錄：先前版本寫「應該等於 d_model」，讀到 T5 後發現說得太重，已改正。

所有尺寸的輸入長度上限（context window）都是 2,048 個 token，前饋層的維度都是 d_model 的 4 倍。〔出處：[Brown 2020 §2.1](../papers/brown-2020.md)〕

## 訓練資料

所有模型都訓練了 3,000 億個 token。資料以 byte-pair encoding 切成 token，混合比例如下：〔出處：[Brown 2020 §2.2、表 2.1、表 2.2](../papers/brown-2020.md)〕

| 資料集 | token 數 | 訓練時的抽樣比例 |
|---|---|---|
| Common Crawl（過濾後） | 4,100 億 | 60% |
| WebText2 | 190 億 | 22% |
| Books1 | 120 億 | 8% |
| Books2 | 550 億 | 8% |
| 維基百科 | 30 億 | 3% |
〔出處：[Brown 2020 表 2.2](../papers/brown-2020.md)〕

抽樣比例不按資料量分配：作者認為品質較高的資料會被抽得比較多次，以接受少量過度擬合來換取更高品質的訓練資料。〔出處：[Brown 2020 §2.2](../papers/brown-2020.md)〕

## 怎麼使用

GPT-3 不做微調，而是用 [In-context Learning](../concepts/in-context-learning.md)：把任務說明和範例直接寫進輸入文字，讓模型接著寫出答案。〔出處：[Brown 2020 摘要、§2](../papers/brown-2020.md)〕

## 和 BERT 的對比

| | [BERT](bert.md) | GPT-3 |
|---|---|---|
| 方向 | 雙向 | 自迴歸（單向） |
| 使用方式 | 預訓練後針對每個任務微調 | 不微調，用文字給說明和範例 |
| 參數量 | 3.4 億（Large） | 1,750 億 |
〔出處：[Devlin 2018 §3](../papers/devlin-2018.md)、[Brown 2020 摘要、§2、§5](../papers/brown-2020.md)〕

GPT-3 的作者也承認，選擇單向架構的代價是：在需要雙向資訊的任務上可能表現較差。〔出處：[Brown 2020 §5](../papers/brown-2020.md)〕
