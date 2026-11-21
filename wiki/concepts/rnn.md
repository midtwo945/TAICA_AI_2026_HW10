# RNN（循環神經網路）

> **類型**：概念 ｜ **出處**：[Bahdanau 2014](../papers/bahdanau-2014.md)、[Vaswani 2017](../papers/vaswani-2017.md) ｜ **相關**：[Encoder-Decoder](encoder-decoder.md)、[Attention](attention.md)、[Transformer](../models/transformer.md)

## 是什麼

RNN（Recurrent Neural Network）是一種**按順序**一個字一個字讀入序列的神經網路。讀到第 t 個字時，它會結合「這個字」和「上一步的隱藏狀態」，算出新的隱藏狀態：〔出處：[Bahdanau 2014 §2.1、式 (1)](../papers/bahdanau-2014.md)〕

```
h_t = f(x_t, h_{t-1})
```

- `x_t`：第 t 個字的向量
- `h_t`：讀到第 t 個字時的隱藏狀態，可以想成「到目前為止讀到內容的摘要」
- `f`：一個非線性函數，例如 LSTM（一種改良過的 RNN 單元）

## 特性

RNN 傾向於把**最近讀到的字**記得比較清楚，所以第 t 步的隱藏狀態會比較偏重第 t 個字附近的內容。〔出處：[Bahdanau 2014 §3.2](../papers/bahdanau-2014.md)〕

## 雙向 RNN（BiRNN）

一般 RNN 只從前往後讀，所以每個位置只知道前文。雙向 RNN 用兩個 RNN：一個從前往後讀，一個從後往前讀，再把兩個方向在同一個位置的隱藏狀態接起來。如此每個字的向量同時包含前文和後文的資訊。〔出處：[Bahdanau 2014 §3.2](../papers/bahdanau-2014.md)〕

## 在翻譯中的角色

在早期的 [Encoder-Decoder](encoder-decoder.md) 中，Encoder 和 Decoder 都用 RNN 實作。[Bahdanau 2014](../papers/bahdanau-2014.md) 用雙向 RNN 當 Encoder，並在 Decoder 加入 [Attention](attention.md)。〔出處：[Bahdanau 2014 §2.1、§3](../papers/bahdanau-2014.md)〕

## 限制：無法平行計算

RNN 第 t 步的計算要用到第 t-1 步的結果，所以必須一步一步依序算，同一個句子內無法平行處理。句子越長，這個限制越嚴重。〔出處：[Vaswani 2017 §1](../papers/vaswani-2017.md)〕

此外，句子中相隔很遠的兩個字，資訊要經過 O(n) 步才能傳到彼此，n 是句子長度，這讓 RNN 較難學到遠距離的關係。[Transformer](../models/transformer.md) 用 [Self-Attention](self-attention.md) 取代 RNN，解決了這兩個問題。〔出處：[Vaswani 2017 §4、表 1](../papers/vaswani-2017.md)〕
