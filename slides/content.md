# 簡報內容（N6 產出）

規則：每頁只能使用大綱中該頁列出的 Wiki 頁面（R11）。每個要點後面的 `〈…〉` 標出它來自哪個 Wiki 頁面。
術語第一次出現時用 **粗體** 並附上解釋（R12）。

---

## 1｜Transformer：一個架構，撐起整個 AI 時代
Wiki：index、papers/vaswani-2017

- 副標：從一篇翻譯論文，到 BERT、GPT-3、T5、ViT 〈index〉
- 時間軸：〈index〉
  - 2014 Bahdanau：在翻譯模型加入 **Attention**（每一步自己決定要看原文哪些字）
  - 2017 **Transformer**：完全只用 attention 的模型
  - 2018 **BERT**：只用 Transformer 的 Encoder（第 5 頁說明），用「猜被遮住的字」來學語言
  - 2019 **T5**：把所有任務變成文字轉文字
  - 2020 **GPT-3**：放大到 1,750 億參數，不用針對每個任務另外訓練
  - 2020 **ViT**：把圖片切成小塊，用 Transformer 做圖片辨識
- 之後的 BERT、GPT-3、T5、ViT 都是以 Transformer 為基礎的變化 〈vaswani-2017〉

## 2｜這堂課的地圖
Wiki：concepts/architecture-variants

- 學完你能回答：① 模型怎麼知道翻譯時該「注意」原文哪些字？② Transformer 內部怎麼運作？③ BERT、GPT-3、T5、ViT 差在哪裡？
- 家族樹預告（Encoder 負責處理輸入、Decoder 負責產生輸出，第 5 頁詳細說明）：Transformer（兩者都用）→ 只用 Encoder：BERT、ViT｜只用 Decoder：GPT 系列 → GPT-3｜兩者都保留：T5 〈architecture-variants〉

## 3｜電腦怎麼讀字？Token 與 Embedding
Wiki：concepts/embedding

- 神經網路只能處理數字，所以要先把每個字轉成一個向量 〈embedding〉
- **Token**：模型處理的單位，不一定等於一個完整的單字 〈embedding〉
- **Embedding**：把每個 token 轉成一個向量；Transformer 用的是 512 維、學習出來的向量 〈embedding〉
- 切法的演變：〈embedding〉
  - Bahdanau 2014：以完整單字為單位，只留最常見的 30,000 個字，其他字一律變成 `[UNK]`（未知字）
  - BERT：用 WordPiece 切成子詞（把單字切成較小的片段），「playing」→ `play` + `##ing`

## 4｜Softmax：把分數變成權重
Wiki：concepts/softmax

- **Softmax**：把一串任意分數，轉成一串「都是正數、加起來等於 1」的權重 〈softmax〉
- 公式：`α_j = exp(e_j) / Σ_k exp(e_k)` 〈softmax〉
- 例子：分數 `[2.0, 1.0, 0.1]` → 權重約 `[0.659, 0.242, 0.099]` 〈softmax〉
- 分數最高的拿到大部分權重，但其他項目仍保有一些權重 〈softmax〉

## 5｜起點：RNN 翻譯模型的瓶頸
Wiki：concepts/rnn、concepts/encoder-decoder、papers/bahdanau-2014

- **RNN**（循環神經網路）：按順序一個字一個字讀；每一步的隱藏狀態可以想成「到目前為止讀到內容的摘要」 〈rnn〉
- **Encoder-Decoder**：Encoder 讀入原文、轉成向量；Decoder 根據這個向量逐字產生譯文 〈encoder-decoder〉
- 早期做法：Encoder 把**整句**壓縮成**一個固定長度的向量** 〈encoder-decoder〉
- 問題（瓶頸）：不論句子多長都要塞進同一個大小的向量，句子越長，翻譯品質掉得越快 〈encoder-decoder、bahdanau-2014〉

## 6｜Attention：翻譯每個字時，回頭看原文
Wiki：concepts/attention、papers/bahdanau-2014

- 解法：Encoder 為原文**每個字**都保留一個向量 〈attention〉
- **Attention**：Decoder 每產生一個譯文字，就自己決定要看原文的哪些字 〈attention〉
  1. 算分數：原文每個字和現在要產生的字有多相關
  2. 用 softmax 轉成權重
  3. 用權重把原文的向量加權平均，交給 Decoder
- **軟對齊**：每個譯文字可以同時參考好幾個原文字。例：「the man」→ 法文「l' homme」，產生「l'」時要同時看「the」和「man」 〈attention〉
- 結果：BLEU（翻譯品質指標，越高越好）26.75，舊架構 17.82；句子超過 50 個字也沒有退步 〈bahdanau-2014〉

## 7｜Attention Is All You Need（2017）
Wiki：papers/vaswani-2017、models/transformer、concepts/rnn

- RNN 的限制：第 t 步要等第 t-1 步算完，無法平行計算 〈rnn〉
- **Transformer**：保留 Encoder-Decoder 結構，但**完全拿掉 RNN，只用 attention** 〈vaswani-2017、transformer〉
- 和 RNN 比較：〈transformer、rnn〉
  - Transformer 可以平行計算；RNN 必須一步一步依序算
  - 句子中任兩個字：Transformer 一步就能互相影響；RNN 要經過的步數隨句子長度增加
- 結果：英翻德 BLEU 28.4；base 模型用 8 張 P100 GPU 訓練約 12 小時 〈vaswani-2017〉

## 8｜Self-Attention：Q、K、V
Wiki：concepts/self-attention、concepts/softmax

- **Self-Attention**：在同一個句子內部做 attention，每個字都去看句子裡所有的字 〈self-attention〉
- 每個字有三個向量：〈self-attention〉
  - **Query（Q）**：我要找什麼
  - **Key（K）**：我有什麼可以被找
  - **Value（V）**：被找到之後要提供的內容
- 公式：`Attention(Q, K, V) = softmax(Q·Kᵀ / √d_k) · V` 〈self-attention〉
- 為什麼除以 √d_k（d_k 是 Key 的維度）：維度大時內積會變得很大，模型會很難學習 〈self-attention、softmax〉
- **遮罩（mask）**：Decoder 產生第 i 個字時不能偷看後面；把那些分數設成 −∞，softmax 後權重就變成 0 〈self-attention、softmax〉
- 互動 demo：3 個字 `[1,0]`、`[0,1]`、`[1,1]` 的權重（簡化版：Q = K = V），可切換有／無遮罩 〈self-attention〉
  - 無遮罩：字 1 `[0.401, 0.198, 0.401]`；字 2 `[0.198, 0.401, 0.401]`；字 3 `[0.248, 0.248, 0.503]`
  - 有遮罩：字 1 `[1, 0, 0]`；字 2 `[0.33, 0.67, 0]`；字 3 `[0.248, 0.248, 0.503]`

## 9｜Multi-Head 與 Positional Encoding
Wiki：concepts/multi-head-attention、concepts/positional-encoding

- **Multi-Head Attention**：同時做好幾組 attention（稱為「頭」），最後接起來 〈multi-head-attention〉
  - Transformer 用 8 個頭，每個頭 64 維（512 ÷ 8）
  - 論文觀察到不同的頭學會了不同的任務
  - 只用 1 個頭時，BLEU 比最佳設定低 0.9
- **Positional Encoding**：Self-Attention 本身不管字的先後，所以要為每個位置產生一個位置向量，加到字的 embedding 上 〈positional-encoding〉
  - 用不同頻率的 sin、cos 產生
  - 讓模型自己學位置向量，結果和 sin／cos 版本幾乎一樣

## 10｜Transformer 全貌
Wiki：models/transformer

- 資料流程：〈transformer〉
  1. 字 → Embedding → 加上 Positional Encoding
  2. Encoder：6 層
  3. Decoder：6 層，參考 Encoder 的輸出，一次預測一個字
  4. 線性轉換 + Softmax → 每個候選字的機率
- Encoder 每層：多頭自注意力 + 前饋網路（對每個位置各自做兩次線性轉換） 〈transformer〉
- Decoder 每層：遮罩自注意力 + Encoder-Decoder Attention + 前饋網路 〈transformer〉
- 每個子層都有**殘差連接**（把輸入直接加回輸出）和 **LayerNorm**（正規化） 〈transformer〉
- 基本設定：N（層數）= 6、d_model（字向量的維度）= 512、d_ff（前饋網路中間層的維度）= 2048、h（頭數）= 8 〈transformer〉

## 11｜一個遮罩，分出整個家族
Wiki：concepts/architecture-variants、papers/raffel-2019

- 不同架構最主要的差別，在於 attention 用的遮罩 〈architecture-variants〉
- 三種遮罩：〈architecture-variants〉
  - **全可見**：每個位置都能看全部 → Encoder、BERT
  - **因果**：只能看自己和前面 → Decoder、語言模型
  - **前綴**：前綴部分全可見，之後用因果 → Prefix LM
- 四種架構：Encoder-Decoder（Transformer、T5）、Encoder-only（BERT、ViT）、Decoder-only（GPT 系列）、Prefix LM 〈architecture-variants〉
- T5 的實驗：在 text-to-text 框架下，Encoder-Decoder 表現最好 〈architecture-variants、raffel-2019〉

## 12｜BERT：只用 Encoder，做克漏字
Wiki：models/bert、concepts/masked-language-model、concepts/pretraining-finetuning、papers/devlin-2018

- **BERT**：多層的**雙向** Transformer Encoder，每個字可以同時看左右兩邊 〈bert〉
- **預訓練 → 微調**：先用大量沒有標註的文字預訓練，再用各任務的標註資料微調 〈pretraining-finetuning〉
- **Masked Language Model（MLM）**：隨機選 15% 的 token 讓模型猜原本的字 〈masked-language-model〉
  - 被選中的：80% 換成 `[MASK]`、10% 換成隨機字、10% 保持不變
  - 例：`my dog is hairy` → `my dog is [MASK]`，模型要猜出 hairy
- 微調：分類任務只要把 `[CLS]` 的向量接到一層輸出層 〈bert〉
- 結果：11 個任務達到當時最佳；GLUE（一組多樣的語言理解測驗）80.5 〈devlin-2018〉
- 實驗：改成只看左邊（像 GPT），所有任務都變差 〈devlin-2018〉

## 13｜GPT-3：只用 Decoder，給範例就會做
Wiki：models/gpt-3、concepts/in-context-learning、concepts/language-model、papers/brown-2020

- **GPT-3**：1,750 億參數的**自迴歸語言模型**，使用時讓它「預測接下來的內容」 〈gpt-3、language-model〉
- 屬於「只用 Decoder」的類型（這是依 BERT、T5 論文的說法推論，GPT-3 原文沒有直接這樣寫） 〈gpt-3〉
- **In-context Learning**：不更新任何參數，把任務說明和範例寫在輸入裡 〈in-context-learning〉
  - Zero-shot：只有一句說明｜One-shot：說明 + 1 個範例｜Few-shot：說明 + 10～100 個範例
- 算術例子：`Q: What is 48 plus 76?  A: 124` 〈in-context-learning〉
- 結果（few-shot）：2 位數加法 100%、3 位數加法 80.2%、5 位數只有 9～10% 〈brown-2020〉
- 不是背答案：3 位數加法題只有 0.8% 出現在訓練資料中；錯誤常常是「忘了進位」 〈brown-2020〉
- 代價：單向模型在需要「回頭比較兩段內容」的任務上表現較差 〈brown-2020〉

## 14｜T5：一切都是文字轉文字
Wiki：models/t5、concepts/text-to-text、concepts/masked-language-model、papers/raffel-2019

- **Text-to-Text**：每一個任務都是「輸入文字 → 輸出文字」，用任務前綴指定要做什麼 〈text-to-text〉
  - `translate English to German: That is good.` → `Das ist gut.`
  - `mnli premise: I hate pigeons. hypothesis: …` → `entailment`
- **T5**：標準的 Encoder-Decoder Transformer 〈t5〉
- 預訓練（span corruption）：隨機遮住 15% 的 token，連續被遮住的字合併成一個標記，模型要輸出被遮住的片段 〈t5、masked-language-model〉
  - `Thank you <X> me to your party <Y> week.` → `<X> for inviting <Y> last <Z>`
- 結果：最大 110 億參數；24 個任務中 18 個達到當時最佳 〈raffel-2019〉

## 15｜ViT：一張圖值 16×16 個字
Wiki：models/vit、concepts/patch-embedding、concepts/inductive-bias、papers/dosovitskiy-2020

- **ViT**：把圖片切成 **patch**（固定大小的小方塊），每個 patch 當成一個 token，丟進標準的 Transformer Encoder 〈vit、patch-embedding〉
- patch 數：`N = H × W / P²`；例：假設 224 × 224 的圖片、16 × 16 的 patch → 196 個 〈patch-embedding〉
- 前面加一個分類 token（類似 BERT 的 `[CLS]`），再加上位置 embedding 〈vit〉
- **歸納偏置**：模型架構中事先內建的假設。CNN（卷積網路，當時圖片辨識的主流）內建「局部性」等圖片專用假設，ViT 幾乎沒有 〈inductive-bias、dosovitskiy-2020〉
  - 只用 ImageNet（130 萬張）：ViT 比同樣大小的 ResNet（一種 CNN）低幾個百分點
  - 用 1,400 萬～3 億張預訓練：ViT 反超
- 作者的結論：「大規模訓練勝過歸納偏置」 〈inductive-bias、dosovitskiy-2020〉

## 16｜共同主題：越大越強
Wiki：concepts/scaling

- GPT-3：模型越大，越擅長 in-context learning；算術能力從 130 億到 1,750 億參數有明顯跳升 〈scaling〉
- BERT：模型越大，所有測試任務都越好，連只有 3,600 筆訓練資料的任務也一樣 〈scaling〉
- T5：「用更多資料訓練小模型」常常不如「訓練大模型、但步數少一點」 〈scaling〉
- ViT：在測試範圍內還沒有飽和 〈scaling〉
- 極限：GPT-3 的作者認為單純放大可能會碰到預訓練目標本身的極限 〈scaling〉

## 17｜總整理與常見誤會
Wiki：concepts/architecture-variants、concepts/masked-language-model、concepts/in-context-learning

- 比較表：〈architecture-variants〉

  | 模型 | 架構 | 遮罩 |
  |---|---|---|
  | Transformer | Encoder-Decoder | Encoder 全可見、Decoder 因果 |
  | BERT | Encoder-only | 全可見 |
  | GPT-3 | Decoder-only（推論） | 因果 |
  | T5 | Encoder-Decoder | Encoder 全可見、Decoder 因果 |
  | ViT | Encoder-only（圖片） | 全可見 |

- ⚠️ 兩種「mask」：BERT 的 `[MASK]` 是把**輸入的字遮住**讓模型猜；attention 的遮罩是**禁止看後面的字**。名稱相同，但不是同一件事 〈masked-language-model〉
- ⚠️ 兩種「few-shot」：GPT-3 是在**輸入中給範例**、不更新參數；ViT 是**凍結模型**，用少量圖片的特徵另外算一個分類器 〈in-context-learning〉

## 18｜小測驗與參考資料
Wiki：index

- Q1：為什麼 Transformer 比 RNN 容易平行計算？ → RNN 第 t 步要等第 t-1 步；self-attention 一次看全部 〈第 7 頁〉
- Q2：BERT 和 GPT-3 最大的差別是什麼？ → 遮罩：BERT 雙向（全可見），GPT-3 只看前面（因果） 〈第 11～13 頁〉
- Q3：ViT 在什麼情況下會贏過 CNN？ → 預訓練資料夠多的時候 〈第 15 頁〉
- 參考資料：6 篇論文（arXiv 連結）與本 Wiki 〈index〉
