# 語言模型（Language Model）

> **類型**：概念 ｜ **出處**：[Devlin 2018](../papers/devlin-2018.md)、[Bahdanau 2014](../papers/bahdanau-2014.md)、[Vaswani 2017](../papers/vaswani-2017.md)、[Brown 2020](../papers/brown-2020.md) ｜ **相關**：[GPT-3](../models/gpt-3.md)、[Masked Language Model](masked-language-model.md)、[預訓練與微調](pretraining-finetuning.md)、[BERT](../models/bert.md)

## 是什麼

由左到右的模型會把一段文字的機率拆成一連串「根據前面所有的字，預測下一個字」的機率相乘。[Bahdanau 2014](../papers/bahdanau-2014.md) 的 Decoder 就是用這種方式定義譯文的機率：第 t 個字的機率取決於前 t-1 個字（以及原文）。〔出處：[Bahdanau 2014 §2.1、式 (2)](../papers/bahdanau-2014.md)〕

[Transformer](../models/transformer.md) 的 Decoder 也是每次產生一個字，並把已產生的字當作下一步的輸入，這種方式稱為 auto-regressive（自迴歸）。〔出處：[Vaswani 2017 §3](../papers/vaswani-2017.md)〕

[Devlin 2018](../papers/devlin-2018.md) 指出，標準的條件式語言模型只能由左到右、或由右到左訓練。〔出處：[Devlin 2018 §3.1](../papers/devlin-2018.md)〕

## 單向 vs. 雙向

〔出處：[Devlin 2018 §1、§2.1、§3](../papers/devlin-2018.md)〕

| 類型 | 代表 | 做法 |
|---|---|---|
| 單向（由左到右） | OpenAI GPT | self-attention 中每個 token 只能看前面的 token |
| 淺層雙向 | ELMo | 分別訓練「由左到右」和「由右到左」兩個模型，再把結果接起來 |
| 深層雙向 | [BERT](../models/bert.md) | 用 [Masked Language Model](masked-language-model.md) 訓練，每一層都能同時看左右兩邊 |
〔出處：同上〕

## 單向的限制

對問答這類任務，每個字都需要同時參考前後文，只看左邊的模型表現會比較差。BERT 的實驗中，把模型改成由左到右訓練後，所有任務的表現都下降。〔出處：[Devlin 2018 §1、§5.1](../papers/devlin-2018.md)〕

BERT 的作者也指出 ELMo 的做法有缺點：成本是單一雙向模型的兩倍；而且每一層都能看左右兩邊的深層雙向模型，能力嚴格來說比它更強。〔出處：[Devlin 2018 §5.1](../papers/devlin-2018.md)〕

## 單向的用途

只看左邊的版本可以用來**生成文字**，因為產生下一個字時本來就只有前面的字可以參考。這也是它常被稱為「Transformer decoder」的原因。〔出處：[Devlin 2018 §3 註 4](../papers/devlin-2018.md)〕

## GPT-3：把單向語言模型放大

[GPT-3](../models/gpt-3.md) 是一個 1,750 億參數的自迴歸語言模型。作者選擇自迴歸模型，是因為這類模型容易取樣生成文字，也容易計算機率。〔出處：[Brown 2020 摘要、§5](../papers/brown-2020.md)〕

GPT-3 的作者也承認單向的代價：在填空、回頭比較兩段內容、或要讀完長文再回答簡短答案的任務上，雙向模型可能較有優勢。這和 [BERT](../models/bert.md) 論文的主張一致。〔出處：[Brown 2020 §5](../papers/brown-2020.md)、[Devlin 2018 §1](../papers/devlin-2018.md)〕
