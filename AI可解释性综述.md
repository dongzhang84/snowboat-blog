# AI 可解释性综述：我们究竟能不能看懂一个大模型，看懂了又能拿它怎么办

大模型越来越强，但我们对它内部发生了什么，了解得还很少。一个几千亿参数的网络给出一句回答，我们能看到输入和输出，却很难说清中间到底经过了哪些计算。

可解释性（interpretability）研究的，就是这个黑箱。它关心模型说了什么，也关心模型为什么会这么说。这个问题听起来像学术兴趣，实际上已经变成工程、合规和安全问题。

我更关心一个实际问题：如果我们真的看懂了模型，这种理解到底有多真，又能拿来做什么？能调试模型吗，能监控危险行为吗，能直接改模型吗，甚至能反过来指导训练吗？

带着这个问题看，LIME、SHAP、SAE这些方法名只是入口。可解释性更像一条链路，从诊断、监控、干预，一直延伸到训练指导。

# 一、为什么需要可解释性

## 1.1 三种需求：调试、合规和安全

人们想看懂模型，出发点其实不一样，而出发点决定了用什么方法。这是整个领域分裂的根源。

最朴素的动机是工程调试。模型答错了、有偏见、被一个奇怪的输入带跑，工程师要知道问题出在哪里，才有机会修。传统机器学习里的特征重要性、LIME、SHAP、saliency图，很多都服务于这种需求。

第二种动机是信任与合规。银行用模型拒了贷款，医院用模型辅助判断病情，至少要能留下可审计、可申诉的依据。在欧盟AI Act和GDPR相关讨论里，高风险或重大影响的自动化决策会面对更强的透明度要求。这里的"解释权"有适用边界，但方向很清楚，高风险模型不能只给一个分数就结束。

第三种动机是AI安全。模型越强，人们越担心它学会欺骗、谄媚、隐藏真实目标。只看输出很容易被骗，因为模型可以说出漂亮的话。安全研究者因此想看进模型内部，看看某些危险特征有没有出现，某些计算路径有没有被激活。

这三种需求对"好解释"的标准并不一致。工程师要的是能定位bug，监管要的是人能看懂、能追责，安全研究者要的是解释足够忠实，能支持风险判断。很多争论表面上是在争方法，底层其实是在争标准。

## 1.2 模型能力跑在理解前面

Anthropic的CEO Dario Amodei在2025年4月写过一篇文章，标题叫《可解释性的紧迫性》（The Urgency of Interpretability）。他的比喻很直接：将来我们最好能给前沿模型做"脑扫描"，像医生用核磁共振检查病人一样，在模型部署前先看内部有没有危险苗头。

这个时间表未必准确，但问题是真实的。模型能力在快速增长，理解能力没有同步增长。我们正在越来越多地使用一个自己看不太懂的系统，这就是可解释性突然变重要的原因。

## 1.3 先把边界说清楚

可解释性的第一步是看懂模型，不是直接限制模型。顺序不能反。只有先弄清模型内部到底在算什么，后面才谈得上监控、干预和管控。

在小模型和孤立任务上，我们已经能做到相当扎实的理解。归纳头、模运算电路这类例子，研究者不只是给出一个说法，还能用因果实验验证它。到了前沿大模型，情况就完全不同了。我们能提取一些特征，追出几条电路，但相对于整个模型，这仍然只是给黑箱开了几扇小窗。

更危险的情况是假装看懂。一个解释可以写得很顺，图也画得很漂亮，但如果它没有对应模型真实的计算过程，它反而会让人放松警惕。所以后面讲任何方法，都要先问忠实性：一个解释先要是真的，然后才谈得上好不好懂。

这个领域的难点也在这里。模型内部表示本来就不是给人类阅读用的，解释又很难被彻底证伪，研究对象还在快速迭代。所以可解释性不是多招几个人、多买几张卡就能立刻解决的问题。它的困难来自问题本身。

# 二、可解释性到底有什么用

## 2.1 真理解和假理解

可解释性最容易被讲虚，因为"理解"这个词太好用了。一个解释写得顺，图画得漂亮，读者很容易以为模型已经被看懂了。真正要问的是：这个解释有没有碰到模型真实的计算过程？

在小模型、孤立任务上，答案是肯定的。前面提到的归纳头（induction head）就是一个被完整逆向的例子，研究者能说清它由哪几个注意力头组合而成、在算什么。模运算电路是另一个例子，Neel Nanda等人在2023年把一个小transformer学会模加法的算法完整拆了出来，连它偷偷用了傅里叶变换都查清楚了。这些是真懂，而且能用因果实验验证。

在前沿大模型整体上，答案是远未做到。我们能在Claude这样的模型里提取出几百万个可解释的特征，能追出几条电路，但相对于整个模型的运作，这仍然是在一面巨墙上开了几扇小窗。说"我们理解了大模型"是夸大。

## 2.2 从诊断到安全保证

理解还要分层。最低一层是诊断，看懂模型为什么错、哪里有偏差，但不直接改模型。比如查清一个信贷模型是不是在偷偷依赖邮编这种代理变量，这是工业界早就在做的事。

再往上一层是监控。在模型运行时盯着内部特征，看"欺骗""谄媚""恶意"这类方向有没有亮起来。这个层级相当于给模型装仪表盘，研究上已经有进展，也出现了一些早期系统探索，但还谈不上生产标准。

第三层是编辑与干预。ROME、MEMIT这类模型编辑方法，可以定位并改写模型里的某条事实。Anthropic的金门大桥实验则更像一个极端演示：把Claude 3 Sonnet里的"金门大桥"特征人为放大，模型聊什么都会绕回金门大桥。

更高一层是指导训练。理想情况是，研究者发现某个坏机制后，可以改数据、改训练目标，甚至把"内部不该出现某种特征"写进训练流程。今天主流大模型的训练还基本靠数据、算力、规模定律和工程经验，可解释性还没有真正成为训练方向盘。

最高一层是安全保证。目标是在部署前从模型内部发现高风险倾向，并显著降低它做出危险行为的概率。至于从数学上证明"模型不会做某一类危险的事"，现在基本还看不到路径。

# 三、什么叫"解释"，以及术语之乱

## 3.1 几个词为什么总是混用

这个领域有一个让新人头疼的问题，几个核心词没有公认定义，还经常被换着用。interpretability、explainability、XAI、transparency，不同论文给的含义能差出十万八千里。

Zachary Lipton在2016年那篇《模型可解释性的迷思》（The Mythos of Model Interpretability）里就专门论证过，"可解释性"这个词含义滑动，各篇论文动机各异，常常不加定义就当成公理来用。读综述时如果觉得不同来源对不上，很可能是因为大家压根说的不是一回事。

我在这篇里取一个相对窄的口径：聚焦于理解模型内部的机制与决策依据。公平性、隐私、鲁棒性这些相邻话题不展开。

## 3.2 事后、内在、局部、全局

理清方法，可以先看两条轴。第一条轴是事后解释还是内在解释。事后解释（post-hoc）是先有一个训练好的黑箱，再想办法解释它，LIME、SHAP、saliency都属于这一类。内在解释（intrinsic）则是模型本身结构就透明，看模型就能看解释，线性回归、逻辑回归、决策树都在这边。

第二条轴是局部还是全局。局部解释针对单个预测，"模型为什么把这一张图判成猫"。全局解释针对整个模型，"模型整体上靠哪些特征做判断"。

把这两条轴交叉，就能给市面上几乎所有方法画一张分类地图。一个方法是"事后、局部"的，还是"内在、全局"的，位置一摆，性质就清楚一半。

还有一个更关键的概念，叫"解释的单位"。早期方法解释的是输入特征，关注"这张图的哪些像素重要""这条记录的哪个字段重要"。到了大模型，解释对象开始转向内部表示和电路，也就是"模型内部哪个特征、哪条回路在起作用"。

## 3.3 忠实性比顺耳更重要

忠实性（faithfulness）说的是，这个解释有没有真实反映模型实际的计算过程。可信度或者说可读性（plausibility）说的是，这个解释在人看来可不可信、有没有说服力。Jacovi和Goldberg在2020年那篇ACL论文里把这对概念区分得很清楚，现在已经是NLP可解释性评估的基础框架。

关键在于，这两者可以彻底背离。一个解释可以非常可信、读起来头头是道，却跟模型真正的运作毫无关系。

一个看起来合理的解释会让你停止怀疑。如果它恰好不忠实，你就被它骗了，还浑然不觉。一个明显粗糙的解释反而会让你保持警惕。

最有力的反面证据来自Adebayo等人2018年的《Saliency图的理智检查》（Sanity Checks for Saliency Maps）。他们做了个很狠的实验，把训练好的模型权重逐层随机化，理论上这个模型已经废了，它的解释也该跟着崩。结果某些saliency方法画出来的热力图几乎纹丝不动。这说明那些热力图根本没在反映模型学到的东西，更像是在做边缘检测，谁看了都觉得"嗯有道理"，其实跟模型无关。

这个实验给了一条很实用的判断标准：如果模型本身已经变了，解释却几乎不变，那这个解释大概率没有抓住模型真正学到的东西。后面看任何方法，都要先问这一点。

# 四、经典方法：透明模型、LIME、SHAP 和 saliency

## 4.1 最干净的解释：直接用透明模型

机制可解释性很热闹，但经典派仍然是工业界最常用的一类工具。这套方法更成熟，也更贴近日常模型调试和合规审计。

最干净的可解释性，是一开始就用结构透明的模型。线性回归和逻辑回归，每个特征一个系数，系数多大、正负如何，一目了然。决策树，每个判断是一条能读出来的规则。

广义可加模型（GAM）是这一类里更强的一档，它允许每个特征对结果有非线性的影响，但各特征的影响仍然是分开、可画成曲线的，所以照样可读。微软InterpretML里的EBM（Explainable Boosting Machine）是这条线的现代代表，本质是带自动交互检测的、基于树的GAM，谱系可以上溯到Lou等人2013年的GA2M工作。在很多结构化数据任务上，这类模型精度并不输给黑箱，却天生可读。

## 4.2 给黑箱做事后归因

但现实里大量模型就是黑箱，于是有了一批事后归因方法，专门给"已经训练好的黑箱"找解释。

置换重要性（permutation importance）最朴素，把某个特征的取值打乱，看模型精度掉多少，掉得越多说明这个特征越重要。它最早是Breiman在2001年随机森林那篇论文里提出的，绑定袋外样本，后来才被推广成模型无关的通用版本。

LIME由Ribeiro等人在2016年的KDD上提出，思路是在你关心的那个样本附近采一堆点，用一个简单的线性模型去局部近似那个黑箱，于是你得到一个"在这一带，哪些特征推高了、哪些压低了预测"的局部解释。

SHAP由Lundberg和Lee在2017年的NeurIPS上提出，它的底子是博弈论里的Shapley值。Shapley值是Lloyd Shapley 1953年为合作博弈设计的分配方案，思路是把每个"玩家"在所有可能联盟里的平均边际贡献算出来。SHAP把这套搬到特征归因上，每个特征分到一份"贡献额"。这里有个常被搞错的点，Shapley值的精确计算是指数级复杂度，SHAP（比如KernelSHAP、TreeSHAP）是它的高效近似，不等于精确的Shapley值。

saliency一类则是给神经网络、尤其是图像模型用的，靠梯度告诉你输入的哪些部分对输出影响大。最早是Simonyan等人2013年的工作，后来有Grad-CAM（ICCV 2017），还有Sundararajan等人在ICML 2017提出的积分梯度，论文题目其实叫《深度网络的公理化归因》（Axiomatic Attribution for Deep Networks），它沿着一条从基线到输入的路径把梯度积起来，满足几条好性质。

## 4.3 高风险场景里的反黑箱立场

Cynthia Rudin在2019年《自然·机器智能》上发过一篇态度很硬的文章，标题直接就是《别再为高风险决策解释黑箱模型了，请直接用可解释的模型》。

她的核心论点是，在医疗、刑事司法这类高风险场景，给黑箱套一个事后解释是危险的，因为事后解释经常对黑箱不忠实，会把坏做法包装得很体面。而且很多场景下，结构透明的模型精度并不比黑箱差。与其费劲解释一个黑箱，不如一开始就别用黑箱。

这个立场跟机制可解释性的取向几乎相反，值得记住。它提醒我们，"可解释性"有时既是一种技术，也是一种建模选择。高风险场景里，如果透明模型已经够好，直接使用透明模型往往比事后解释一个黑箱更稳。

# 五、大模型之后，解释单位变了

## 5.1 输入特征解释不够用了

经典派在结构化数据、传统图像任务上很好用。放到大语言模型上，它开始失效。高维、强非线性是一方面，更根本的问题是解释单位变了。

设想你问模型一个问题，它生成了一段回答。saliency告诉你"输入里第47个token最重要"。这等于没说。语言的意义不在单个token上，模型真正在做的计算发生在几十层网络的内部，输入层那点信息量根本承载不了解释。

于是注意力从"看外面"转向了"看里面"。对大模型来说，值得解释的对象是内部的表示和回路，是模型把一个概念存在哪个方向上、用哪几个注意力头把信息搬来搬去。

这个转向是被问题逼出来的。输入层的解释单位失效以后，想看懂大模型，就只能进入模型内部。这就是机制可解释性登场的逻辑起点。

## 5.2 神经元为什么读不出来

最自然的想法是一个神经元一个神经元地看，搞清每个神经元代表什么。这条路走不通，因为神经元是多义的（polysemantic）。同一个神经元会在"猫""法律文书""日语""某种代码模式"等一堆毫不相干的输入上激活。你盯着它看，根本读不出一个干净的含义。

为什么会多义？Anthropic 2022年的《叠加的玩具模型》（Toy Models of Superposition）给了一个漂亮的解释，叫叠加（superposition）。

打个比方。假设你只有十个灯泡，却想表示几百种状态。你不会一个灯泡只管一种状态，那样只能表示十种。你会用灯泡的组合，亮一三五是一个意思，亮二四是另一个意思。模型也一样，它要表示的概念（特征）远多于它有的神经元，于是它把多个特征压进同一组方向，用组合来区分。代价就是单个神经元变得多义，没法单独读。

叠加的关键含义是，多义并不代表模型偷懒，恰恰说明它在用一种高效策略，在有限维度里塞下尽可能多的信息。这也预示了后面一个麻烦结论，叠加可能来自模型表示本身，未必能被简单消掉。

# 六、机制可解释性：特征、电路和因果干预

## 6.1 从线性表示到 SAE

既然单个神经元读不出来，那概念到底藏在哪？一个有影响力的猜想叫线性表示假设，认为概念是激活空间里的一个方向，而不是某个单独的神经元。沿着这个方向走，模型对某个概念的"信号"就增强。早期直觉来自word2vec那个著名的"国王减男人加女人约等于女王"。

要强调，这是假设，不是定理。已经有反例，比如Engels等人2024年发现"星期几""月份"这类概念在模型里是绕成一个圈的非线性结构。所以稳妥的说法是，线性表示在经验上大量成立，但有已知的例外。

如果概念是叠加在一起的方向，能不能用某种工具把它们重新摊成一个个干净的、单义的特征？稀疏自编码器（SAE）就是干这个的。

SAE的思路是训练一个又宽又稀疏的网络，去重建模型某一层的激活，强迫每次只点亮极少数单元。理想情况下，这样学出来的每个单元，往往对应一个人能读懂的概念。Anthropic 2023年的《迈向单义性》（Towards Monosemanticity）在一个单层模型上用这招提取出约四千多个可解释特征。2024年5月的《扩展单义性》（Scaling Monosemanticity）把它放大到了生产级模型Claude 3 Sonnet的中间层，提取出多达约三千四百万个特征，涵盖具体事物、抽象概念、多语言和多模态。

SAE之外还有变体，比如transcoder（转码器）。SAE是给某一层拍快照，看这一层有哪些特征。transcoder更进一步，用一个又宽又稀疏的结构去近似替代一个稠密的MLP层，于是它能告诉你哪些输入特征导致了哪些输出特征，暴露的是变换本身。跨层版本（CLT）能从某层读、向后面多层写，也是归因图的底层组件。

## 6.2 从特征到电路

有了干净的特征，下一步是看它们怎么连起来算东西，这就是电路（circuit）。

归纳头是最经典的一个电路。Anthropic 2021年的《transformer电路的数学框架》第一次在一个两层小模型里识别出它，由"前一个token头"和"归纳头"两个不同层的注意力头组合而成。它干的事很简单，看到序列里某个token上次出现后面跟了什么，这次就预测同样的东西，完成 [A][B]...[A] 后面接 [B]。2022年的后续论文进一步论证，这类电路可能是上下文学习的重要机制之一，而且它在训练中会在某一阶段突然形成。小模型里的证据更强，放到前沿大模型上，还更接近一个有力假设。

模运算电路是另一个被完整逆向的例子，前面提过，Nanda等人2023年发现小模型学模加法时，内部其实在用傅里叶变换加三角恒等式，把加法变成了圆上的旋转。需要分清，这是"模加法"，跟大模型做普通两位数加法是两回事，后者Claude用的是"先估个大概、再精确算末位"的并行启发式，是另一项工作里的发现。

到了2025年，Anthropic的电路追踪（circuit tracing）和《一个大语言模型的生物学》两篇配套工作，用跨层转码器构造出归因图（attribution graph），把信息怎么从输入流经中间特征到输出画成一张可读的计算图，研究对象是Claude 3.5 Haiku。

## 6.3 高层结构和因果干预

机制可解释性还摸到了一些让人意外的高层结构。

写诗时的提前规划是一个。在《生物学》那篇里，研究者发现模型写押韵的诗时，会在写出一整行之前就先在行首激活好候选的韵脚词，再倒着把这一行凑出来，让它自然落到那个韵脚上。研究者人为把"计划好的韵脚词"换掉，模型会重新组织整行去配合。这反驳了"模型只是逐字即兴、毫无前瞻"的直觉。

人格向量（persona vector）是另一个。Anthropic 2025年的工作识别出控制某种性格倾向的方向，比如谄媚、恶意、爱编造，可以用来监控甚至在训练时预防这些坏特质。

还有内省（introspection）。Anthropic 2025年做了个有意思的实验，把某个概念的方向直接注入模型内部，再问它有没有察觉到"脑子里被塞了个想法"。在特定实验设置下，Claude Opus 4和4.1大约有两成案例能识别出被注入的概念方向。这件事要非常克制地讲，成功率不高、范围很窄，不能泛化成"模型有可靠内省能力"，Anthropic也明确说这不代表模型有意识。

前面这些发现都有一个共同的风险，会不会只是相关、不是因果？区分的办法是干预。

激活修补（activation patching）是核心手段，把模型某些内部激活换成另一次运行的对应激活，看输出怎么变，从而判断这个组件到底有没有因果作用。这一类做法里有个更具体的叫因果追踪（causal tracing），由ROME那篇工作推广开来。

金门大桥实验是最出圈的因果演示。配合2024年5月的《扩展单义性》，Anthropic从Claude 3 Sonnet里找到"金门大桥"这个特征，把它的强度人为调到很高，做出一个叫"金门大桥Claude"的演示模型，短暂对公众开放过大约一天。被放大之后，模型聊什么话题都会扯到金门大桥上去。这是忠实性的一个范例，因为它证明了那个特征确实在因果上控制着模型的行为，不是事后编的故事。要注意，金门大桥是SAE提取的一个特征方向，不是某个单独的"金门大桥神经元"。

把这些成果放回第二章那条链路里看，机制可解释性目前最稳的地方还是诊断和监控。它能帮我们看见模型内部发生了什么，也能让我们盯住某些危险特征。编辑干预已经有金门大桥这样的演示，但距离可靠生产手段还很远。至于指导训练和安全保证，现在更多是方向感，还没有变成成熟工程能力。

# 七、中间方法、评估和落地

## 7.1 探针和注意力

经典归因派和机制可解释性之间，还有一片中间地带。这些方法不一定能把模型内部机制完整逆向出来，但它们能帮助研究者判断某个信息是否存在、某个组件是否可能参与了计算。

探针（probing）是个常用手段。冻住模型，取某一层的激活，在上面训练一个简单的线性分类器，看能不能从这层激活里读出某个概念，比如词性、句法、情感。读得出来，就说明这层"编码"了这个信息。源头常引Alain和Bengio 2016年的工作。

探针有个绕不开的争议，能解码不等于模型真的用了。你能从某层读出一个信息，只说明信息在场，不代表模型在推理时因果地用了它。而且探针越强，越可能是探针自己算出来的，而不是模型里真有这个结构。Hewitt和Liang 2019年用"控制任务"的设计专门敲打过这一点。这也是为什么后来大家越来越倚重因果类方法。

还有一个经典争论，关于注意力权重能不能当解释。一个很自然的想法是，注意力告诉你模型"在看哪里"，那不就是解释吗？

Jain和Wallace 2019年的《注意力不是解释》（NAACL）泼了盆冷水，他们能构造出跟原本差异很大、却产生相同预测的注意力分布，说明注意力权重不能可靠地当解释。同年Wiegreffe和Pinter的《注意力不是"不是解释"》（EMNLP）又反驳回去，关键看你怎么定义解释，注意力提供的是一种解释，不是唯一的解释，存在不等于排他。这场来回很能说明这个领域的特点，一个看着天经地义的指标，深究下去全是坑。这里也藏着一条忠实性的教训，权重大不等于重要。

## 7.2 怎么评估一个解释

一个解释好不好，至少要从几个维度量。忠实性，它有没有真实反映模型，这是最硬的一条，前面sanity check那套就是干这个。稳定性，输入微小扰动时解释会不会乱跳。可读性，人看了觉不觉得有用，这条通常得靠人来评。

难点在于，这几个维度经常打架。最忠实的解释未必最好读，最好读的解释（回想第四章）恰恰可能最不忠实。

老实说，目前没有一个像ImageNet那样被广泛公认的统一基准。评估高度碎片化，各家方法各用各的指标。有一些因果类的评测和针对特定任务的基准（比如电路定位的共享任务），但还谈不上全领域共识。这种"连怎么算成功都没共识"的状态，本身就是这个领域难做的一个症状。

自动化可解释性是个很有诱惑力的方向。OpenAI 2023年5月做过一件事，用GPT-4给GPT-2的每个神经元自动写解释，再让GPT-4根据这个解释去预测神经元什么时候激活，用预测和真实激活的吻合度给解释打分。

这件事的局限OpenAI自己也讲得很清楚。GPT-4写的解释还远不如人，大多数神经元压根没法被简洁解释（又回到多义性），得高分的解释占比很低。更深的悖论在于，你用一个你并不理解的模型去解释另一个模型，那个解释者本身又由谁来解释？这个循环目前没有出口。

## 7.3 已经落地到哪一步

诊断与数据偏差发现，是落地最实的一块，对应阶梯第一级。查清模型是不是在依赖某个不该依赖的代理变量、训练数据里有没有泄漏，这类工作工业界一直在做。

安全监控对应第二级，开始有真实的研究和早期产品。盯着模型运行时内部的谄媚、幻觉、欺骗相关特征有没有亮起来，给模型装仪表盘，这条线随着人格向量这类工作正在往前走。

模型编辑对应第三级。ROME、MEMIT这类工作能直接定位并改写模型里的某条事实，不用重训。这在研究里可行，但还没成为生产标配，改一处会不会带坏别处，仍是没完全解决的问题。

对齐审计和合规对应阶梯更高处。用可解释性去审一个新模型、决定能不能部署，目前还多是愿景和零星尝试。

把这些落地场景串起来，会发现一个容易被误解的顺序。可解释性先解决理解问题，然后才有可能服务于管控。直接把可解释性等同于管控，会把因果关系倒过来。理解是因，管控是果。

# 八、为什么这件事难，以及谁在做

## 8.1 难在验证，也难在模型本身

可解释性的难，首先难在验证。你几乎无法证明一个解释为真，最多只能找到自洽的旁证，很难真正证伪它。一个解释听起来很顺，各种例子也对得上，但你仍然说不清它是真的抓住了模型机制，还是又编了一个好故事。付出巨大，却拿不到确定性，这是最折磨人的地方。

这个问题还会带出另一个麻烦：成功标准很难统一。"我理解了一个电路"算不算进展？算多大进展？如果一个解释能解释小模型里的一个机制，但不能推广到前沿大模型，它的价值该怎么评估？这些问题没有统一答案，也让这个领域很难像图像识别那样靠一个公认榜单往前推。

第二个难点来自模型本身。模型组织信息的方式，本来就不是给人类阅读用的。叠加、多义、压缩，都是它在有限参数里塞下更多能力的办法。SAE这类工具能把叠加摊开一些，但只要模型继续追求能力和效率，这个问题就很难彻底消失。

## 8.2 难在迭代、规模和算力

第三个难点是研究对象一直在变。研究者刚把一个模型的某个机制摸清楚，新一代模型可能已经换了架构、规模和训练方法。可解释性研究天然面对一个移动靶，而且这个靶跑得很快。

第四个难点是规模和算力。最值得研究的是前沿大模型，但在它们身上做精细机制分析非常贵，而且通常需要接触模型权重。学术界更容易研究小模型、开源模型，可小模型上的发现又会被追问能不能推广到前沿模型。

还有一层不太光鲜的现实：这类研究很耗人。大量工作要靠研究者人工看特征、手动标注、反复设计干预实验。前沿成果展示出来的图很漂亮，背后往往是大量不知道能不能出结果的体力活。自动化解释当然是方向，但自动化本身又卡在忠实性和可信度上。

## 8.3 谁在做，为什么还值得做

这些困难解释了为什么这个领域的分工很特别。经典归因派主要在学术界和工业应用一线，服务于调试、合规这些扎实需求，低调但量大。机制可解释性这边，Anthropic声量最大，前面引的很多工作都来自它的可解释性团队。但远不止它，Google DeepMind有Neel Nanda带的机制可解释性团队，OpenAI做过自动化解释，学术界和独立开源社区也围绕SAE、电路分析形成了一个活跃圈子。

算力决定了分工。在前沿大模型上做机制分析，需要权重、基础设施和大量实验资源，工业界实验室天然占优。学术界更多在小模型、开源模型上做方法创新和原理验证。这种分工没有谁规定，是资源分布自然推出来的。

这也是为什么可解释性还值得做。它今天工具粗糙、结论零散、共识不足，但研究对象足够根本。如果未来真能把诊断、监控、干预、训练指导连起来，它就会变成部署强模型之前的基础检查能力。

## 8.4 还没解决的几个问题

最直接的问题是能不能扩展到前沿大模型。今天很多漂亮成果来自中小模型、单个机制或受控任务，整模型级别的理解还看不到清晰路径。

叠加到底能不能真正解决，也还没有答案。SAE能把一部分叠加摊开，但如果叠加本身就是模型高效表示能力的一部分，那它可能只能被缓解，很难被彻底消灭。

自动化解释也卡在这里。只要解释主要靠人看，规模就上不去。可如果用一个我们还不完全理解的模型去解释另一个模型，又会回到"谁来解释解释者"的问题。

还有一个更底层的问题：忠实性能不能被证明。今天我们更多是在找旁证，用干预、消融、对照实验提高可信度。要想严格证明一个解释为真，目前还看不到通用办法。

可解释性和神经科学有一个相似处：两者都在逆向一个没有说明书的复杂系统。神经科学几十年积累下来的经验，哪些能借过来，哪些借不过来，这也是一个开放问题。这个类比不能过度使用，但它能提醒我们，理解复杂系统往往是一个长期、缓慢、工具驱动的过程。

# 九、结论

可解释性这件事，最容易被讲得太神。它不是给模型套一层漂亮解释，也不是给监管写一段能交差的话。它真正要解决的问题很朴素：我们正在把越来越多决定交给一个黑箱，而这个黑箱内部到底怎么工作，我们还没有真正看清。

所以第一步永远是看懂。看懂之后，才谈得上诊断错误、监控风险、干预行为，甚至反过来影响训练。顺序不能反过来。如果连模型真实的计算过程都没有碰到，后面所有"解释""审计""安全保证"都只是包装。

这也是为什么忠实性这么重要。一个解释可以很顺耳，也可以很漂亮，但它必须先是真的。Adebayo那类sanity check提醒我们的，就是不要被"看起来合理"骗了。可解释性最怕的是假答案，一个假的答案会让人以为自己已经懂了。

今天这个领域最稳的部分，仍然在诊断和监控。干预已经有金门大桥Claude这样的演示，但还不是可靠生产工具。指导训练和安全保证更远，很多时候仍然停在研究愿景上。可解释性的价值，就取决于这条链路能不能一步步接起来。

我对这个方向保持乐观，但这种乐观不能脱离现实。它不会自动让模型安全，也不会自动给监管答案。它真正的意义，是把"盲用黑箱"往后推一点，把理解、验证和干预往前推一点。只要模型能力继续跑在我们的理解前面，这件事就会一直重要。

# 作者其它文章（选）

- [AI for Science 详细介绍（上）：范式与版图](https://github.com/dongzhang84/snowboat-blog/blob/main/AI%20for%20Science%20%E8%AF%A6%E7%BB%86%E4%BB%8B%E7%BB%8D%EF%BC%88%E4%B8%8A%EF%BC%89%EF%BC%9A%E8%8C%83%E5%BC%8F%E4%B8%8E%E7%89%88%E5%9B%BE.md)
- [广义祖父积分学](https://github.com/dongzhang84/snowboat-blog/blob/main/%E5%B9%BF%E4%B9%89%E7%A5%96%E7%88%B6%E7%A7%AF%E5%88%86%E5%AD%A6.md)
- [什么是"涌现"？涌现的研究史](https://github.com/dongzhang84/snowboat-blog/blob/main/%E4%BB%80%E4%B9%88%E6%98%AF%E2%80%9D%E6%B6%8C%E7%8E%B0%E2%80%9C%EF%BC%9F%E6%B6%8C%E7%8E%B0%E7%9A%84%E7%A0%94%E7%A9%B6%E5%8F%B2.md)
- [互联网泡沫简史](https://github.com/dongzhang84/snowboat-blog/blob/main/%E7%AE%80%E6%98%8E%E4%BA%92%E8%81%94%E7%BD%91%E6%B3%A1%E6%B2%AB%E5%8F%B2.md)
- [AI 圈大 V 名单](https://github.com/dongzhang84/snowboat-blog/blob/main/AI%E5%9C%88%E5%A4%A7V%E5%90%8D%E5%8D%95%EF%BC%88%E6%8E%A8%E7%89%B9%E7%89%88%EF%BC%89.md)
- [我打造的个人 AI 系统：哲学基础](https://github.com/dongzhang84/snowboat-blog/blob/main/%E5%BB%BA%E8%AE%BE%E4%B8%AA%E4%BA%BAAI%E7%B3%BB%E7%BB%9F%E7%9A%84%E5%93%B2%E5%AD%A6%E5%9F%BA%E7%A1%80.md)
- [NFT 的叙事是如何崩塌的](https://github.com/dongzhang84/snowboat-blog/blob/main/NFT%E7%9A%84%E5%8F%99%E4%BA%8B%E6%98%AF%E5%A6%82%E4%BD%95%E5%B4%A9%E5%A1%8C%E7%9A%84.md)
- [什么是耗散结构理论？它和 AI 有关系吗？](https://github.com/dongzhang84/snowboat-blog/blob/main/%E4%BB%80%E4%B9%88%E6%98%AF%E8%80%97%E6%95%A3%E7%BB%93%E6%9E%84%E7%90%86%E8%AE%BA%EF%BC%9F%E5%AE%83%E5%92%8CAI%E6%9C%89%E5%85%B3%E7%B3%BB%E5%90%97%EF%BC%9F.md)
- [什么是具身智能？它跟 AI 的关系是什么？](https://github.com/dongzhang84/snowboat-blog/blob/main/%E4%BB%80%E4%B9%88%E6%98%AF%E5%85%B7%E8%BA%AB%E6%99%BA%E8%83%BD%EF%BC%9F%E5%AE%83%E8%B7%9F%20AI%20%E7%9A%84%E5%85%B3%E7%B3%BB%E6%98%AF%E4%BB%80%E4%B9%88%EF%BC%9F.md)
- [长篇分析：SpaceX 未来的展望](https://github.com/dongzhang84/snowboat-blog/blob/main/archive/%E9%95%BF%E7%AF%87%E5%88%86%E6%9E%90%EF%BC%9ASpaceX%E6%9C%AA%E6%9D%A5%E7%9A%84%E5%B1%95%E6%9C%9B.md)
- [一篇文章讲清楚美国的移民系统](https://github.com/dongzhang84/snowboat-blog/blob/main/archive/%E4%B8%80%E7%AF%87%E6%96%87%E7%AB%A0%E8%AE%B2%E6%B8%85%E6%A5%9A%E7%BE%8E%E5%9B%BD%E7%9A%84%E7%A7%BB%E6%B0%91%E7%B3%BB%E7%BB%9F.md)
- [一文讲清楚美国医疗系统](https://github.com/dongzhang84/snowboat-blog/blob/main/archive/%E4%B8%80%E6%96%87%E8%AE%B2%E6%B8%85%E6%A5%9A%E7%BE%8E%E5%9B%BD%E5%8C%BB%E7%96%97%E7%B3%BB%E7%BB%9F.md)
- [细说美国的华人老钱家族](https://github.com/dongzhang84/snowboat-blog/blob/main/%E7%BB%86%E8%AF%B4%E7%BE%8E%E5%9B%BD%E7%9A%84%E5%8D%8E%E4%BA%BA%E8%80%81%E9%92%B1%E5%AE%B6%E6%97%8F.md)
- [美国的犹太人和华人分别抢到了什么资源？](https://github.com/dongzhang84/snowboat-blog/blob/main/archive/%E7%BE%8E%E5%9B%BD%E7%9A%84%E7%8A%B9%E5%A4%AA%E4%BA%BA%E5%92%8C%E5%8D%8E%E4%BA%BA%E5%88%86%E5%88%AB%E6%8A%A2%E5%88%B0%E4%BA%86%E4%BB%80%E4%B9%88%E8%B5%84%E6%BA%90%EF%BC%9F%E8%AF%A6%E7%BB%86%E5%88%86%E6%9E%90.md)
- [一篇文章看懂美国教育全生态](https://github.com/dongzhang84/snowboat-blog/blob/main/archive/%E4%B8%80%E7%AF%87%E6%96%87%E7%AB%A0%E7%9C%8B%E6%87%82%E7%BE%8E%E5%9B%BD%E6%95%99%E8%82%B2%E5%85%A8%E7%94%9F%E6%80%81.md)
- [什么是控制论？控制论是 AI 的上辈子吗？](https://github.com/dongzhang84/snowboat-blog/blob/main/archive/%E4%BB%80%E4%B9%88%E6%98%AF%E6%8E%A7%E5%88%B6%E8%AE%BA%EF%BC%9F%E6%8E%A7%E5%88%B6%E8%AE%BA%E6%98%AFAI%E7%9A%84%E4%B8%8A%E8%BE%88%E5%AD%90%E5%90%97%EF%BC%9F.md)
- [祖父积分学概论](https://github.com/dongzhang84/snowboat-blog/blob/main/archive/%E7%A5%96%E7%88%B6%E7%A7%AF%E5%88%86%E5%AD%A6%E6%A6%82%E8%AE%BA.md)
- [教宗良十四世论人工智能（精华版）](https://github.com/dongzhang84/snowboat-blog/blob/main/archive/%E6%95%99%E5%AE%97%E8%89%AF%E5%8D%81%E5%9B%9B%E4%B8%96%E8%AE%BA%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%EF%BC%88%E7%B2%BE%E5%8D%8E%E7%89%88%EF%BC%89.md)
- [Vibe Reading：AI 时代读书的系统化方法](https://github.com/dongzhang84/snowboat-blog/blob/main/archive/Vibe%20Reading%EF%BC%9AAI%20%E6%97%B6%E4%BB%A3%E8%AF%BB%E4%B9%A6%E7%9A%84%E7%B3%BB%E7%BB%9F%E5%8C%96%E6%96%B9%E6%B3%95.md)
- [美国税收制度完全指南](https://github.com/dongzhang84/snowboat-blog/blob/main/archive/%E7%BE%8E%E5%9B%BD%E7%A8%8E%E6%94%B6%E5%88%B6%E5%BA%A6%E5%AE%8C%E5%85%A8%E6%8C%87%E5%8D%97.md)

# 本文参考文献

- Lipton, Z. C. (2016/2018). [The Mythos of Model Interpretability](https://arxiv.org/abs/1606.03490). arXiv:1606.03490 / ACM Queue.
- Amodei, D. (2025). [The Urgency of Interpretability](https://www.darioamodei.com/post/the-urgency-of-interpretability).
- Jacovi, A., & Goldberg, Y. (2020). [Towards Faithfully Interpretable NLP Systems](https://arxiv.org/abs/2004.03685). ACL 2020.
- Adebayo, J., et al. (2018). [Sanity Checks for Saliency Maps](https://papers.nips.cc/paper/8160-sanity-checks-for-saliency-maps). NeurIPS 2018.
- Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). ["Why Should I Trust You?": Explaining the Predictions of Any Classifier](https://arxiv.org/abs/1602.04938). KDD 2016.
- Lundberg, S. M., & Lee, S.-I. (2017). [A Unified Approach to Interpreting Model Predictions](https://arxiv.org/abs/1705.07874). NeurIPS 2017.
- Shapley, L. S. (1953). A Value for n-Person Games. Contributions to the Theory of Games II.
- Breiman, L. (2001). Random Forests. Machine Learning, 45(1).
- Simonyan, K., Vedaldi, A., & Zisserman, A. (2013). [Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps](https://arxiv.org/abs/1312.6034). arXiv:1312.6034.
- Sundararajan, M., Taly, A., & Yan, Q. (2017). [Axiomatic Attribution for Deep Networks](https://arxiv.org/abs/1703.01365). ICML 2017.
- Selvaraju, R. R., et al. (2017). [Grad-CAM](https://arxiv.org/abs/1610.02391). ICCV 2017.
- Rudin, C. (2019). [Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead](https://www.nature.com/articles/s42256-019-0048-x). Nature Machine Intelligence.
- Nori, H., et al. (2019). [InterpretML: A Unified Framework for Machine Learning Interpretability](https://arxiv.org/abs/1909.09223). arXiv:1909.09223.
- Lou, Y., et al. (2013). Accurate Intelligible Models with Pairwise Interactions (GA2M). KDD 2013.
- Elhage, N., et al. (2021). [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html). Anthropic.
- Olsson, C., et al. (2022). [In-context Learning and Induction Heads](https://www.anthropic.com/news/in-context-learning-and-induction-heads). Anthropic.
- Elhage, N., et al. (2022). [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html). Anthropic.
- Nanda, N., et al. (2023). [Progress Measures for Grokking via Mechanistic Interpretability](https://arxiv.org/abs/2301.05217). ICLR 2023.
- Bricken, T., et al. (2023). [Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](https://transformer-circuits.pub/2023/monosemantic-features/index.html). Anthropic.
- Templeton, A., et al. (2024). [Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html). Anthropic.
- Anthropic (2024). [Golden Gate Claude](https://www.anthropic.com/news/golden-gate-claude).
- Lindsey, J., et al. (2025). [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) / [Circuit Tracing](https://transformer-circuits.pub/2025/attribution-graphs/methods.html). Anthropic.
- Anthropic (2025). [Persona Vectors](https://www.anthropic.com/research/persona-vectors).
- Anthropic (2025). [Emergent Introspective Awareness in Large Language Models](https://www.anthropic.com/research/introspection).
- Engels, J., et al. (2024). [Not All Language Model Features Are Linear](https://arxiv.org/abs/2405.14860). arXiv:2405.14860.
- Meng, K., et al. (2022). [Locating and Editing Factual Associations in GPT (ROME)](https://arxiv.org/abs/2202.05262). NeurIPS 2022.
- Meng, K., et al. (2023). [Mass-Editing Memory in a Transformer (MEMIT)](https://arxiv.org/abs/2210.07229). ICLR 2023.
- Alain, G., & Bengio, Y. (2016). [Understanding Intermediate Layers Using Linear Classifier Probes](https://arxiv.org/abs/1610.01644). arXiv:1610.01644.
- Hewitt, J., & Liang, P. (2019). [Designing and Interpreting Probes with Control Tasks](https://arxiv.org/abs/1909.03368). EMNLP 2019.
- Jain, S., & Wallace, B. C. (2019). [Attention is not Explanation](https://arxiv.org/abs/1902.10186). NAACL 2019.
- Wiegreffe, S., & Pinter, Y. (2019). [Attention is not not Explanation](https://arxiv.org/abs/1908.04626). EMNLP 2019.
- OpenAI (2023). [Language Models Can Explain Neurons in Language Models](https://openai.com/index/language-models-can-explain-neurons-in-language-models/).
- Bereska, L., & Gavves, E. (2024). [Mechanistic Interpretability for AI Safety: A Review](https://arxiv.org/abs/2404.14082). arXiv:2404.14082.

# 附录：原始提纲

> 以下是本文成稿前的原始提纲，原样保留，供对照结构演变。

## 贯穿全文的设计决定

- (a) 沿问题走，不沿方法走：方法会过时，几个核心问题不会。
- (b) 把"忠实性"提到很靠前：它是判断后面一切方法的标尺，放在第 4 节，不塞到最后当注脚。
- (c) 机制派为主，经典派给足一节：本文面向前沿/ML 受众，重心放在机制可解释性，但经典归因派单独成章（第 5 节），不写成偏科综述。
- (d) 术语先给画面，再上名词：SAE、superposition、多义神经元、activation patching 这些，第一次出现都先用日常直觉（灯泡组合、金门大桥）讲清，再引术语。

## 贯穿全文的一条主线

整篇Review真正想回答的总问题，比"有哪些方法"更靠后一层："理解了模型，然后呢？这种理解是真的，且有用吗？尤其能不能反哺模型本身？" 后面每一节都要能回扣到这条主线，具体落点就是第2节定义的"用处阶梯"。

## 提纲各节

- 0. 摘要 + 范围声明。
- 1. 引言：三种动机（工程调试/信任合规/AI 安全）、能力进步 vs 理解滞后（Amodei）、本文核心主张、难度预告。
- 2. 核心追问：理解了然后呢。用处阶梯（诊断/监控/编辑干预/指导训练/安全保证）。
- 3. 概念地基与术语之乱。事后 vs 内在、局部 vs 全局、解释单位。
- 4. 忠实性 vs 可信度（全文标尺）。sanity check。
- 5. 经典/归因式：内在可解释模型、LIME/SHAP/saliency、Rudin 反黑箱、局限。
- 6. 范式转移：解释单位崩塌，从看外面到看里面。
- 7. 机制可解释性（重头）：多义神经元、superposition、线性表示、SAE/transcoder、circuit/induction head、规划/persona/内省、activation patching/金门大桥、回扣阶梯。
- 8. 中间地带：probing、attention 是否解释。
- 9. 评估：忠实性/稳定性/可读性度量、有无公认 benchmark、自动化可解释性的悖论。
- 10. 应用与落地：诊断/监控/编辑/审计/合规，按阶梯归位，理解在先管控在后。
- 11. 结构性困境：验证地狱、superposition 诅咒、追不上迭代、成功定义模糊、规模算力错配、劳动密集、坑深埋金。
- 12. 研究版图：经典派、机制派、各公司、开源社区，算力塑造分工。
- 13. 开放问题：能否 scale、superposition 能否解决、自动化瓶颈、忠实性能否可证、神经科学类比、阶梯能否往上爬。
- 14. 结论：看懂而非限制、忠实性是永恒标尺、理解滞后于能力是存在理由、价值取决于阶梯爬多高。
