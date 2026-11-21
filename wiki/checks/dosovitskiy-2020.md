# N3.5 原文比對紀錄：論文 6（Dosovitskiy 2020，ViT）

依 [CLAUDE.md](../../CLAUDE.md) 的 R20 逐段比對。原文：[raw/dosovitskiy-2020.txt](https://arxiv.org/abs/2010.11929)

結果：✅ = 找到對應句子；❌ = 找不到 → 已修正

## papers/dosovitskiy-2020.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 頁首（單位、ICLR 2021） | 首頁 "Google Research, Brain Team"；頁首 "Published as a conference paper at ICLR 2021" | ✅ |
| 一句話摘要 | 摘要："a pure transformer applied directly to sequences of image patches… requiring substantially fewer computational resources to train" | ✅ |
| 要解決的問題（2 段） | 摘要 "attention is either applied in conjunction with convolutional networks…"；§2 "quadratic cost in the number of pixels"；§1 "not yet been scaled effectively on modern hardware accelerators" | ✅ |
| 提出的方法 1～4 | §3.1："follow the original Transformer… as closely as possible… can be used almost out of the box"；圖 1 說明 | ✅ |
| 主要發現 | §1："modest accuracies of a few percentage points below ResNets… lack some of the inductive biases… large scale training trumps inductive bias" | ✅ |
| 主要結果 | §1（88.55%、90.72%、94.55%、77.63%）；§4.4 "approximately 2 - 4× less compute… appear not to saturate" | ✅ |
| 模型學到了什麼 | §4.5："closer patches tend to have more similar position embeddings… row-column structure… some heads attend to most of the image already in the lowest layers… attention distance increases with network depth" | ✅ |
| 自監督 | §4.6："79.9% accuracy on ImageNet, a significant improvement of 2%… still 4% behind supervised pre-training" | ✅ |
| 未來方向 | §5："detection and segmentation… self-supervised pre-training… further scaling" | ✅ |
| 在 Wiki 中的位置 | 第一版寫「證明 Transformer 不只是語言模型」，原文沒有這個說法 | ❌ → 改成 §5 原文的意思："interpret an image as a sequence of patches and process it by a standard Transformer encoder as used in NLP" |

## models/vit.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 是什麼 | §1："Image patches are treated the same way as tokens (words)"；圖 1 "standard Transformer encoder" | ✅ |
| 資料流程 1～6 | §3.1 逐句（patch embeddings、"Similar to BERT's [class] token"、"standard learnable 1D position embeddings"、MSA 與 MLP 交替、"MLP with one hidden layer at pre-training time and by a single linear layer at fine-tuning time"） | ✅ |
| 模型大小表 | 表 1；§4.1 "'Base' and 'Large' models are directly adopted from BERT and we add the larger 'Huge'" | ✅ |
| 命名方式 | §4.1："ViT-L/16 means the 'Large' variant with 16 × 16 input patch size… smaller patch size are computationally more expensive" | ✅ |
| 與原始 Transformer 的差異 | §3.1："Layernorm (LN) is applied before every block, and residual connections after every block" | ✅ |
| 訓練資料表 | §4.1（1k 類 1.3M 張；21k 類 14M 張；18k 類 303M 張） | ✅ |
| 微調解析度與內插 | §3.2："fine-tune at higher resolution… 2D interpolation of the pre-trained position embeddings… the only points at which an inductive bias about the 2D structure… is manually injected" | ✅ |
| 混合架構 | §3.1 Hybrid Architecture；§4.4 "hybrids slightly outperform ViT at small computational budgets, but the difference vanishes for larger models" | ✅ |
| ⚠️ few-shot | §4.1 Metrics："solving a regularized least-squares regression problem that maps the (frozen) representation…" | ✅ |

## concepts/patch-embedding.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 為什麼需要 | §3.1 "1D sequence of token embeddings"；§2 "quadratic cost" | ✅ |
| 做法 | 第一版寫「大小相同、**不重疊**的 patch」。§3.1 只說 "fixed-size patches"，**沒有說不重疊** | ❌ → 刪除「不重疊」 |
| 公式 N = HW/P² | §3.1 | ✅ |
| 計算例子 | 已標註為假設的圖片大小、以 Python 計算；名稱欄第一版寫「ViT-?/32」，改成原文出現過的 ViT-B/32、L/16、H/14（§4.2、§4.4） | ✅（假設，已標註） |
| patch 越小越貴 | §4.1 | ✅ |
| 標題的意思 | 第一版寫「標題指的就是每個 16×16 patch 像一個字」，原文沒有解釋標題 | ❌ → 改成「呼應 §1 的說法：patch 被當成 token（words）處理」 |
| 模型學到的 patch 特徵 | 第一版寫「濾波器看起來像基底函數」；§4.5 原文是「濾波器的**主成分**」"top principal components of the learned embedding filters… resemble plausible basis functions" | ❌ → 補上「做主成分分析」 |
| 文字 vs. 圖片對照表 | 第一版 BERT 欄寫「查詢 embedding 表」，Devlin 原文只說 "WordPiece embeddings"，沒有說「查表」 | ❌ → 改成「token embedding」 |

## concepts/inductive-bias.md

| 段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| 是什麼 | §3.1："In CNNs, locality, two-dimensional neighborhood structure, and translation equivariance are baked into each layer"。第一版另外加了「平移等變性（物體移動位置後，特徵也跟著移動）」的白話解釋，**原文沒有** | ❌ → 刪除括號內的解釋 |
| ViT 的歸納偏置很少 | §3.1："only MLP layers are local and translationally equivariant, while the self-attention layers are global… all spatial relations between the patches have to be learned from scratch" | ✅ |
| 資料量表 | §4.3："ViT-Large models underperform compared to ViT-Base… With ImageNet-21k pre-training, their performances are similar. Only with JFT-300M, do we see the full benefit" | ✅ |
| JFT 子集 | §4.3："ViT-B/32 is slightly faster than ResNet50; it performs much worse on the 9M subset, but better on 90M+ subsets" | ✅ |
| 作者的結論 | §4.3："convolutional inductive bias is useful for smaller datasets, but for larger ones, learning the relevant patterns directly from data is sufficient, even beneficial" | ✅ |
| 2D 結構證據 | §4.5："position embeddings learn to represent 2D image topology explains why hand-crafted 2D-aware embedding variants do not yield improvements" | ✅ |

## 舊頁面修改

| 頁面／段落 | 原文對應句子（節錄） | 結果 |
|---|---|---|
| architecture-variants.md／ViT 列、家族樹 | §3.1、圖 1 "standard Transformer encoder" | ✅ |
| positional-encoding.md／ViT 三段 | §3.1（1D、2D-aware 無明顯改善）、§4.5、§3.2 | ✅ |
| masked-language-model.md／Masked patch | §4.6 | ✅ |
| scaling.md／ViT 三段 | §1、§4.3、§4.4；§1 "over 100B parameters… still no sign of saturating performance" | ✅ |
| pretraining-finetuning.md／ViT 兩段 | §3.2 "zero-initialized D × K feedforward layer"；§1 "in supervised fashion" | ✅ |
| transformer.md／LayerNorm、跨到圖片 | §3.1 | ✅ |
| vaswani-2017.md／後續 | Dosovitskiy §1、§3.1 | ✅ |
| in-context-learning.md／⚠️ few-shot | §4.1 Metrics | ✅ |

## 統計

- 檢查段落：38
- ❌ 找不到對應：6（全部已修正）
  - 4 個是 **AI 自己加的白話解釋或修飾**：「不重疊」、「平移等變性」的括號說明、標題的解讀、「查詢 embedding 表」
  - 1 個是 **漏掉關鍵限定詞**：「濾波器的主成分」寫成「濾波器」
  - 1 個是 **AI 的總結判斷**：「證明 Transformer 不只是語言模型」
- 錯誤數從論文 5 的 1 個又回升到 6 個。這篇是視覺領域，AI 為了讓不熟的讀者看懂，在寫作時加了很多原文沒有的解釋。**為了教學而補的白話說明，正好是最容易超出原文的地方**
