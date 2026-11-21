# Encoder-Decoder（編碼器-解碼器）

> **類型**：概念 ｜ **出處**：[Bahdanau 2014](../papers/bahdanau-2014.md)、[Vaswani 2017](../papers/vaswani-2017.md) ｜ **相關**：[RNN](rnn.md)、[Attention](attention.md)、[Transformer](../models/transformer.md)

## 是什麼

一種處理「輸入一段序列、輸出另一段序列」的架構，最典型的用途是翻譯。它由兩個部分組成：〔出處：[Bahdanau 2014 §1、§2.1](../papers/bahdanau-2014.md)〕

- **Encoder（編碼器）**：讀入原文，把它轉成向量表示。
- **Decoder（解碼器）**：根據 Encoder 給的向量，逐字產生譯文。每次預測下一個字時，會參考已經產生的字。

兩個部分會一起訓練，目標是讓「給定原文時，產生正確譯文」的機率越大越好。〔出處：[Bahdanau 2014 §1、§2](../papers/bahdanau-2014.md)〕

## 早期做法：固定長度向量

早期的 Encoder-Decoder 通常用 [RNN](rnn.md) 實作。Encoder 讀完整句之後，把整句資訊壓縮成**一個固定長度的向量**，Decoder 只能根據這個向量來翻譯。〔出處：[Bahdanau 2014 §2.1](../papers/bahdanau-2014.md)〕

## 問題：瓶頸

不論句子長短，都要塞進同一個大小的向量裡。句子一長，資訊就裝不下。實驗也顯示，這種架構的翻譯品質會隨句子變長而快速下降。〔出處：[Bahdanau 2014 §1、§5.1](../papers/bahdanau-2014.md)〕

## 解法：加入 Attention

[Bahdanau 2014](../papers/bahdanau-2014.md) 的做法是讓 Encoder 為**每個字**都保留一個向量，Decoder 每產生一個字，就用 [Attention](attention.md) 決定這一步要看原文的哪些字。如此就不必把整句壓成單一向量。〔出處：[Bahdanau 2014 §3](../papers/bahdanau-2014.md)〕

## Transformer：不用 RNN 的 Encoder-Decoder

[Transformer](../models/transformer.md) 保留了 Encoder-Decoder 的整體結構：Encoder 把輸入轉成一串向量，Decoder 每次產生一個字，並把已經產生的字當作下一步的輸入。差別在於 Encoder 和 Decoder 內部都不用 [RNN](rnn.md)，改用 [Self-Attention](self-attention.md)。〔出處：[Vaswani 2017 §3](../papers/vaswani-2017.md)〕
