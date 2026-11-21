# Embedding（嵌入／字向量）

> **類型**：概念 ｜ **出處**：[Vaswani 2017](../papers/vaswani-2017.md)、[Bahdanau 2014](../papers/bahdanau-2014.md)、[Devlin 2018](../papers/devlin-2018.md)、[Raffel 2019](../papers/raffel-2019.md) ｜ **相關**：[T5](../models/t5.md)、[Positional Encoding](positional-encoding.md)、[Transformer](../models/transformer.md)、[BERT](../models/bert.md)

## 是什麼

神經網路只能處理數字，所以要先把每個字（token）轉成一個向量，這個步驟就是 embedding。Transformer 使用**學習出來的** embedding，把每個 token 轉成 d_model = 512 維的向量。〔出處：[Vaswani 2017 §3.4](../papers/vaswani-2017.md)〕

## Token：模型看到的「字」

模型處理的單位叫做 token，不一定等於一個完整的單字：〔出處：[Bahdanau 2014 §4.1](../papers/bahdanau-2014.md)、[Vaswani 2017 §5.1](../papers/vaswani-2017.md)〕

- [Bahdanau 2014](../papers/bahdanau-2014.md) 以**完整單字**為單位，只保留每種語言最常見的 30,000 個字，其他字一律變成特殊符號 `[UNK]`（未知字）。這也是它不擅長處理罕見字的原因之一。
- [Vaswani 2017](../papers/vaswani-2017.md) 使用 byte-pair encoding 和 word-piece，把單字切成較小的片段。英德翻譯共用約 37,000 個 token，英法翻譯約 32,000 個。

## 在 Transformer 中的細節

- Embedding 之後會加上 [Positional Encoding](positional-encoding.md)，補上位置資訊。〔出處：[Vaswani 2017 §3.5](../papers/vaswani-2017.md)〕
- 輸入的 embedding、輸出的 embedding，以及 softmax 前的線性轉換，三者共用同一個權重矩陣。〔出處：[Vaswani 2017 §3.4](../papers/vaswani-2017.md)〕

## BERT 的輸入：三種 embedding 相加

[BERT](../models/bert.md) 每個 token 的輸入向量，是以下三種 embedding 相加的結果：〔出處：[Devlin 2018 §3、圖 2](../papers/devlin-2018.md)〕

- **Token embedding**：這個 token 本身的向量。
- **Segment embedding**：標示這個 token 屬於句子 A 還是句子 B，是學習出來的向量。
- **Position embedding**：這個 token 的位置。

BERT 使用 WordPiece 切字，詞彙量 30,000。論文圖 2 的例子中，「playing」被切成 `play` 和 `##ing` 兩個 token。〔出處：[Devlin 2018 §3、圖 2](../papers/devlin-2018.md)〕

## T5 的詞彙表

[T5](../models/t5.md) 用 SentencePiece 切出 32,000 個 wordpiece。因為之後要做英翻德、法、羅馬尼亞文，詞彙表也必須涵蓋這些語言：訓練切字模型的資料是 10 份英文配上德、法、羅馬尼亞文各 1 份。輸入和輸出共用同一個詞彙表，代價是模型只能處理事先決定好的幾種語言。〔出處：[Raffel 2019 §3.1.3](../papers/raffel-2019.md)〕
