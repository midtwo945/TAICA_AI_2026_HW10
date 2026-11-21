# Attention（注意力機制）

> **類型**：概念 ｜ **出處**：[Bahdanau 2014](../papers/bahdanau-2014.md)、[Vaswani 2017](../papers/vaswani-2017.md) ｜ **相關**：[Softmax](softmax.md)、[Encoder-Decoder](encoder-decoder.md)、[RNN](rnn.md)、[Self-Attention](self-attention.md)

## 直覺

翻譯時，產生每個譯文字都只需要看原文的某幾個字。Attention 讓模型在每一步**自己決定要把注意力放在原文的哪些字上**，而不是只靠一個壓縮過的向量。〔出處：[Bahdanau 2014 §3.1](../papers/bahdanau-2014.md)〕

## 算法（Bahdanau 2014 版本）

假設 Encoder 已經為原文每個字 j 算出一個向量 `h_j`。Decoder 要產生第 i 個譯文字時：〔出處：[Bahdanau 2014 §3.1、式 (5)(6)](../papers/bahdanau-2014.md)〕

1. **算分數**：對原文每個字 j，算一個分數 `e_ij = a(s_{i-1}, h_j)`，表示「原文第 j 個字和現在要產生的字有多相關」。`s_{i-1}` 是 Decoder 上一步的隱藏狀態，`a` 是一個小型神經網路。
2. **轉成權重**：用 [Softmax](softmax.md) 把分數轉成權重 `α_ij`。所有權重都是正數，而且加起來等於 1。
3. **加權平均**：`c_i = Σ_j α_ij · h_j`。得到的 `c_i` 就是這一步專用的 context vector，再交給 Decoder 產生第 i 個字。

計算分數的函數 `a` 在論文中的形式是 `v_aᵀ tanh(W_a s_{i-1} + U_a h_j)`：先把兩個向量各自乘上矩陣後相加，再經過 tanh。〔出處：[Bahdanau 2014 附錄 A.1.2](../papers/bahdanau-2014.md)〕

[Vaswani 2017](../papers/vaswani-2017.md) 把這種用小型前饋網路算分數的方式稱為「加法式（additive）attention」，並引用 Bahdanau 2014 作為代表。〔出處：[Vaswani 2017 §3.2.1](../papers/vaswani-2017.md)〕

## 軟對齊 vs. 硬對齊

傳統翻譯系統會把每個譯文字**硬性**對到某一個原文字。Attention 是**軟對齊**：每個譯文字可以同時參考好幾個原文字，只是權重不同。〔出處：[Bahdanau 2014 §3.1、§5.2.1](../papers/bahdanau-2014.md)〕

例子：英文「the man」翻成法文「l' homme」。法文冠詞要用 le、la、les 還是 l'，取決於後面的名詞。軟對齊讓模型在產生「l'」時，可以同時看「the」和「man」。〔出處：[Bahdanau 2014 §5.2.1、圖 3(d)](../papers/bahdanau-2014.md)〕

因為整個過程都可以微分，負責算分數的網路可以跟翻譯模型一起訓練，不需要人工標註哪個字對哪個字。〔出處：[Bahdanau 2014 §3.1](../papers/bahdanau-2014.md)〕

## 好處

- 解決 [Encoder-Decoder](encoder-decoder.md) 把整句壓成固定長度向量的瓶頸，長句翻譯品質明顯改善。〔出處：[Bahdanau 2014 §5.1](../papers/bahdanau-2014.md)〕
- 權重可以畫成圖，看出模型翻譯每個字時在看哪裡，具有可解釋性。〔出處：[Bahdanau 2014 §5.2.1](../papers/bahdanau-2014.md)〕

## 後續發展：Transformer 的版本

[Vaswani 2017](../papers/vaswani-2017.md) 把算分數的方式從「加法式」改成**內積**再除以 √d_k，稱為 Scaled Dot-Product Attention。兩者理論複雜度相近，但內積可以直接用高度最佳化的矩陣乘法計算，實際上快很多，也更省記憶體。〔出處：[Vaswani 2017 §3.2.1](../papers/vaswani-2017.md)〕

Vaswani 2017 也把 attention 推廣成 Query、Key、Value 的形式，並讓句子對自己做 attention，也就是 [Self-Attention](self-attention.md)。Bahdanau 2014 這種「譯文看原文」的 attention，在 [Transformer](../models/transformer.md) 中稱為 Encoder-Decoder Attention。〔出處：[Vaswani 2017 §3.2、§3.2.3](../papers/vaswani-2017.md)〕
