# Raffel 2019：Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer（T5）

> **類型**：論文 ｜ **出處**：[arXiv:1910.10683](https://arxiv.org/abs/1910.10683)（Raffel 等，Google；arXiv 2019，正式發表於 JMLR 第 21 卷，2020） ｜ **相關**：[T5](../models/t5.md)、[Text-to-Text](../concepts/text-to-text.md)、[Transformer 架構家族](../concepts/architecture-variants.md)、[預訓練與微調](../concepts/pretraining-finetuning.md)、[Masked Language Model](../concepts/masked-language-model.md)

## 一句話摘要

把所有 NLP 任務都改寫成「輸入文字 → 輸出文字」，在這個統一框架下系統性比較各種架構、預訓練目標和資料集，再把最好的組合放大到 110 億參數（T5），在許多任務上達到當時最佳。〔出處：摘要、§1，[原文](https://arxiv.org/abs/1910.10683)〕

## 這篇論文的定位

作者強調目的不是提出新方法，而是對現有的 transfer learning 技術做全面的調查、探索和實證比較。〔出處：§1，[原文](https://arxiv.org/abs/1910.10683)〕

## 主要內容

1. **[Text-to-Text](../concepts/text-to-text.md) 框架**：每個任務都是「餵進一段文字，訓練模型產生目標文字」，在輸入前加上任務前綴來指定任務。如此所有任務都能使用同一個模型、損失函數和訓練流程。〔出處：§1、§2.4、圖 1，[原文](https://arxiv.org/abs/1910.10683)〕
2. **架構比較**：比較 Encoder-Decoder、Decoder-only 語言模型、Prefix LM 等變化，以及它們使用的不同 attention 遮罩。詳見 [Transformer 架構家族](../concepts/architecture-variants.md)。〔出處：§3.2，[原文](https://arxiv.org/abs/1910.10683)〕
3. **預訓練目標**：受 BERT 的 masked language modeling 啟發，設計一種「遮住部分 token，再讓模型輸出被遮住的部分」的 denoising 目標。詳見 [Masked Language Model](../concepts/masked-language-model.md)。〔出處：§3.1.4，[原文](https://arxiv.org/abs/1910.10683)〕
4. **C4 資料集**：從 Common Crawl 清理出約 750 GB 乾淨的英文文字，稱為 Colossal Clean Crawled Corpus。〔出處：§2.2，[原文](https://arxiv.org/abs/1910.10683)〕

## 主要發現

〔出處：§4.1，[原文](https://arxiv.org/abs/1910.10683)〕

- **架構**：在 text-to-text 框架下，原始的 Encoder-Decoder 表現最好。它的參數量是「encoder-only（如 BERT）」或「decoder-only（語言模型）」的兩倍，但計算量相近。
- **預訓練目標**：大部分「把隨機破壞的文字還原」的 denoising 目標表現差不多，所以建議選擇目標序列較短、計算較省的那種。
- **資料**：預訓練資料太小、被重複看很多次時，表現會變差，所以需要像 C4 這樣大而多樣的資料集。
- **訓練策略**：微調時更新全部參數，表現優於只更新少部分參數的方法，但成本最高。
- **規模**：訓練更大的模型、訓練更久、集成多個模型都有幫助；「用更多資料訓練小模型」常常不如「訓練大模型但步數少一點」。

## 最終結果

最大的 T5 有 110 億參數，在 24 個任務中的 18 個達到當時最佳，GLUE 平均分數 90.3。作者指出，把模型放大到 110 億參數是達到最佳表現最重要的因素。〔出處：§3.7，[原文](https://arxiv.org/abs/1910.10683)〕

## 在這個 Wiki 中的位置

T5 回到原始 Transformer 的 Encoder-Decoder 架構，並且直接比較了 encoder-only、decoder-only 等變化，是整理「Transformer 家族」最重要的來源。〔出處：§3.1.1、§3.2、§4.1，[原文](https://arxiv.org/abs/1910.10683)〕
