# Dosovitskiy 2020：An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale（ViT）

> **類型**：論文 ｜ **出處**：[arXiv:2010.11929](https://arxiv.org/abs/2010.11929)（Dosovitskiy 等，Google Research, Brain Team；ICLR 2021） ｜ **相關**：[ViT](../models/vit.md)、[Patch Embedding](../concepts/patch-embedding.md)、[歸納偏置](../concepts/inductive-bias.md)、[Vaswani 2017](vaswani-2017.md)、[Devlin 2018](devlin-2018.md)

## 一句話摘要

把圖片切成小塊（patch），把每一塊當成一個「字」，直接丟進標準的 Transformer Encoder 做圖片分類。只要預訓練資料夠多，表現就能追上甚至超越當時最好的卷積網路，而且訓練所需的運算更少。〔出處：摘要、§1，[原文](https://arxiv.org/abs/2010.11929)〕

## 要解決的問題

Transformer 已經是 NLP 的標準架構，但在電腦視覺中，attention 通常只是搭配卷積網路（CNN）使用，或取代 CNN 的部分元件，大型圖片辨識仍以 ResNet 這類 CNN 為主。〔出處：摘要、§1，[原文](https://arxiv.org/abs/2010.11929)〕

如果直接讓每個像素都對其他所有像素做 self-attention，計算量會隨像素數平方成長，無法用在實際大小的圖片上。過去的替代做法多半需要特殊的 attention 樣式，在硬體上很難有效率地實作。〔出處：§1、§2，[原文](https://arxiv.org/abs/2010.11929)〕

## 提出的方法

作者盡量照原始 Transformer 設計，好處是可擴展的 NLP Transformer 架構和實作幾乎可以直接拿來用。完整流程見 [ViT](../models/vit.md)：〔出處：§3.1，[原文](https://arxiv.org/abs/2010.11929)〕

1. 把圖片切成固定大小的 patch，攤平後經過線性轉換變成向量。詳見 [Patch Embedding](../concepts/patch-embedding.md)。
2. 在最前面加上一個可學習的分類 token，作用類似 BERT 的 `[class]` token。
3. 加上位置 embedding。
4. 丟進標準的 Transformer Encoder，最後用分類 token 的輸出做分類。


## 主要發現：資料量決定一切

〔出處：§1、§4.3，[原文](https://arxiv.org/abs/2010.11929)〕

- 只在 ImageNet 這種中型資料集上訓練時，ViT 的準確率比同樣大小的 ResNet 低幾個百分點。作者的解釋是 Transformer 缺少 CNN 內建的[歸納偏置](../concepts/inductive-bias.md)，資料不夠時推廣能力較差。
- 在更大的資料集（1,400 萬到 3 億張圖片）上預訓練後，情況反轉。作者的結論是：**大規模訓練勝過歸納偏置**。

## 主要結果

- 最好的模型在 ImageNet 達到 88.55%、ImageNet-ReaL 90.72%、CIFAR-100 94.55%、VTAB（19 個任務）77.63%。〔出處：§1，[原文](https://arxiv.org/abs/2010.11929)〕
- 在「表現 vs. 運算量」上，ViT 全面勝過 ResNet：達到同樣表現約只需 1/2 到 1/4 的運算。〔出處：§4.4，[原文](https://arxiv.org/abs/2010.11929)〕
- ViT 在實驗範圍內還沒有出現飽和的跡象，值得繼續放大。〔出處：§4.4，[原文](https://arxiv.org/abs/2010.11929)〕

## 模型學到了什麼

〔出處：§4.5，[原文](https://arxiv.org/abs/2010.11929)〕

- 位置 embedding 自己學會了圖片的 2D 結構：距離越近的 patch，位置 embedding 越相似，而且同一行或同一列的 patch 也比較相似。
- Self-attention 讓 ViT 在最底層就能整合整張圖的資訊。有些頭在最底層就已經看向大部分的圖片，有些頭則只看局部；而 attention 看的距離會隨著層數加深而變大。

## 自監督預訓練的初步實驗

模仿 BERT 的 masked language modeling，改成「遮住 patch 讓模型猜」。ViT-B/16 在 ImageNet 達到 79.9%，比從零訓練好 2%，但仍比監督式預訓練差 4%。〔出處：§4.6，[原文](https://arxiv.org/abs/2010.11929)〕

## 未來方向

把 ViT 用到偵測、分割等其他視覺任務；繼續探索自監督預訓練；繼續放大模型。〔出處：§5，[原文](https://arxiv.org/abs/2010.11929)〕

## 在這個 Wiki 中的位置

ViT 實現了 [Vaswani 2017](vaswani-2017.md) 結論中「把 Transformer 用到文字以外的資料」的展望：把圖片視為一串 patch，用 NLP 所用的標準 Transformer Encoder 處理。〔出處：§5，[原文](https://arxiv.org/abs/2010.11929)；[Vaswani 2017 §7](vaswani-2017.md)〕
