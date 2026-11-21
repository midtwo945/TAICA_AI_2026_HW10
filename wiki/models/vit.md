# ViT（Vision Transformer）

> **類型**：模型 ｜ **出處**：[Dosovitskiy 2020](../papers/dosovitskiy-2020.md) ｜ **相關**：[Transformer](transformer.md)、[BERT](bert.md)、[Patch Embedding](../concepts/patch-embedding.md)、[歸納偏置](../concepts/inductive-bias.md)、[Transformer 架構家族](../concepts/architecture-variants.md)

## 是什麼

ViT 是把**標準 Transformer Encoder** 直接用在圖片上的模型：把圖片切成 patch，把每個 patch 當成 NLP 中的一個 token（字）。〔出處：[Dosovitskiy 2020 §1、§3.1、圖 1](../papers/dosovitskiy-2020.md)〕

## 資料流程

〔出處：[Dosovitskiy 2020 §3.1、圖 1](../papers/dosovitskiy-2020.md)〕

1. **切塊**：把圖片切成固定大小的 patch，詳見 [Patch Embedding](../concepts/patch-embedding.md)。
2. **轉成向量**：每個 patch 攤平後，用可訓練的線性轉換變成 D 維向量。
3. **加分類 token**：在序列最前面加一個可學習的 embedding，類似 [BERT](bert.md) 的 `[class]` token。它在 Encoder 最後的輸出就代表整張圖。
4. **加位置 embedding**：使用一般可學習的 1D 位置 embedding。
5. **Transformer Encoder**：多頭 self-attention 和 MLP 區塊交替堆疊。
6. **分類**：把分類 token 的輸出接到分類頭。預訓練時是有一個隱藏層的 MLP，微調時是一層線性層。

## 模型大小

設定直接沿用 BERT：Base 和 Large 取自 BERT，另外加了更大的 Huge。〔出處：[Dosovitskiy 2020 §4.1、表 1](../papers/dosovitskiy-2020.md)〕

| 版本 | 層數 | 隱藏維度 D | MLP 維度 | 頭數 | 參數量 |
|---|---|---|---|---|---|
| ViT-Base | 12 | 768 | 3,072 | 12 | 8,600 萬 |
| ViT-Large | 24 | 1,024 | 4,096 | 16 | 3.07 億 |
| ViT-Huge | 32 | 1,280 | 5,120 | 16 | 6.32 億 |
〔出處：[Dosovitskiy 2020 表 1](../papers/dosovitskiy-2020.md)〕

命名方式：「ViT-L/16」表示 Large 版本、輸入 patch 大小為 16×16。patch 越小，序列越長，計算越貴。〔出處：[Dosovitskiy 2020 §4.1](../papers/dosovitskiy-2020.md)〕

## 和原始 Transformer 的差異

- **只用 Encoder**，沒有 Decoder，用分類 token 做分類，這點和 [BERT](bert.md) 相同。〔出處：[Dosovitskiy 2020 §3.1](../papers/dosovitskiy-2020.md)〕
- **LayerNorm 放在每個區塊之前**，殘差連接放在每個區塊之後。這和 [T5](t5.md) 一樣，和原始 Transformer 不同。〔出處：[Dosovitskiy 2020 §3.1](../papers/dosovitskiy-2020.md)、[Raffel 2019 §2.1](../papers/raffel-2019.md)、[Vaswani 2017 §3.1](../papers/vaswani-2017.md)〕

## 訓練方式

先在大型資料集上預訓練，再針對較小的下游任務微調。預訓練資料集包括：〔出處：[Dosovitskiy 2020 §3.2、§4.1](../papers/dosovitskiy-2020.md)〕

| 資料集 | 類別數 | 圖片數 |
|---|---|---|
| ImageNet | 1,000 | 130 萬 |
| ImageNet-21k | 21,000 | 1,400 萬 |
| JFT | 18,000 | 3.03 億 |
〔出處：[Dosovitskiy 2020 §4.1](../papers/dosovitskiy-2020.md)〕

微調時常用比預訓練更高的解析度。patch 大小不變，所以序列會變長；預訓練好的位置 embedding 則依照它們在原圖中的位置做 2D 內插。這和切塊一樣，是 ViT 唯一刻意放入「圖片是 2D」這項假設的地方。〔出處：[Dosovitskiy 2020 §3.2](../papers/dosovitskiy-2020.md)〕

## 資料量的影響

資料少時 ViT 輸給 CNN，資料多時反超，詳見 [歸納偏置](../concepts/inductive-bias.md)。〔出處：[Dosovitskiy 2020 §1、§4.3](../papers/dosovitskiy-2020.md)〕

## 混合架構（簡述）

也可以先用 CNN 抽出特徵圖，再把特徵圖切塊送進 ViT。在運算預算小時，混合架構略勝純 ViT，但模型變大後差距就消失了。〔出處：[Dosovitskiy 2020 §3.1、§4.4](../papers/dosovitskiy-2020.md)〕

## ⚠️ 不要搞混：ViT 的「few-shot」

ViT 論文中的「few-shot 準確率」是指：**凍結**模型，取少量訓練圖片的特徵，解一個正規化的最小平方迴歸問題來分類。這和 [GPT-3](gpt-3.md) 的 few-shot（在輸入文字中給範例，見 [In-context Learning](../concepts/in-context-learning.md)）是完全不同的東西。〔出處：[Dosovitskiy 2020 §4.1](../papers/dosovitskiy-2020.md)、[Brown 2020 §2](../papers/brown-2020.md)〕
