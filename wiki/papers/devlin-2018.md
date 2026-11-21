# Devlin 2018：BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

> **類型**：論文 ｜ **出處**：[arXiv:1810.04805](https://arxiv.org/abs/1810.04805)（Devlin, Chang, Lee, Toutanova；Google AI Language） ｜ **相關**：[BERT](../models/bert.md)、[預訓練與微調](../concepts/pretraining-finetuning.md)、[Masked Language Model](../concepts/masked-language-model.md)、[語言模型](../concepts/language-model.md)、[Vaswani 2017](vaswani-2017.md)

## 一句話摘要

只用 [Transformer](../models/transformer.md) 的 Encoder，以「克漏字」方式預訓練出**雙向**的語言表示，之後只要加一層輸出層微調，就能在 11 個 NLP 任務上達到當時最佳。〔出處：摘要，[原文](https://arxiv.org/abs/1810.04805)〕

## 要解決的問題

當時把預訓練模型用到下游任務有兩種做法：feature-based（例如 ELMo）和 fine-tuning（例如 OpenAI GPT）。兩者在預訓練時都使用**單向**的語言模型。〔出處：§1，[原文](https://arxiv.org/abs/1810.04805)〕

作者認為單向是主要限制。例如 OpenAI GPT 採用由左到右的架構，self-attention 中每個 token 只能看前面的 token。這對問答這類需要同時考慮前後文的任務特別不利。〔出處：§1，[原文](https://arxiv.org/abs/1810.04805)〕

## 提出的方法

1. **架構**：多層的雙向 Transformer Encoder，和 Vaswani 2017 的原始實作幾乎相同。詳見 [BERT](../models/bert.md)。〔出處：§3，[原文](https://arxiv.org/abs/1810.04805)〕
2. **兩階段**：先在大量無標註文字上預訓練，再用各任務的標註資料微調所有參數。詳見 [預訓練與微調](../concepts/pretraining-finetuning.md)。〔出處：§3，[原文](https://arxiv.org/abs/1810.04805)〕
3. **預訓練任務一：Masked LM**：隨機遮住部分 token，讓模型根據前後文猜出原本的字。詳見 [Masked Language Model](../concepts/masked-language-model.md)。〔出處：§1、§3.1，[原文](https://arxiv.org/abs/1810.04805)〕
4. **預訓練任務二：Next Sentence Prediction（NSP）**：判斷句子 B 是不是句子 A 的下一句。〔出處：§3.1，[原文](https://arxiv.org/abs/1810.04805)〕

## 主要結果

- 在 11 個 NLP 任務上達到當時最佳。GLUE 分數 80.5，提升 7.7 分；MultiNLI 準確率 86.7%；SQuAD v1.1 問答 Test F1 為 93.2。〔出處：摘要，[原文](https://arxiv.org/abs/1810.04805)〕
- 在 GLUE 官方排行榜上，BERT-Large 得到 80.5，OpenAI GPT 為 72.8。〔出處：§4.1，[原文](https://arxiv.org/abs/1810.04805)〕
- GLUE（General Language Understanding Evaluation）是一組多樣的自然語言理解任務所組成的測驗集。〔出處：§4.1，[原文](https://arxiv.org/abs/1810.04805)〕

## 消融實驗：哪些設計真的有用

〔出處：§5.1、表 5，[原文](https://arxiv.org/abs/1810.04805)〕

- **拿掉 NSP**：QNLI、MNLI、SQuAD 1.1 的表現明顯下降。
- **改成只看左邊**（和 OpenAI GPT 一樣的由左到右語言模型）：所有任務都變差，MRPC 和 SQuAD 下降最多。即使在上面加一層雙向 LSTM 補救，結果仍然遠不如雙向預訓練。

作者的結論是：BERT 的進步主要來自**雙向性**和兩個預訓練任務。〔出處：§5.1、附錄 A.4，[原文](https://arxiv.org/abs/1810.04805)〕

## 模型大小的影響

模型越大，所有測試任務的準確率都越高，包括只有 3,600 筆訓練資料的 MRPC。作者認為這是第一篇有力證明「只要預訓練充分，把模型放大到極大，在很小的任務上也會大幅進步」的研究。〔出處：§5.2，[原文](https://arxiv.org/abs/1810.04805)〕

## 在這個 Wiki 中的位置

BERT 是「只用 Encoder」的代表，擅長理解文字。它和「只用 Decoder、由左到右」的 GPT 系列形成對比。〔出處：§3、附錄 A.4，[原文](https://arxiv.org/abs/1810.04805)〕
