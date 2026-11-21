# Patch Embedding（圖片切塊嵌入）

> **類型**：概念 ｜ **出處**：[Dosovitskiy 2020](../papers/dosovitskiy-2020.md) ｜ **相關**：[ViT](../models/vit.md)、[Embedding](embedding.md)、[Positional Encoding](positional-encoding.md)

## 為什麼需要

標準 Transformer 的輸入是一串 1D 的 token embedding。圖片是 2D 的，必須先轉成一串向量才能輸入。〔出處：[Dosovitskiy 2020 §3.1](../papers/dosovitskiy-2020.md)〕

最直接的想法是把每個像素當成一個 token，但 self-attention 的計算量會隨像素數平方成長，無法用在實際大小的圖片上。〔出處：[Dosovitskiy 2020 §2](../papers/dosovitskiy-2020.md)〕

## 做法

把圖片切成固定大小的 patch，每個 patch 當成一個 token：〔出處：[Dosovitskiy 2020 §3.1、式 (1)](../papers/dosovitskiy-2020.md)〕

1. 圖片大小為 H × W，有 C 個色彩通道；每個 patch 大小為 P × P。
2. 每個 patch 攤平成長度 P² × C 的向量。
3. 用一個可訓練的線性轉換，把它映射到 Transformer 使用的 D 維向量，這就是 patch embedding。

patch 的數量是：〔出處：[Dosovitskiy 2020 §3.1](../papers/dosovitskiy-2020.md)〕

```
N = H × W / P²
```

N 同時也是 Transformer 的輸入序列長度。〔出處：同上〕

## 計算例子

假設一張 224 × 224 的圖片（這裡的圖片大小是為了說明公式而假設的）：〔出處：依 [Dosovitskiy 2020 §3.1](../papers/dosovitskiy-2020.md) 的公式以 Python 計算〕

| patch 大小 P | patch 數 N | 模型名稱中的寫法 |
|---|---|---|
| 32 | 49 | 例如 ViT-B/32 |
| 16 | 196 | 例如 ViT-L/16 |
| 14 | 256 | 例如 ViT-H/14 |
〔出處：同上計算〕

patch 越小，序列越長，計算越貴。〔出處：[Dosovitskiy 2020 §4.1](../papers/dosovitskiy-2020.md)〕

論文標題「An Image is Worth 16x16 Words」呼應了 §1 的說法：圖片的 patch 被當成 NLP 中的 token（字）來處理。〔出處：[Dosovitskiy 2020](../papers/dosovitskiy-2020.md) 標題、§1〕

## 模型學到的 patch 特徵

把 ViT 第一層線性轉換學到的濾波器做主成分分析，前幾個主成分看起來像是能表示 patch 內部細節的基底函數。〔出處：[Dosovitskiy 2020 §4.5、圖 7](../papers/dosovitskiy-2020.md)〕

## 和文字 token 的對照

| | 文字（例如 BERT） | 圖片（ViT） |
|---|---|---|
| 基本單位 | token（字或子詞） | patch（P × P 的小方塊） |
| 轉成向量 | token embedding | 攤平後做線性轉換 |
| 位置資訊 | 位置 embedding | 位置 embedding |
| 分類用 | `[CLS]` token | 可學習的分類 token |
〔出處：[Devlin 2018 §3](../papers/devlin-2018.md)、[Dosovitskiy 2020 §1、§3.1](../papers/dosovitskiy-2020.md)〕
