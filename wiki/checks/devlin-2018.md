# N3.5 原文比對紀錄：論文 3（Devlin 2018，BERT）

依 [CLAUDE.md](../../CLAUDE.md) 的 R20：這次新增或修改的每個段落，都要回原文找到對應的句子。
原文：[raw/devlin-2018.txt](https://arxiv.org/abs/1810.04805)（依閱讀順序轉檔；部分段落因雙欄排版順序有些錯亂，以內容判斷所屬章節）

結果：✅ = 找到對應句子；❌ = 找不到 → 已修正

## papers/devlin-2018.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 一句話摘要 | 摘要："pre-trained BERT model can be fine-tuned with just one additional output layer…" | ✅ |
| 要解決的問題（兩種做法） | §1："two existing strategies… feature-based and fine-tuning… share the same objective function… unidirectional language models" | ✅ |
| 要解決的問題（GPT 只看左邊） | §1："in OpenAI GPT… every token can only attend to previous tokens… could be very harmful… question answering" | ✅ |
| 提出的方法 1～4 | §3 "multi-layer bidirectional Transformer encoder… almost identical to the original"；§3.1 Task #1、Task #2 | ✅ |
| 主要結果（摘要數字） | 摘要："GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7%… SQuAD v1.1… 93.2" | ✅ |
| 主要結果（排行榜） | §4.1："BERTLARGE obtains a score of 80.5, compared to OpenAI GPT, which obtains 72.8" | ✅ |
| 消融實驗 | §5.1："removing NSP hurts performance significantly on QNLI, MNLI, and SQuAD 1.1… LTR model performs worse… large drops on MRPC and SQuAD"；"+BiLSTM… still far worse" | ✅ |
| 作者結論 | 附錄 A.4："majority of the improvements are in fact coming from the two pre-training tasks and the bidirectionality" | ✅ |
| 模型大小 | §5.2："MRPC which only has 3,600 labeled training examples… first work to demonstrate convincingly…" | ✅ |
| 在 Wiki 中的位置 | §3 註 4（encoder／decoder 用語）、附錄 A.4（GPT 是 left-to-right Transformer LM） | ✅ |

## models/bert.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 是什麼 | 摘要（名稱縮寫）；§3 "multi-layer bidirectional Transformer encoder" | ✅ |
| 模型大小表 | §3："BERTBASE (L=12, H=768, A=12, Total Parameters=110M) and BERTLARGE (L=24, H=1024, A=16, Total Parameters=340M)" | ✅ |
| 與 GPT 同大小 | §3："BERTBASE was chosen to have the same model size as OpenAI GPT"；§4.1 "nearly identical… apart from the attention masking" | ✅ |
| 輸入格式 | §3 Input/Output Representations：[CLS]、[SEP]、C、三種 embedding 相加 | ✅ |
| 預訓練資料與 NSP | §3.1："BooksCorpus (800M words)… English Wikipedia (2,500M words)"；"50% of the time B is the actual next sentence" | ✅ |
| 微調（分類／token 任務） | §3.2："token representations are fed into an output layer for token-level tasks… [CLS] representation… for classification, such as entailment or sentiment analysis" | ✅ |
| 微調（問答找答案位置） | 第一版寫在 §3.2 底下，但 §3.2 沒有「找答案位置」的說法 | ❌ → 已改：另立一段，出處改為 §4.2 "start vector S… end vector E" 與圖 1 "Start/End Span" |
| 微調成本 | §3.2："at most 1 hour on a single Cloud TPU, or a few hours on a GPU" | ✅ |
| 與 GPT 的差異表 | 附錄 A.4 三個條列（資料、[SEP]/[CLS]、…） | ✅ |

## concepts/pretraining-finetuning.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 是什麼（兩階段） | §3："two steps in our framework: pre-training and fine-tuning…" | ✅ |
| 同一份參數出發 | §3："Each downstream task has separate fine-tuned models, even though they are initialized with the same pre-trained parameters" | ✅ |
| 為什麼有用 | §1："Language model pre-training has been shown to be effective… sentence-level tasks… token-level tasks" | ✅ |
| ImageNet | §2.3："fine-tune models pre-trained with ImageNet" | ✅ |
| 兩種方式 | §1（feature-based = ELMo；fine-tuning = GPT）；附錄 A.4（BERT 和 GPT 都是 fine-tuning） | ✅ |
| 成本差異 | §3.2（同上） | ✅ |

## concepts/masked-language-model.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 是什麼 | §1："randomly masks some of the tokens… predict the original vocabulary id… inspired by the Cloze task" | ✅ |
| 為什麼需要 | §3.1："bidirectional conditioning would allow each word to indirectly 'see itself'" | ✅ |
| 做法（15%、80/10/10、softmax） | §3.1："mask 15% of all WordPiece tokens"；"(1) the [MASK] token 80%… (2) a random token 10%… (3) the unchanged 10%"；"fed into an output softmax over the vocabulary" | ✅ |
| 不重建整段 | §3.1："we only predict the masked words rather than reconstructing the entire input" | ✅ |
| 例子 my dog is hairy | 附錄 A.1 三個條列 | ✅ |
| 為什麼不全部換成 [MASK] | §3.1 "mismatch between pre-training and fine-tuning"；附錄 A.1 "does not know which words it will be asked to predict… 1.5% of all tokens" | ✅ |
| 代價 | 附錄 A.1："only make predictions on 15% of tokens… more pre-training steps may be required" | ✅ |
| 兩種 mask | Devlin §3.1（[MASK] token）＋ Vaswani §3.2.3（masking out illegal connections） | ✅ |

## concepts/language-model.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 是什麼（第一版） | 第一版寫「標準語言模型是根據前面的字預測下一個字」並標 Devlin §3.1。**Devlin 全文找不到 "next word"、"predict the next" 等說法**，§3.1 只說 "can only be trained left-to-right or right-to-left" | ❌ → 已改：「拆成一連串條件機率相乘」改引 Bahdanau §2.1 式 (2)："decomposing the joint probability into the ordered conditionals"；Devlin §3.1 只用來支持「只能單向訓練」 |
| auto-regressive | Vaswani §3："the model is auto-regressive… consuming the previously generated symbols as additional input" | ✅ |
| 單向 vs. 雙向表 | §1（GPT 只看前面）、§2.1（ELMo 串接左右兩個模型）、§1（BERT 用 MLM 做深層雙向） | ✅ |
| 單向的限制 | §1（問答需要兩個方向）；§5.1（LTR 所有任務變差） | ✅ |
| ELMo 的缺點 | §5.1："(a) this is twice as expensive… (c)… strictly less powerful than a deep bidirectional model"（轉檔順序錯亂，內容接在 §5.1 的 BiLSTM 討論後） | ✅ |
| 單向的用途 | §3 註 4："left-context-only version is referred to as a 'Transformer decoder' since it can be used for text generation" | ✅ |

## 舊頁面修改

| 頁面／段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| embedding.md／三種 embedding 相加 | §3："summing the corresponding token, segment, and position embeddings"；"add a learned embedding… sentence A or sentence B" | ✅ |
| embedding.md／WordPiece 與 ##ing | §3 "WordPiece embeddings… 30,000 token vocabulary"；圖 2 "play ##ing"。第一版另外寫了「`##` 表示接在前一個片段後面」，**原文沒有解釋 ## 的意思**（AI 自己的知識） | ❌ → 已刪除該說明 |
| self-attention.md／雙向 vs. 只看左邊 | §3："BERT Transformer uses bidirectional self-attention, while the GPT Transformer uses constrained self-attention…"；§4.1 "nearly identical… apart from the attention masking" | ✅ |
| self-attention.md／⚠️ 兩種遮罩 | 同 MLM 頁 | ✅ |
| transformer.md／後續變化與用語 | Devlin §3 註 4；Vaswani §3.1（Decoder 的第三個子層） | ✅ |

## 統計

- 檢查段落：44
- ❌ 找不到對應：3（全部已修正）
  - 2 個是 **AI 用自己的知識補充**（"predict next word" 的定義、## 的意思）
  - 1 個是 **出處標錯章節**（問答找答案位置）
