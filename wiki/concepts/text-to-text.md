# Text-to-Text（文字轉文字框架）

> **類型**：概念 ｜ **出處**：[Raffel 2019](../papers/raffel-2019.md) ｜ **相關**：[T5](../models/t5.md)、[In-context Learning](in-context-learning.md)、[Transformer 架構家族](architecture-variants.md)

## 是什麼

把**每一個**文字處理任務都當成「輸入一段文字，輸出一段新文字」。如此所有任務都能使用同一個模型、同一個目標函數、同一套訓練流程和解碼方式。〔出處：[Raffel 2019 §1](../papers/raffel-2019.md)〕

## 怎麼指定任務

在原本的輸入前面加上一段**任務前綴**：〔出處：[Raffel 2019 §2.4](../papers/raffel-2019.md)〕

| 任務 | 輸入 | 輸出 |
|---|---|---|
| 英翻德 | `translate English to German: That is good.` | `Das ist gut.` |
| 文字推論（MNLI） | `mnli premise: I hate pigeons. hypothesis: My feelings towards pigeons are filled with animosity.` | `entailment` |
〔出處：同上〕

分類任務只要輸出代表類別的那個字即可。如果模型輸出的字不屬於任何類別（例如輸出「hamburger」），一律算錯；不過作者在訓練好的模型中從未觀察到這種情況。〔出處：[Raffel 2019 §2.4](../papers/raffel-2019.md)〕

前綴的確切用詞可以視為一個超參數，但作者發現改變用詞的影響有限。〔出處：[Raffel 2019 §2.4](../papers/raffel-2019.md)〕

## 適用範圍

這個框架可以處理生成類任務（例如摘要）、分類類任務（例如推論），甚至回歸任務（例如 STS-B 的相似度分數）。雖然做法簡單，表現卻和為各任務特別設計的架構相當，加上規模化之後更達到當時最佳。〔出處：[Raffel 2019 §4.1](../papers/raffel-2019.md)〕

## 靈感來源

這個想法受到先前「把所有任務都變成某種統一形式」的研究啟發，例如都變成問答、都變成語言模型，或都變成從文字中擷取片段。〔出處：[Raffel 2019 §1](../papers/raffel-2019.md)〕
