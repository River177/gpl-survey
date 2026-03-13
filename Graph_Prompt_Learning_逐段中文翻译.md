# Graph Prompt Learning: A Comprehensive Survey and Beyond
## 逐段中文翻译（自动生成）



---

## 文件：`0.main.tex`

### 原文

Jiawen Zhang, Xixi Wu, Hong~Cheng, Yun Xiong, Jia Li

### 中文

张嘉文、吴希希、程宏、熊云、李嘉

### 原文

} }

### 中文

} }

### 原文

{Xiangguo Sun \MakeLowercase{\textit{et al.}}: }

### 中文

{孙祥国\textit{等人}: }

### 原文

ProG and the website can be accessed by \url{https://github.com/WxxShirley/Awesome-Graph-Prompt}, and \url{https://github.com/sheldonresearch/ProG}, respectively. }

### 中文

ProG 和网站可以分别通过 https://github.com/WxxShirley/Awesome-Graph-Prompt 和 https://github.com/sheldonresearch/ProG 访问。 }

### 原文

graph prompt, graph pre-training, graph learning, artificial general intelligence.

### 中文

图提示、图预训练、图学习、通用人工智能。



---

## 文件：`1.intro.tex`

### 原文

In an era marked by the rapid evolution of Artificial General Intelligence (AGI), there emerged many fantastic applications with AGI techniques such as ChatGPT in Natural Language Processing (NLP) and Midjourney in Computer Vision (CV). AGI has greatly improved our lives, making our work more efficient and freeing us from repetitive tasks to focus on more creative endeavors. However, when it comes to working with graph data, AGI applications are still in their early stages compared with the huge success in NLP \cite{ devlin2019bert, brown2020language, liu2023pretrain} and CV areas \cite{

### 中文

在通用人工智能（AGI）快速发展的时代，AGI技术出现了许多精彩的应用，例如自然语言处理（NLP）中的ChatGPT和计算机视觉（CV）中的Midjourney。 AGI 极大地改善了我们的生活，使我们的工作更加高效，并将我们从重复性任务中解放出来，专注于更具创造性的工作。然而，在处理图数据方面，与 NLP 和 CV 领域的巨大成功相比，AGI 应用仍处于早期阶段 \cite{

### 原文

wang2023chatvideo, zhang2023videollama}. In our increasingly interconnected world, understanding and extracting valuable insights from graphs is crucial. This places AGI applied to graph data at the forefront of both academic and industrial interest \cite{liu2023graph, zhang2023large, yang2023datacentric}, with the potential to redefine fields like drug design \cite{rong2020selfsupervised, qian2023can} and battery development \cite{wang2023scientific}, etc.

### 中文

wang2023chatvideo、zhang2023videollama}。在我们日益互联的世界中，从图表中理解并提取有价值的见解至关重要。这使得应用于图形数据的 AGI 处​​于学术和工业界的前沿，并有可能重新定义药物设计和电池开发等领域。

### 原文

However, realizing this vision is never easy. Figure \ref{fig:AGIProblems} illustrates this landscape for recent research in Artificial General Intelligence, from which we can see that there are at least three fundamental problems in technique: How to make the model general for different modalities, different domains, and different tasks? Within the NLP and CV areas, there have been many commercial models that can understand and translate information across these modalities \cite{ devlin2019bert,

### 中文

然而，实现这一愿景绝非易事。图：AGIProblems 阐释了通用人工智能近期研究的现状，从中我们可以看到技术上至少存在三个基本问题：如何使模型通用于不同模态、不同领域、不同任务？在 NLP 和 CV 领域，有许多商业模型可以跨这些模式理解和翻译信息 \cite{ devlin2019bert,

### 原文

zhang2023videollama, brown2020language}. For example, models like BERT \cite{devlin2019bert} and GPT-3 \cite{brown2020language} have demonstrated the ability to perform tasks that involve both textual and visual information. However, in the context of graph data, the harmonization of information from multiple modalities remains largely uncharted territory \cite{li2023graphadapter}.

### 中文

zhang2023videollama，brown2020语言}。例如，BERT 和 GPT-3 等模型已经证明了执行涉及文本和视觉信息的任务的能力。然而，在图数据的背景下，多种模式信息的协调在很大程度上仍然是未知领域。

### 原文

For the cross-domain issue, transfer learning has proven effective, enabling models to apply knowledge learned from images and text in one domain to another. However, transferring knowledge between different graph domains is very tough because the semantic spaces are not aligned \cite{zhu2023graphcontrol} and the structural patterns are also not similar \cite{ zhao2023graphglow}, making graph domain adaptation remains a very frontier and not well-solved AGI problem. Currently, most graph research on transfer learning focuses on the third problem, how to leverage the pre-trained graph knowledge in the same graph domain to perform different graph tasks (like node classification, link prediction, graph classification, etc) \cite{sun2022gppt, liu2023graphprompt, sun2023all, fang2023universal, zhu2023sglpt, hu2020gptgnn, shirkavand2023deep, ge2023enhancing}. However, compared with the huge success in NLP and CV, task transferring within the same graph domain is still primitive with far fewer instances of successful industrial applications. While the AGI research boasts notable achievements in many linear data like images,

### 中文

对于跨领域问题，迁移学习已被证明是有效的，使模型能够将从一个领域的图像和文本中学到的知识应用到另一个领域。然而，在不同图域之间转移知识是非常困难的，因为语义空间不对齐，结构模式也不相似，使得图域适应仍然是一个非常前沿且尚未得到很好解决的AGI问题。目前，大多数关于迁移学习的图研究都集中在第三个问题上，即如何利用同一图域中预训练的图知识来执行不同的图任务（如节点分类、链接预测、图分类等）。然而，与 NLP 和 CV 的巨大成功相比，同一图域内的任务转移仍然很原始，成功的工业应用实例还少得多。虽然 AGI 研究在图像等许多线性数据方面取得了显着的成就，

### 原文

text \cite{robinson2023leveraging, devlin2019bert, brown2020language}, and videos \cite{wang2023chatvideo, zhang2023videollama}, the fundamental problems within the realm of graph data remain underexplored. Besides the above three foundation problems, Artificial General Intelligence has also encountered many social disputes. For example, training large foundation models consumes exorbitant amounts of energy and may yield unintended counterfactual outcomes \cite{liu2022ptuning, schick2021it}. These concerns have led to a growing consensus within the AI community on the efficient extraction of useful knowledge preserved by these large models, minimizing the need for repetitive fine-tuning across various downstream tasks \cite{gao2021making, lester2021power}. This consensus not only promises to alleviate the environmental impact but also offers a practical solution to the challenge of model efficiency and adaptability in an era of AGI.

### 中文

文本和视频，图数据领域的基本问题仍未得到充分探索。除了上述三个基础问题外，通用人工智能还遇到了很多社会争议。例如，训练大型基础模型会消耗大量能量，并可能产生意想不到的反事实结果。这些担忧导致人工智能界越来越一致地认识到如何有效提取这些大型模型保存的有用知识，从而最大限度地减少各种下游任务的重复微调的需要。这一共识不仅有望减轻对环境的影响，而且为应对AGI时代模型效率和适应性的挑战提供了切实可行的解决方案。

### 原文

At the core of recent AGI technology, prompt learning has presented huge potential to solve the above problems and demonstrated remarkable success in NLP and CV applications \cite{qin2021learning, tsimpoukelli2021multimodal, liu2023pretrain}. Prompt learning is the art of designing informative prompts  to manipulate input data for the pre-trained foundation models. Figure \ref{fig:PromptExample} shows an example of a textual-format prompt applied to a pre-trained language model to directly perform downstream inference tasks. By reformulating downstream tasks into pre-training tasks, this approach avoids the need for extensive model tuning and efficiently extracts preserved knowledge \cite{brown2020language, jiang2020how}. Since its powerful capabilities in data manipulation, task reformulation, and extraction of significant insights, prompting is very promising to address the aforementioned cross-modalities, cross-domains, and cross-task challenges in one way. Compared with large models, the prompt is usually very lightweight and can efficiently extract useful knowledge by reducing the extensive computational resources caused by repeat tuning of these large models \cite{lester2021power, shin2020autoprompt}. Intuitively, text and images can be perceived as specific instances of a more general graph data structure. For instance, a sentence can be treated as a graph path, with words as nodes, and an image can be viewed as a grid graph, where each pixel serves as a graph node. This insight encourages us to explore the transference of successful prompting techniques from text to the graph area for similar concerns.

### 中文

作为最新 AGI 技术的核心，即时学习为解决上述问题提供了巨大的潜力，并在 NLP 和 CV 应用中取得了显着的成功。即时学习是设计信息提示来操作预先训练的基础模型的输入数据的艺术。图 Fig:PromptExample 显示了应用于预训练语言模型以直接执行下游推理任务的文本格式提示的示例。通过将下游任务重新表述为预训练任务，这种方法避免了广泛的模型调整的需要，并有效地提取保留的知识。由于其在数据操作、任务重新制定和提取重要见解方面的强大功能，提示非常有希望以一种方式解决上述跨模式、跨领域和跨任务挑战。与大型模型相比，提示通常非常轻量级，可以通过减少这些大型模型的重复调优所带来的大量计算资源来有效地提取有用的知识。直观上，文本和图像可以被视为更通用的图形数据结构的特定实例。例如，句子可以被视为图形路径，单词作为节点，图像可以被视为网格图，其中每个像素充当图形节点。这种见解鼓励我们探索将成功的提示技术从文本转移到图形区域以解决类似问题。

### 原文

Recently, some researchers have started to introduce prompt learning to graph data \cite{sun2022gppt, liu2023graphprompt, sun2023all, fang2023universal, zhu2023sglpt, ma2023hetgpt, guo2023datacentric, chen2023ultradp, gong2023prompt}. However, some further studies have found that the graph prompt is very different from their counterparts in the NLP area \cite{sun2023all}. First, the design of graph prompts proves to be a far more intricate endeavor compared to the formulation of language prompts. Classic language prompts often comprise predefined phrases or learnable vectors appended to input text \cite{brown2020language, gao2021making}. Here, the primary focus lies in the content of the language prompt. However, we actually do not know what a graph prompt looks like. A graph prompt not only contains the prompt "content" but also includes the undefined task of determining how to structure these prompt tokens and seamlessly integrate them into the original graph. Second, the harmonization of downstream graph problems with the pre-training task is more difficult than language tasks \cite{liu2023graphprompt, sun2023all}. For example, a typical pre-training approach for a language model is to predict a masked word by the model \cite{devlin2019bert}. Then many downstream tasks such as question answering, and sentiment classification can be easily reformulated as word-level tasks \cite{liu2023pretrain}. Unlike NLP, where pre-training tasks often share a substantial task sub-space, graph tasks span node-level \cite{grover2016node2vec}, edge-level \cite{zhang2018link}, and graph-level objectives \cite{sun2020infograph, sun2021heterogeneous}, making pre-training pretexts less adaptable. Third, compared with prompts in NLP which are usually some understandable phrases, graph prompts are usually less intuitive to non-specialists. The fundamental nature and role that graph prompts play within the graph model remain somewhat elusive without comprehensive theoretical analysis. There is also a lack of clear-cut evaluation criteria for the quality of designed graph prompts. In addition, there are still many unclear questions for us to further understand graph prompting. For example, how effective are these graph prompts? What is their efficiency in terms of parameter complexity and training burden? How powerful and flexible do these prompts manipulate the original graph data? In light of these intricacies questions, there is a pressing need for delving deeper into the potential of graph prompts in AGI, thereby paving the way for a more profound understanding of this evolving frontier within the broader data science landscape.

### 中文

最近，一些研究人员开始将即时学习引入图数据。然而，一些进一步的研究发现，图形提示与 NLP 领域的对应提示有很大不同。首先，与语言提示的制定相比，图形提示的设计被证明是一项更加复杂的工作。经典语言提示通常包含预定义的短语或附加到输入文本的可学习向量。这里，主要关注的是语言提示的内容。然而，我们实际上并不知道图形提示是什么样的。图形提示不仅包含提示“内容”，还包括确定如何构造这些提示标记并将它们无缝集成到原始图形中的未定义任务。其次，下游图问题与预训练任务的协调比语言任务更困难。例如，语言模型的典型预训练方法是通过模型预测屏蔽词。然后，许多下游任务（例如问答和情感分类）可以轻松地重新表述为单词级任务。与 NLP 不同，预训练任务通常共享大量任务子空间，图任务跨越节点级、边级和图级目标，使得预训练借口的适应性较差。第三，与NLP中的提示通常是一些可以理解的短语相比，图形提示对于非专业人士来说通常不太直观。如果没有全面的理论分析，图形提示在图形模型中发挥的基本性质和作用仍然有些难以捉摸。对于图形提示设计的质量也缺乏明确的评价标准。此外，还有很多不清楚的问题需要我们进一步理解图形提示。例如，这些图形提示的效果如何？它们在参数复杂性和训练负担方面的效率如何？这些提示对原始图形数据的操作有多强大和灵活？鉴于这些错综复杂的问题，迫切需要深入研究 AGI 中图形提示的潜力，从而为更深入地理解更广泛的数据科学领域中这一不断发展的前沿领域铺平道路。

### 原文

While there have been recent endeavors to explore graph prompting, a consistent framework or clear route remains unavailable. These efforts vary significantly in terms of perspective, methodology, and target tasks, which present a fragmented landscape of graph prompting and pose a considerable obstacle to the systematical advancement of this research area. There arises an urgent need to provide a panoramic view, analysis, and synthesis of the latest advances in this realm with a unified framework. In light of this situation, we offer this survey to present how existing work on graph prompts tries to solve the three foundation problems towards AGI as previously mentioned.  Beyond that, we also wish to push forward the research area by answering the following detailed research questions (RQs):

### 中文

尽管最近人们在探索图形提示方面做出了努力，但仍然缺乏一致的框架或清晰的路线。这些努力在视角、方法论和目标任务方面存在很大差异，呈现出图提示的碎片化格局，并对该研究领域的系统推进构成了相当大的障碍。迫切需要以统一的框架来对这一领域的最新进展进行全景、分析和综合。鉴于这种情况，我们提供这项调查来展示现有的图提示工作如何尝试解决前面提到的 AGI 的三个基础问题。除此之外，我们还希望通过回答以下详细的研究问题（RQ）来推动该研究领域的发展：

### 原文

In this part of our study, we aim to understand why prompts are important. We want to uncover the fundamental aspects of graph prompts. What exactly do graph prompts do in graph problems? How do they fit into the complex graphs, and how do they help us achieve the broader goal of creating AI systems that can handle graph data effectively? These questions highlight the significant role that graph prompts play in shaping the future of AI when dealing with graph information.

### 中文

在我们研究的这一部分中，我们的目的是了解为什么提示很重要。我们想要揭示图形提示的基本方面。图形提示在图形问题中到底有什么作用？它们如何适应复杂的图形，以及它们如何帮助我们实现创建能够有效处理图形数据的人工智能系统的更广泛目标？这些问题凸显了图形提示在处理图形信息时在塑造人工智能的未来方面发挥的重要作用。

### 原文

To answer the first research question (RQ1), we propose a unified framework to analyze graph prompt learning work. Our framework casts the concept of a graph prompt into prompt tokens, token structures, and inserting patterns. This higher-level perspective offers clarity and comprehensiveness, providing readers with a structured understanding of this burgeoning field. To the best of our knowledge, our survey marks the first of its kind to bring together these multifaceted aspects of graph prompting within a single unified framework.

### 中文

为了回答第一个研究问题（RQ1），我们提出了一个统一的框架来分析图提示学习工作。我们的框架将图形提示的概念转化为提示标记、标记结构和插入模式。这种更高层次的视角提供了清晰度和全面性，为读者提供了对这个新兴领域的结构化理解。据我们所知，我们的调查标志着首次将图形提示的这些多方面方面整合到一个统一的框架中。

### 原文

To answer the second research question (RQ2), we explore the correlations between prompts and existing graph models through the lenses of flexibility and expressiveness and then present a fresh and insightful perspective to uncover the nature of graph prompts. Unlike most prompt learning surveys in NLP areas \cite{liu2023pretrain} that treat prompting as a trick of filling the gap between the pre-training tasks and downstream tasks, we reveal that graph prompts and graph models are interconnected on a deeper level. This novel perspective offers invaluable insights into why prompt learning holds promise in the graph area and what distinguishes it from traditional fine-tuning methods \cite{hu2020strategies}. To our knowledge, this is the first endeavor to offer such an illuminating perspective on graph prompting.

### 中文

为了回答第二个研究问题（RQ2），我们通过灵活性和表现力的角度探索提示与现有图模型之间的相关性，然后提出一个新颖而富有洞察力的视角来揭示图提示的本质。与 NLP 领域的大多数即时学习调查将提示视为填补预训练任务和下游任务之间差距的技巧不同，我们揭示了图提示和图模型在更深层次上相互关联。这种新颖的视角为为什么即时学习在图形领域有希望以及它与传统微调方法的区别提供了宝贵的见解。据我们所知，这是第一次为图形提示提供如此具有启发性的视角。

### 原文

To answer the third research question (RQ3), we introduce a comprehensive taxonomy that includes more than 100 related works. Our taxonomy dissects these works, categorizing them according to node-level, edge-level, and graph-level tasks, thereby aligning them with the broader context of the pre-training task. This will empower our readers with a clearer comprehension of the mechanisms underlying prompts within the whole "pre-training and prompting" workflow.

### 中文

为了回答第三个研究问题 (RQ3)，我们引入了一个全面的分类法，其中包括 100 多个相关作品。我们的分类法剖析了这些工作，根据节点级、边缘级和图级任务对它们进行分类，从而使它们与预训练任务的更广泛背景保持一致。这将使我们的读者能够更清楚地理解整个“预训练和提示”工作流程中提示的机制。

### 原文

To answer the fourth research question (RQ4), we developed ProG (prompt graph) \footnote{\url{https://github.com/sheldonresearch/ProG}}, a unified Python library to support graph prompting. Additionally, we established a website\footnote{\url{https://github.com/WxxShirley/Awesome-Graph-Prompt}} that serves as a repository for the latest graph prompt research. This platform curates a comprehensive collection of research papers, benchmark datasets, and readily accessible code implementations. By providing this accessible ecosystem, we aim to empower researchers and practitioners to advance this burgeoning field more effectively.

### 中文

为了回答第四个研究问题（RQ4），我们开发了ProG（提示图）\url{https://github.com/sheldonresearch/ProG}，一个支持图形提示的统一Python库。此外，我们还建立了一个网站\url{https://github.com/WxxShirley/Awesome-Graph-Prompt}，作为最新图形提示研究的存储库。该平台汇集了研究论文、基准数据集和易于访问的代码实现的全面集合。通过提供这个可访问的生态系统，我们的目标是使研究人员和从业者能够更有效地推进这一新兴领域。

### 原文

Beyond these, our survey goes a step further with an introduction of potential applications, a thoughtful analysis of the current challenges, and a discussion of future directions, thus providing a comprehensive roadmap for the evolution of this vibrant and evolving field (RQ5). Our contributions are summarised as follows:

### 中文

除此之外，我们的调查还进一步介绍了潜在的应用，对当前挑战进行了深思熟虑的分析，并讨论了未来的方向，从而为这个充满活力和不断发展的领域的发展提供了全面的路线图（RQ5）。我们的贡献总结如下：



---

## 文件：`2.methodology.tex`

### 原文

This survey will introduce the art of prompting from a big picture of artificial general intelligence (AGI). We first present three fundamental problems towards AGI in Table \ref{tab:rqs}. Recently, prompt learning has been demonstrated as a promising solution to these problems in many linear data such as text \cite{brown2020language, gao2021making}, images \cite{

### 中文

本次调查将从通用人工智能 (AGI) 的大局出发介绍提示的艺术。我们首先在 Table tab:rqs 中提出 AGI 的三个基本问题。最近，即时学习已被证明是许多线性数据（例如文本、图像）中这些问题的有前途的解决方案\cite{

### 原文

wang2023chatvideo}, etc. However, whether the prompt technique can still solve these problems in the graph area, is not clearly discussed. Through this survey, we wish to figure out how the graph prompt potentially helps graph models to be more general across various tasks and domains, and how it generalizes the foundation models to interact with other modalities (e.g. text, image, etc). Beyond the above common problems of AGI in NLP, CV, and graph areas, graph prompting is usually very different from its counterparts in NLP and CV areas, leading to many detailed questions as shown in Table \ref{tab:rqs}.

### 中文

然而，提示技术是否仍然可以解决图形区域中的这些问题，还没有明确的讨论。通过这项调查，我们希望弄清楚图形提示如何潜在地帮助图形模型在各种任务和领域中变得更加通用，以及它如何概括基础模型以与其他模式（例如文本、图像等）交互。除了上述 AGI 在 NLP、CV 和图领域的常见问题之外，图提示通常与 NLP 和 CV 领域的同行有很大不同，导致了许多详细问题，如表 tab:rqs 所示。

### 原文

The taxonomy of this survey is presented in \figref{fig:Taxonomy}, which is intricately designed to categorize graph prompts based on their specific applications and functionalities, providing a structured approach to understanding their role in AGI.

### 中文

这项调查的分类如图所示：分类，它经过精心设计，根据图形提示的特定应用和功能对其进行分类，提供了一种结构化的方法来理解它们在 AGI 中的作用。

### 原文

Since prompting techniques mostly seek to reformulate downstream tasks to the pre-training tasks, they are highly customized for detailed pre-training approaches, thus we briefly discuss the representative pre-training work in the graph area before we formally introduce graph prompt content. We split existing pre-training approaches into node-level, edge-level, graph-level, and multi-task pre-training strategies. Next, we present how different prompting ideas reformulate various downstream tasks to the corresponding pre-training tasks in the graph area. By revisiting existing pre-training literature, we will be more clear about the role of graph prompts in the whole "pre-training and prompting" framework.

### 中文

由于提示技术主要寻求将下游任务重新表述为预训练任务，因此它们针对详细的预训练方法进行了高度定制，因此在正式介绍图提示内容之前，我们简要讨论了图区域中代表性的预训练工作。我们将现有的预训练方法分为节点级、边缘级、图级和多任务预训练策略。接下来，我们展示不同的提示想法如何将各种下游任务重新表述为图形区域中相应的预训练任务。通过重新审视现有的预训练文献，我们将更加清楚图提示在整个“预训练和提示”框架中的作用。

### 原文

Aiming at the three foundation problems mentioned in the research objectives (P1-P3 in \tabref{tab:rqs}), we analyze graph prompting from three aspects: \romannumeral1. prompt design for graph tasks (\secref{sec:ptask}); \romannumeral2. multi-modal prompting with graphs (\secref{subsec:pmodal}); and \romannumeral3. graph domain adaptation with prompting techniques (\secref{subsec:pdomain}). Within each aspect, we present a detailed discussion related to the five specific problems in the graph prompt area (Q1-Q5 in \tabref{tab:rqs}).

### 中文

针对研究目标中提到的三个基础问题（tab:rqs中的P1-P3），我们从三个方面分析图提示：\romannumeral1。图形任务的提示设计（秒：ptask）； \罗马数字2。用图形进行多模式提示（亚秒：pmodal）；和 \romannumeral3。具有提示技术的图域适应（亚秒：pdomain）。在每个方面，我们在图形提示区域（tab:rqs 中的 Q1-Q5）中对五个具体问题进行了详细讨论。

### 原文

& \makecell[l]{P1: How to Make the Model General for Different\\ Modalities? (\secref{subsec:multi_modal}) } \\\cmidrule(l){2-2} & \makecell[l]{P2: How to Make the Model General for Different \\Domains? (\secref{subsec:pdomain})} \\\cmidrule(l){2-2} & \makecell[l]{P3: How to Make the Model General for Different \\Tasks?  (\secref{sec:ptask}) }  \\ \midrule

### 中文

& \makecell[l]{P1: 如何使模型适用于不同的模态？ (subsec:multi_modal) } \\\cmidrule(l){2-2} & \makecell[l]{P2: 如何使模型适用于不同的 \\Domains？ (subsec:pdomain)} \\\cmidrule(l){2-2} & \makecell[l]{P3: 如何使模型通用于不同的 \\任务？ (sec:ptask) } \\ \midrule

### 原文

& \makecell[l]{Q1: How to Understand Existing Work with a \\Unified Framework? (\secref{subsec:pdesign})} \\\cmidrule(l){2-2} & \makecell[l]{Q2: What's the Nature of Graph Prompt? \\(\secref{subsec:why_prompt}, \secref{subsec:pdiscussion})}   \\\cmidrule(l){2-2} & \makecell[l]{Q3: How to Design Graph Prompts? (\secref{sec:ptask}) } \\\cmidrule(l){2-2}

### 中文

& \makecell[l]{Q1：如何理解 \\统一框架的现有工作？ (subsec:pdesign)} \\\cmidrule(l){2-2} & \makecell[l]{Q2: 图形提示的本质是什么？ \\(subsec:why_prompt, subsec:pdiscussion)} \\\cmidrule(l){2-2} & \makecell[l]{Q3: 如何设计图形提示？ (秒:ptask) } \\\cmidrule(l){2-2}

### 原文

& \makecell[l]{Q4: How to Deploy Graph Prompts in Real-world \\Applications?  (\secref{sec:app}, \secref{sec:prog})}  \\\cmidrule(l){2-2} & \makecell[l]{Q5: What Are the Current Challenges and Future \\Directions? (\secref{sec:challenges}) }   \\ \bottomrule

### 中文

& \makecell[l]{Q4：如何在现实世界的应用程序中部署图形提示？ (sec:app, sec:prog)} \\\cmidrule(l){2-2} & \makecell[l]{Q5：当前的挑战和未来的方向是什么？ （秒：挑战）} \\ \bottomrule

### 原文

In this survey, we carefully studied more than 100 high-quality papers published within the past 5 years from reputable conferences and journals including but not limited to NeurIPS, SIGKDD, The Web Conference, ICLR, CIKM, ICML, IJCAI, EMNLP, SIGIR, ACL, AAAI, WSDM, TKDE, etc. Most of these venues are ranked as CCF A\footnote{\url{https://www.ccf.org.cn/Academic_Evaluation/By_category}} or CORA A*\footnote{\url{https://www.core.edu.au/conference-portal}}. Besides these works, we also introduce several latest works in arXiv so that our survey can catch up with the frontier and latest progress in this area. A more detailed pie chart (Figure \ref{fig:venue_dis}) presents the distribution of collected papers over these venues. Furthermore, we conducted an analysis of the topics covered by these references. In Figure \ref{fig:top10keys}, we present the top 15 keywords that appeared in the titles of these papers. Notably, these keywords align closely with the focus of our survey, which is centered around graph domains and prompt learning.

### 中文

在本次调查中，我们仔细研究了过去5年内发表的100多篇来自知名会议和期刊的高质量论文，包括但不限于NeurIPS、SIGKDD、The Web Conference、ICLR、CIKM、ICML、IJCAI、EMNLP、SIGIR、ACL、AAAI、WSDM、TKDE等。这些会场大部分被评为CCF A\url{https://www.ccf.org.cn/Academic_Evaluation/By_category} 或 CORA A*\url{https://www.core.edu.au/conference-portal}。除了这些工作之外，我们还介绍了arXiv中的几项最新工作，以便我们的调查能够赶上该领域的前沿和最新进展。更详细的饼图（图Fig:venue_dis）显示了收集到的论文在这些场所的分布情况。此外，我们对这些参考文献所涵盖的主题进行了分析。在图 Fig:top10keys 中，我们展示了这些论文标题中出现的前 15 个关键词。值得注意的是，这些关键词与我们调查的重点密切相关，调查的重点是图形领域和即时学习。

### 原文

Our survey stands out from existing surveys in several notable ways. For example, \citet{liu2023graph} primarily focuses on graph foundation models (GFMs). Their survey does not specifically target graph prompts, and only a few papers in this area are briefly discussed. \citet{li2023survey} systematically analyze recent works that integrate graphs and LLMs, which is a detailed analysis of a small portion (Section \ref{subsec:multi_modal}) in our survey. We go beyond their scope by exploring various aspects of graph prompts in a more extensive manner. Meanwhile, surveys \cite{xie2023selfsupervised, yu2023selfsupervised} focus primarily on the pre-training stages, without involving the crucial aspect of graph prompt learning. While a prior survey on graph prompt learning by \citet{wu2023survey} exists, our survey surpasses it in several key aspects. Firstly, we provide \textbf{a more comprehensive analysis of related works}. Their survey was published in May 2023 when there were only a few graph prompt works available \cite{sun2022gppt, zhu2023sglpt, fang2022prompt}. In contrast, our survey encompasses a broader scope, including all relevant works in the field. Secondly, we offer \textbf{a systematic analysis of existing works} within a uniform framework, facilitating comprehension and comparison between different approaches. Thirdly, our survey provides deep insights into \textbf{the relationship between graph pre-training and prompts}, shedding light on the interplay between these critical elements. Lastly, we not only present empirical insights but also include \textbf{engineering works} aimed at deploying graph prompts in real-world applications, ensuring the practical applicability of our survey.

### 中文

我们的调查在几个显着的方面从现有的调查中脱颖而出。例如，主要关注图基础模型（GFM）。他们的调查并没有专门针对图形提示，并且只简要讨论了该领域的几篇论文。系统地分析了最近整合图和LLM的作品，这是对我们调查中的一小部分（Section subsec:multi_modal）的详细分析。我们以更广泛的方式探索图形提示的各个方面，从而超出了它们的范围。同时，调查主要集中在预训练阶段，而没有涉及图提示学习的关键方面。虽然之前存在关于图形提示学习的调查，但我们的调查在几个关键方面超越了它。首先，我们对相关工作进行更全面的分析。他们的调查于 2023 年 5 月发布，当时只有少数图表提示作品可用。相比之下，我们的调查涵盖了更广泛的范围，包括该领域的所有相关工作。其次，我们在统一的框架内对现有作品进行系统分析，促进不同方法之间的理解和比较。第三，我们的调查深入了解了图预训练和提示之间的关系，揭示了这些关键元素之间的相互作用。最后，我们不仅提供实证见解，还包括旨在在实际应用中部署图形提示的工程工作，确保我们调查的实际适用性。



---

## 文件：`3.Preliminaries.tex`

### 原文

Graph representation learning has been a topic of extensive research over the past few decades. This journey, illustrated in Figure~\ref{fig:pre1}, has witnessed the evolution from shallow embedding methods to supervised graph neural networks, transitioning from the fine-tuning paradigm to the emerging prompting paradigm. In this section, we will provide an overview of the fundamental notations employed in this survey, delve into the historical developments of graph representation learning, explore the pre-training and fine-tuning paradigm, and trace the evolution of prompt-based learning. Most importantly, we will present a novel perspective focusing on flexibility and expressiveness, shedding light on why prompts offer a promising solution to address the limitations of existing graph representation learning methods.

### 中文

在过去的几十年里，图表示学习一直是广泛研究的主题。这段旅程如图Fig:pre1所示，见证了从浅层嵌入方法到有监督图神经网络的演变，从微调范式到新兴提示范式的转变。在本节中，我们将概述本次调查中使用的基本符号，深入研究图表示学习的历史发展，探索预训练和微调范式，并追踪基于提示的学习的演变。最重要的是，我们将提出一个关注灵活性和表现力的新颖视角，阐明为什么提示提供了一个有前途的解决方案来解决现有图表示学习方法的局限性。

### 原文

Let a graph instance denoted as $\mathcal{G} = \{ \mathcal{V}, \mathcal{E} \}$, where $\mathcal{V} = \{ v_1,v_2, \ldots, v_N \}$ represents the node set containing $N$ nodes. The edge set $\mathcal{E} \in \mathcal{V} \times \mathcal{V}$ describes the connection between nodes. Each node $v_i$ is associated with a feature vector represented as $\textbf{x}_i \in \mathbb{R}^D$. To characterize the connectivity within the graph, we employ the adjacency matrix denoted as $\textbf{A} \in \{0,1\}^{N \times N}$, where the entry $\textbf{A}_{ij} = 1$ if and only if the edge $(v_i,v_j) \in \mathcal{E}$.

### 中文

设一个图实例表示为 ，其中 表示包含节点的节点集。边集描述了节点之间的连接。每个节点都与表示为 的特征向量相关联。为了表征图中的连通性，我们使用表示为 的邻接矩阵，其中条目当且仅当边 。

### 原文

The last decades have witnessed a notable surge in the development of graph representation learning techniques. These approaches can be broadly categorized into two main branches: shallow embedding methods and deep graph neural networks (GNNs). The shallow embedding approach is centered on mapping nodes into lower-dimensional, learnable embeddings, enhancing their applicability in various downstream tasks, as exemplified by node2vec~\cite{grover2016node2vec} and DeepWalk~\cite{perozzi2014deepwalk}. On the other hand, the deep GNNs maintain the input node features as constants and optimize deep graph model parameters for specific tasks, leading to more expressive representation capabilities, as seen in methods such as Graph Convolution Networks (GCN)~\cite{niepert2016learning} and GraphSAGE~\cite{hamilton2017inductive}.

### 中文

过去几十年见证了图表示学习技术的显着发展。这些方法可以大致分为两个主要分支：浅嵌入方法和深度图神经网络（GNN）。浅嵌入方法的核心是将节点映射到低维、可学习的嵌入中，增强它们在各种下游任务中的适用性，如 node2vec 和 DeepWalk 所示。另一方面，深度 GNN 将输入节点特征保持为常量，并针对特定任务优化深度图模型参数，从而产生更具表现力的表示能力，如图卷积网络（GCN）和 GraphSAGE 等方法所示。

### 原文

Shallow embedding approaches make input node features learnable parameters, aiming at encoding nodes in a manner that retains the original network's similarity structure. According to node similarity definition, these methods can be categorized as factorization-based~\cite{

### 中文

浅嵌入方法使输入节点具有可学习的参数，旨在以保留原始网络相似结构的方式对节点进行编码。根据节点相似度定义，这些方法可以归类为基于分解的\cite{

### 原文

ou2016asymmetric, zhang2019prone} and random walk approaches~\cite{grover2016node2vec, perozzi2014deepwalk, wang2019hyperbolic, wang2022common}. Despite the flexibility that shallow embedding methods offer for various downstream tasks, they are constrained by their inability to generate embeddings for nodes not encountered during training. Additionally, these approaches lack the capability to incorporate node features. Therefore, more ``deeper" methods, specifically those based on graph neural networks, have been developed to address these limitations.

### 中文

ou2016asymmetry, zhang2019prone} 和随机游走方法。尽管浅嵌入方法为各种下游任务提供了灵活性，但它们受到无法为训练期间未遇到的节点生成嵌入的限制。此外，这些方法缺乏合并节点特征的能力。因此，已经开发出更多“更深层次”的方法，特别是基于图神经网络的方法来解决这些限制。

### 原文

Most deep GNNs follow a message-passing schema and use a more complex encoder, resulting in powerful expressiveness in graph representation. The representative neural network structure is convolutional graph neural networks (ConvGNNs), which comprise spectral~\cite{defferrard2016convolutional,he2021bernnet} and spatial methods~\cite{

### 中文

大多数深度 GNN 遵循消息传递模式并使用更复杂的编码器，从而在图表示中产生强大的表达能力。代表性的神经网络结构是卷积图神经网络（ConvGNN），它包括光谱和空间方法\cite{

### 原文

niepert2016learning, hamilton2017inductive,

### 中文

niepert2016学习，hamilton2017归纳，

### 原文

velickovic2018graph, shi2021masked, xu2018how}. While these methods have exhibited remarkable capabilities in various graph-based applications, their reliance on task-specific supervision imposes constraints on their adaptability and generalizability, particularly when dealing with tasks that have limited labeled data.

### 中文

velickovic2018graph、shi2021masked、xu2018how}。虽然这些方法在各种基于图的应用程序中表现出了卓越的能力，但它们对特定于任务的监督的依赖限制了它们的适应性和泛化性，特别是在处理标记数据有限的任务时。

### 原文

In summary, shallow embedding methods offer flexibility, preserving network structure and node content for straightforward graph analytic tasks. However, they lack expressiveness and the ability to encapsulate additional node features. Conversely, GNNs provide more expressive graph representations but require task-specific training data, limiting their transferability. Hence, it calls for a graph learning mechanism that combines expressiveness and flexibility. This need led to the development of the pre-training and fine-tuning paradigm.

### 中文

总之，浅嵌入方法提供了灵活性，为简单的图分析任务保留了网络结构和节点内容。然而，它们缺乏表现力和封装额外节点功能的能力。相反，GNN 提供更具表现力的图形表示，但需要特定于任务的训练数据，限制了它们的可迁移性。因此，它需要一种兼具表达性和灵活性的图学习机制。这种需求导致了预训练和微调范式的发展。

### 原文

To address the challenges of limited labeled data and generalization issues in GNNs, the pre-training and fine-tuning paradigm, thriving in the natural language processing (NLP) community, has gained widespread adoption in graph representation learning. These approaches involve pre-training models on large-scale graph data, with or without labels, followed by fine-tuning model parameters for diverse downstream tasks. This two-step process improves model initialization, yielding broader optima and enhanced generalization compared to training from scratch. Commonly employed pre-training schemes include Graph AutoEncoders (GAEs)~\cite{

### 中文

为了解决 GNN 中有限标记数据和泛化问题的挑战，在自然语言处理 (NLP) 社区中蓬勃发展的预训练和微调范式已在图表示学习中得到广泛采用。这些方法涉及在带有或不带有标签的大规模图数据上预训练模型，然后针对不同的下游任务微调模型参数。与从头开始训练相比，这个两步过程改进了模型初始化，产生更广泛的优化并增强了泛化能力。常用的预训练方案包括图自动编码器（GAE）\cite{

### 原文

wang2017mgae}, Masked Components Modeling (MCM)~\cite{hu2020strategies, rong2020selfsupervised}, Graph Contrastive Learning (GCL)~\cite{velickovic2019deep, sun2020infograph}, etc. In Section~\ref{sec:pretrain_method}, we will delve into a detailed discussion of the pre-training and fine-tuning method, offering a comprehensive picture.

### 中文

wang2017mgae}、掩蔽组件建模（MCM）、图对比学习（GCL）等。在第 sec:pretrain_method 节中，我们将深入讨论预训练和微调方法，提供全面的了解。

### 原文

Due to the growing number of model parameters, the conventional \emph{pre-training and fine-tuning} process is evolving into a new approach termed \emph{pre-training, prompting, and predicting}~\cite{liu2023pretrain}. In this paradigm, instead of manually adapting the pre-trained model for specific downstream tasks, these tasks are reformulated to resemble those addressed during the pre-training phase, aided by prompts. Prompts in NLP take various shapes, including cloze prompts

### 中文

由于模型参数数量不断增加，传统的预训练和微调过程正在演变为一种新的方法，称为预训练、提示和预测。在此范例中，不是手动调整预训练模型以适应特定的下游任务，而是在提示的帮助下重新制定这些任务以类似于预训练阶段处理的任务。 NLP 中的提示有多种形式，包括完形填空提示

### 原文

, which complete textual strings like those used in masked language models, and prefix prompts~\cite{lester2021power,li2021prefixtuning}, where the input text precedes the answer slot, as employed by autoregressive language models. Some studies involve manually designed templates based on human insights~\cite{

### 中文

，它完成文本字符串，如掩码语言模型中使用的文本字符串，以及前缀提示 ，其中输入文本位于答案槽之前，如自回归语言模型所使用的那样。一些研究涉及基于人类洞察力手动设计的模板\cite{

### 原文

brown2020language,schick2021fewshot,schick2021it}, while others explore automated template learning. This includes searching for templates in a discrete space~\cite{jiang2020how, haviv2021bertese, shin2020autoprompt,gao2021making} or conducting prompting directly in the embedding space~\cite{li2021prefixtuning, lester2021power,tsimpoukelli2021multimodal,qin2021learning}. Such a paradigm enables a single pre-trained model to address a multitude of downstream tasks in an unsupervised manner, which has been widely demonstrated by large language models. In light of this, the application of prompting techniques in the context of graph-based tasks is currently an area of active exploration.

### 中文

Brown2020language,schick2021fewshot,schick2021it}，而其他人则探索自动化模板学习。这包括在离散空间中搜索模板或直接在嵌入空间中进行提示。这种范式使得单个预训练模型能够以无监督的方式处理大量下游任务，这已被大型语言模型广泛证明。有鉴于此，在基于图的任务中应用提示技术是当前积极探索的领域。

### 原文

Why is prompt learning promising for the graph domain? An existing perspective that appears in most related work is that prompt can reformulate downstream tasks to the pre-training task, which might fill the gap between them. This perspective is good but still not profound enough to see the intrinsic difference from traditional fine-tuning. For example, in a similar perspective, pre-training and fine-tuning can be treated as using fine-tuning to reformulate the pre-training task to the downstream task. It seems that these two technique routines can both address the same problem. Why the first choice is better than the second one?

### 中文

为什么即时学习对于图领域来说是有希望的？大多数相关工作中出现的现有观点是，提示可以将下游任务重新表述为预训练任务，这可能会填补它们之间的空白。这个视角很好，但还不够深刻，看不到与传统微调的本质区别。例如，从类似的角度来看，预训练和微调可以视为使用微调将预训练任务重新表述为下游任务。看来这两种技术例程都可以解决同一个问题。为什么第一个选择比第二个更好？

### 原文

In this section, we propose a new perspective, from this view, we can further see the difference between prompting and fine-tuning. As discussed in previous sections, existing graph representation learning methods fail to achieve a satisfactory trade-off between expressiveness and flexibility. Shallow graph embedding approaches offer flexibility as they can be applied to a wide range of downstream tasks. However, they sacrifice expressiveness due to limited parameterization and the inability to incorporate original node features. Take the DeepWalk model as an example, shallow graph methods usually treat node representations as free parameters, which is very flexible because each node can learn its individual representations independently. However, for the reason of gradient, they can not rely on more complicated networks later, which might lose some expressiveness. Actually, there are many more advanced works with deep graph layers using the node representations from DeepWalk as their input features as these node representations are very general in various tasks. On the other hand, GNN-based methods treat node embedding as constant features and seek to find a powerful network for mapping node features to a specific task, which is very expressive. However, the learned feature transform pattern is applied to all the nodes, which means the model can not treat each node embedding as free parameters, and can not achieve as flexible results as the previous ones. When we have multiple tasks, we usually need to train different versions of the same GNN model, which is not as flexible as the previous one.

### 中文

在本节中，我们提出了一个新的视角，从这个角度，我们可以进一步看到提示和微调之间的区别。正如前面几节所讨论的，现有的图表示学习方法未能在表达性和灵活性之间实现令人满意的权衡。浅图嵌入方法提供了灵活性，因为它们可以应用于广泛的下游任务。然而，由于有限的参数化和无法合并原始节点特征，它们牺牲了表达能力。以 DeepWalk 模型为例，浅图方法通常将节点表示视为自由参数，这非常灵活，因为每个节点都可以独立学习其各自的表示。然而，由于梯度的原因，他们以后不能依赖更复杂的网络，这可能会失去一些表达能力。实际上，有许多更高级的深度图层工作使用 DeepWalk 的节点表示作为输入特征，因为这些节点表示在各种任务中非常通用。另一方面，基于 GNN 的方法将节点嵌入视为恒定特征，并寻求找到一个强大的网络来将节点特征映射到特定任务，这非常具有表现力。然而，学习到的特征变换模式应用于所有节点，这意味着该模型不能将每个节点嵌入视为自由参数，并且不能获得像以前的那样灵活的结果。当我们有多个任务时，通常需要训练同一个 GNN 模型的不同版本，这不如之前的灵活。

### 原文

With the above analysis, we can find that traditional fine-tuning actually seeks to further improve the expressiveness of a new task with the pre-trained graph model and can not take care of node flexibility. Unlike fine-tuning, a graph prompt usually has several tokens with free parameters, which is very similar to shallow graph methods. In the meantime, each node in the original graph has constant features for GNN models. By inserting the prompt graph to the original graph, the combined graph has both nodes with constant features and tokens with free parameters. The token parameters can be efficiently tuned, preserving node flexibility. The combined graph is sent to a frozen pre-trained GNN model to leverage the powerful expressiveness of deep graph models.

### 中文

通过以上分析我们可以发现，传统的fine-tuning实际上是寻求利用预训练的图模型进一步提高新任务的表达能力，而无法照顾到节点的灵活性。与微调不同，图形提示通常具有多个具有自由参数的标记，这与浅图方法非常相似。同时，原始图中的每个节点都具有 GNN 模型的恒定特征。通过将提示图插入到原始图中，组合图既有具有恒定特征的节点，又有具有自由参数的标记。可以有效地调整令牌参数，从而保持节点的灵活性。组合图被发送到冻结的预训练 GNN 模型，以利用深度图模型的强大表达能力。

### 原文

In this paper, we argue that the prompting mechanism offers a promising solution to address the limitations of existing graph representation learning methods, effectively balancing flexibility and expressiveness. Pre-trained GNNs inherently possess knowledge of both structural and semantic aspects, enabling the desired level of expressiveness. By introducing prompts, we can seamlessly apply powerful pre-trained models to diverse downstream tasks across various domains in an efficient manner. This is achieved by aligning the format of downstream tasks with that of pre-trained tasks, thus leveraging the full potential of pre-trained models even with minimal supervision signals. While the fine-tuning mechanism can also facilitate domain or task adaptation of pre-trained graph models, it often necessitates a considerable amount of labeled information and requires exhaustive re-training of the pre-trained model. In comparison, the prompt mechanism offers a higher degree of flexibility and efficiency.

### 中文

在本文中，我们认为提示机制提供了一种有前途的解决方案，可以解决现有图表示学习方法的局限性，有效地平衡灵活性和表现力。预训练的 GNN 本质上拥有结构和语义方面的知识，从而实现所需的表达水平。通过引入提示，我们可以以有效的方式将强大的预训练模型无缝地应用于各个领域的各种下游任务。这是通过将下游任务的格式与预训练任务的格式保持一致来实现的，从而即使在监督信号最少的情况下也能充分利用预训练模型的潜力。虽然微调机制还可以促进预训练图模型的领域或任务适应，但它通常需要大量标记信息，并且需要对预训练模型进行彻底的重新训练。相比之下，提示机制具有更高的灵活性和效率。



---

## 文件：`4.Pre-training.tex`

### 原文

Graph pre-training is a pivotal step of the pre-training, prompting, and predicting paradigm in graph representation learning. This approach leverages readily available information to encode the inherent graph structure, providing a robust foundation for generalization across diverse downstream tasks. By integrating these pre-training methods into the comprehensive workflow, we offer an exploration of their interplay with the subsequent prompting and predicting phases, shedding light on the strengths and limitations of this holistic approach. This unique perspective distinguishes our survey, framing graph pre-training as an integral part of the broader graph-prompting learning process. To better illustrate the motivation behind the prompting paradigm, we will now delve into four distinct pre-training strategies within the traditional pre-training and fine-tuning framework.

### 中文

图预训练是图表示学习中预训练、提示和预测范式的关键步骤。这种方法利用现成的信息对固有的图结构进行编码，为跨不同下游任务的泛化提供了坚实的基础。通过将这些预训练方法集成到综合工作流程中，我们探索了它们与后续提示和预测阶段的相互作用，揭示了这种整体方法的优点和局限性。这种独特的视角使我们的调查与众不同，将图预训练视为更广泛的图提示学习过程的一个组成部分。为了更好地说明提示范式背后的动机，我们现在将在传统的预训练和微调框架内深入研究四种不同的预训练策略。

### 原文

Node-level pre-training strategies empower the acquisition of valuable local structure representations that can be transferred to downstream tasks. As shown in Figure~\ref{fig:pretrain}, these strategies encompass both contrastive and predictive learning methods. In contrastive learning, self-supervised signals typically result from perturbations in the original graph structure or attributes, with the goal of maximizing Mutual Information (MI) between the original and self-supervised views. Noteworthy node-level contrastive methods include those presented in~\cite{cheng2023wiener, zhu2021graph, jin2021multiscale, peng2020graph, jiang2021pretraining, wang2021selfsuperviseda}. On the other hand, predictive models focus on reconstructing perturbed data using information from the unperturbed data, as demonstrated in~\cite{hamilton2017inductive, hou2022graphmae, wang2017mgae,park2019symmetric,wang2021selfsupervised,hou2023graphmae2}. However, its emphasis on partially semantic topology patterns restricts its ability to capture higher-order information.

### 中文

节点级预训练策略能够获取有价值的局部结构表示，并将其转移到下游任务。如图所示：预训练，这些策略涵盖对比学习方法和预测学习方法。在对比学习中，自监督信号通常是由原始图结构或属性中的扰动产生的，其目标是最大化原始视图和自监督视图之间的互信息（MI）。值得注意的节点级对比方法包括 中介绍的方法。另一方面，预测模型侧重于使用来自未扰动数据的信息来重建扰动数据，如 中所示。然而，它对部分语义拓扑模式的强调限制了其捕获高阶信息的能力。

### 原文

To enhance performance in tasks such as link prediction, diverse edge-level pre-training strategies have been developed. These strategies excel at capturing node interactions and have undergone extensive exploration. One approach involves discriminating the presence of edges between pairs of nodes, which can be regarded as contrastive methods~\cite{jin2021node, long2022pretraining}. Another approach focuses on reconstructing masked edges by recovering the adjacency matrix~\cite{tan2023s2gae, li2023what, pan2018adversarially, hasanzadeh2019semiimplicit, kim2021how}. Although this pre-training strategy performs admirably in tasks closely related to predicting node relations, it concentrates solely on structural aspects, neglecting the portrayal of node properties, and may encounter challenges when applied to graph-level downstream tasks.

### 中文

为了提高链路预测等任务的性能，已经开发了多种边缘级预训练策略。这些策略擅长捕获节点交互，并且经过了广泛的探索。一种方法涉及区分节点对之间边缘的存在，这可以被视为对比方法。另一种方法侧重于通过恢复邻接矩阵来重建屏蔽边缘。尽管这种预训练策略在与预测节点关系密切相关的任务中表现出色，但它仅关注结构方面，忽略了节点属性的刻画，在应用于图级下游任务时可能会遇到挑战。

### 原文

The necessity to improve graph-level representations for subgraph-related downstream tasks has prompted the exploration of various graph-level pre-training strategies. Similar to node- and edge-level strategies, these approaches can be broadly categorized into two main groups: graph reconstruction methods, involving the masking of graph components and their subsequent recovery~\cite{xie2022selfsupervised, rong2020selfsupervised}, and contrastive methods focused on maximizing mutual information. These contrastive methods target either local patches of node features and global graph features~\cite{velickovic2019deep, sun2020infograph, hassani2020contrastive, sun2021mocl, subramonian2021motifdriven}, or positive and negative pairs of graphs~\cite{you2020graph, suresh2021adversarial, thakoor2021bootstrapped,qiu2020gcc}. While these approaches effectively encode global information and generate valuable graph-level representations, a significant challenge lies in transferring knowledge from a specific pretext task to downstream tasks with substantial gaps, potentially resulting in negative transfer~\cite{rosenstein2005transfer}. This can limit the applicability and reliability of pre-trained models and potentially yield less favorable outcomes, even worse than learning from scratch.

### 中文

改进与子图相关的下游任务的图级表示的必要性促使人们探索各种图级预训练策略。与节点级和边缘级策略类似，这些方法可以大致分为两大类：图重建方法，涉及图组件的屏蔽及其随后的恢复，以及侧重于最大化互信息的对比方法。这些对比方法要么针对节点特征的局部补丁和全局图特征，要么针对正负图对。虽然这些方法有效地编码全局信息并生成有价值的图级表示，但一个重大挑战在于将知识从特定借口任务转移到存在巨大差距的下游任务，这可能导致负转移。这可能会限制预训练模型的适用性和可靠性，并可能产生不太有利的结果，甚至比从头开始学习更糟糕。

### 原文

Multi-task pre-training accommodates multiple optimization objectives, addressing a broad spectrum of graph-related aspects to enhance generalization while mitigating negative transfer issues. These objectives may encompass various combinations, such as concurrent training of node attribution reconstruction and structural recovery~\cite{hu2020strategies, hu2020gptgnn, zhang2020graphbert,

### 中文

多任务预训练可容纳多个优化目标，解决广泛的图相关方面，以增强泛化能力，同时减轻负迁移问题。这些目标可能包含各种组合，例如节点归因重建和结构恢复的并发训练\cite{hu2020strategies，hu2020gptgnn，zhang2020graphbert，

### 原文

fang2022geometryenhanced}. For example, Hu et al.~\cite{hu2020strategies} pre-trained a GNN at both the node and graph levels, enabling the GNN to learn valuable local and global representations simultaneously. Furthermore, some works have employed contrastive learning at different levels~\cite{jiang2021contrastive, xu2021infogcl}, or joint optimization of both contrastive loss and graph reconstruction error~\cite{li2023adaptergnn}. However, it is crucial to recognize that multi-task pre-training approaches may face optimization challenges, potentially resulting in suboptimal performance across tasks. As a result, optimizing model performance for each task while mitigating the negative transfer problem remains a significant but unresolved concern.

### 中文

fang2022几何增强}。例如，胡等人。在节点和图级别预训练 GNN，使 GNN 能够同时学习有价值的局部和全局表示。此外，一些工作采用了不同级别的对比学习，或者对比损失和图重建误差的联合优化。然而，重要的是要认识到多任务预训练方法可能面临优化挑战，可能导致跨任务的性能不佳。因此，优化每个任务的模型性能，同时减轻负迁移问题仍然是一个重要但尚未解决的问题。

### 原文

Fortunately, the prompting and predicting paradigm offers a robust solution to the challenges mentioned above. This approach can fully exploit model performance and seamlessly integrate with advanced GNN architectures. Instead of adapting pre-trained GNNs to downstream tasks through objective engineering, this paradigm reformulates downstream tasks into those solved during the pre-training phase using a graph prompt. This innovative strategy effectively bridges the gap between pretext and downstream tasks while sidestepping suboptimal performance pitfalls. Furthermore, in comparison to traditional fine-tuning approaches, the prompting paradigm showcases remarkable flexibility, enabling it to excel in scenarios demanding few-shot or even zero-shot learning, where adapting to new contexts with limited or no labeled data is paramount. In the current landscape marked by surging model volumes and an ever-expanding array of downstream tasks, the ascent of the prompting paradigm represents an irresistible and transformative trend.

### 中文

幸运的是，提示和预测范例为上述挑战提供了强大的解决方案。这种方法可以充分利用模型性能并与先进的 GNN 架构无缝集成。该范式不是通过目标工程使预训练的 GNN 适应下游任务，而是使用图形提示将下游任务重新表述为预训练阶段解决的任务。这种创新策略有效地弥合了借口和下游任务之间的差距，同时避开了次优的性能陷阱。此外，与传统的微调方法相比，提示范式展示了显着的灵活性，使其能够在需要少样本甚至零样本学习的场景中表现出色，在这些场景中，适应具有有限或无标记数据的新环境至关重要。在当前模型数量激增和下游任务不断扩大的格局中，提示范式的崛起代表了一种不可抗拒的变革趋势。



---

## 文件：`5.tex`

### 原文

In this section, we propose a unified view for the graph prompt. As shown in \figref{fig:prompt}, the graph prompt should contain at least three components: prompt tokens with prompt vector; token structures preserving inner correlations of these tokens; and inserting patterns indicating how to integrate the original graph with prompts. Beyond these details, we are particularly interested in the following questions: \textit{Question 1:} How do these works design the graph prompt? \textit{Question 2:} How do these works reformulate downstream tasks to the pre-training tasks? \textit{Question 3:} How do these works learn an effective prompt? and \textit{Question 4:} What are the inner connections of these works, their advantages and limitations? With these questions, we summarize the most representative works published recently and present them in \tabref{tab:graph_prompt_summary}.

### 中文

在本节中，我们提出了图形提示的统一视图。如图所示：提示，图形提示应至少包含三个组成部分：带有提示向量的提示标记；保留这些令牌的内部相关性的令牌结构；并插入指示如何将原始图形与提示结合起来的模式。除了这些细节之外，我们对以下问题特别感兴趣： 问题一：这些作品是如何设计图形提示的？问题2：这些工作如何将下游任务重新表述为预训练任务？问题3：这些作品如何学习有效的提示？问题4：这些作品的内在联系、优点和局限性是什么？带着这些问题，我们总结了最近发表的最具代表性的作品，并在 tab:graph_prompt_summary 中呈现。

### 原文

The simplest graph prompt can be treated as some additional features added to the original graph features \cite{zhu2023graphcontrol}. For example, given a graph feature matrix $\mathbf{X}=\{x_1,\cdots, x_N\} \in \mathbb{R}^{N\times d}$ where $x_i\in \mathbb{R}^{1\times d}$ is the feature of $i$-th node and $d$ is the dimension of the feature space. \citet{fang2022prompt} and \citet{shirkavand2023deep} treat the basic prompt as a learnable vector $p \in \mathbb{R}^{1\times d}$, which can be added to all node features and make the manipulated feature matrix be $\mathbf{X}^{*}=\{x_1+p,\cdots, x_N+p\}$. In this way, we can use the reformulated features to replace the original features and process the graph with pre-trained graph models. A later work \cite{fang2023universal} further extends one prompt token to multiple tokens and makes the performance better. PGCL \cite{gong2023prompt} design a prompt vector for semantic view and another prompt vector for contextual view, then they add these prompt vectors to the graph-level representations by element-wise multiplication. A similar prompt design is also adopted in VNT \cite{tan2023virtual}. The difference is that their inserting pattern does not add the prompt token to the original graph feature but concatenates the prompt token with the original node set and tries to integrate them by the self-attention function in a graph transformer. In GraphPrompt \cite{liu2023graphprompt}, the prompt token is similar to the format defined by \citet{fang2022prompt}. The difference thing is that previous work designed the prompt tokens in the initial feature space, while this method assumes the prompt in the hidden layer of the graph model. Usually, the hidden size will be smaller than the original feature, making their prompt token shorter than the previous one. Another different thing is that the graph prompt here is used to assist graph pooling operation (a.k.a $\text{Readout}$). For example, given the node set $\mathcal{V}=\{v_1,\cdots, v_{|\mathcal{V}|}\}$, the embedding of node $v$ is $\textbf{h}_v \in \mathbb{R}^{1\times d}$, a prompt token $\textbf{p}_t \in \mathbb{R}^{1\times d}$ specified to task $t$ is inserted to the graph nodes by the element-wise multiplication ($\otimes$): $\textbf{s}_t=\text{Readout}(\{\textbf{p}_t \otimes \textbf{h}_v:v \in \mathcal{V}\})$. Similarly, SGL-PT \cite{zhu2023sglpt} creates a prompt token to connect to all nodes in the graph. The prompt token preserves a global perception of the graph and can assist their global branch of the pre-training tasks, which can be also treated as a pooling strategy. Aiming at aligning node classification and link prediction, GPPT \cite{sun2022gppt} defines graph prompts as additional tokens that contain task tokens and structure tokens. Here the task token refers to the description of the downstream node label to be classified and the structure token is the representation of the subgraph surrounding the target node. By this means, predicting node $v$'s label can be reformulated to predict a potential link between node $v$'s structure token and the label task token. Aiming at the node classification task, ULTRA-DP \cite{chen2023ultradp} creates a prompt token for each target node, where the token feature is the weighted sum of position embedding of the target node and a task embedding of the pre-training task. HetGPT \cite{ma2023hetgpt} design a prompt with node tokens and class tokens, which are organized in a similar way to GPPT. The difference is that they also add a type-specific feature token to make graph prompts sensitive to different node types, by which they can extend existing graph prompts to heterogeneous graphs.

### 中文

最简单的图形提示可以看作是在原始图形特征上添加的一些附加特征。例如，给定一个图特征矩阵，其中 是第 - 个节点的特征， 是特征空间的维度。将基本提示视为可学习向量，将其与所有节点特征相加，使操作后的特征矩阵为 。这样，我们就可以使用重新表述的特征来替换原始特征，并用预先训练的图模型来处理图。后来的工作进一步将一个提示令牌扩展到多个令牌，并使性能更好。 PGCL 为语义视图设计一个提示向量，为上下文视图设计另一个提示向量，然后通过逐元素乘法将这些提示向量添加到图级表示中。 VNT中也采用了类似的提示设计。不同之处在于，它们的插入模式不会将提示标记添加到原始图特征中，而是将提示标记与原始节点集连接起来，并尝试通过图转换器中的自注意力函数将它们集成。在 GraphPrompt 中，提示标记与 定义的格式类似。不同之处在于，之前的工作在初始特征空间中设计了提示标记，而该方法假设提示位于图模型的隐藏层中。通常，隐藏的尺寸会小于原始特征，使得它们的提示标记比前一个更短。另一个不同的是，这里的图形提示用于辅助图形池操作（又名）。例如，给定节点集 ，节点的嵌入为 ，指定给任务的提示标记通过逐元素乘法 (): 插入到图节点中。同样，SGL-PT 创建一个提示令牌来连接到图中的所有节点。提示令牌保留了对图的全局感知，并且可以协助其预训练任务的全局分支，这也可以被视为池化策略。为了协调节点分类和链接预测，GPPT 将图形提示定义为包含任务标记和结构标记的附加标记。这里的任务令牌是指对要分类的下游节点标签的描述，结构令牌是目标节点周围的子图的表示。通过这种方式，可以重新表述预测节点的标签以预测节点的结构令牌和标签任务令牌之间的潜在链接。针对节点分类任务，ULTRA-DP为每个目标节点创建一个提示令牌，其中令牌特征是目标节点的位置嵌入和预训练任务的任务嵌入的加权和。 HetGPT 设计了带有节点标记和类标记的提示，其组织方式与 GPPT 类似。不同之处在于，他们还添加了特定于类型的特征标记，使图形提示对不同的节点类型敏感，从而可以将现有的图形提示扩展到异构图形。

### 原文

The graph prompt in All in One \cite{sun2023all} is an additional subgraph that can be learned by efficient tuning. The prompt tokens are some additional nodes that have the same size of node representation as the original nodes. They assume the prompt tokens should be in the same semantic space as the original node features so that we can easily manipulate node features with these tokens. The token structures include two parts. The first part is the inner links among different tokens, and the second part is the cross-links between the prompt graph and the original graph. These links can be pre-calculated by the dot product between one token to another token (inner links) or one token to another original node (cross links). The inserting pattern is to add the prompt graph to the original graph by the cross-links and then treat the combined graph as a new graph, and send it to the pre-trained graph model to get the graph-level representation. The prompt graph in PRODIGY \cite{huang2023prodigy} includes data graphs and a task graph. The data graphs can be treated as subgraphs surrounding the target nodes (for node classification task), node pairs (for edge classification task), or just denoted as the graph classification instance. Here the prompt tokens and prompt structures are just the same as in the original graph. The task graph contains data tokens and label tokens where each data token connects to one data graph and is further connected by label tokens. Unlike previous works that aim at reformulating downstream tasks to the pre-training task by prompting the downstream data, PRODIGY leverages the prompt graph to unify all the upstream and downstream tasks. Their pre-training strategy is a set of tasks including neighboring matching and label matching, which can be reformulated as predicting the similarity between the data token and the label token in the prompt graph. SAP \cite{ge2023enhancing} also connects several prompt tokens (each token corresponds to one class) to the original graph by cross-links defined in All in One. The difference is that their prompting task is a node-level contrastive task, in which they use MLP to encode the node features as the first view and they use a GNN to encode the prompted graph as the second view, which is consistent with their pre-training task.

### 中文

All in One 中的图形提示是一个额外的子图，可以通过高效调优来学习。提示标记是一些附加节点，其节点表示大小与原始节点相同。他们假设提示标记应该与原始节点特征位于相同的语义空间中，以便我们可以轻松地使用这些标记来操作节点特征。代币结构包括两部分。第一部分是不同token之间的内部链接，第二部分是提示图与原始图之间的交叉链接。这些链接可以通过一个令牌到另一个令牌（内部链接）或一个令牌到另一个原始节点（交叉链接）之间的点积来预先计算。插入模式是通过交叉链接将提示图添加到原始图上，然后将组合后的图视为新图，并将其发送到预训练的图模型中以获得图级表示。 PRODIGY 中的提示图包括数据图和任务图。数据图可以被视为围绕目标节点的子图（对于节点分类任务）、节点对（对于边缘分类任务），或者仅表示为图分类实例。这里的提示标记和提示结构与原始图中的相同。任务图包含数据令牌和标签令牌，其中每个数据令牌连接到一个数据图，并通过标签令牌进一步连接。与之前旨在通过提示下游数据将下游任务重新表述为预训练任务的工作不同，PRODIGY 利用提示图来统一所有上下游任务。他们的预训练策略是一组包括邻近匹配和标签匹配的任务，可以将其重新表述为预测提示图中数据标记和标签标记之间的相似性。 SAP 还通过 All in One 中定义的交叉链接将多个提示标记（每个标记对应一个类）连接到原始图。不同之处在于，他们的提示任务是节点级对比任务，其中他们使用 MLP 将节点特征编码为第一个视图，并使用 GNN 将提示图编码为第二个视图，这与他们的预训练任务一致。

### 原文

All in One \cite{sun2023all} pre-trains the graph model via graph-level contrastive learning. The pre-training task aims to learn a robust graph encoder over different graph views generated by the perturbations of the original graph. To reformulate various graph tasks to this graph-level pretext, they first unify node-level, edge-level, and graph-level tasks to the graph-level task by induced subgraphs, which are also introduced in PRODIGY \cite{huang2023prodigy,liu2023graphprompt,gong2023prompt}. Then they claim that the graph prompt added to the original graph is in nature the simulation of any graph operations such as node feature masking, node or edge perturbations, subgraph removing, etc. With this opinion, we just need to add an appropriate graph prompt to downstream graph datasets then it will be promising to further reformulate the downstream task to the pretext.

### 中文

All in One 通过图级对比学习来预训练图模型。预训练任务的目的是在原始图的扰动生成的不同图视图上学习鲁棒的图编码器。为了将各种图任务重新表述为图级借口，他们首先通过诱导子图将节点级、边级和图级任务统一为图级任务，这也在 PRODIGY 中引入。然后他们声称添加到原始图中的图提示本质上是对任何图操作的模拟，例如节点特征屏蔽、节点或边缘扰动、子图删除等。按照这种观点，我们只需向下游图数据集添加适当的图提示，然后就有希望进一步重新制定下游任务的借口。

### 原文

To output the results of downstream tasks, \citet{sun2023all} design two types of answering functions. The first one is a learnable task head (such as an MLP mapping function) that can be easily tuned with very limited data. It takes the graph-level representation generated by the pre-trained graph model and then outputs the downstream result. For example, if the downstream is a three-class node classification, we can simply use a dense layer with three hidden units to connect the graph representation, which is generated by the pre-trained model on the combined graph with node included graph and a graph prompt. In this case, both the graph prompt and the task head are tunable, so we can adjust them alternately. Similar learnable answering functions are also adopted in other works like \cite{fang2022prompt, fang2023universal,tan2023virtual}. The good point is that they are very easy to align two tasks, however, it also increases the tuning workflow.

### 中文

为了输出下游任务的结果，设计两种类型的应答函数。第一个是可学习的任务头（例如 MLP 映射函数），可以使用非常有限的数据轻松调整。它采用预先训练的图模型生成的图级表示，然后输出下游结果。例如，如果下游是三类节点分类，我们可以简单地使用具有三个隐藏单元的密集层来连接图表示，该图表示是由预训练模型在包含节点的图和图提示的组合图上生成的。在这种情况下，图形提示和任务头都是可调的，因此我们可以交替调整它们。类似的可学习答题功能在其他作品中也有采用。好处是它们很容易协调两个任务，但是，它也增加了调整工作流程。

### 原文

To further reduce the tuning burden, All in One \cite{sun2023all} also proposes a second answering function, which is hand-crafted without any trainable task head. For example, for a node classification task, we can set up $K$ unique sub-prompts, each aligning with a different node type, where $K$ represents the total number of node categories. If the pre-training involves a task like GraphCL \cite{you2020graph}, which aims to maximize similarity at the graph level between pairs of graph views, then the target node can be classified with label $\ell, (\ell=1,2,\cdots,K)$ if the $\ell$-th graph most closely resembles the original node-inclusive graph. Similarly, GPPT \cite{sun2022gppt} and  HetGPT \cite{ma2023hetgpt} use link prediction as their pre-training task and reformulate downstream node classification by unifying it as the same task template. For example, by treating the node label as an additional token, we can use the pre-trained model to directly output the possibility of an edge between the label token and the target node. The pre-training strategy in SAP \cite{ge2023enhancing} is to compare node representations from two graph views, the first of which is generated by node feature encoding and the second of which is encoded by a graph model. To this end, their prompt tokens denote class information and they compare node representation with each class token to find the class with the largest similarity as the inference results. By designing a unified task template, PRODIGY \cite{huang2023prodigy} uses a hand-crafted graph prompt to describe all node, edge, and graph classification tasks by predicting the link between data tokens and label tokens. \citet{liu2023graphprompt} extend the link prediction task as graph pair similarity and treat it as their pre-training task, to align the downstream node classification and graph classification task, they design a unified answering template making the downstream side aligned with the pre-training side. Specifically, given a triplet of induced graphs $(g_1,g_2, g_3)$ where $g_1$ and $g_2$ have the same label, $g_1$ and $g_3$ have different labels. In particular, when the target task is node classification, the induced graph refers to the contextual subgraph of the target node. The unified answering template is defined as  $\text{sim}(g_1,g_2)>\text{sim}(g_1,g_3)$.

### 中文

为了进一步减轻调优负担，All in One 还提出了第二个应答功能，该功能是手工制作的，没有任何可训练的任务头。例如，对于节点分类任务，我们可以设置唯一的子提示，每个子提示与不同的节点类型对齐，其中表示节点类别的总数。如果预训练涉及像 GraphCL 这样的任务，其目的是最大化图视图对之间图级别的相似性，那么如果第 - 个图最接近原始包含节点的图，则可以使用标签对目标节点进行分类。类似地，GPPT 和 HetGPT 使用链路预测作为预训练任务，并通过将其统一为相同的任务模板来重新制定下游节点分类。例如，通过将节点标签视为附加标记，我们可以使用预训练模型直接输出标签标记与目标节点之间存在边的可能性。 SAP 中的预训练策略是比较两个图视图的节点表示，第一个图视图是由节点特征编码生成的，第二个图视图是由图模型编码的。为此，他们的提示标记表示类别信息，并将节点表示与每个类别标记进行比较，以找到相似度最大的类别作为推理结果。通过设计统一的任务模板，PRODIGY 通过预测数据标记和标签标记之间的链接，使用手工制作的图形提示来描述所有节点、边和图分类任务。将链路预测任务扩展为图对相似度并将其视为预训练任务，为了对齐下游节点分类和图分类任务，他们设计了统一的答案模板，使下游侧与预训练侧对齐。具体来说，给定一个三元组的归纳图，其中 和 具有相同的标签，并且具有不同的标签。特别地，当目标任务是节点分类时，归纳图指的是目标节点的上下文子图。统一答题模板定义为 。

### 原文

To learn appropriate prompts, \citet{sun2023all}  leverage meta-learning techniques (such as MAML\cite{finn2017modelagnostic} model) to obtain a robust starting point for the prompt parameters. Since the support set and query set include various graph tasks (such as node classification, link prediction, graph classification, etc), the learned graph prompt is expected to be more general on various downstream tasks.

### 中文

要学习适当的提示，请利用元学习技术（例如 MAML 模型）来获取提示参数的可靠起点。由于支持集和查询集包括各种图任务（例如节点分类、链接预测、图分类等），因此学习到的图提示有望在各种下游任务上更加通用。

### 原文

Besides All in One \cite{sun2023all}, which aims to learn a general prompt on various downstream tasks, there are also some works that target specific downstream tasks such as graph classification. In this case, the prompt tuning can be more task-directed. For example, GPF \cite{fang2022prompt} aims at a graph classification task, so it just needs to tune the prompt token $\textbf{p}$ and the task head $\phi$ by maximizing the likelihood of predicted correct graph labels given the prompted graph representation $\tilde{\textbf{s}}_i$ from the pre-trained graph model $\pi$. In this case, the task head tuning and the prompt tuning share the same objectives, which can be formulated by: $\max_{\textbf{p}, \phi} \sum_{(y_i,\tilde{\textbf{s}}_i)} p_{\pi, \phi} (y_i| \tilde{\textbf{s}}_i)$.

### 中文

除了 All in One 旨在学习各种下游任务的通用提示之外，还有一些针对特定下游任务（例如图分类）的作品。在这种情况下，提示调整可以更加以任务为导向。例如，GPF针对的是图分类任务，因此它只需要根据预训练图模型的提示图表示，通过最大化预测正确图标签的可能性来调整提示标记和任务头。在这种情况下，任务头调整和提示调整具有相同的目标，可以表示为： 。

### 原文

Intuitively, prompting aims at reformulating downstream tasks to the pre-training task. Therefore, it would be more natural if the prompt tuning shares the same objective with the pre-training task. As suggested in GraphPrompt \cite{liu2023graphprompt}, the authors use a similar loss function to learn prompts. Similarly, GPPT \cite{sun2022gppt} and VNT \cite{tan2023virtual} adopt the same loss function (Cross-Entropy) as their link prediction and node classification tasks, respectively. HetGPT \cite{ma2023hetgpt} and  SAP \cite{ge2023enhancing} use a node-level contrastive loss to learn their prompt tokens because their pre-training task is also conducted by the same contrastive task (node pair comparison). PGCL \cite{gong2023prompt} introduces graph-level loss to align with the pre-training task. ULTRA-DP \cite{chen2023ultradp} develop two pre-training tasks including edge prediction and neighboring prediction, each of which corresponds to one task embedding. In the pre-training phase, they randomly select a task and then integrate specific task-related embeddings into the prompt tokens. These learnable task embeddings are then trained with the graph model.

### 中文

直观上，提示的目的是将下游任务重新表述为预训练任务。因此，如果提示调整与预训练任务具有相同的目标，那就更自然了。正如 GraphPrompt 中所建议的，作者使用类似的损失函数来学习提示。类似地，GPPT 和 VNT 分别采用相同的损失函数（交叉熵）作为其链路预测和节点分类任务。 HetGPT 和 SAP 使用节点级对比损失来学习它们的提示标记，因为它们的预训练任务也是通过相同的对比任务（节点对比较）进行的。 PGCL 引入了图级损失以与预训练任务保持一致。 ULTRA-DP开发了边缘预测和邻近预测两个预训练任务，每个任务对应一个任务嵌入。在预训练阶段，他们随机选择一个任务，然后将特定的与任务相关的嵌入集成到提示标记中。然后使用图模型训练这些可学习的任务嵌入。

### 原文

The good point of GPF \cite{fang2022prompt} is that they propose a very simple prompt that can be easily used in various pre-training tasks and downstream tasks. However, a single prompt token added to all nodes is very limited in expressiveness and generalization. A potential solution is to learn an independent prompt token for each node, which means one node corresponds to one prompt token, but this will cause low efficiency in parameters. To this end, we can train K-independent basis vectors and use them to compound each node token (GPF-Plus \cite{fang2023universal}). This improvement makes their work have more similar insights with All in One \cite{sun2023all}.

### 中文

GPF的优点在于他们提出了一个非常简单的提示，可以很容易地用于各种预训练任务和下游任务。然而，添加到所有节点的单个提示标记在表达性和泛化性方面非常有限。一种可能的解决方案是为每个节点学习一个独立的提示标记，即一个节点对应一个提示标记，但这会导致参数效率低下。为此，我们可以训练 K 独立基向量并使用它们来复合每个节点标记（GPF-Plus）。这一改进使得他们的工作与 All in One 有了更多相似的感悟。

### 原文

HetGPT \cite{ma2023hetgpt} extends prompt tokens to type-specific format, which can deal with graph prompting in heterogeneous data. However, they can only deal with node classification tasks. To this end, GraphPrompt \cite{liu2023graphprompt} reformulates link prediction to graph pair similarity task. It is worth noticing that the role of their prompt token is very similar to the project vector in the graph attention network. There are also some attention-based graph-pooling methods, which share the same motivation. The difference is that the authors claim the graph-pooling component in the pre-training stage might not fit other downstream tasks, thus needing additional prompts to redirect the graph-pooling component in the graph model.

### 中文

HetGPT将提示标记扩展为特定于类型的格式，可以处理异构数据中的图形提示。然而，它们只能处理节点分类任务。为此，GraphPrompt 将链接预测重新表述为图对相似性任务。值得注意的是，它们的提示标记的作用与图注意力网络中的项目向量非常相似。还有一些基于注意力的图池方法，它们具有相同的动机。不同之处在于，作者声称预训练阶段的图池组件可能不适合其他下游任务，因此需要额外的提示来重定向图模型中的图池组件。

### 原文

GPPT \cite{sun2022gppt} represents a specific instance within the broader framework of All in One \cite{sun2023all}. For instance, if we minimize the prompt graph to isolated tokens that correlate with node classes and substitute the resulting graphs with a complete graph, the All in One prompt structure can be simplified into the GPPT format. This allows for the utilization of edge-level pretexts in node classification tasks within the GPPT framework. The shortcoming of GPPT might be that it is restricted to binary edge prediction pretexts and is solely effective for node classification in downstream tasks. In comparison, frameworks like GraphPrompt and All in One are designed to accommodate a wider array of graph-related tasks, extending beyond just node-level classification. The good point is that when adapting models for different tasks, GraphPrompt, GPF, and GPF-Plus often require the tuning of an extra task-specific module. In contrast, All in One, and GPPT utilize task templates that focus more on the manipulation of input data and are less dependent on the specifics of downstream tasks.

### 中文

GPPT 代表了 All in One 更广泛框架内的一个特定实例。例如，如果我们将提示图最小化为与节点类相关的孤立标记，并用完整图替换结果图，则 All in One 提示结构可以简化为 GPPT 格式。这允许在 GPPT 框架内的节点分类任务中利用边缘级借口。 GPPT 的缺点可能是它仅限于二进制边缘预测借口，并且仅对下游任务中的节点分类有效。相比之下，像 GraphPrompt 和 All in One 这样的框架旨在适应更广泛的图形相关任务，而不仅仅是节点级分类。好处是，当针对不同任务调整模型时，GraphPrompt、GPF 和 GPF-Plus 通常需要调整额外的特定于任务的模块。相比之下，All in One 和 GPPT 使用的任务模板更注重输入数据的操作，较少依赖于下游任务的具体情况。

### 原文

Intuitively, the data graphs, one of the components in PRODIGY \cite{huang2023prodigy}, are very similar to the induced graph in All in One and GraphPrompt. The pre-training task in PRODIGY can be seen as predicting a link between the data token and the label token, which shares a similar insight with GPPT. The good thing is that their prompts have no trainable parameters, which means they do not need to tune the prompt and are more efficient in the in-context learning area. PRODIGY  does not need any tuning work and can be used in knowledge transferring between different datasets. However, a non-tunable prompt is usually not flexible enough, which might also limit the generalization of the pre-trained model when the downstream tasks to be transferred are located in a different domain from the pre-training one. In contrast, ULTRA-DP \cite{chen2023ultradp} tune prompt both in the pre-training stage and the downstream tasks. It first put the prompt tuning work in the pre-training stage to obtain the task embeddings, which are one of the main components in their prompt. Then they use these task embeddings to initialize a downstream prompt. Intuitively, their prompts are not used to reformulate downstream tasks to the pretext. Instead, these prompt tokens are used to select suitable pre-training tasks from a task pool to fit the downstream task. It is still an interesting question of how to achieve the optimal balance given efficiency, generalization, and the flexibility of prompt.

### 中文

直观上，数据图（PRODIGY 中的组件之一）与 All in One 和 GraphPrompt 中的归纳图非常相似。 PRODIGY 中的预训练任务可以看作是预测数据令牌和标签令牌之间的联系，这与 GPPT 具有类似的见解。好处是他们的提示没有可训练的参数，这意味着他们不需要调整提示，并且在上下文学习领域更加高效。 PRODIGY不需要任何调整工作，可以用于不同数据集之间的知识转移。然而，不可调整的提示通常不够灵活，当要转移的下游任务与预训练任务位于不同的域时，这也可能限制预训练模型的泛化。相比之下，ULTRA-DP 在预训练阶段和下游任务中都会提示。它首先将提示调整工作放在预训练阶段以获得任务嵌入，这是提示的主要组成部分之一。然后他们使用这些任务嵌入来初始化下游提示。直观上，他们的提示不会被用来借口重新制定下游任务。相反，这些提示令牌用于从任务池中选择合适的预训练任务以适应下游任务。如何在效率、泛化性和提示的灵活性之间达到最佳平衡，仍然是一个有趣的问题。

### 原文

Compared with other works that usually define clear inserting patterns, VNT \cite{tan2023virtual} concatenates prompt tokens with the original node set and then puts all of them into the graph transformer. Actually, the graph transformer will leverage a self-attention function to further calculate the correlations among them, which can also be treated as a variant of inserting patterns defined in All in One. The good thing is that we do not need to design a threshold to tailor the connection but the shortcoming is that it can only use a graph transformer as its backbone and can not applied to more message-passing-based graph models. In addition, there are also some more advanced variants of graph transformers requiring additional position embedding as one of their input. However, the prompt tokens in VNT have no clear inserting links to the original graph, which might not make it easy to apply existing position encoding approaches for these graph transformer variants.

### 中文

与通常定义明确插入模式的其他作品相比，VNT 将提示标记与原始节点集连接起来，然后将它们全部放入图形转换器中。实际上，图转换器将利用自注意力函数来进一步计算它们之间的相关性，这也可以视为 All in One 中定义的插入模式的一种变体。好处是我们不需要设计阈值来定制连接，但缺点是它只能使用图转换器作为其骨干，不能应用于更多基于消息传递的图模型。此外，还有一些更高级的图形转换器变体需要额外的位置嵌入作为其输入之一。然而，VNT 中的提示标记没有指向原始图的明确插入链接，这可能不容易为这些图变换器变体应用现有的位置编码方法。

### 原文

The fusion of images, sound, and text has been widely studied and achieved remarkable success. However, most of these modalities are described by linear data structure. In our real-world life, there are more kinds of data in non-linear structures like graphs. How to connect these linear modalities (e.g. text, images, sound, etc) to the non-linear modalities (e.g. graphs) has become a very attractive research topic because it is a bigger move towards artificial general intelligence. Unfortunately, reaching this vision is very tough. Currently, we only see some hard progress in the fusion of text and graphs, especially in the text-attributed graphs. With the help of recent large language models, the fusion of text and graph has achieved even more notable performance. Since there have already been some informative surveys on this topic, we next briefly discuss some representative works that are closely related to \textit{\dotuline{prompt techniques}}. We suggest readers refer to the mentioned literature \cite{li2023survey,liu2023graph} to require more detailed information further.

### 中文

图像、声音和文本的融合已被广泛研究并取得了显着的成功。然而，大多数这些模态都是通过线性数据结构来描述的。在我们的现实生活中，存在更多类型的非线性结构（例如图形）数据。如何将这些线性模态（例如文本、图像、声音等）与非线性模态（例如图形）连接起来已经成为一个非常有吸引力的研究课题，因为它是迈向通用人工智能的更大一步。不幸的是，实现这一愿景非常困难。目前，我们在文本和图形的融合方面只看到了一些艰难的进展，特别是在文本属性图形方面。在最近的大型语言模型的帮助下，文本和图形的融合取得了更加显着的性能。由于关于这个主题已经有一些信息丰富的调查，我们接下来简要讨论一些与 dotuline{提示技术} 密切相关的代表性作品。我们建议读者参考上述文献以进一步了解更详细的信息。

### 原文

The integration of multi-modal data using graph and prompting techniques has seen remarkable progress in recent years. For example, \citet{edwards2023synergpt} propose SynerGPT in the field of drug synergy prediction. This model leverages a transformer-based approach, uniquely combining in-context learning with genetic algorithms to predict drug synergies. In the area of vision-language models, \citet{li2023graphadapter} develop GraphAdapter, a prompt-based strategy that utilizes an adapter-style tuning mechanism, bringing together textual and visual modalities through a dual knowledge graph. \citet{liu2023gitmol} extend work multi-modal fusion into molecular science with their proposed GIT-Mol. A large language model integrates graph, image, and textual data with the help of prompt, offering substantial improvements in various tasks like molecule generation and property prediction. Although much effort has been made in the past few years, the academic is still trying hard to find better solutions to integrate text and graphs via text-attributed graphs or knowledge graphs. There is still a very large imagination in the fusion of more kinds of modalities.

### 中文

近年来，使用图和提示技术集成多模态数据取得了显着进展。例如在药物协同预测领域提出SynerGPT。该模型利用基于变压器的方法，独特地将上下文学习与遗传算法相结合来预测药物协同作用。在视觉语言模型领域，开发GraphAdapter，这是一种基于提示的策略，利用适配器式调整机制，通过双知识图将文本和视觉模式结合在一起。通过他们提出的 GIT-Mol 将多模式融合工作扩展到分子科学。大型语言模型在提示的帮助下集成了图形、图像和文本数据，为分子生成和属性预测等各种任务提供了实质性改进。尽管过去几年已经做出了很多努力，但学术界仍在努力寻找更好的解决方案，通过文本归因图或知识图来整合文本和图。更多种形态的融合还有非常大的想象空间。

### 原文

The field of graph domain adaptation has seen significant advancements, particularly with the integration of prompting techniques. However, graph domain adaptation is still not a well-solved problem because there exist at least two challenges: The first one is how to align semantic spaces from different domains. The second one is how to identify structural differences.

### 中文

图域适应领域已经取得了重大进展，特别是在提示技术的集成方面。然而，图域适应仍然不是一个很好解决的问题，因为至少存在两个挑战：第一个是如何对齐不同域的语义空间。第二个是如何识别结构性差异。

### 原文

In particular, All in One \cite{sun2023all} extends the ``pre-training and fine-tuning'' workflow with multi-task prompting for GNNs, unifying prompt formats, and introducing meta-learning for prompt optimization. To make the graph model adaptive to different graph domains, they first reveal that the graph prompt in nature can be seen as graph operation and then they use graph prompt to manipulate different domain graph datasets. GraphControl \cite{zhu2023graphcontrol} introduces a unique deployment module inspired by ControlNet, effectively integrating downstream-specific information as conditional inputs to enhance the adaptability of pre-trained models to target data. This approach aligns input space across various graphs and incorporates unique characteristics of the target data. \citet{zhang2023structure} presents a pre-training model for knowledge graph transfer learning. This model uses a general prompt-tuning mechanism, treating task data as a triple prompt, enabling flexible interactions between task KGs and task data. \citet{yi2023contrastive} combines personalized graph prompts with contrastive learning for efficient and effective cross-domain recommendation, particularly in cold-start scenarios. A representative work is proposed by \citet{liu2023one}, in which they describe graph nodes from different domains by language and then use LLM to get a textual embedding. However, this work needs the semantic name of each feature while sometimes graph features are usually latent vectors without clear semantic meaning.

### 中文

特别是，All in One 通过 GNN 的多任务提示、统一提示格式以及引入用于提示优化的元学习来扩展“预训练和微调”工作流程。为了使图模型适应不同的图域，他们首先揭示了图提示本质上可以看作图操作，然后使用图提示来操作不同域的图数据集。 GraphControl 引入了受 ControlNet 启发的独特部署模块，有效地将下游特定信息集成为条件输入，以增强预训练模型对目标数据的适应性。这种方法跨各种图表对齐输入空间，并结合目标数据的独特特征。提出了知识图迁移学习的预训练模型。该模型采用通用的提示调优机制，将任务数据视为三重提示，实现任务知识图谱和任务数据之间的灵活交互。将个性化图形提示与对比学习相结合，以实现高效且有效的跨域推荐，特别是在冷启动场景中。提出了一个代表性的工作，其中他们通过语言描述来自不同领域的图节点，然后使用LLM得到文本嵌入。然而，这项工作需要每个特征的语义名称，而有时图特征通常是没有明确语义的潜在向量。



---

## 文件：`6.Applications.tex`

### 原文

With the widespread utilization of networks as a data modeling structure for representing diverse relational information across social, natural, and academic domains, the graph prompt mechanism exhibits substantial potential for a wide range of real-world applications. In this section, we explore the potential applications of graph prompting in online social networks, recommender systems, knowledge management, and biology.

### 中文

随着网络作为数据建模结构的广泛使用，用于表示跨社会、自然和学术领域的各种关系信息，图提示机制在广泛的现实世界应用中展现出了巨大的潜力。在本节中，我们将探讨图形提示在在线社交网络、推荐系统、知识管理和生物学中的潜在应用。

### 原文

Online social platforms consist of users who can be represented as nodes, and their social connections form online social networks (OSNs). Previous research has investigated the potential of prompting mechanisms in identifying fake news within OSNs to prevent malicious attacks \cite{wu2023promptandalign}. Specifically, they employ textual prompts applied to pre-trained language models (PLMs) to distill general semantic information. By combining this semantic signal with the dynamics of information propagation within social networks, improved classification performance can be achieved. While the use of tailored textual prompts for PLMs has been studied, the application of graph prompting mechanisms within social networks is still under-explored. In the future, it is promising to directly apply prompt tuning techniques to social networks, utilizing few-shot labels for tasks such as fake news detection or anomaly detection \cite{wen2023voucher, guo2023datacentric}, where the labeling process is laborious and requires domain expertise. By incorporating prompts directly within social networks, this approach can address the scarcity of labeled data and enhance the security and trustworthiness of online social networks.

### 中文

在线社交平台由可以表示为节点的用户组成，他们的社交联系形成在线社交网络（OSN）。先前的研究已经调查了 OSN 中识别假新闻的提示机制以防止恶意攻击的潜力。具体来说，他们采用应用于预训练语言模型（PLM）的文本提示来提取一般语义信息。通过将这种语义信号与社交网络内信息传播的动态相结合，可以提高分类性能。虽然已经研究了 PLM 中定制文本提示的使用，但社交网络中图形提示机制的应用仍有待探索。未来，有望直接将即时调整技术应用于社交网络，利用少样本标签来执行诸如假新闻检测或异常检测等任务，其中标记过程非常费力并且需要领域专业知识。通过将提示直接合并到社交网络中，这种方法可以解决标记数据的稀缺问题，并增强在线社交网络的安全性和可信度。

### 原文

E-commerce platforms provide a valuable opportunity to leverage recommender systems for enhancing online services. While prompt tuning in recommender systems has received limited research attention, it holds significant potential \cite{yi2023contrastive,yang2023empirical, wu2023personalized, hao2024motifbased}. In \cite{yi2023contrastive}, the graph prompt tuning technique is applied to cross-domain recommendation scenarios to address the challenges of domain adaptation. Specifically, when applying a pre-trained recommendation model to the target domain, extra prompt nodes are introduced to achieve both efficient and effective domain recommendation. Meanwhile, \citet{yang2023empirical} propose personalized user prompts to bridge the gap between contrastive pretext \cite{wu2021selfsupervised, yu2022are} to downstream recommendation task. They design different kinds of personalized prompts, in combination with pre-trained user embeddings to facilitate dynamic user representations, leading to more accurate and personalized recommending results. In the future, further exploration into the integration of graph prompt tuning within recommender systems can be conducted to enhance recommendation performance, personalization, and adaptability across different domains.

### 中文

电子商务平台提供了利用推荐系统来增强在线服务的宝贵机会。虽然推荐系统的即时调整受到的研究关注有限，但它具有巨大的潜力。在 中，图提示调优技术被应用于跨域推荐场景，以解决域适应的挑战。具体来说，当将预训练的推荐模型应用于目标领域时，引入额外的提示节点以实现高效且有效的领域推荐。同时，提出个性化的用户提示，以弥合对比借口与下游推荐任务之间的差距。他们设计了不同类型的个性化提示，结合预先训练的用户嵌入来促进动态用户表示，从而产生更准确和个性化的推荐结果。未来，可以进一步探索图提示调整在推荐系统中的集成，以增强推荐性能、个性化和跨不同领域的适应性。



---

## 文件：`7.ProG.tex`

### 原文

An indispensable component for fortifying the graph prompting ecosystem is a well-crafted tool. Despite the plethora of tools proposed for generalized graph learning, a notable absence persists in the realm of libraries dedicated to graph prompt functionalities. Addressing this gap, we are introducing \texttt{ProG} (Prompt Graph), an open-source, unified library meticulously designed to cater to the specific needs of graph prompting. This initiative promises to significantly enhance the landscape of graph-based applications by providing a versatile and comprehensive resource for researchers and practitioners alike.

### 中文

强化图形提示生态系统不可或缺的组成部分是精心设计的工具。尽管为广义图形学习提出了过多的工具，但在专用于图形提示功能的库领域仍然明显缺乏。为了解决这一差距，我们推出了 ProG（Prompt Graph），这是一个开源的统一库，经过精心设计，可以满足图形提示的特定需求。该计划有望通过为研究人员和从业者等提供多功能且全面的资源，显着增强基于图的应用程序的前景。

### 原文

The architecture is illustrated in Figure~\ref{fig:prog}. It seamlessly integrates several widely used datasets in the graph prompt evaluation, including Cora, CiteSeer, Reddit,

### 中文

该架构如图 Fig:prog 所示。它在图提示评估中无缝集成了多个广泛使用的数据集，包括 Cora、CiteSeer、Reddit、

### 原文

Amazon,

### 中文

亚马逊，

### 原文

and Pubmed etc.

### 中文

和考研等

### 原文

The tool is equipped with essential evaluation metrics such as Accuracy, F1 Score, and AUC score, commonly employed in various graph prompt-related tasks. Notably, \texttt{ProG} incorporates state-of-the-art methods like All in One~\cite{sun2023all}, GPPT~\cite{sun2022gppt}, GPF~\cite{fang2022prompt}, and GPF-Plus ~\cite{fang2023universal}, and it continues integrating more graph prompt models. In summary, \texttt{ProG} offers the following key features:

### 中文

该工具配备了准确率、F1 分数和 AUC 分数等基本评估指标，这些指标常用于各种图形提示相关的任务。值得注意的是，ProG 结合了 All in One、GPPT、GPF 和 GPF-Plus 等最先进的方法，并且继续集成更多的图形提示模型。总而言之，ProG 提供以下主要功能：

### 原文

For additional information and access to the library, please visit the website of our library\footnote{\url{https://github.com/sheldonresearch/ProG}}. Additionally, we have curated a GitHub repository\footnote{\url{https://github.com/WxxShirley/Awesome-Graph-Prompt}}, serving as a centralized resource for the latest advancements in graph prompt learning. This repository includes a list of research papers, benchmark datasets, and available codes, fostering an environment conducive to ongoing research in this dynamic field. Regular real-time updates ensure that the repository remains current with emerging papers and associated codes.

### 中文

有关更多信息和访问图书馆的信息，请访问我们图书馆的网站\url{https://github.com/sheldonresearch/ProG}。此外，我们还策划了一个 GitHub 存储库\url{https://github.com/WxxShirley/Awesome-Graph-Prompt}，作为图形提示学习最新进展的集中资源。该存储库包括研究论文列表、基准数据集和可用代码，营造了一个有利于这一动态领域持续研究的环境。定期实时更新可确保存储库与新兴论文和相关代码保持同步。



---

## 文件：`8.Discussion.tex`

### 原文

Graph prompt learning has made significant research progress, but it still encounters several challenges. In this subsection, we will discuss current challenges in detail.

### 中文

图提示学习已经取得了重大的研究进展，但仍然遇到了一些挑战。在本小节中，我们将详细讨论当前的挑战。

### 原文

In the NLP field, prompts are typically in a discrete textual format \cite{brown2020language, robinson2023leveraging}, allowing for intuitive understanding, comparison, and explanation. However, existing graph prompts are represented as learnable tokens \cite{sun2022gppt, fang2023universal, fang2022prompt, tan2023virtual, ma2023hetgpt, ge2023enhancing} or augmented graphs \cite{sun2023all, huang2023prodigy}. Such format poses challenges in intuitively understanding and interpreting graph prompts, as they lack a readable design. As a result, the effectiveness of prompts can only be evaluated based on downstream tasks, limiting efficient and comprehensive performance comparison among different kinds of graph prompts. Therefore, the development of a more intuitive graph prompt design with a readable format remains an open problem.

### 中文

在NLP领域，提示通常采用离散的文本格式，可以直观地理解、比较和解释。然而，现有的图形提示被表示为可学习的标记或增强的图形。这种格式给直观理解和解释图形提示带来了挑战，因为它们缺乏可读的设计。因此，只能根据下游任务来评估提示的有效性，限制了不同类型图提示之间的高效、全面的性能比较。因此，开发具有可读格式的更直观的图形提示设计仍然是一个悬而未决的问题。

### 原文

Currently, graph prompt learning is primarily applied to node or graph classification tasks on open-source benchmarks \cite{hamilton2017inductive, xu2018how}. Although potential applications have been discussed in Section \ref{sec:app}, the real-world utilization of graph prompt learning remains limited. A notable example is its use in fraud detection within real-world transaction networks, addressing the issue of label scarcity \cite{wen2023voucher}. However, compared to the widespread application of prompting techniques in the NLP domain \cite{bran2023transformers,  robinson2023leveraging, zhang2023benchmarking}, the potential of graph prompt learning in diverse real-world applications requires further exploration.  Overcoming the main challenges of obtaining powerful domain-specific pre-trained graph models and designing suitable prompts for specific application scenarios that exhibit unique characteristics remains crucial.

### 中文

目前，图提示学习主要应用于开源基准上的节点或图分类任务。尽管在第 sec:app 节中讨论了潜在的应用，但图提示学习的实际应用仍然有限。一个值得注意的例子是它在现实交易网络中的欺诈检测中的应用，解决了标签稀缺的问题。然而，与提示技术在 NLP 领域的广泛应用相比，图提示学习在各种现实世界应用中的潜力还需要进一步探索。克服获得强大的特定领​​域预训练图形模型的主要挑战，并为表现出独特特征的特定应用场景设计合适的提示仍然至关重要。

### 原文

Existing studies on graph prompt learning \cite{liu2023graphprompt, sun2022gppt, gong2023prompt, fang2023universal, fang2022prompt, ge2023enhancing} typically focus on pre-training and prompt tuning using the same dataset, which limits the exploration of more transferable designs and empirical evaluation. Although PRODIGY \cite{huang2023prodigy} explores transferability within the same domain and All in One \cite{sun2023all} provides empirical results regarding transferability across tasks and domains, the investigation of prompt learning across diverse domains and tasks remains limited. Achieving transferability across diverse tasks and domains requires aligning the task space \cite{sun2023all}, semantic features \cite{zhu2023graphcontrol}, and structural patterns \cite{zhao2023graphglow}, which necessitates further theoretical work to provide insights guiding the development of transferable prompt designs.

### 中文

现有的图提示学习研究通常集中于使用相同数据集的预训练和提示调整，这限制了对更多可转移设计和实证评估的探索。尽管 PRODIGY 探索了同一领域内的可迁移性，并且 All in One 提供了有关跨任务和领域的可迁移性的实证结果，但对跨不同领域和任务的即时学习的调查仍然有限。实现跨不同任务和领域的可转移性需要调整任务空间、语义特征和结构模式，这需要进一步的理论工作来提供指导可转移提示设计开发的见解。

### 原文

With the above analysis on graph prompt, we summarize future directions as follows:

### 中文

通过以上对图形提示的分析，我们总结未来的方向如下：

### 原文

to enable intuitive explanations of graph prompts. By gaining insights into the learned prompt vectors and structures, we can enhance our understanding of the underlying mechanisms and improve the interpretability of graph prompts. This, in turn, can lead to more effective utilization of prompts for security- or privacy-related downstream tasks.

### 中文

启用图形提示的直观解释。通过深入了解学习到的提示向量和结构，我们可以增强对底层机制的理解并提高图形提示的可解释性。反过来，这可以更有效地利用安全或隐私相关下游任务的提示。



---

## 文件：`9.Conclusion.tex`

### 原文

In this survey, we explore the promising intersection between Artificial General Intelligence and graph data by graph prompt. Our unified framework has unveiled a structured understanding of graph prompts, dissecting them into tokens, token structures, and inserting patterns. This framework is a novel contribution, providing clarity and comprehensiveness for researchers and practitioners. By exploring the interplay between graph prompts and models, we've revealed fresh insights into the essence of graph prompts, highlighting their pivotal role in reshaping AI for graph data. With the development of ProG, a Python library, and a dedicated website, we've expanded the graph prompting ecosystem, enhancing collaboration and access to research, benchmark datasets, and code implementations. Our survey outlines a roadmap for the future. The challenges and future directions we've discussed serve as a beacon for the evolving field of graph prompting. With the above work, we hope our survey can push forward a new era of insights and applications in AGI family.

### 中文

在本次调查中，我们通过图形提示探索通用人工智能和图形数据之间有希望的交叉点。我们的统一框架揭示了对图形提示的结构化理解，将它们分解为标记、标记结构和插入模式。该框架是一项新颖的贡献，为研究人员和从业者提供了清晰度和全面性。通过探索图形提示和模型之间的相互作用，我们对图形提示的本质提出了新的见解，强调了它们在重塑图形数据人工智能方面的关键作用。随着 ProG、Python 库和专用网站的开发，我们扩展了图形提示生态系统，增强了协作以及对研究、基准数据集和代码实现的访问。我们的调查概述了未来的路线图。我们讨论的挑战和未来方向是不断发展的图形提示领域的灯塔。通过上述工作，我们希望我们的调查能够推动 AGI 家族的见解和应用进入新时代。



---

## 文件：`Ack.tex`

### 原文

The work was supported by grants from the Research Grant Council of the Hong Kong Special Administrative Region, China (Project No. CUHK 14217622), and CUHK Direct Grant No. 4055159. \dotuline{The first author, Dr. Xiangguo Sun, in particular, wants to thank his parents for their kind support during his tough period.}

### 中文

这项工作得到中国香港特别行政区研究资助局的资助（项目编号：CUHK 14217622）和香港中文大学直接资助编号：4055159。第一作者孙祥国博士特别感谢他的父母在他困难时期的鼎力支持。

