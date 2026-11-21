# BERT

> **類型**：模型 ｜ **出處**：[Devlin 2018](../papers/devlin-2018.md) ｜ **相關**：[Transformer](transformer.md)、[預訓練與微調](../concepts/pretraining-finetuning.md)、[Masked Language Model](../concepts/masked-language-model.md)、[語言模型](../concepts/language-model.md)、[Embedding](../concepts/embedding.md)

## 是什麼

BERT 是 **B**idirectional **E**ncoder **R**epresentations from **T**ransformers 的縮寫。架構是多層的**雙向** [Transformer](transformer.md) Encoder，和原始 Transformer 的實作幾乎相同，只是沒有 Decoder。〔出處：[Devlin 2018 摘要、§3](../papers/devlin-2018.md)〕

## 模型大小

| 版本 | 層數 L | 隱藏維度 H | 頭數 A | 參數量 |
|---|---|---|---|---|
| BERT-Base | 12 | 768 | 12 | 1.1 億 |
| BERT-Large | 24 | 1024 | 16 | 3.4 億 |
〔出處：[Devlin 2018 §3](../papers/devlin-2018.md)〕

BERT-Base 刻意做成和 OpenAI GPT 一樣大，方便比較。兩者架構幾乎相同，關鍵差別在 attention：BERT 每個 token 可以看左右兩邊，GPT 只能看左邊。〔出處：[Devlin 2018 §3、§4.1](../papers/devlin-2018.md)〕

## 輸入格式

〔出處：[Devlin 2018 §3、圖 2](../papers/devlin-2018.md)〕

- 每段輸入的第一個 token 一定是特殊符號 `[CLS]`。它最後的輸出向量（記作 C）代表整段輸入，用在分類任務。
- 兩個句子用 `[SEP]` 隔開，例如「問題 `[SEP]` 文章」。
- 每個 token 的輸入向量是三個 embedding 相加，詳見 [Embedding](../concepts/embedding.md)。

## 預訓練

使用 BooksCorpus（8 億字）和英文維基百科（25 億字），同時訓練兩個任務：〔出處：[Devlin 2018 §3.1](../papers/devlin-2018.md)〕

1. **[Masked Language Model](../concepts/masked-language-model.md)**：猜出被遮住的字。
2. **Next Sentence Prediction（NSP）**：給句子 A 和 B，50% 的情況 B 真的是 A 的下一句，另外 50% 是隨機挑的句子，讓模型判斷是哪一種。用 `[CLS]` 的輸出向量 C 來判斷。這個任務是為了讓模型學會理解句子之間的關係，問答和推論任務都需要這種能力。

## 微調

針對每個任務，只要把任務的輸入和輸出接上 BERT，再微調全部參數即可：〔出處：[Devlin 2018 §3.2](../papers/devlin-2018.md)〕

- **分類任務**（例如情感分析）：把 `[CLS]` 的向量接到一層輸出層。
- **token 層級的任務**（例如序列標註、問答）：把每個 token 的向量接到輸出層。

以問答（SQuAD）為例，微調時只新增「起點向量」和「終點向量」兩組參數，用來找出答案在文章中的起點和終點。〔出處：[Devlin 2018 §4.2、圖 1](../papers/devlin-2018.md)〕

微調比預訓練便宜很多：論文中所有結果，在一個 Cloud TPU 上最多 1 小時、在 GPU 上幾小時就能重現。〔出處：[Devlin 2018 §3.2](../papers/devlin-2018.md)〕

## 和 OpenAI GPT 的差異

〔出處：[Devlin 2018 附錄 A.4](../papers/devlin-2018.md)〕

| | OpenAI GPT | BERT |
|---|---|---|
| 方向 | 由左到右 | 雙向 |
| 預訓練資料 | BooksCorpus（8 億字） | BooksCorpus + 維基百科（共 33 億字） |
| `[CLS]`、`[SEP]` | 微調時才加入 | 預訓練時就學 |
〔出處：同上〕

作者透過消融實驗證明，進步主要來自雙向性和兩個預訓練任務，而不是這些訓練細節上的差異。〔出處：[Devlin 2018 §5.1、附錄 A.4](../papers/devlin-2018.md)〕
