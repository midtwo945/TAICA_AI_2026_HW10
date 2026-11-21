# Multi-Head Attention（多頭注意力）

> **類型**：概念 ｜ **出處**：[Vaswani 2017](../papers/vaswani-2017.md) ｜ **相關**：[Self-Attention](self-attention.md)、[Transformer](../models/transformer.md)

## 是什麼

不只做一次 attention，而是**同時做好幾組**（稱為「頭」），每組用不同的學習矩陣把 Q、K、V 投影到較小的維度，各自計算 [Self-Attention](self-attention.md)，最後把結果接起來，再做一次線性轉換。〔出處：[Vaswani 2017 §3.2.2](../papers/vaswani-2017.md)〕

```
MultiHead(Q, K, V) = Concat(head_1, …, head_h) · W^O
head_i = Attention(Q·W_i^Q, K·W_i^K, V·W_i^V)
```

## 為什麼需要多個頭

只有一個頭時，所有資訊會被平均在一起，模型很難同時關注不同面向。多個頭可以讓模型**同時從不同角度**看句子。論文觀察到不同的頭確實學會了不同的任務，很多頭的行為和句子的文法、語意結構有關。〔出處：[Vaswani 2017 §3.2.2、§4](../papers/vaswani-2017.md)〕

## Transformer 的設定

Transformer 使用 h = 8 個頭，每個頭的維度是 d_k = d_v = 512 / 8 = 64。因為每個頭的維度變小了，總計算量和「一個全維度的頭」差不多。〔出處：[Vaswani 2017 §3.2.2](../papers/vaswani-2017.md)〕

## 頭數的影響

論文在固定總計算量的前提下改變頭數：只用 1 個頭時，BLEU 比最佳設定低 0.9；但頭太多，品質也會下降。〔出處：[Vaswani 2017 §6.2、表 3 (A)](../papers/vaswani-2017.md)〕
