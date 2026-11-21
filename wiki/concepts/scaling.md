# 規模化（Scaling）

> **類型**：概念 ｜ **出處**：[Brown 2020](../papers/brown-2020.md)、[Devlin 2018](../papers/devlin-2018.md)、[Raffel 2019](../papers/raffel-2019.md)、[Dosovitskiy 2020](../papers/dosovitskiy-2020.md) ｜ **相關**：[ViT](../models/vit.md)、[歸納偏置](inductive-bias.md)、[T5](../models/t5.md)、[GPT-3](../models/gpt-3.md)、[BERT](../models/bert.md)、[In-context Learning](in-context-learning.md)

## 是什麼

指把模型大小、訓練資料的量與多樣性、訓練時間放大，觀察能力如何隨之改變。〔出處：[Brown 2020 §2](../papers/brown-2020.md)〕

## 模型越來越大

GPT-3 論文整理了 Transformer 語言模型的參數成長：1 億 → 3 億 → 15 億 → 80 億 → 110 億 → 170 億，每次放大都帶來文字生成或下游任務的進步。GPT-3 則是 1,750 億，比之前任何非稀疏語言模型大 10 倍。〔出處：[Brown 2020 摘要、§1](../papers/brown-2020.md)〕

## 觀察到的規律

- **平滑的趨勢**：先前研究顯示，只要訓練資料足夠，驗證損失會隨模型大小呈現平滑的冪律（power law）改善。GPT-3 訓練 8 種大小，就是為了檢驗這個假設。〔出處：[Brown 2020 §1、§2.1](../papers/brown-2020.md)〕
- **大模型更會情境學習**：zero-shot 表現隨規模穩定上升，few-shot 上升得更快。〔出處：[Brown 2020 §1、圖 1.3](../papers/brown-2020.md)〕
- **有些能力在最大的模型才明顯出現**：以算術為例，從 130 億參數到 1,750 億參數，表現有明顯的跳升。〔出處：[Brown 2020 §3.9.1、圖 3.10](../papers/brown-2020.md)〕

## BERT 也看到同樣的現象

在 BERT 的實驗中，模型越大，所有測試任務的準確率都越高，連只有 3,600 筆訓練資料的小任務也一樣。〔出處：[Devlin 2018 §5.2](../papers/devlin-2018.md)〕

## 規模的極限

GPT-3 的作者認為，單純放大自監督的預測模型，最終可能會碰到預訓練目標本身的極限。他們提出的方向包括：從人類身上學習目標函數、用強化學習微調、加入圖片等其他模態。此外，模型在預訓練時看的文字量遠多於人類一生看到的量，資料效率仍然很差。〔出處：[Brown 2020 §5](../papers/brown-2020.md)〕

## T5 的發現：怎麼用額外的運算資源

T5 比較了幾種使用額外運算的方式：用更多資料訓練、訓練更大的模型、集成多個模型。每一種都有明顯幫助，但「用更多資料訓練較小的模型」常常比不上「訓練較大的模型、但步數少一點」。〔出處：[Raffel 2019 §4.1](../papers/raffel-2019.md)〕

T5 的最終實驗中，把模型放大到 110 億參數，是達到最佳表現最重要的因素。〔出處：[Raffel 2019 §3.7](../papers/raffel-2019.md)〕

## ViT：規模勝過歸納偏置

在圖片上，[ViT](../models/vit.md) 只用中型資料集訓練時輸給 CNN，但預訓練資料放大到 1,400 萬到 3 億張後就反超。作者的結論是「大規模訓練勝過歸納偏置」，詳見 [歸納偏置](inductive-bias.md)。〔出處：[Dosovitskiy 2020 §1、§4.3](../papers/dosovitskiy-2020.md)〕

在同樣的運算預算下，ViT 勝過 ResNet，達到同樣表現約只需 1/2 到 1/4 的運算；而且在測試範圍內還沒有飽和。〔出處：[Dosovitskiy 2020 §4.4](../papers/dosovitskiy-2020.md)〕

ViT 的論文也提到，Transformer 的運算效率和可擴展性，讓 NLP 能夠訓練超過 1,000 億參數的模型，而且隨著模型和資料變大，表現仍看不到飽和的跡象。〔出處：[Dosovitskiy 2020 §1](../papers/dosovitskiy-2020.md)〕
