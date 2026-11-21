# Positional Encoding（位置編碼）

> **類型**：概念 ｜ **出處**：[Vaswani 2017](../papers/vaswani-2017.md)、[Raffel 2019](../papers/raffel-2019.md)、[Dosovitskiy 2020](../papers/dosovitskiy-2020.md) ｜ **相關**：[ViT](../models/vit.md)、[T5](../models/t5.md)、[Embedding](embedding.md)、[Transformer](../models/transformer.md)、[RNN](rnn.md)

## 為什麼需要

[RNN](rnn.md) 依照順序一個字一個字讀，所以天生知道字的順序。[Transformer](../models/transformer.md) 拿掉了 RNN，[Self-Attention](self-attention.md) 本身不管字的先後，所以必須額外告訴模型每個字在第幾個位置。〔出處：[Vaswani 2017 §3.5](../papers/vaswani-2017.md)〕

## 做法

為每個位置產生一個和字向量維度相同（d_model）的「位置向量」，直接**加**到字的 [Embedding](embedding.md) 上。〔出處：[Vaswani 2017 §3.5](../papers/vaswani-2017.md)〕

Vaswani 2017 用不同頻率的 sin 和 cos 函數產生位置向量：〔出處：[Vaswani 2017 §3.5](../papers/vaswani-2017.md)〕

```
PE(pos, 2i)   = sin( pos / 10000^(2i/d_model) )
PE(pos, 2i+1) = cos( pos / 10000^(2i/d_model) )
```

- `pos`：字的位置（第幾個字）
- `i`：向量的第幾個維度。每個維度對應一個頻率不同的正弦波。

選擇這種函數的原因：作者推測，對任意固定的距離 k，位置 pos+k 的編碼都能用位置 pos 的編碼做線性轉換得到，模型因此比較容易學會「相對位置」。〔出處：[Vaswani 2017 §3.5](../papers/vaswani-2017.md)〕

## 另一種做法：學出來的位置向量

作者也試過讓模型自己學位置向量，結果和 sin／cos 版本幾乎一樣。最後選 sin／cos，是因為它可能讓模型處理比訓練時更長的句子。〔出處：[Vaswani 2017 §3.5、表 3 (E)](../papers/vaswani-2017.md)〕

## 後續變化：相對位置 Embedding

Self-attention 本身不管順序（它是對「集合」的運算），所以一定要額外提供位置資訊。[T5](../models/t5.md) 的論文指出，原始 Transformer 使用 sin／cos 或學習出來的位置向量，但後來越來越常使用**相對位置 embedding**：不是為每個位置學一個固定向量，而是依照 Query 和 Key 之間的**距離**學不同的 embedding。〔出處：[Raffel 2019 §2.1](../papers/raffel-2019.md)〕

T5 使用簡化版：每個「embedding」只是一個純量，直接加到計算 attention 權重的分數上。共有 32 個，對應的距離範圍以對數方式變大，距離超過 128 的全部共用同一個。所有層共用這些參數，但同一層內每個頭各有自己的一組。〔出處：[Raffel 2019 §2.1](../papers/raffel-2019.md)〕

## ViT：位置 embedding 自己學會 2D 結構

[ViT](../models/vit.md) 把圖片切成 patch 後，使用一般可學習的 1D 位置 embedding。作者試過更進階、考慮 2D 的位置 embedding，沒有觀察到明顯的改善。〔出處：[Dosovitskiy 2020 §3.1](../papers/dosovitskiy-2020.md)〕

原因是模型自己學會了 2D 結構：訓練後，距離越近的 patch 位置 embedding 越相似，同一行或同一列的 patch 也比較相似。〔出處：[Dosovitskiy 2020 §4.5](../papers/dosovitskiy-2020.md)〕

微調時如果改用更高的解析度，patch 數變多，預訓練好的位置 embedding 會依照它們在原圖中的位置做 2D 內插。〔出處：[Dosovitskiy 2020 §3.2](../papers/dosovitskiy-2020.md)〕
