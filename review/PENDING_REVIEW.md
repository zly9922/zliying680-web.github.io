# 待审核论文（免费元数据版本）

运行日期：2026-10-27（UTC）

⚠️ **仅供人工审核；尚未公开发布。** 内容由 OpenAlex 元数据和关键词规则生成，中文摘要没有自动翻译，请核实原文、日期、相关性并改写摘要。

审核时在 PR 的 Files changed 中核查 papers.json；移除不合适论文后再合并。

- **[Personalized LLM Recommendation with Semantic IDs: Autoregressive Beam Search vs. Multi-Token Prediction](https://doi.org/10.48550/arxiv.2610.15864)**（2026；生成式推荐；匹配分 15）
  - 标签：Semantic ID
  - 英文摘要（未经过 AI 翻译）: Large-scale personalization is shifting from embedding-table retrieval to LLM-based recommenders that generate the Semantic ID (SID) of the item to recommend, where each SID is a short sequence of discrete hierarchical content codes. A single instruction-tuned model can then unify retrieval, content understanding, and language, and recommend brand-new titles from their content alone using SID; then, how should…

- **[Evolving Semantic Indexes for Generative Retrieval](https://doi.org/10.48550/arxiv.2610.28568)**（2026；生成式推荐；匹配分 14）
  - 标签：Semantic ID
  - 英文摘要（未经过 AI 翻译）: Generative retrieval (GR) casts search and recommendation as autoregressive generation of discrete semantic identifiers (SIDs). SID design largely determines GR quality, but its discrete, interdependent components (SID construction, collision handling, decoding, and training) cannot be optimized end-to-end with gradients and remain largely hand-designed. We introduce a framework that improves these components …

- **[Beyond Semantic IDs: Finite-Beam Reachability and Continuous-Query Generation in Generative Recommendation](https://doi.org/10.48550/arxiv.2610.12977)**（2026；生成式推荐；匹配分 13）
  - 标签：Semantic ID
  - 英文摘要（未经过 AI 翻译）: Generative recommendation (GR) of social media platforms commonly retrieves items by autoregressively decoding discrete Semantic IDs (SIDs) with finite-width beam search. This work examines how this output interface constrains whether held-out targets enter finite returned lists, while distinguishing catalog-wide scoreability from empirical top-K support. We introduce two continuous-query paradigms: CQG-Single…

- **[UniSGR-V2: Stepwise Target-Side Feature Anticipation and Crossing for Generative Recommendation](https://doi.org/10.48550/arxiv.2610.16132)**（2026；生成式推荐；匹配分 12）
  - 标签：码本稳定性
  - 英文摘要（未经过 AI 翻译）: Semantic-ID-based generative recommendation unifies retrieval and ranking through autoregressive decoding but differs structurally from discriminative models, which can directly access rich target-item side features. The attributes are compressed into a finite codebook during quantization, while the target item remains undetermined during decoding and its features cannot be looked up. This target-side feature …

- **[WeGR: Towards Unified Generative Retrieval via Behavior-aware Tokenization and Preference Alignment](https://doi.org/10.48550/arxiv.2610.16979)**（2026；生成式推荐；匹配分 12）
  - 标签：码本稳定性
  - 英文摘要（未经过 AI 翻译）: Generative retrieval (GR) offers a promising paradigm for industrial search by unifying candidate generation within an autoregressive framework. However, effectively leveraging user behaviors in industrial GR remains challenging: existing SID tokenization methods struggle to preserve collaborative signals while maintaining balanced codebook utilization, whereas reinforcement learning (RL) for prioritizing high…
