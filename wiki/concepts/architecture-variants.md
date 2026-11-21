# Transformer 架構家族

> **類型**：概念 ｜ **出處**：[Raffel 2019](../papers/raffel-2019.md)、[Vaswani 2017](../papers/vaswani-2017.md)、[Devlin 2018](../papers/devlin-2018.md)、[Dosovitskiy 2020](../papers/dosovitskiy-2020.md) ｜ **相關**：[ViT](../models/vit.md)、[Transformer](../models/transformer.md)、[BERT](../models/bert.md)、[GPT-3](../models/gpt-3.md)、[T5](../models/t5.md)、[Self-Attention](self-attention.md)

## 關鍵：attention 遮罩

不同架構之間最主要的差別，在於 attention 使用的「遮罩」：遮罩把某些 attention 權重設為 0，限制每個輸出位置能看到哪些輸入。〔出處：[Raffel 2019 §3.2.1](../papers/raffel-2019.md)〕

| 遮罩 | 規則 | 用在哪裡 |
|---|---|---|
| **全可見（fully-visible）** | 每個位置都能看全部的輸入 | Encoder；BERT |
| **因果（causal）** | 第 i 個位置只能看第 i 個以前的位置（j > i 的權重設為 0） | Decoder；語言模型 |
| **前綴（causal with prefix）** | 輸入的前綴部分全可見，之後的部分用因果遮罩 | Prefix LM |
〔出處：[Raffel 2019 §3.2.1、圖 3](../papers/raffel-2019.md)〕

## 四種架構

| 架構 | 結構 | 代表 | 適合 |
|---|---|---|---|
| **Encoder-Decoder** | 兩個堆疊：Encoder 全可見，Decoder 因果，中間有 Encoder-Decoder Attention | 原始 [Transformer](../models/transformer.md)、[T5](../models/t5.md) | 輸入一段、輸出另一段（如翻譯） |
| **Encoder-only** | 一個全可見的堆疊 | [BERT](../models/bert.md)、[ViT](../models/vit.md)（圖片） | 分類、找出片段 |
| **Decoder-only（語言模型）** | 一個因果的堆疊，只做「預測下一步」 | OpenAI GPT、[GPT-3](../models/gpt-3.md)（推論，見該頁） | 生成文字 |
| **Prefix LM** | 一個堆疊，前綴全可見、其餘因果 | — | 先讀完一段，再接著生成 |
〔出處：[Raffel 2019 §3.1.1、§3.2.1、§4.1](../papers/raffel-2019.md)、[Vaswani 2017 §3.1](../papers/vaswani-2017.md)、[Devlin 2018 §3](../papers/devlin-2018.md)、[Dosovitskiy 2020 §3.1](../papers/dosovitskiy-2020.md)〕

T5 的作者直接指出：沒有 Encoder 的 Transformer decoder 可以當作語言模型使用，也就是只為了預測下一步而訓練的模型；早期的 NLP transfer learning 就是用這種架構加上語言模型目標來預訓練。〔出處：[Raffel 2019 §3.2.1](../papers/raffel-2019.md)〕

## Decoder-only 的缺點與 Prefix LM

在 text-to-text 任務中，如果整段都用因果遮罩，模型對輸入（前綴）中第 i 個字的表示只能依賴第 i 個字以前的內容，資訊被不必要地限制住。Prefix LM 的解法是：前綴部分改用全可見遮罩。〔出處：[Raffel 2019 §3.2.1](../papers/raffel-2019.md)〕

作者也指出，Prefix LM 在分類任務上和 BERT 很像：全可見的前綴就像 BERT 的分類符號，差別只在於分類器被整合進 Decoder 的輸出層。〔出處：[Raffel 2019 §3.2.1](../papers/raffel-2019.md)〕

## 哪一種比較好（T5 的實驗）

在 T5 的 text-to-text 框架下比較的結果：〔出處：[Raffel 2019 §3.2.4、§4.1](../papers/raffel-2019.md)〕

- **Encoder-Decoder 加 denoising 目標**在所有任務上表現最好。
- 它的參數量是單一堆疊的兩倍，但計算量相近：Encoder 只處理輸入、Decoder 只處理輸出；單一堆疊的模型則要同時處理輸入和輸出。
- Encoder 和 Decoder **共用參數**，參數量減半，表現也幾乎一樣好。
- 共用參數的 Encoder-Decoder 仍然勝過 Prefix LM，表示明確的 Encoder-Decoder Attention 有幫助。
- 使用 denoising 目標，下游任務的表現一律優於語言模型目標。

## 小結：家族樹

```
Transformer（2017，Encoder-Decoder）
├── 只用 Encoder（全可見）       → BERT（2018）
│                                → ViT（2020，從文字跨到圖片）
├── 只用 Decoder（因果）         → GPT 系列 → GPT-3（2020）
└── 保留 Encoder-Decoder         → T5（2019）
```
〔出處：整理自 [Vaswani 2017](../papers/vaswani-2017.md)、[Devlin 2018 §3 註 4](../papers/devlin-2018.md)、[Brown 2020 §2.1](../papers/brown-2020.md)、[Raffel 2019 §3.2](../papers/raffel-2019.md)、[Dosovitskiy 2020 §3.1](../papers/dosovitskiy-2020.md)；GPT-3 的歸類為推論〕
