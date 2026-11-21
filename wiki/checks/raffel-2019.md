# N3.5 原文比對紀錄：論文 5（Raffel 2019，T5）

依 [CLAUDE.md](../../CLAUDE.md) 的 R20 逐段比對。原文：[raw/raffel-2019.txt](https://arxiv.org/abs/1910.10683)

結果：✅ = 找到對應句子；❌ = 找不到 → 已修正

## papers/raffel-2019.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 頁首（單位、JMLR） | 首頁作者 email 為 google.com；授權說明 "jmlr.org/papers/v21/20-074.html" | ✅ |
| 一句話摘要 | 摘要："converts all text-based language problems into a text-to-text format… compares pre-training objectives, architectures…"；§1 "up to 11 billion parameters" | ✅ |
| 論文定位 | §1："our goal is not to propose new methods but instead to provide a comprehensive perspective… survey, exploration, and empirical comparison" | ✅ |
| 主要內容 1～4 | §1、§2.4（task-specific prefix）；§3.2；§3.1.4 "Inspired by BERT's 'masked language modeling'"；§2.2 "about 750 GB" | ✅ |
| 主要發現（5 點） | §4.1 Architectures／Unsupervised objectives／Data sets／Training strategies／Scaling 各段 | ✅ |
| 最終結果 | §3.7："state-of-the-art performance on 18 out of the 24 tasks… scaling the model size to 11 billion parameters was the most important ingredient… GLUE score of 90.3" | ✅ |
| 在 Wiki 中的位置 | §3.1.1（standard encoder-decoder）、§3.2、§4.1（"encoder-only"／"decoder-only"）；「最重要的來源」是本 Wiki 的整理判斷 | ✅ |

## models/t5.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 是什麼 | 圖 1 說明 "'T5' refers to our model… 'Text-to-Text Transfer Transformer'"；§3.1.1 "standard encoder-decoder Transformer" | ✅ |
| 選擇原因 | §3.1.1："using a standard encoder-decoder structure achieved good results on both generative and classification tasks" | ✅ |
| LayerNorm 位置 | §2.1："Layer normalization is applied to the input of each subcomponent… simplified version… only rescaled and no additive bias… a residual skip connection adds each subcomponent's input to its output"；Vaswani §3.1 "LayerNorm(x + Sublayer(x))" | ✅ |
| 相對位置 | §2.1："it has recently become more common to use relative position embeddings" | ✅ |
| 模型大小表 | §3.1.1（Base）、§3.7（Small／Large／3B／11B）。第一版 Small 的 d_kv 填了「64（預設值）」，**原文 Small 段只列 dmodel、dff、頭數、層數，沒有 d_kv** | ❌ → 改成「—（原文未列出）」 |
| Base 約 BERT-Base 兩倍 | §3.1.1："roughly twice the number of parameters of BERTBASE since our baseline model contains two layer stacks" | ✅ |
| 放大 d_ff 的原因 | §3.7："modern accelerators… most efficient for large dense matrix multiplications" | ✅ |
| 頭數 × d_kv ≠ d_model | §3.7 數字＋ Python 驗算 | ✅ |
| 訓練（資料、目標、1 兆 token、多任務） | §2.2；§3.7 "span-corruption objective"；"about 1 trillion pre-training tokens"；"multi-task pre-training" | ✅ |
| 詞彙表 | §3.1.3："vocabulary of 32,000 wordpieces… German, French, and Romanian" | ✅ |
| 結果 | §3.7 | ✅ |

## concepts/text-to-text.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 是什麼 | §1："treat every text processing problem as a 'text-to-text' problem… same model, objective, training procedure, and decoding process" | ✅ |
| 任務前綴表 | §2.4："translate English to German: That is good."；"mnli premise: I hate pigeons…"→"entailment" | ✅ |
| hamburger | §2.4："we always count the model's output as wrong, though we never observed this behavior" | ✅ |
| 前綴用詞 | §2.4："changing the exact wording of the prefix had limited impact" | ✅ |
| 適用範圍 | §4.1 Text-to-text 段："generative tasks… classification tasks… even regression tasks like STS-B" | ✅ |
| 靈感來源 | §1："casting all text problems as question answering… language modeling… or span extraction" | ✅ |

## concepts/architecture-variants.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 關鍵：遮罩 | §3.2.1："A major distinguishing factor for different architectures is the 'mask'… used to zero out certain weights" | ✅ |
| 三種遮罩表 | §3.2.1、圖 3 說明（fully-visible／causal "sets any wi,j to zero if j > i"／causal with prefix） | ✅ |
| 四種架構表 | §2.1（single stack for language modeling／classification and span prediction）；§3.2.1（encoder-decoder、LM、prefix LM）；§4.1（"encoder-only" e.g. BERT） | ✅ |
| decoder 可當 LM | §3.2.1："a Transformer decoder (without an encoder) can be used as a language model… early work… used this architecture" | ✅ |
| Decoder-only 缺點與 Prefix LM | §3.2.1："causal masking forces the model's representation of the ith entry… unnecessarily limited… use fully-visible masking during the prefix" | ✅ |
| Prefix LM 像 BERT | §3.2.1："the main difference between a prefix LM and the BERT architecture is that the classifier is simply integrated into the output layer" | ✅ |
| 實驗結果（5 點） | §3.2.4："encoder-decoder architecture with the denoising objective performed best… sharing parameters… nearly as well… shared parameter encoder-decoder outperforms the decoder-only prefix LM… denoising objective always results in better" | ✅ |
| 計算量相近的原因 | §3.2.2："the encoder is only applied to the input sequence and the decoder is only applied to the output sequence" | ✅ |
| 家族樹 | 各頁出處；GPT-3 已標註為推論 | ✅ |

## 舊頁面修改

| 頁面／段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| masked-language-model.md／Denoising | §3.1.4："'denoising' objectives… (also called 'masked language modeling') produce better performance… quickly become standard" | ✅ |
| masked-language-model.md／Span corruption | §3.1.4："drops out 15% of tokens… All consecutive spans… replaced by a single sentinel token"；圖 2 說明 | ✅ |
| masked-language-model.md／例子表 | 圖 2 說明逐字對照（for、inviting、last；<X>、<Y>、<Z>） | ✅（依說明整理，已標註） |
| masked-language-model.md／最終版本 | §3.7："mean span length of 3 and corrupt 15%… marginally better… shorter target sequence lengths" | ✅ |
| self-attention.md／三種遮罩 | §3.2.1、圖 3 | ✅ |
| positional-encoding.md／相對位置 | §2.1："self-attention is order-independent (i.e. it is an operation on sets)… 32 embeddings… up to an offset of 128… share the position embedding parameters across all layers… each attention head uses a different" | ✅ |
| pretraining-finetuning.md／Transfer learning | 摘要："a model is first pre-trained on a data-rich task before being fine-tuned"；§1（ImageNet 監督 vs. NLP 無監督） | ✅ |
| pretraining-finetuning.md／微調方式 | §4.1 Training strategies 段 | ✅ |
| scaling.md／T5 | §4.1 Scaling 段；§3.7 | ✅ |
| embedding.md／T5 詞彙表 | §3.1.3："10 parts of English C4 data with 1 part each… only process a predetermined, fixed set of languages" | ✅ |
| gpt-3.md／修正「應該等於」 | Raffel §3.7 數字（Python 驗算）；Vaswani §3.2.2 "For each of these we use dk = dv = dmodel/h"（是選擇，不是規定） | ✅ |
| gpt-3.md／T5 支持 decoder-only 歸類 | §3.2.1、§4.1 | ✅ |
| transformer.md／T5 條列、LayerNorm 差異 | §3.1.1、§2.1 | ✅ |

## 統計

- 檢查段落：47
- ❌ 找不到對應：1（已修正）—— **AI 自行填補表格空格**（T5-Small 的 d_kv）
- 和前兩篇（3 個、8 個）相比明顯減少。可能原因：這次 N3 寫作時就以「每句都要能找到原文」為前提，寫之前先把要用的段落讀完，而不是先寫再對照
- R6 小提醒（不算錯誤）：T5 說原始 Transformer「使用 sin／cos 或學習出來的位置向量」，Vaswani 實際上是「選用 sin／cos，並實驗過學習版本」。兩者不衝突，`positional-encoding.md` 已分別寫出兩篇的說法
