# Vaswani 2017：Attention Is All You Need

> **類型**：論文 ｜ **出處**：[arXiv:1706.03762](https://arxiv.org/abs/1706.03762)（Vaswani 等，Google Brain／Google Research；NIPS 2017） ｜ **相關**：[Transformer](../models/transformer.md)、[Self-Attention](../concepts/self-attention.md)、[Multi-Head Attention](../concepts/multi-head-attention.md)、[Positional Encoding](../concepts/positional-encoding.md)、[Embedding](../concepts/embedding.md)、[Bahdanau 2014](bahdanau-2014.md)

## 一句話摘要

提出 [Transformer](../models/transformer.md)：保留 [Encoder-Decoder](../concepts/encoder-decoder.md) 結構，但完全拿掉 [RNN](../concepts/rnn.md)，只用 attention。翻譯品質更好，訓練也更快。〔出處：摘要、§1，[原文](https://arxiv.org/abs/1706.03762)〕

## 要解決的問題

RNN 必須依照字的順序一步一步計算，第 t 步要等第 t-1 步算完。這種先天的循序性讓同一個句子內無法平行計算，句子越長，問題越嚴重。〔出處：§1，[原文](https://arxiv.org/abs/1706.03762)〕

當時的 attention 幾乎都是搭配 RNN 使用，例如 [Bahdanau 2014](bahdanau-2014.md)。〔出處：§1，[原文](https://arxiv.org/abs/1706.03762)〕

## 提出的方法

1. **[Self-Attention](../concepts/self-attention.md)**：讓句子裡每個字都直接看其他所有字，用 Query、Key、Value 三種向量計算，並採用 Scaled Dot-Product 的算法。〔出處：§3.2.1、§3.2.3，[原文](https://arxiv.org/abs/1706.03762)〕
2. **[Multi-Head Attention](../concepts/multi-head-attention.md)**：同時做 8 組 attention，每組關注不同面向。〔出處：§3.2.2，[原文](https://arxiv.org/abs/1706.03762)〕
3. **[Positional Encoding](../concepts/positional-encoding.md)**：沒有 RNN 之後模型不知道字的順序，所以要額外加上位置資訊。〔出處：§3.5，[原文](https://arxiv.org/abs/1706.03762)〕
4. **整體架構**：Encoder、Decoder 各疊 6 層，詳見 [Transformer](../models/transformer.md)。〔出處：§3.1，[原文](https://arxiv.org/abs/1706.03762)〕

## 為什麼用 Self-Attention（與 RNN 比較）

論文從三個面向比較（表 1）：〔出處：§4、表 1，[原文](https://arxiv.org/abs/1706.03762)〕

- **能否平行計算**：Self-Attention 需要的循序步驟數是 O(1)，RNN 是 O(n)，n 為句子長度。
- **遠距離的字要經過幾步才能互相影響**：Self-Attention 是 O(1)，任兩個字直接相連；RNN 是 O(n)。路徑越短，越容易學到遠距離的關係。
- **每層計算量**：句子長度 n 小於向量維度 d 時（翻譯任務通常如此），Self-Attention 比 RNN 快。

## 主要結果

- 英翻德：Transformer (big) 的 BLEU 為 28.4，比之前最好的成績（包含多模型集成）高出 2 分以上。〔出處：§6.1、表 2，[原文](https://arxiv.org/abs/1706.03762)〕
- 英翻法：摘要與表 2 寫 BLEU **41.8**，是當時單一模型的最佳成績。〔出處：摘要、表 2，[原文](https://arxiv.org/abs/1706.03762)〕
- ⚠️ **原文矛盾（R6）**：§6.1 內文寫英翻法 BLEU 為 **41.0**，與摘要和表 2 的 41.8 不一致。本 Wiki 採用摘要與表 2 的 41.8，並在此保留矛盾紀錄。〔出處：摘要、§6.1、表 2，[原文](https://arxiv.org/abs/1706.03762)〕
- 訓練成本：base 模型用 8 張 P100 GPU 訓練約 12 小時；big 模型約 3.5 天。訓練成本只有其他頂尖模型的一小部分。〔出處：§5.2、§6.1，[原文](https://arxiv.org/abs/1706.03762)〕
- 除了翻譯，Transformer 也能用在英文句法分析，表示它不只適用於單一任務。〔出處：摘要，[原文](https://arxiv.org/abs/1706.03762)〕

## 作者對未來的展望

作者計畫把 Transformer 用到文字以外的資料，例如圖片、音訊、影片。〔出處：§7，[原文](https://arxiv.org/abs/1706.03762)〕

後續：[Dosovitskiy 2020](dosovitskiy-2020.md)（ViT）把標準 Transformer Encoder 直接用在圖片辨識上。〔出處：[Dosovitskiy 2020 §1、§3.1](dosovitskiy-2020.md)〕

## 在這個 Wiki 中的位置

本篇是整個主題的核心。之後的 BERT、GPT-3、T5、ViT 都是以 Transformer 為基礎的變化。〔出處：§3、§7，[原文](https://arxiv.org/abs/1706.03762)〕
