# Self-Attention（自注意力）

> **類型**：概念 ｜ **出處**：[Vaswani 2017](../papers/vaswani-2017.md)、[Devlin 2018](../papers/devlin-2018.md)、[Raffel 2019](../papers/raffel-2019.md) ｜ **相關**：[Transformer 架構家族](architecture-variants.md)、[Attention](attention.md)、[Multi-Head Attention](multi-head-attention.md)、[Softmax](softmax.md)、[Transformer](../models/transformer.md)、[Masked Language Model](masked-language-model.md)

## 是什麼

Self-Attention 是一種在**同一個句子內部**計算 attention 的方法：每個字都去看句子裡的所有字（包括自己），根據相關程度把它們的資訊混合起來，得到新的向量。〔出處：[Vaswani 2017 §2、§3.2.3](../papers/vaswani-2017.md)〕

它和 [Bahdanau 2014](../papers/bahdanau-2014.md) 的 [Attention](attention.md) 不同：Bahdanau 是「譯文看原文」，Self-Attention 是「句子看自己」。〔出處：[Vaswani 2017 §2、§3.2.3](../papers/vaswani-2017.md)〕

## Query、Key、Value

Vaswani 2017 把 attention 描述成：用一個 **Query** 去和一組 **Key** 比對，根據比對結果對對應的 **Value** 加權平均。〔出處：[Vaswani 2017 §3.2](../papers/vaswani-2017.md)〕

- **Query（Q）**：我要找什麼
- **Key（K）**：我有什麼可以被找
- **Value（V）**：被找到之後要提供的內容

在 Self-Attention 中，Q、K、V 都來自同一個句子（同一層的輸入），各自乘上不同的學習矩陣得到。〔出處：[Vaswani 2017 §3.2.2、§3.2.3](../papers/vaswani-2017.md)〕

## Scaled Dot-Product Attention

Transformer 使用的算法是：〔出處：[Vaswani 2017 §3.2.1、式 (1)](../papers/vaswani-2017.md)〕

```
Attention(Q, K, V) = softmax( Q·Kᵀ / √d_k ) · V
```

1. 用 Q 和每個 K 做**內積**，得到分數。內積越大，代表越相關。
2. 分數**除以 √d_k**（d_k 是 Key 的維度）。
3. 用 [Softmax](softmax.md) 轉成權重。
4. 用權重對 V 加權平均。

實際計算時，所有字的 Q、K、V 各自排成矩陣，一次用矩陣乘法算完，所以可以平行處理。〔出處：[Vaswani 2017 §3.2.1](../papers/vaswani-2017.md)〕

**為什麼要除以 √d_k**：維度大的時候，內積的數值會變得很大，softmax 就會進入梯度極小的區域，模型很難學習。除以 √d_k 可以抵銷這個效果。〔出處：[Vaswani 2017 §3.2.1、註 4](../papers/vaswani-2017.md)〕

## 計算例子（簡化版）

為了方便理解，這裡省略學習矩陣，直接令 Q = K = V = 每個字的向量。假設句子有 3 個字，向量分別是 `[1,0]`、`[0,1]`、`[1,1]`，d_k = 2：〔出處：依 [Vaswani 2017 式 (1)](../papers/vaswani-2017.md) 以 Python 實際計算〕

| | 對字 1 的權重 | 對字 2 的權重 | 對字 3 的權重 | 輸出向量 |
|---|---|---|---|---|
| 字 1 `[1,0]` | 0.401 | 0.198 | 0.401 | `[0.802, 0.599]` |
| 字 2 `[0,1]` | 0.198 | 0.401 | 0.401 | `[0.599, 0.802]` |
| 字 3 `[1,1]` | 0.248 | 0.248 | 0.503 | `[0.752, 0.752]` |
〔出處：同上計算；每列權重加總為 1〕

字 1 跟自己和字 3 最像（都有第一維），所以權重集中在這兩個字上；輸出向量就是三個字的加權混合。〔出處：同上計算〕

## 遮罩（Mask）

在 Decoder 中，產生第 i 個字時不能偷看後面還沒產生的字。做法是在 softmax 之前，把「看向後面字」的分數設成 −∞，經過 softmax 後這些權重就變成 0。〔出處：[Vaswani 2017 §3.1、§3.2.3](../papers/vaswani-2017.md)〕

套用到上面的例子，字 1 只能看自己，權重是 `[1, 0, 0]`；字 2 能看字 1 和字 2，權重是 `[0.33, 0.67, 0]`；字 3 能看全部，權重不變。〔出處：依 [Vaswani 2017 §3.2.3](../papers/vaswani-2017.md) 以 Python 實際計算〕

## Transformer 裡的三種用法

〔出處：[Vaswani 2017 §3.2.3](../papers/vaswani-2017.md)〕

1. **Encoder 的 Self-Attention**：原文每個字看原文所有字。
2. **Decoder 的遮罩 Self-Attention**：譯文每個字只看自己和前面的字。
3. **Encoder-Decoder Attention**：Q 來自 Decoder，K 和 V 來自 Encoder，也就是「譯文看原文」，作用就像 [Bahdanau 2014](../papers/bahdanau-2014.md) 的 attention。

## 附帶好處：可解釋性

把 attention 權重畫出來，可以發現不同的頭各自學會不同的任務，很多頭的行為和句子的文法、語意結構有關。〔出處：[Vaswani 2017 §4](../papers/vaswani-2017.md)〕

## 雙向 vs. 只看左邊

是否使用遮罩，決定了模型能看的範圍：〔出處：[Devlin 2018 §1、§3](../papers/devlin-2018.md)〕

- **雙向**：每個 token 可以看左右兩邊所有的 token。[BERT](../models/bert.md) 採用這種方式，對理解文字較有利。
- **只看左邊**：每個 token 只能看前面的 token，也就是使用上面提到的遮罩。OpenAI GPT 採用這種方式，適合生成文字。

BERT-Base 和 OpenAI GPT 的架構幾乎相同，主要差別就在這一點。〔出處：[Devlin 2018 §4.1](../papers/devlin-2018.md)〕

⚠️ 這裡的「遮罩」是禁止 attention 看後面的字，和 BERT 預訓練時把輸入的字換成 `[MASK]`（見 [Masked Language Model](masked-language-model.md)）是兩件不同的事。〔出處：[Vaswani 2017 §3.2.3](../papers/vaswani-2017.md)、[Devlin 2018 §3.1](../papers/devlin-2018.md)〕

## 三種遮罩的名稱

[T5](../models/t5.md) 的論文為遮罩取了名稱：每個位置都能看全部的叫「全可見（fully-visible）」；只能看前面的叫「因果（causal）」；前綴部分全可見、其餘因果的叫「帶前綴的因果遮罩」。不同遮罩對應到不同的架構，詳見 [Transformer 架構家族](architecture-variants.md)。〔出處：[Raffel 2019 §3.2.1、圖 3](../papers/raffel-2019.md)〕
