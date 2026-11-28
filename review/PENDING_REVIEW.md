# 待审核论文（免费元数据版本）

运行日期：2026-11-28（UTC）

⚠️ **仅供人工审核；尚未公开发布。** 内容由 OpenAlex 元数据和关键词规则生成，中文摘要没有自动翻译，请核实原文、日期、相关性并改写摘要。

审核时在 PR 的 Files changed 中核查 papers.json；移除不合适论文后再合并。

- **[LQ-Rec: Late Quantization for Sequential Recommendation](https://doi.org/10.48550/arxiv.2611.25256)**（2026；生成式推荐；匹配分 18）
  - 标签：Semantic ID
  - 英文摘要（未经过 AI 翻译）: Generative retrieval (GR) for sequential recommendation compresses each item into a short semantic ID and trains an autoregressive decoder to generate next-item codes from a user history. While appealing for cold-start handling and storage, au- toregressive GR suffers a structural scaling limit: typically, longer semantic IDs reduce quantization error in principle but degrade ranking quality and quadratic memo…

- **[CARE: Contrastive-Anchored Residual Encoding with Listwise Reconstruction for Retrieval-Oriented Semantic IDs](https://doi.org/10.48550/arxiv.2611.20721)**（2026；生成式推荐；匹配分 15）
  - 标签：Semantic ID, RQ-VAE, 码本稳定性
  - 英文摘要（未经过 AI 翻译）: Generative retrieval replaces nearest-neighbor search with the generation of a document's semantic ID (SID), so the SID tokenizer bounds what the retriever can recall. Common SID constructions (residual k-means, RQ-VAE, finite scalar quantization, capacity balancing) optimize criteria defined on document embeddings alone and do not control whether a query can still find its relevant documents after quantizatio…

- **[From Patches to Codebooks: A Discrete-Continuous Spectrum of Transformer Tokenization Across Modalities](https://doi.org/10.70267/cai.v3n6.186196)**（2026；生成式推荐；匹配分 9）
  - 标签：码本稳定性
  - 英文摘要（未经过 AI 翻译）: Since its introduction, the Transformer has expanded from text processing to multimodal fields such as images and speech. During this process, a recurring question is how to convert continuous and heterogeneous raw signals into token representations that a model can process. This tokenization process is often accompanied by varying degrees of information selection or bottlenecks, and has consequently developed…

- **[Cluster-Guided Decoding with Trust-Region Constraints for Personalized Recommendation](https://doi.org/10.48550/arxiv.2611.22163)**（2026；生成式推荐；匹配分 9）
  - 标签：生成式推荐
  - 英文摘要（未经过 AI 翻译）: Most recommenders score each item in the catalog separately, and do not explicitly model which semantic region of the catalog a recommendation belongs to. Models expressive enough to offer that control are often too slow to run over a full catalog for online inference. In this paper, we present Cluster-Guided Generative Reconstruction (CG2R), which learns a hierarchy of semantic clusters and uses a cluster-lev…

- **[Better Rankers, Worse Retrievers: The Hidden Cost of RL Post-Training in Generative Recommendation](https://doi.org/10.48550/arxiv.2611.22838)**（2026；生成式推荐；匹配分 9）
  - 标签：Semantic ID
  - 英文摘要（未经过 AI 翻译）: Generative recommenders decode the semantic ID of a user's next item with a language model, and post-training them with reinforcement learning (RL) after supervised fine-tuning (SFT) has become standard practice. The gains are mostly reported on the first ten results, yet in deployment such models hand hundreds of candidates to a downstream ranker or reward model. We show that RL post-training has a hidden cos…

- **["None of This Is Normal": The Golden Age of Legal Bribery](https://openalex.org/W7167871313)**（2026；金融市场；匹配分 5）
  - 标签：特朗普言论, 黄金
  - 英文摘要（未经过 AI 翻译）: Pennsylvania who signed a petition circulated by his super PAC. 5 The petition was nominally "in support of free speech [and the] right to bear arms."6 Musk delivered such rewards, replete with oversized sweepstakes checks, that garnered exactly the attention, publicity, and incentives of the spectacle-by-design. 7 Functionally, however, Musk's petition-based rewards had little to do with free speech or the ri…
