# Masked Language Model（MLM，遮罩語言模型）

> **類型**：概念 ｜ **出處**：[Devlin 2018](../papers/devlin-2018.md)、[Raffel 2019](../papers/raffel-2019.md)、[Dosovitskiy 2020](../papers/dosovitskiy-2020.md) ｜ **相關**：[ViT](../models/vit.md)、[T5](../models/t5.md)、[BERT](../models/bert.md)、[語言模型](language-model.md)、[預訓練與微調](pretraining-finetuning.md)

## 是什麼

一種預訓練任務：隨機把輸入中的一些 token 遮住，讓模型根據**前後文**猜出原本的字。概念和「克漏字測驗」（Cloze task）相同。〔出處：[Devlin 2018 §1、§3.1](../papers/devlin-2018.md)〕

## 為什麼需要它

一般的[語言模型](language-model.md)只能由左到右（或由右到左）訓練。如果直接讓模型同時看左右兩邊再預測某個字，多層網路中每個字會間接「看到自己」，模型就能輕易作弊。把要預測的字遮住，就能安全地訓練雙向模型。〔出處：[Devlin 2018 §3.1](../papers/devlin-2018.md)〕

## 做法

〔出處：[Devlin 2018 §3.1](../papers/devlin-2018.md)〕

1. 每段輸入隨機選出 **15%** 的 token 作為預測目標。
2. 被選中的 token：
   - **80%** 換成特殊符號 `[MASK]`
   - **10%** 換成隨機的字
   - **10%** 保持不變
3. 模型在這些位置的輸出向量經過 [Softmax](softmax.md)，對整個詞彙表預測原本的字。

只預測被選中的字，不重建整段輸入。〔出處：[Devlin 2018 §3.1](../papers/devlin-2018.md)〕

## 例子

原句是「my dog is hairy」，選中第 4 個 token「hairy」：〔出處：[Devlin 2018 附錄 A.1](../papers/devlin-2018.md)〕

| 機率 | 模型看到的輸入 | 模型要猜 |
|---|---|---|
| 80% | my dog is `[MASK]` | hairy |
| 10% | my dog is apple | hairy |
| 10% | my dog is hairy | hairy |
〔出處：同上〕

## 為什麼不全部換成 `[MASK]`

`[MASK]` 只在預訓練時出現，微調時不會出現，全部換成 `[MASK]` 會造成兩個階段的落差。混入隨機字和原字之後，模型不知道哪些字要被預測、哪些字被換過，只好對每個 token 都保持完整的上下文理解。隨機替換只占全部 token 的 1.5%（15% 的 10%），不會傷害模型的理解能力。〔出處：[Devlin 2018 §3.1、附錄 A.1](../papers/devlin-2018.md)〕

## 代價

每批資料只有 15% 的 token 被拿來預測，比一般語言模型（每個 token 都預測）少，所以可能需要更多預訓練步數。〔出處：[Devlin 2018 附錄 A.1](../papers/devlin-2018.md)〕

## ⚠️ 不要搞混：兩種「mask」

這裡的 mask 是把**輸入的字遮住**，讓模型去猜。它和 [Self-Attention](self-attention.md) 頁面提到的「遮罩」（在 Decoder 中禁止 attention 看後面的字）是兩件不同的事，只是名稱相同。〔出處：[Devlin 2018 §3.1](../papers/devlin-2018.md)、[Vaswani 2017 §3.2.3](../papers/vaswani-2017.md)〕

## 更廣的名稱：Denoising 目標

[T5](../models/t5.md) 的論文把這類目標統稱為「denoising」（去噪）目標，也稱為 masked language modeling：訓練模型預測輸入中缺少或被破壞的 token。這類目標已被證明比因果語言模型目標表現更好，因此很快成為標準做法。〔出處：[Raffel 2019 §3.1.4](../papers/raffel-2019.md)〕

## T5 的變化：Span Corruption

T5 受 BERT 啟發，但做法不同：隨機丟掉輸入中 15% 的 token，**連續被丟掉的 token 合併成一個特殊標記**（sentinel），模型要輸出被丟掉的所有片段，並用同樣的標記隔開。〔出處：[Raffel 2019 §3.1.4、圖 2](../papers/raffel-2019.md)〕

以論文圖 2 為例，原句「Thank you for inviting me to your party last week.」中，「for」「inviting」「last」被選中。「for inviting」是連續的，所以合併成一個標記 `<X>`；「last」換成 `<Y>`；輸出最後再加上結尾標記 `<Z>`：〔出處：[Raffel 2019 圖 2](../papers/raffel-2019.md)〕

| | 內容 |
|---|---|
| 輸入 | `Thank you <X> me to your party <Y> week.` |
| 輸出 | `<X> for inviting <Y> last <Z>` |
〔出處：依 [Raffel 2019 圖 2](../papers/raffel-2019.md) 的說明整理〕

和 BERT 的差別：BERT 只在被遮住的位置預測原字；T5 的輸出是一段**文字**，符合 [Text-to-Text](text-to-text.md) 框架。T5 最終版本使用平均長度 3 的片段、遮住 15%，表現略好，而且因為目標序列較短，計算也比較省。〔出處：[Devlin 2018 §3.1](../papers/devlin-2018.md)、[Raffel 2019 §3.1.4、§3.7](../papers/raffel-2019.md)〕

## 用到圖片：Masked Patch Prediction

[ViT](../models/vit.md) 的作者初步試了模仿 BERT 的做法：遮住部分 patch 讓模型預測。自監督預訓練的 ViT-B/16 在 ImageNet 達到 79.9%，比從零訓練好 2%，但仍比監督式預訓練差 4%。〔出處：[Dosovitskiy 2020 §4.6](../papers/dosovitskiy-2020.md)〕
