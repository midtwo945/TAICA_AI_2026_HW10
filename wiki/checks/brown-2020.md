# N3.5 原文比對紀錄：論文 4（Brown 2020，GPT-3）

依 [CLAUDE.md](../../CLAUDE.md) 的 R20 逐段比對。原文：[raw/brown-2020.txt](https://arxiv.org/abs/2005.14165)

結果：✅ = 找到對應句子；❌ = 找不到 → 已修正

## papers/brown-2020.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 頁首（發表場合） | 第一版寫「NeurIPS 2020」。**全文找不到 NeurIPS**（只出現在參考文獻裡別人的論文），是 AI 憑記憶補的 | ❌ → 改為原文首頁的作者單位「OpenAI、Johns Hopkins University」 |
| 一句話摘要 | 第一版寫「把**由左到右**的語言模型放大」。**全文沒有出現 left-to-right**，原文用 "autoregressive language model" | ❌ → 改成「自迴歸語言模型」 |
| 要解決的問題 | 摘要："requires task-specific fine-tuning datasets of thousands or tens of thousands of examples… humans can generally perform a new language task from only a few examples" | ✅ |
| 方法 1（架構） | §2.1："same model and architecture as GPT-2… alternating dense and locally banded sparse attention patterns" | ✅ |
| 方法 2（8 種大小） | §2.1："we train 8 different sizes of model… from 125 million parameters to 175 billion parameters" | ✅ |
| 方法 3（評估） | 摘要："applied without any gradient updates or fine-tuning"；§1 三種設定 | ✅ |
| 結果：規模 | §1、圖 1.3："zero-shot performance improves steadily… few-shot performance increases more rapidly" | ✅ |
| 結果：TriviaQA | §1："64.3%… 68.0%… 71.2%… state-of-the-art relative to fine-tuned models operating in the same closed-book setting" | ✅ |
| 結果：算術 | §3.9.1："First we evaluate GPT-3 in the few-shot setting… 100%… 98.9%… 80.2%… 94.2%… 25-26%… 9-10%… 29.2%" | ✅ |
| 結果：新聞 | §3.9.4："barely above chance at 52%"；摘要 "human evaluators have difficulty distinguishing" | ✅ |
| 背答案還是會算 | §3.9.1："Out of 2,000 addition problems we found only 17 matches (0.8%)… 2 matches (0.1%)… not carrying a '1'" | ✅ |
| 限制（5 點） | §5 各段：repeat themselves / cheese into the fridge / WIC and ANLI / "from scratch" / expensive and inconvenient / retains the biases | ✅ |
| 資料污染 | §2.2："a bug in the filtering caused us to ignore some overlaps… not feasible to retrain" | ✅ |
| 在 Wiki 中的位置 | 第一版寫「由左到右」，出處標 §1、§5；「規模帶來不需微調的能力」在 §1、§5 都沒有直接對應 | ❌ → 改成「自迴歸、不微調」，並改引 §8："documented roughly predictable trends of scaling in performance without using fine-tuning" |

## models/gpt-3.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 是什麼 | 第一版寫「由左到右，根據前面的 token 預測下一個 token」，Brown 原文沒有 left-to-right | ❌ → 改成「使用時只要讓它預測接下來的內容」，對應 §1 "simply by predicting what comes next" |
| 屬於哪一種 Transformer | 依使用者核准的預設，明確標為「推論」；Devlin §3 註 4、附錄 A.4 ＋ Brown §2.1 | ✅（推論，已標註） |
| 模型大小表 | 表 2.1 逐欄抄錄 | ✅ |
| ⚠️ 數字不一致 | Python 驗算 8 個尺寸，XL、13B 不符；Vaswani §3.2.2 "dk = dv = dmodel/h" | ✅ |
| context window、d_ff | §2.1："context window of nctx = 2048 tokens"；"dff = 4 ∗ dmodel" | ✅ |
| 訓練資料表 | 表 2.2；表 2.1 說明 "trained for a total of 300 billion tokens"；§2.2 "byte-pair-encoded tokens" | ✅ |
| 抽樣比例說明 | §2.2："accepts a small amount of overfitting in exchange for higher quality training data" | ✅ |
| 怎麼使用 | 摘要、§2 | ✅ |
| 與 BERT 對比表 | 第一版「方向」欄寫「由左到右」 | ❌ → 改成「自迴歸（單向）」；其他欄 ✅ |
| 單向的代價 | §5："our design decision comes at the cost of potentially worse performance on tasks which empirically benefit from bidirectionality" | ✅ |

## concepts/in-context-learning.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 是什麼 | §1："conditioned on a natural language instruction and/or a few demonstrations… simply by predicting what comes next"；"no gradient updates" | ✅ |
| 作者的解釋 | §1、圖 1.1："develops a broad set of skills and pattern recognition abilities at training time… at inference time to rapidly adapt to or recognize" | ✅ |
| 三種設定表 | §2 Zero-Shot／One-Shot／Few-Shot 三段 | ✅ |
| 例子 | §3.9.1："Q: What is 48 plus 76? A: 124." | ✅ |
| Few-shot 做法 | §2："giving K examples of context and completion, and then one final example of context" | ✅ |
| 與微調比較表 | 第一版 few-shot 資料量寫「幾個到幾十個」，原文是 "typically set K in the range of 10 to 100" | ❌ → 改成「通常 10～100 個範例」；其他欄 ✅ |
| 用語說明 | §1 註 1 | ✅ |
| 規模的影響 | §1："gap between zero-, one-, and few-shot performance often grows with model capacity… more proficient meta-learners" | ✅ |
| 尚未解決的問題 | §5："ambiguity about whether few-shot learning actually learns new tasks 'from scratch'… may also vary from task to task" | ✅ |

## concepts/scaling.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 是什麼 | 第一版寫「參數量、訓練資料量和**運算量**」，原文 §2 是 "scaling up of the model size, dataset size and diversity, and length of training" | ❌ → 改成「模型大小、訓練資料的量與多樣性、訓練時間」 |
| 模型越來越大 | §1："from 100 million… 300 million… 1.5 billion… 8 billion… 11 billion… 17 billion"；摘要 "10x more" | ✅ |
| 平滑的趨勢 | §2.1："scaling of validation loss should be approximately a smooth power law" | ✅ |
| 大模型更會情境學習 | 圖 1.3 說明 | ✅ |
| 算術跳升 | 圖 3.10 說明："significant jump from the second largest model (GPT-3 13B) to the largest model" | ✅ |
| BERT 也一樣 | Devlin §5.2 | ✅ |
| 規模的極限 | §5："likely to hit limits… learning the objective function from humans… reinforcement learning… adding additional modalities such as images"；"poor sample efficiency" | ✅ |

## 舊頁面修改

| 頁面／段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| language-model.md／GPT-3 段落 1 | §5："straightforward to both sample and compute likelihoods with this model class" | ✅ |
| language-model.md／GPT-3 段落 2 | §5："fill-in-the-blank tasks, tasks that involve looking back and comparing two pieces of content…" | ✅ |
| pretraining-finetuning.md／不微調 | §2 Fine-Tuning 條列（main disadvantages）；"GPT-3 can be fine-tuned in principle… future work" | ✅ |
| transformer.md／GPT-3 條列 | 摘要、§2.1；並註明是推論 | ✅ |

## 統計

- 檢查段落：41
- ❌ 找不到對應：8（全部已修正）
  - 4 個是 **把別篇論文的用語套到這篇**：「由左到右」來自 BERT 論文對 GPT 的描述，GPT-3 原文從沒用過
  - 2 個是 **AI 憑記憶補充**：NeurIPS 2020、「運算量」
  - 1 個是 **數字改寫失真**：10～100 個 → 幾個到幾十個
  - 1 個是 **出處標錯章節**
