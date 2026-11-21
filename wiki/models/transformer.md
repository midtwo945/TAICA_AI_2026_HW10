# Transformer

> **類型**：模型 ｜ **出處**：[Vaswani 2017](../papers/vaswani-2017.md)、[Devlin 2018](../papers/devlin-2018.md)、[Brown 2020](../papers/brown-2020.md)、[Raffel 2019](../papers/raffel-2019.md)、[Dosovitskiy 2020](../papers/dosovitskiy-2020.md) ｜ **相關**：[ViT](vit.md)、[T5](t5.md)、[Transformer 架構家族](../concepts/architecture-variants.md)、[BERT](bert.md)、[GPT-3](gpt-3.md)、[Self-Attention](../concepts/self-attention.md)、[Multi-Head Attention](../concepts/multi-head-attention.md)、[Positional Encoding](../concepts/positional-encoding.md)、[Embedding](../concepts/embedding.md)、[Encoder-Decoder](../concepts/encoder-decoder.md)

## 是什麼

Transformer 是第一個**完全只靠 attention** 的序列轉換模型（例如翻譯），不使用 [RNN](../concepts/rnn.md)，也不使用卷積網路。它保留了 [Encoder-Decoder](../concepts/encoder-decoder.md) 的整體結構。〔出處：[Vaswani 2017 摘要、§2、§3](../papers/vaswani-2017.md)〕

## 資料流程

1. 輸入的字先經過 [Embedding](../concepts/embedding.md) 轉成向量，再加上 [Positional Encoding](../concepts/positional-encoding.md) 補上位置資訊。〔出處：[Vaswani 2017 §3.4、§3.5](../papers/vaswani-2017.md)〕
2. 向量經過 **Encoder** 的 6 層處理。〔出處：[Vaswani 2017 §3.1](../papers/vaswani-2017.md)〕
3. **Decoder** 的 6 層一邊參考 Encoder 的輸出，一邊根據已經產生的字預測下一個字。〔出處：[Vaswani 2017 §3、§3.1](../papers/vaswani-2017.md)〕
4. Decoder 的輸出經過線性轉換和 [Softmax](../concepts/softmax.md)，得到每個候選字的機率。〔出處：[Vaswani 2017 §3.4](../papers/vaswani-2017.md)〕

## Encoder 的每一層

每層有兩個子層：〔出處：[Vaswani 2017 §3.1、§3.3](../papers/vaswani-2017.md)〕

- **多頭自注意力**（[Multi-Head](../concepts/multi-head-attention.md) [Self-Attention](../concepts/self-attention.md)）：每個字看句子裡所有的字。
- **前饋網路（FFN）**：對每個位置各自做兩次線性轉換，中間夾一個 ReLU。每個位置使用相同的參數。

每個子層外面都包著**殘差連接**（把輸入直接加回輸出）和 **LayerNorm**（正規化）。寫成式子是 `LayerNorm(x + Sublayer(x))`。〔出處：[Vaswani 2017 §3.1](../papers/vaswani-2017.md)〕

## Decoder 的每一層

在 Encoder 的兩個子層之外，Decoder 多了第三個子層，總共三個：〔出處：[Vaswani 2017 §3.1、§3.2.3](../papers/vaswani-2017.md)〕

- **遮罩自注意力（masked self-attention）**：只能看自己和前面已經產生的字，不能偷看後面的字。
- **Encoder-Decoder Attention**：Query 來自 Decoder，Key 和 Value 來自 Encoder 的輸出，作用就像 [Bahdanau 2014](../papers/bahdanau-2014.md) 的 [Attention](../concepts/attention.md)。
- **前饋網路（FFN）**

## 基本設定（base 模型）

| 參數 | 值 | 意義 |
|---|---|---|
| N | 6 | Encoder、Decoder 各自的層數 |
| d_model | 512 | 每個字向量的維度 |
| d_ff | 2048 | FFN 中間層的維度 |
| h | 8 | attention 的頭數 |
| d_k = d_v | 64 | 每個頭的 Key／Value 維度（= 512 / 8） |
〔出處：[Vaswani 2017 §3.1、§3.2.2、§3.3、表 3](../papers/vaswani-2017.md)〕

## 優點

- 可以平行計算，訓練時間大幅縮短。〔出處：[Vaswani 2017 §1、§4、§6.1](../papers/vaswani-2017.md)〕
- 任兩個字之間只要一步就能互相影響，容易學到遠距離的關係。〔出處：[Vaswani 2017 §4、表 1](../papers/vaswani-2017.md)〕
- 翻譯品質超越當時所有模型。〔出處：[Vaswani 2017 §6.1、表 2](../papers/vaswani-2017.md)〕

## 後續變化與用語

後來的模型常常只取 Transformer 的一半來用。在文獻中，雙向的版本常被稱為「Transformer encoder」，只看左邊的版本因為可以用來生成文字，常被稱為「Transformer decoder」。〔出處：[Devlin 2018 §3 註 4](../papers/devlin-2018.md)〕

- **只用 Encoder**：例如 [BERT](bert.md)。〔出處：[Devlin 2018 §3](../papers/devlin-2018.md)〕
- **只用由左到右的 Decoder**：例如 OpenAI GPT。〔出處：[Devlin 2018 §1、附錄 A.4](../papers/devlin-2018.md)〕
- **保留 Encoder-Decoder**：例如 [T5](t5.md)。〔出處：[Raffel 2019 §3.1.1](../papers/raffel-2019.md)〕
- [GPT-3](gpt-3.md) 沿用 GPT 系列的自迴歸架構，放大到 1,750 億參數；它屬於這一類是推論而來，詳見該頁。〔出處：[Brown 2020 摘要、§2.1](../papers/brown-2020.md)〕

⚠️ 用語差異：原始 Transformer 的 Decoder 除了遮罩 self-attention，還有一層看 Encoder 輸出的 Encoder-Decoder Attention。只有 Decoder 的模型沒有 Encoder 可看，所以「Transformer decoder」這個稱呼和原始論文的 Decoder 並不完全相同。〔出處：[Vaswani 2017 §3.1](../papers/vaswani-2017.md)、[Devlin 2018 §3 註 4](../papers/devlin-2018.md)〕

四種架構的完整比較，見 [Transformer 架構家族](../concepts/architecture-variants.md)。〔出處：[Raffel 2019 §3.2](../papers/raffel-2019.md)〕

⚠️ 設計變化：[T5](t5.md) 把 LayerNorm 放在每個子層的**輸入**，[ViT](vit.md) 也把 LayerNorm 放在每個區塊之前，而不是本頁寫的「殘差相加之後」。這幾篇論文不衝突，只是不同的設計。〔出處：[Raffel 2019 §2.1](../papers/raffel-2019.md)、[Dosovitskiy 2020 §3.1](../papers/dosovitskiy-2020.md)、[Vaswani 2017 §3.1](../papers/vaswani-2017.md)〕

- **從文字跨到圖片**：[ViT](vit.md) 把圖片切成 patch，直接使用標準的 Transformer Encoder。〔出處：[Dosovitskiy 2020 §3.1](../papers/dosovitskiy-2020.md)〕
