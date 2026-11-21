# Bahdanau 2014：Neural Machine Translation by Jointly Learning to Align and Translate

> **類型**：論文 ｜ **出處**：[arXiv:1409.0473](https://arxiv.org/abs/1409.0473)（Bahdanau, Cho, Bengio；ICLR 2015） ｜ **相關**：[Encoder-Decoder](../concepts/encoder-decoder.md)、[RNN](../concepts/rnn.md)、[Attention](../concepts/attention.md)、[Softmax](../concepts/softmax.md)

## 一句話摘要

在 RNN 翻譯模型中加入「每產生一個譯文字，就回頭看原文哪些字最重要」的機制，解決了把整句壓縮成一個固定長度向量的瓶頸。這個機制後來被稱為 [Attention](../concepts/attention.md)。〔出處：§1、§3.1，[原文](https://arxiv.org/abs/1409.0473)〕

## 要解決的問題

當時的神經機器翻譯多採用 [Encoder-Decoder](../concepts/encoder-decoder.md) 架構：Encoder 把整句原文壓縮成一個固定長度的向量，Decoder 再根據這個向量產生譯文。不論句子多長都要塞進同一個大小的向量，作者認為這是提升效能的瓶頸，而且先前研究已發現句子越長，表現下降得越快。〔出處：§1，[原文](https://arxiv.org/abs/1409.0473)〕

## 提出的方法

1. **Encoder 改用雙向 [RNN](../concepts/rnn.md)**：從前往後、從後往前各讀一次，把兩個方向的隱藏狀態接起來，作為每個字的向量（論文稱為 annotation）。這樣每個字的向量同時包含前文與後文的資訊。〔出處：§3.2，[原文](https://arxiv.org/abs/1409.0473)〕
2. **Decoder 每一步都重新決定要看哪裡**：產生第 i 個譯文字之前，先對原文每個字算一個分數，用 [Softmax](../concepts/softmax.md) 轉成權重，再把所有 annotation 加權平均，得到這一步專用的 context vector。詳細算法見 [Attention](../concepts/attention.md)。〔出處：§3.1、式 (5)(6)，[原文](https://arxiv.org/abs/1409.0473)〕
3. **全部一起訓練**：負責算分數的對齊模型（alignment model）是一個小型前饋神經網路，與翻譯模型的其他部分一起訓練。〔出處：§3.1、附錄 A.1.2，[原文](https://arxiv.org/abs/1409.0473)〕

論文將這個模型命名為 **RNNsearch**，並指出這「直覺上在 Decoder 中實現了 attention 機制」。〔出處：§3.1、§4.2，[原文](https://arxiv.org/abs/1409.0473)〕

## 主要結果

- 英翻法任務的 BLEU 分數（越高代表翻譯品質越好）：以 50 字以內句子訓練的 RNNsearch-50 為 26.75，舊架構 RNNencdec-50 為 17.82。〔出處：§5.1、表 1，[原文](https://arxiv.org/abs/1409.0473)〕
- 舊架構遇到長句時分數明顯下降；RNNsearch-50 在句長 50 字以上時也沒有退步。〔出處：§5.1、圖 2，[原文](https://arxiv.org/abs/1409.0473)〕
- 只看不含生字的句子時，RNNsearch 的表現與當時主流的傳統片語式翻譯系統 Moses 相當。〔出處：§5.1、表 1，[原文](https://arxiv.org/abs/1409.0473)〕
- 把權重畫成圖，可以看到模型自己學會了詞序對應。例如英文「European Economic Area」對到法文「zone économique européenne」，詞序相反，模型也能正確對齊。〔出處：§5.2.1、圖 3，[原文](https://arxiv.org/abs/1409.0473)〕

## 限制

作者在結論指出，生字與罕見字的處理仍是未來要解決的問題。〔出處：§7，[原文](https://arxiv.org/abs/1409.0473)〕

## 在這個 Wiki 中的位置

本篇是 Transformer 的「前傳」：attention 在這裡仍然搭配 RNN 使用，作為 RNN 的輔助機制。〔出處：§3，[原文](https://arxiv.org/abs/1409.0473)〕
