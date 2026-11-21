# 預訓練與微調（Pre-training & Fine-tuning）

> **類型**：概念 ｜ **出處**：[Devlin 2018](../papers/devlin-2018.md)、[Brown 2020](../papers/brown-2020.md)、[Raffel 2019](../papers/raffel-2019.md)、[Dosovitskiy 2020](../papers/dosovitskiy-2020.md) ｜ **相關**：[ViT](../models/vit.md)、[T5](../models/t5.md)、[In-context Learning](in-context-learning.md)、[BERT](../models/bert.md)、[語言模型](language-model.md)、[Masked Language Model](masked-language-model.md)

## 是什麼

把訓練分成兩個階段：〔出處：[Devlin 2018 §3](../papers/devlin-2018.md)〕

1. **預訓練（pre-training）**：用大量**沒有標註**的文字訓練模型，讓它學會一般的語言知識。
2. **微調（fine-tuning）**：用預訓練好的參數當起點，再用某個任務的**標註資料**繼續訓練所有參數。

不同任務各自微調出不同的模型，但都從同一份預訓練參數出發。〔出處：[Devlin 2018 §3](../papers/devlin-2018.md)〕

## 為什麼有用

預訓練語言模型已被證明能改善許多 NLP 任務，包括判斷兩個句子關係的任務，以及問答這類 token 層級的任務。〔出處：[Devlin 2018 §1](../papers/devlin-2018.md)〕

這種做法在電腦視覺領域也很常見：先在 ImageNet 上預訓練大模型，再針對任務微調。〔出處：[Devlin 2018 §2.3](../papers/devlin-2018.md)〕

## 兩種使用預訓練模型的方式

〔出處：[Devlin 2018 §1](../papers/devlin-2018.md)〕

- **Feature-based**：把預訓練模型的輸出當作額外特徵，放進為每個任務另外設計的架構裡。例如 ELMo。
- **Fine-tuning**：幾乎不加新參數，直接在任務資料上微調整個預訓練模型。例如 OpenAI GPT 和 BERT。

## 成本差異

預訓練需要大量資料和運算；微調相對便宜。以 BERT 為例，論文中所有任務的微調結果，在一個 Cloud TPU 上最多 1 小時就能重現。〔出處：[Devlin 2018 §3.2](../papers/devlin-2018.md)〕

## 另一條路：不微調

[GPT-3](../models/gpt-3.md) 的作者指出微調的缺點：每個新任務都需要一份新的大型標註資料集；模型可能無法推廣到不同分布的資料；也可能學到訓練資料中的表面特徵。〔出處：[Brown 2020 §2](../papers/brown-2020.md)〕

因此 GPT-3 只做預訓練、不做微調，改用 [In-context Learning](in-context-learning.md)：直接在輸入文字中給任務說明和範例。作者也說明，GPT-3 原則上可以微調，但這留待未來研究。〔出處：[Brown 2020 §1、§2](../papers/brown-2020.md)〕

## 用語：Transfer Learning

[T5](../models/t5.md) 的論文把「先在資料豐富的任務上預訓練，再在下游任務上微調」稱為 transfer learning（遷移學習）。與電腦視覺通常用有標註的 ImageNet 預訓練不同，NLP 的預訓練通常是在無標註資料上做無監督學習。〔出處：[Raffel 2019 摘要、§1](../papers/raffel-2019.md)〕

## T5 對微調方式的比較

T5 比較了幾種微調策略，發現**更新全部參數**的基本做法，表現優於只更新少部分參數的方法，雖然成本最高。同時訓練多個任務時，最難的是決定各任務的比例；作者沒有找到比「無監督預訓練 + 監督微調」更好的比例設定，但「先在多任務混合上預訓練、再微調」的表現差不多。〔出處：[Raffel 2019 §4.1](../papers/raffel-2019.md)〕

## 圖片上的預訓練與微調：ViT

[ViT](../models/vit.md) 也採用「先在大資料集上預訓練，再在較小的任務上微調」的做法。微調時拿掉預訓練的分類頭，換上一層初始化為 0 的新分類層；而且常用比預訓練更高的解析度。〔出處：[Dosovitskiy 2020 §3.2](../papers/dosovitskiy-2020.md)〕

和 NLP 不同的是，ViT 的主要結果來自**有標註**的大型圖片資料集（ImageNet-21k、JFT-300M）的監督式預訓練；自監督預訓練只做了初步實驗。〔出處：[Dosovitskiy 2020 §1、§4.1、§4.6](../papers/dosovitskiy-2020.md)〕
