# Softmax

> **類型**：概念 ｜ **出處**：[Bahdanau 2014](../papers/bahdanau-2014.md)、[Vaswani 2017](../papers/vaswani-2017.md) ｜ **相關**：[Attention](attention.md)、[Self-Attention](self-attention.md)

## 是什麼

Softmax 是一個把「一串任意分數」轉成「一串加起來等於 1 的正數權重」的函數。在 [Attention](attention.md) 裡，它用來把相關程度的分數轉成權重。〔出處：[Bahdanau 2014 式 (6)、附錄 A.1](../papers/bahdanau-2014.md)〕

## 公式

對分數 `e_1, e_2, …, e_T`，第 j 個權重為：〔出處：[Bahdanau 2014 式 (6)](../papers/bahdanau-2014.md)〕

```
α_j = exp(e_j) / Σ_k exp(e_k)
```

- `exp` 是指數函數，會把任何數字變成正數，而且分數越大，結果放大得越多。
- 除以總和之後，所有權重加起來剛好等於 1。

## 計算例子

分數 `[2.0, 1.0, 0.1]` 經過 softmax 後，約為 `[0.659, 0.242, 0.099]`，總和為 1。分數最高的項目拿到大部分權重，但其他項目仍保有一些權重。這正是 [Attention](attention.md) 「軟對齊」的基礎。〔出處：依 [Bahdanau 2014 式 (6)](../papers/bahdanau-2014.md) 以 Python 實際計算〕

## 其他用途

Bahdanau 2014 也在 Decoder 的最後一步使用 softmax，把每個候選字的分數轉成機率，以決定下一個字。〔出處：[Bahdanau 2014 附錄 A.1.1](../papers/bahdanau-2014.md)〕

## 在 Transformer 中的注意事項

**分數太大會出問題**：[Self-Attention](self-attention.md) 用內積算分數。向量維度 d_k 很大時，內積的數值也會很大，softmax 會被推到梯度極小的區域，模型很難學習。因此 Transformer 先把分數除以 √d_k，再做 softmax。〔出處：[Vaswani 2017 §3.2.1、註 4](../papers/vaswani-2017.md)〕

以 Python 模擬：兩個隨機向量的每個元素都是平均 0、變異數 1 時，維度 4、64、512 的內積變異數分別約為 4、64、534，與論文註 4「變異數為 d_k」的說法一致。除以 √d_k 之後，變異數就回到 1 左右。〔出處：依 [Vaswani 2017 註 4](../papers/vaswani-2017.md) 以 Python 實際模擬（每組 4,000 次）〕

**用 −∞ 做遮罩**：把某個分數設成 −∞，經過 softmax 後該項權重會變成 0。Transformer 的 Decoder 用這個方法，禁止模型看到後面還沒產生的字。〔出處：[Vaswani 2017 §3.2.3](../papers/vaswani-2017.md)〕

**輸出機率**：Transformer 也在 Decoder 的最後一步用 softmax，把每個候選 token 的分數轉成機率。〔出處：[Vaswani 2017 §3.4](../papers/vaswani-2017.md)〕
