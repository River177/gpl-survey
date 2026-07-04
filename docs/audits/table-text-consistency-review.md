# 表格与正文一致性复核报告

> 生成时间：2026-07-04  
> 范围：`tex/table/graph_prompt_summary.tex` 与 `tex/5.tex`、`tex/5.modal.tex` 的一致性。  
> 处理原则：本文只给解释和修复方案，暂不执行 TeX 修改，等待审查后再动正文和表格。

## 1. 结论摘要

当前表格的主要问题不是 LaTeX 结构，而是语义口径不够统一。最需要优先改的是 All in One、PGCL、SGL-PT、DeepGPT，以及正文出现但表格缺席的 HetGPT 和 GraphControl。另一个横向问题是表头里的 `pre-training task` 没有明确说明它到底指"方法自身使用的预训练目标"，还是"可兼容的上游预训练任务"。这会直接影响 DeepGPT、GPF/GPF-Plus、SUPT、UniPrompt 等行的勾选解释。

建议采用保守方案：先统一表格口径，再做少量行级修正。表格不需要重做 taxonomy，也不必把所有正文方法都塞进去；但 caption 需要明确它是 selected representative works，并解释列的含义。对确实会造成误读的行，例如 All in One 的插入公式和 PGCL/SGL-PT 的下游任务标记，应直接修改。

## 2. 复核来源

本次复核使用了当前 TeX 源码、BibTeX、公开论文页面和已下载 survey 文本。关键来源如下：

| 方法/问题 | 主要来源 |
|---|---|
| All in One | `tex/table/graph_prompt_summary.tex:33-40`；`tex/5.tex:31,45,54,66,89`；arXiv:2307.01504 页面说明其将 node/edge/graph tasks reformulate to graph-level task，并使用 meta-learning |
| PGCL | `tex/table/graph_prompt_summary.tex:55-63`；`tex/5.tex:23,74`；DBLP 记录 `journals/corr/abs-2310-10362`；注意 arXiv 当前 `2310.10362` 页面显示为 Self-Pro，存在元数据冲突 |
| SGL-PT | `tex/table/graph_prompt_summary.tex:78-82`；`tex/5.tex:23`；arXiv:2302.12449 摘要明确 "aiming for graph classification task" |
| DeepGPT | `tex/table/graph_prompt_summary.tex:105-112`；`tex/5.modal.tex:40`；arXiv:2309.10131 摘要称其面向 graph based prediction tasks，核心是 freeze pre-trained parameters and update added tokens |
| HetGPT | `tex/5.tex:25,54,74,87,106`；ACM DOI 10.1145/3589334.3645685 摘要说明其用于 pre-trained HGNNs，semi-supervised node classification |
| GraphControl | `tex/5.tex:20`、`tex/5.modal.tex:34`；ACM DOI 10.1145/3589334.3645439 摘要说明其用于 graph domain transfer learning，通过 conditional inputs/control module 适配目标 attributed datasets |

## 3. 列语义先统一

### 3.1 当前问题

表格现在把列分成 pre-training task、prompt design、downstream tasks、answering function。这个结构本身可以保留，但当前 caption 没有定义列语义，只解释了少量符号。结果是读者很难判断某个勾选表示"方法论文中实际使用的预训练目标"，还是"该 prompt 机制理论上兼容的任务"。

这个问题在 DeepGPT 行最明显。DeepGPT 是一种 prompt tuning for graph transformers 的适配方法，论文重点是往图 Transformer 加 trainable feature nodes 和 task-specific tokens，并冻结预训练参数后只更新 added tokens。表格如果把 node、edge、graph 三个 pre-training task 全部打勾，容易让读者理解为 DeepGPT 自己定义并使用了三类 pretext task；但更准确的说法是它依赖一个 already pre-trained graph transformer/backbone。

### 3.2 建议口径

建议把列语义定为：

| 列 | 建议含义 |
|---|---|
| `pre-training task` | 该方法论文中实际使用或显式假设的上游预训练目标层级；如果方法只依赖外部 backbone，应写 `backbone-dependent` 或在单元格中说明，而不是强行三列全勾 |
| `prompt components` | prompt 的可学习对象或结构对象，例如 prompt vector、prompt subgraph、class prototype、edge prompt、control condition |
| `inserting pattern` | prompt 如何进入输入图、表示空间或模型层；应区分 feature addition、graph attachment、virtual node/token、layer/prefix insertion、condition/control injection |
| `prompt tuning` | prompt 或相关轻量参数如何优化；如果是 fixed/preset prompt，写 fixed；如果是 meta-learning、contrastive loss、RL、CE、domain-transfer objective，应具体说明 |
| `downstream tasks` | 论文中明确评测或声称支持的下游任务层级，不用把理论可转化但未实验的任务都打勾 |
| `answering function` | `Preset` 建议改名为 `Hand-crafted` 或在 caption 中说明 Preset = no trainable task head / rule-based prediction；`Learnable` = trainable task head/classifier/decoder |

### 3.3 caption 建议

建议后续把 caption 改成类似：

```latex
\caption{Summary of selected representative graph prompting methods. The pre-training columns indicate the task level explicitly used or assumed by each method's upstream objective, while the downstream columns indicate task levels explicitly evaluated or supported in the original paper. ``Preset'' denotes a hand-crafted or rule-based answering function without a trainable task head; ``Learnable'' denotes a learned classifier, decoder, or task head. $\mathcal{S}$ denotes a subgraph, $V(\mathcal{S})$ its node set, $\pi$ pre-trained parameters, $\phi$ task-head parameters, and $\theta$ prompt parameters. Tilded variables and $X^*$ denote prompted representations or prompted features.}
```

如果版面允许，可以把符号解释移到 table note，减少 caption 负担。

## 4. 方法级复核与解决方案

### 4.1 All in One

#### 相关解释

当前正文对 All in One 的描述基本正确：`tex/5.tex:31` 写它是 learnable subgraph，包含 prompt nodes、prompt-node links，以及 prompt nodes 与 original nodes 之间的 weighted cross-links。arXiv:2307.01504 摘要也明确说该方法先统一 graph prompt format，包括 prompt token、token structure、inserting pattern，然后研究 task space，将不同 graph applications reformulate 到 graph-level task，并用 meta-learning 学 multi-task prompt initialization。

表格的问题在 insertion pattern。当前 `graph_prompt_summary.tex:36-38` 写成：

```latex
w_{ik} <- sigma(p_k x_i^T)
tilde{s}_i <- x_i + sum_k w_{ik} p_k
```

这个写法读起来像 GPF/GPF-Plus 的 feature addition，而不是 All in One 的 graph prompt attachment。它没有明确保留 prompt subgraph、prompt-prompt edges 和 prompt-original cross edges。

#### 解决方案

建议保留 All in One 的 pre-training graph 勾选、downstream node/edge/graph 勾选、Meta-Learning、Preset+Learnable 两个 answering function 勾选。需要改的是 insertion pattern 单元格：

```latex
\makecell{
$w_{ik}\leftarrow\sigma(\mathbf{p}_k\mathbf{x}_i^\top)$ if $>\delta$\\
$G'\leftarrow(V\cup\mathcal{P},\ E\cup E_{\mathcal{P}}\cup E_{\mathrm{cross}})$\\
$E_{\mathrm{cross}}=\{(v_i,\mathbf{p}_k,w_{ik})\}$
}
```

正文不需要大改。最多在 `tex/5.tex:31` 之后加一句说明：All in One modifies both the node set and the edge set, rather than simply adding a prompt vector to node features.

### 4.2 PGCL

#### 相关解释

当前表格把 PGCL 的 downstream tasks 标为 node、edge、graph 全部支持。正文却把 PGCL 描述为 semantic/contextual prompt vectors applied to graph-level representations，并在 tuning 段说 PGCL introduces graph-level loss to align with the pre-training task。二者明显不一致。

PGCL 的公开元数据存在一个需要特别记录的问题。`tex/zotero.bib` 里 `gong2023prompt` 的标题是 "Prompt Tuning for Multi-View Graph Contrastive Learning"。DBLP 也记录了同题名、作者 Chenghua Gong 等、CoRR `abs/2310.10362`、DOI `10.48550/arXiv.2310.10362`。但是 arXiv 当前 `2310.10362` 页面显示为 "Self-Pro: A Self-Prompt and Tuning Framework for Graph Neural Networks"，这与 DBLP 和若干搜索摘要不一致。也就是说，PGCL 原文页面目前不能稳定复核，可能是 arXiv 元数据被替换、撤稿/覆盖、或外部索引错误。

在无法稳定读取原文 PDF 的情况下，应避免继续声称 node+edge+graph 三类下游都明确支持。结合当前正文对 PGCL 的 graph-level representation / graph-level loss 描述，保守处理应把 PGCL 视为 graph-level prompt tuning 方法。

#### 解决方案

建议把 PGCL downstream tasks 暂改为 graph only：

```latex
& \xmark & \xmark & \cmark
```

prompt tuning 单元格建议避免使用 `(v,a,b)` 这种会让读者误解为节点/边三元组的符号，改成 graph/view-level contrastive notation，例如：

```latex
\makecell{
$\mathcal{L}_{\mathrm{GCL}}(\tilde{\mathbf{z}}^{s},\tilde{\mathbf{z}}^{c})$\\
graph/view-level contrastive loss
}
```

同时建议在审稿前人工确认 PGCL 原文 PDF。如果后续能找到原文且其确实显式评测 node/edge tasks，再恢复对应勾选；在当前证据下不建议保留三类全勾。

### 4.3 SGL-PT

#### 相关解释

SGL-PT 当前表格只标 node downstream，但 arXiv:2302.12449 摘要明确写 "aiming for graph classification task"，并说明它设计 verbalizer-free prompting function，把 downstream task reformulate 成类似 pretext task 的格式。当前正文 `tex/5.tex:23` 也写它提供 graph-level representation learning 的 global information。

因此这里不是正文夸大，而是表格 downstream 标记错误。SGL-PT 的主 downstream 应是 graph classification，而不是 node classification。

#### 解决方案

建议把 SGL-PT downstream tasks 改为：

```latex
& \xmark & \xmark & \cmark
```

pre-training task 当前标 node+graph。SGL-PT 摘要称 SGL combines generative and contrastive self-supervised graph learning，并服务于 graph classification。若不进一步拆原文细节，建议保守写 graph-level pre-training 为主；如果认为其 SGL 也包含节点/结构 reconstruction，可在 pre-training task 保留 node+graph，但 caption 必须说明这些勾选指 upstream objective level。为了减少误解，推荐：

```latex
pre-training task: graph \cmark, node optional only if verified from method section
```

正文 `tex/5.tex:23` 可以改得更准确：把 "graph-level representation learning" 保留，但不要和 node-level downstream 放在一起解释。

### 4.4 DeepGPT

#### 相关解释

DeepGPT 当前表格把 pre-training task 的 node、edge、graph 三列全部打勾。arXiv:2309.10131 摘要显示，这篇论文的核心是 deep graph prompt tuning for graph transformers：向图加入 trainable feature nodes，并向 graph transformer prepend task-specific tokens；通过 freeze pre-trained parameters and only update added tokens 来减少任务特定参数。摘要没有说 DeepGPT 自己定义了 node/edge/graph 三类预训练任务。

因此，全勾会让读者误解为 DeepGPT 是一个覆盖三类 pretext 的预训练方法。它更准确地说是 parameter-efficient adaptation of pre-trained graph transformers。

#### 解决方案

建议不要在三列 pre-training task 中全勾。两个可选方案：

1. 如果表格允许文字单元格或脚注，DeepGPT 的 pre-training task 写 `backbone-dependent`，三列不做强勾。
2. 如果必须使用三列勾选，建议全部改成 `\xmark`，并在 prompt components 或 tuning 单元格说明 `pre-trained graph transformer`。

推荐方案 1，因为 DeepGPT 确实依赖预训练参数，但预训练任务不是它的贡献核心。可以把 DeepGPT 行改为：

```latex
\makecell{DeepGPT\\(arXiv \cite{shirkavand2023deep})} &
\multicolumn{3}{c|}{backbone-dependent} &
...
```

如果不想破坏表格结构，则在 caption 中说明 `\xmark` 不代表不能使用预训练模型，而是原文未定义该层级 pretext。

### 4.5 HetGPT

#### 相关解释

HetGPT 在正文中出现多次：token-based prompt、hand-crafted answering function、pretext-aligned tuning、heterogeneous graph prompting。ACM 摘要说明 HetGPT 是用于 pre-trained heterogeneous graph neural networks 的 post-training prompting framework，设计 virtual class prompt 和 heterogeneous feature prompt，目标是 semi-supervised node classification。

它代表了一个正文中明确单独讨论的类型：heterogeneous graph prompting。当前表格没有 HetGPT，会让读者觉得表格没有覆盖正文的重要方法。不过，Section 5 末尾已经新增了 heterogeneous graph prompting 小节，表格如果无限扩展，会变得过大。

#### 解决方案

建议二选一：

**方案 A（推荐）：不补 HetGPT 行，但改 caption。** 因为表格已经很大，且 heterogeneous graph prompting 现在有单独 prose 小节。caption 明确 "selected representative works" 后，HetGPT 可留在正文，不必进入主表。

**方案 B：补 HetGPT 行。** 如果希望表格覆盖正文高频方法，可加一行：

| 列 | 建议内容 |
|---|---|
| Paper | `HetGPT (WWW 2024 \cite{ma2023hetgpt})` |
| pre-training task | node-level heterogeneous pre-training / node `\cmark` |
| prompt components | virtual class prompt + heterogeneous feature prompt |
| inserting pattern | attach/compose class and type-specific feature prompts for target node representations |
| prompt tuning | node-level contrastive / classification-aligned objective |
| downstream tasks | node `\cmark`, edge `\xmark`, graph `\xmark` |
| answering function | Preset/hand-crafted `\cmark` if using link-style label prompt; Learnable only if a trainable classifier is used in the implementation |

我建议采用方案 A，同时在正文中保留 HetGPT 的描述。这样不扩大表格，也不会漏掉 heterogeneity 方向。

### 4.6 GraphControl

#### 相关解释

GraphControl 出现在 `tex/5.modal.tex:34` 的 domain adaptation 语义对齐段，也在 `tex/5.tex:20` 被用来说明 prompt as feature vector 的背景。ACM 摘要说明它不是典型的 task prompting 方法，而是给 universal graph pre-trained models 加 conditional control，用于 graph domain transfer learning。它通过对齐 input space 和加入 target data conditional inputs，解决 transferability-specificity dilemma。

这说明 GraphControl 更适合多领域/域迁移章节，而不是 Section 5 的主表。主表标题是 graph prompt representative works，列设计也围绕 pre-training task、prompt design、downstream tasks、answering function。GraphControl 的核心是 domain transfer control module，强行塞入表格会让列含义更混乱。

#### 解决方案

不建议把 GraphControl 加入 `graph_prompt_summary.tex`。建议在 caption 或 Section 5 过渡处说明主表聚焦 graph task prompting methods，domain adaptation methods are discussed separately in Section~\ref{subsec:pdomain}。如果一定要表格覆盖，可考虑在后续另做 multi-modal/domain adaptation 小表，而不是加入当前 12 列主表。

## 5. 推荐执行方案

### 5.1 必改项

| 优先级 | 修改对象 | 具体动作 |
---|---|---|
| P0 | Caption/列语义 | 把表格定义为 "selected representative graph prompting methods"，明确 pre-training/downstream 勾选口径 |
| P0 | All in One | 改 insertion pattern，从 feature addition 改为 prompt subgraph attachment |
| P0 | SGL-PT | downstream 从 node 改为 graph；必要时修正文段避免歧义 |
| P1 | DeepGPT | pre-training task 不再三列全勾，改为 backbone-dependent 或全部 `\xmark` + 说明 |
| P1 | PGCL | 暂按 graph-only downstream 处理，并在内部备注原文 metadata 需人工确认 |

### 5.2 可选项

| 修改对象 | 建议 |
---|---|
| HetGPT | 不补表格行，依靠 caption 说明 selected representative works，并在 heterogeneous graph prompting 小节保留描述 |
| GraphControl | 不补主表，保留在 domain adaptation 小节；如需表格化，未来另建 domain adaptation 表 |
| Row ordering | 后续可按 taxonomy 分组：feature/token prompts、graph/subgraph prompts、answering/template methods、structure-aware recent methods、domain/specialized methods |
| Symbol note | 若 caption 过长，把符号解释移到 table note |

## 6. 建议的 TeX 修改草案

### 6.1 Caption 草案

```latex
\caption{Summary of selected representative graph prompting methods. The pre-training columns indicate the task level explicitly used or assumed by each method's upstream objective, while the downstream columns indicate task levels explicitly evaluated or supported in the original paper. ``Preset'' denotes a hand-crafted or rule-based answering function without a trainable task head; ``Learnable'' denotes a learned classifier, decoder, or task head. $\mathcal{S}$ denotes a subgraph, $V(\mathcal{S})$ its node set, $\pi$ pre-trained parameters, $\phi$ task-head parameters, and $\theta$ prompt parameters. Tilded variables and $X^*$ denote prompted representations or prompted features.}
```

### 6.2 All in One insertion 草案

```latex
\makecell{
$w_{ik}\leftarrow\sigma(\mathbf{p}_k\mathbf{x}_i^\top)$ if $>\delta$\\
$G'\leftarrow(V\cup\mathcal{P}, E\cup E_{\mathcal{P}}\cup E_{\mathrm{cross}})$\\
$E_{\mathrm{cross}}=\{(v_i,\mathbf{p}_k,w_{ik})\}$
}
```

### 6.3 SGL-PT 行草案

```latex
\makecell{SGL-PT \\(arXiv \cite{zhu2023sglpt}) } & \xmark & \xmark & \cmark &
\makecell{prompt token: \\one vector for each graph}
& connect to all nodes in the graph
& \makecell{contrastive loss and \\reconstruction loss}
& \xmark & \xmark & \cmark & \cmark & \xmark \\ \midrule
```

### 6.4 DeepGPT pre-training 草案

如果允许破坏三列勾选格式：

```latex
\makecell{DeepGPT\\(arXiv \cite{shirkavand2023deep})} &
\multicolumn{3}{c|}{backbone-dependent}
```

如果不允许破坏格式：

```latex
\makecell{DeepGPT\\(arXiv \cite{shirkavand2023deep})} & \xmark & \xmark & \xmark
```

并在 prompt component 或 insertion cell 保留 `pre-trained graph transformer` 的信息。

## 7. 仍需人工确认的问题

PGCL 的原文元数据需要人工确认。DBLP 记录 `Prompt Tuning for Multi-View Graph Contrastive Learning` 为 CoRR `abs/2310.10362`，但 arXiv 当前 `2310.10362` 页面是 Self-Pro。为避免引入错误，建议在修改前找到 PGCL 的 PDF 或作者主页版本。如果找不到，保守方案是把 PGCL 视为 graph-level prompt tuning 方法，并把 downstream 勾选收缩到 graph。

## 8. 本次不执行的内容

本文档不直接修改 `graph_prompt_summary.tex` 或 `5.tex`。待审查确认后，再按上面的 P0/P1 顺序执行 TeX 修改，并重新编译全文。
