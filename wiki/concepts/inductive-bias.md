# 歸納偏置（Inductive Bias）

> **類型**：概念 ｜ **出處**：[Dosovitskiy 2020](../papers/dosovitskiy-2020.md) ｜ **相關**：[ViT](../models/vit.md)、[規模化](scaling.md)、[Patch Embedding](patch-embedding.md)

## 是什麼

指模型架構中**事先內建**的假設。ViT 論文以 CNN 為例：CNN 的每一層都內建了「局部性」、「二維鄰近結構」和「平移等變性」這些圖片專用的假設。〔出處：[Dosovitskiy 2020 §1、§3.1](../papers/dosovitskiy-2020.md)〕

## ViT 的歸納偏置很少

ViT 中只有 MLP 層是局部且平移等變的，self-attention 層則是全域的。二維結構只在兩個地方用到：一開始把圖片切成 patch，以及微調時依原圖位置調整位置 embedding。除此之外，位置 embedding 初始化時不帶任何 2D 位置資訊，patch 之間的空間關係都要從零學起。〔出處：[Dosovitskiy 2020 §3.1、§3.2](../papers/dosovitskiy-2020.md)〕

## 取捨：歸納偏置 vs. 資料量

〔出處：[Dosovitskiy 2020 §1、§4.3、圖 3、圖 4](../papers/dosovitskiy-2020.md)〕

| 預訓練資料 | 結果 |
|---|---|
| 少（ImageNet，130 萬張） | ViT 比同樣大小的 ResNet 低幾個百分點；ViT-Large 甚至不如 ViT-Base |
| 中（ImageNet-21k，1,400 萬張） | Large 與 Base 表現差不多 |
| 多（JFT-300M，3 億張） | ViT 反超 ResNet，大模型的優勢才完全發揮 |
〔出處：同上〕

作者用 JFT 的子集做對照：在 900 萬張的子集上，ViT-B/32 比運算量相近的 ResNet50 差很多；但在 9,000 萬張以上的子集上，ViT 反而比較好。〔出處：[Dosovitskiy 2020 §4.3](../papers/dosovitskiy-2020.md)〕

作者的結論：卷積的歸納偏置在資料少時很有用；資料夠多時，直接從資料中學出需要的模式就足夠，甚至更好。也就是「大規模訓練勝過歸納偏置」。〔出處：[Dosovitskiy 2020 §1、§4.3](../papers/dosovitskiy-2020.md)〕

## 證據：模型自己學會了 2D 結構

雖然位置 embedding 一開始不帶 2D 資訊，訓練後卻學會了圖片的 2D 拓撲：距離近的 patch 位置 embedding 比較相似，同一行或同一列的也比較相似。這也解釋了為什麼人工設計的 2D 位置 embedding 沒有帶來改善。〔出處：[Dosovitskiy 2020 §4.5](../papers/dosovitskiy-2020.md)〕
