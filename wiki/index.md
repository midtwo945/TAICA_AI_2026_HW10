# Wiki 目錄：Transformer 論文與其應用變化

規則見 [CLAUDE.md](../CLAUDE.md)，執行紀錄見 [log.md](log.md)。

## 論文頁

- [Bahdanau 2014](papers/bahdanau-2014.md)：在 RNN 翻譯模型加入 attention，解決固定長度向量的瓶頸（Transformer 的前傳）
- [Vaswani 2017](papers/vaswani-2017.md)：Attention Is All You Need，提出完全只用 attention 的 Transformer
- [Devlin 2018](papers/devlin-2018.md)：BERT，只用 Encoder、以克漏字預訓練出雙向表示
- [Raffel 2019](papers/raffel-2019.md)：T5，把所有任務變成文字轉文字，系統性比較架構與預訓練目標
- [Brown 2020](papers/brown-2020.md)：GPT-3，把自迴歸語言模型放大到 1,750 億參數，不微調也能做任務
- [Dosovitskiy 2020](papers/dosovitskiy-2020.md)：ViT，把圖片切成 patch，用標準 Transformer Encoder 做圖片辨識

## 概念頁

- [Encoder-Decoder](concepts/encoder-decoder.md)：Encoder 讀原文、Decoder 產生譯文的架構，以及固定長度向量的瓶頸
- [RNN](concepts/rnn.md)：按順序讀入序列的神經網路，包含雙向 RNN 與無法平行計算的限制
- [Attention](concepts/attention.md)：每一步自己決定要看原文哪些字（算分數 → softmax → 加權平均）
- [Softmax](concepts/softmax.md)：把一串分數轉成加起來等於 1 的權重；為何要除以 √d_k、如何用 −∞ 遮罩
- [Self-Attention](concepts/self-attention.md)：句子對自己做 attention；Q／K／V、Scaled Dot-Product、遮罩
- [Multi-Head Attention](concepts/multi-head-attention.md)：同時做多組 attention，從不同角度看句子
- [Positional Encoding](concepts/positional-encoding.md)：用 sin／cos 為每個位置加上位置資訊
- [Embedding](concepts/embedding.md)：把 token 轉成向量；token 的切法（單字 vs. 子詞）；BERT 的三種 embedding 相加
- [語言模型](concepts/language-model.md)：由左到右預測文字；單向 vs. 雙向
- [預訓練與微調](concepts/pretraining-finetuning.md)：先用無標註資料學語言，再用任務資料微調
- [Masked Language Model](concepts/masked-language-model.md)：遮住 15% 的 token 讓模型猜（克漏字）
- [In-context Learning](concepts/in-context-learning.md)：在輸入中給說明和範例，不更新參數（zero-／one-／few-shot）
- [規模化](concepts/scaling.md)：模型越大能力越強的規律與極限
- [Text-to-Text](concepts/text-to-text.md)：所有任務都是「輸入文字 → 輸出文字」，用前綴指定任務
- [Transformer 架構家族](concepts/architecture-variants.md)：三種遮罩、四種架構（encoder-only／decoder-only／prefix LM／encoder-decoder）
- [Patch Embedding](concepts/patch-embedding.md)：把圖片切成固定大小的 patch，當成 token
- [歸納偏置](concepts/inductive-bias.md)：架構內建的假設；資料少時有用，資料多時被規模取代

## 模型頁

- [Transformer](models/transformer.md)：Encoder、Decoder 各 6 層，只用 attention 和前饋網路
- [BERT](models/bert.md)：只用 Encoder 的雙向模型，預訓練（MLM + NSP）後微調
- [GPT-3](models/gpt-3.md)：1,750 億參數的自迴歸模型，用 in-context learning 而不微調
- [T5](models/t5.md)：Encoder-Decoder，text-to-text，最大 110 億參數
- [ViT](models/vit.md)：只用 Encoder 的圖片模型，資料夠多時勝過 CNN
