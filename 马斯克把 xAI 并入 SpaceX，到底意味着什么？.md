2026年5月6日早上，Elon Musk在X上[发了一条推文](https://x.com/elonmusk/status/2052069691372478511)，说他上周花了不少时间见Anthropic团队的核心成员，结论是：

> "Everyone I met was highly competent and cared a great deal about doing the right thing. No one set off my evil detector."
> （每个人都非常专业，并且很在意做正确的事。没人触发我的邪恶探测器。）

读到这条推文的人都愣了一下。

90天前，Musk还在公开称Anthropic是"misanthropic"（厌恶人类的）、"hates Western civilization"（憎恨西方文明）、"evil AI"。再往前一年，他批评过Anthropic的Constitutional AI是"enforced diversity"，强加的多元主义。在这之前的两三年里，Musk嘴里几乎没有说过一句Anthropic的好话。

但就在这条推文发出来的同一天，两件大事同时发生。

一件是Anthropic和SpaceX签下了一份算力大合同。Anthropic拿下了SpaceX的Colossus 1超算，22万张GPU、300多兆瓦电力，全部用来跑Claude，年付30到40亿美元。这是Anthropic历史上签下的最大一笔算力合同，也是2026年AI行业最受关注的一笔基础设施交易。

另一件是xAI作为独立公司彻底解散，所有AI业务整合进SpaceX，统一改名叫SpaceXAI。这件事其实早有铺垫。2026年2月SpaceX就以全股权方式收购了xAI，把它变成自己的子公司，合并实体估值1.25万亿美元（SpaceX 1万亿+xAI 2500亿）。5月6日这一步只是把"xAI"这个法律实体也拿掉，让Grok和X这些产品直接挂在SpaceX名下。Musk砸了三年、堆了顶级研究员、烧掉几十亿美元做出来的xAI，从这一天起彻底不再以独立AI实验室的身份存在。

两件事看起来各自独立，但其实是同一条逻辑链上的两端。Musk 90天里从公开对立Anthropic到签下数十亿美元合同，原因要在xAI的财务困境、Colossus 1的闲置算力、SpaceX即将到来的IPO三件事里一起找。

我们今天就来详细讲述这件事。

# 一、xAI这家公司是怎么走到这一步的

## 1.1 从一份招聘清单开始

故事的起点在2023年初。Musk跟OpenAI已经分道扬镳，他参与创办的非营利组织变成了估值千亿的盈利公司，主导权落在Sam Altman手里。Musk嘴上的指控是OpenAI"背叛了创始使命"，业务上的逻辑很清楚：他要做一个新的对抗性AI公司。

2023年3月9日，xAI在内华达州悄悄注册。4个月后正式对外亮相，使命写得很大：理解宇宙的真实本质（understand the true nature of the universe）。但xAI最值得关注的部分在它的初始名单上。Musk把12个人从OpenAI、DeepMind、Google Brain、Microsoft Research一个一个挖了出来。

| 联合创始人 | 背景 |
|---|---|
| Igor Babuschkin | 前DeepMind / OpenAI，挂首席工程师 |
| Yuhuai "Tony" Wu | 前Google DeepMind |
| Christian Szegedy | 前Google，深度学习里GAN和Inception那一拨 |
| Jimmy Ba | 多伦多大学副教授，Adam优化器作者之一 |
| Greg Yang | 前Microsoft Research研究员 |
| Kyle Kosic等其他6人 | 各大顶尖实验室出身 |

看这份名单，最直接的共同点是非常浓厚的学术背景。其中有大学在职副教授（Jimmy Ba），有顶会论文常客（Christian Szegedy、Greg Yang），有做形式化数学和大模型推理交叉的研究者（Tony Wu），加上几个研究项目出身的工程师。整支队伍的日常更靠近大学实验室和企业研究院的节奏：写论文、做实验、上顶会、长周期试错。

Musk这一轮招人的style非常学术化，他要的是能在前沿做突破、能打榜、能写出新算法的人。做工业界产品、做规模化运维、做企业销售这些工种几乎不在他的清单上。这种招聘style在2023年AI实验室刚崛起的时候是行业共识，OpenAI、DeepMind、Anthropic当时也都是这么招人的。但这个选择会在3年之后给xAI带来文化上的根本冲突，后面1.3节会讲到。

Musk给他们的承诺是研究自由加影响力。这群泡在论文堆里的人能在Big Tech之外找到的最有诱惑力的故事。

后面发生的事情比所有人预料的都快。2023年公司估值6.7亿美元。2024年涨到240亿。2025年涨到500亿。2026年1月Series E一轮融资20亿美元，估值2300亿。2月并入SpaceX，合并实体估值1.25万亿。3年里估值翻342倍。这个速度，连2010年代那批最热的AI公司加起来都没跑出来过。

## 1.2 Grok打榜成绩很猛，但企业不买账

xAI从2023年11月发了第一版Grok起，几乎是按一年三代的节奏在出新模型。Grok 1（2023年11月）、Grok 1.5（2024年3月）、Grok 2（2024年8月）、Grok 3（2025年2月）、Grok 4和4.1（2025年下半年），Grok 5正在训练中。每一代都比上一代大、训练数据多、参数量提升，背后烧的是Colossus超算的算力。

Musk给Grok定的目标很清楚：一边把benchmark打到第一，一边靠X的5亿用户走消费分发，不依赖企业API。这两件事互相支撑，benchmark第一带来"这是最强模型"的舆论位，X免费流量带来用户量，用户量再反过来给广告主和Premium订阅讲故事。Musk反复说xAI要做"world's most powerful AI"和"AGI for everyone"，对应的就是这套路径。

按打榜成绩看，Grok做到了这一目标。2025年底到2026年初，Grok 4和4.1在LMArena的Text Elo榜上排到1483，全球第一。Humanity's Last Exam这种被设计成模型很难做对的考题，Grok做到50.7%，依然第一。AIME数学题91.7%。一个常常被Musk称为"理论物理级"的模型，benchmark上的表现的确够看。

但企业市场不吃这套，原因有两层。

最直接的一层是代码能力。SWE-bench Verified这条榜上Grok做到75%，Claude做到87.6%。代码是2025到2026年企业市场的核心场景，Cursor、Claude Code、GitHub Copilot这一类工具的兴起，让"AI写代码能不能用"直接挂钩到了模型的企业付费率。Grok在通用推理和数学上打榜赢，但企业掏钱时选Claude。

更深一层是路线根本不重叠。xAI走的是消费分发路径，Grok直接嵌进X靠免费流量做推广。Anthropic走的是企业基础设施路径，卖token给开发者，让Claude Code在程序员的工作流里建立粘性。两条路服务的客户不一样，定价模型不一样，留存机制也不一样。Musk下的赌注是消费市场，2025到2026年AI变现的真正爆点恰好在企业端。

把财务并排放，差距大到不需要解释。xAI 2025年的年化收入大概3亿美元，季度净亏14.6亿，每月烧10亿美元。Anthropic 2026年初的年化收入是300亿美元，已经接近盈亏平衡。Anthropic Claude的企业订阅可以做到211美元一个月一个用户，OpenAI的ChatGPT普通版25美元一周。同样的token，Anthropic能多收三五倍的钱。Anthropic用5%于ChatGPT的用户量，做到了OpenAI 40%以上的收入。

Grok的问题主要在路线选择上。模型本身没有大毛病，benchmark也确实做到了第一。Musk选的那条消费路径，在2025到2026年的市场结构里跑不出钱来。

## 1.3 十一位联合创始人是怎么一个一个走的

到2026年3月，xAI的11位联合创始人全部离职。算上80多名研究员和工程师集体出走。一家不到3年的公司，初始团队走得一个不剩，这在AI行业是少见的事。

故事真正的转折点是2026年2月10日和11日。

2月10日下午，Tony Wu在内部Slack发了一封告别信。他没说去哪，只说"AI这件事，要按它本来的节奏做"。第二天，2月11日，Jimmy Ba也走了。

Jimmy Ba离职这一刻很关键。他是Adam优化器的作者之一，整个深度学习行业每天都在用他论文里的算法做训练。一个写出来基础工具的人离开一家AI公司，意味着的是这家公司在他眼里已经不再值得留下。

接下来一个月，瀑布效应开始。Babuschkin走，他没去别的实验室，自己开了家VC基金，等于"我看好AI赛道，但不看好这家公司"。Dai走、Zhang走、Pohlen走、Kroiss走、Nordeen走。到3月底，11个人一个不剩。一位还没走的xAI工程师对外说了一句被反复引用的话：

> "AI开发那种流动的、探索性的本质，被Starship和Starlink项目里那种刚性的、里程碑式的指标取代了。"

这句话把所有问题点穿了。

xAI当初按"研究实验室"招的人。这些人习惯长实验周期、试错驱动、论文导向、自由探索。但2026年2月SpaceX收购xAI、把它变成子公司之后，Musk把他在火箭和工厂那一套以高强度长工时著称的硬件文化整套搬过来：内部把xAI重组成"模块化、产品驱动的组织"，参照Starship和Starlink的里程碑式管理。产品决策不再走xAI内部的研究流程，而是按Musk一贯的SpaceX风格在小圈子里直接拍板。研究周期从"几个月一次评审"压到周级别的迭代。

Starship这套管理方式有它自身的合理性，火箭工程的目标足够具体，要把多少吨送上轨道、落在哪里。AI研究的性质不一样，它的产出常常需要几个月的探索才会有方向感。把火箭那套节奏搬到AI研究里，等于让一群本来要画地图的人天天写日报。这群人留下的概率会很低。

文化冲突是被点得最多的一条。外面流传的还有几条原因，没有官方确认，但反复被业内提到：

- **Musk的决策风格**：产品方向不再走xAI内部的研究评审流程，更多由Musk在小圈子里直接拍板。一些研究员公开说过类似的体验：按学术方法论提一个RLHF改进方案，第二天看见Musk在X上转一条相反方向的tweet，要求按那个方向改。"老板一句话推翻一周工作"重复几次就把人逼走。

- **Grok的内容争议**：2024到2025年Grok几次出过比较严重的公关事故，生成"MechaHitler"内容、对某些政治话题的回应被外界批评。一部分做alignment和safety的研究员对Grok的输出方向不认同。Anthropic的Constitutional AI路线虽然被Musk公开骂过，但在研究员价值观里其实更接近主流。

- **合并的股权安排**：xAI早期股权在换算SpaceX股权时，行权条款、归属期、流动性安排各有变化。具体细节没公开，但据报道一些早期员工对换算条件不满，认为合并对Musk的好处远大于对自己。

- **同行挖人**：Anthropic、OpenAI、Google DeepMind在2025到2026年给顶级研究员开的包高到夸张，staff researcher级别200到500万美元一年加股权的offer变得常见。一旦xAI的故事开始动摇，确定的高薪对不确定的未来，选项很清楚。

这几条里多少是真因，多少是借口，外面看不清。但它们叠加在一起，把"11位联合创始人在不到3个月里走光"这件事从反常事件变成几股力量合力的结果。

Musk自己罕见地公开承认了这件事。他在X上发的原话是：

> "xAI was not built right first time around, so is being rebuilt from the foundations up."（xAI 第一次没建对，正在从基础重建。）

这是过去十年Musk最罕见的一句承认错误的话。但他没把xAI拆掉重新雇人，而是把xAI整个塞进了SpaceX。

## 1.4 为什么XAI必须塞进SpaceX

XAI塞进SpaceX的理由，对外界说的非常宏大：轨道数据中心，垂直整合AI。听起来非常Musk，也很适合放进发布会和投资人材料里。

但如果分析一下细节（上一节所述），真正的问题其实更简单：xAI已经没法作为一家独立AI实验室继续讲故事了。

它的模型能打榜，团队却走空了。它的用户入口在X，企业收入却跑不出来。它有Colossus这种重资产，利用率又撑不起资本开支。季度亏14.6亿、月烧10亿、11位联合创始人全走光，这种公司继续独立融资，下一轮会非常难看。

塞进SpaceX之后，问题的外观立刻变了。月烧10亿美元的亏损，单独看是融资危机。放进Starlink一年80亿美元利润的合并实体里，就变成资产负债表里的一行注脚。xAI不再需要每12到18个月出去讲一次新故事，SpaceX替它把融资压力吸收掉。

反过来，SpaceX也需要xAI。SpaceX单独上市，按Starlink的SaaS估值倍数算，大概是5000到8000亿美元的故事。加上“AI加太空”，就可以把估值讲到1.5到2万亿。中间多出来的7000亿到1.2万亿，不来自火箭本身，主要来自AI叙事溢价。

还有一层是政府渠道。对比Anthropic 2025年被五角大楼定为“供应链风险”，丢了一份2亿美元的合同。SpaceX和Antropic不同，跟五角大楼、NASA、情报机构的关系深得多。Grok如果挂在SpaceX名下，拿政府合同的路径会比xAI自己去敲门顺很多。

所以这场合并表面上是“AI业务并入航天公司”，底层更像一次资产重组。SpaceX给xAI提供资产容器、现金流遮蔽和政府渠道。xAI给SpaceX提供IPO估值故事和AI标签。两边各取所需，只是代价不一样。

对Musk个人和SpaceX整体业务来说，这是合理选择。对xAI这家公司本身来说，就是被吞掉、被肢解、被改造。从2月起，它已经只是SpaceX名下的一个子公司。到5月6日，连“xAI”这个法律实体也被解散，独立AI实验室的品牌彻底消失。

# 二、合并之后的SpaceX

## 2.1 财务真相和负担

SpaceX的财务在2025年是亮眼的。营收155亿美元，比2024年涨18%。EBITDA利润80亿，利润率超过50%。这里面Starlink贡献大头，约100亿美元，每年增长又快又稳。这是全球商业航天里唯一真正赚钱的公司。

但合并完xAI之后，SpaceX的资产负债表就变得复杂了。账面上多出一个年亏60亿美元的AI公司，外加一个年亏几十亿、还在还120亿美元收购债务利息的X。Starlink的现金流要先去喂这两个亏损业务，剩下的才能继续投星舰、星链卫星。

监管包袱也跟着合并进来。xAI在印尼和马来西亚被国家级封禁，欧盟有一系列调查，深度伪造的集体诉讼还在审。这些原本跟SpaceX没关系，合并之后全都进了同一份招股书。

招股书是这场IPO的核心文件。SpaceX计划2026年6月递交S-1。审计师面对一份"火箭+卫星+AI+社交"的混合资产，要给一个估值，要回答董事会和监管机构上百个具体问题。"这家公司到底是干什么的"，将变成IPO路演里反复被问的问题。

但市场可能愿意接受这种复杂度。2026年的资本市场对AI和太空都给了很高的叙事溢价，"AI加太空"这个组合在路演阶段大概率能撑住高估值。这种估值是否合理，要看未来3到5年业务整合的实际表现。

## 2.2 X在三家公司之间的归属变迁

X这家公司的归属变迁是一条曲折的路径。理解这条路径，要先区分公开市场股价和私有公司估值。X、xAI、SpaceX在这些交易里都没有公开上市，相关“价格”指的是交易双方认可的估值，不能按交易所里每天跳动的股价来理解。

私有公司的“股价”通常是折算出来的。融资或并购时，双方先谈一个总估值，比如“这家公司值330亿美元”。再根据完全摊薄后的股份数，折算出每股价格，用来换股、记账、签协议。这个价格有法律和会计意义，但没有公开市场那种连续交易的价格发现。

按这个口径看，X经过了三次重新定价。2022年10月，Musk以440亿美元个人收购Twitter，私有化后改名X。2025年3月，Musk把X卖给xAI，X在交易里的估值是330亿美元，相当于比收购价缩水25%。2026年2月，SpaceX收购xAI，X跟着xAI一起进入SpaceX体系，xAI整体估值从800亿跳到2500亿。到2026年5月，xAI法律实体解散，X直接归SpaceX/SpaceXAI。

核心变化发生在打包方式上。X自己没有突然变好，但它被放进了不同的资产包。单独看X，它是一家广告受损、债务很重、监管麻烦不少的社交平台。放进xAI，它变成Grok的数据源、用户入口和分发渠道。再放进SpaceX，它又变成“太空连接+社交入口+AI推理”这条故事线的一部分。

所以同一份资产会在不同交易里出现不同价格。这里没有神秘魔法，就是私有市场最常见的打包重估：资产本身没换，讲故事的上下文换了，买方愿意承认的协同价值也跟着换了。后面SpaceX IPO时，审计师和公开市场要重新判断，这些协同价值到底能落到收入和利润里多少。

X对SpaceX的实际用途，最先落在Grok上。X有实时文本流、热点事件、用户关系链、互动反馈和海量对话场景，这些都能给Grok提供训练数据、RLHF反馈、产品分发和用户留存。没有X，Grok只能像普通AI App一样买流量；有了X，Grok可以直接嵌进一个几亿用户每天刷的信息流。

对SpaceX本体，X的帮助要弱得多。X不会让火箭更可靠，也不会让Starship更快入轨。它能做的主要是外围层：给Starlink做消费者入口，给Grok做服务渠道，给政府和企业客户展示“通信+AI+社交数据”的组合方案。

最有想象力的部分在Starlink。未来如果Starlink终端内置Grok服务，X可以承担账号体系、内容分发、客服入口和用户反馈层。比如偏远地区用户用Starlink上网，同时通过Grok获得本地语言客服、故障诊断、教育内容、实时信息服务。这些服务离火箭业务本身还有距离，但可以变成Starlink订阅之外的增值服务。

政府场景也类似。SpaceX本来就有卫星通信和发射能力，X和Grok可以补上信息处理、舆情监测、战场文本分析、灾害响应客服这类软件层。这个方向能不能做大，要看监管和客户接受度；但它至少说明，X除了重估资产以外，还有一层实际业务可能性。

真正的边界也要说清楚。X对SpaceX的硬科技核心没有直接增益，它不能替代火箭工程、卫星制造、轨道调度和地面站建设。它的作用更像入口、数据层和叙事拼图。对IPO估值来说，这已经足够有用；对长期经营来说，还要看这些入口和数据能不能变成可持续现金流。

## 2.3 可能的下一步：SpaceX反向收购Tesla

很多人以为合并xAI是Musk的终局。其实可能只是中场。下一步分析师们已经在公开下注：SpaceX反向收购Tesla。

Tesla和SpaceX的财务对比放在一起看，会让你重新思考这两家公司谁是谁的母舰。

Tesla 2025年营收948亿美元，是SpaceX的6倍。但Tesla的GAAP利润是38亿，同比下降46.5%。增长是负的2.9%，史上第一次年度营收下降。SpaceX只有155亿营收，但EBITDA利润80亿，利润率50%以上，增长18%。Tesla市值1.5万亿，市盈率343到364倍。SpaceX如果按合并实体估值1.5到2万亿IPO，市盈率反而会比Tesla低。

把这件事翻译成大白话：Tesla营收大但赚不到钱，SpaceX营收小但赚钱比例高。如果两家合并，财务上是SpaceX在为Tesla提供利润支撑，而不是反过来。

Wedbush的Dan Ives给SpaceX反向收购Tesla的概率打到80%到90%，时间窗口2027年上半年。前Tesla总裁Jon McNeill估的概率是50%以上。

但财务只是表层原因。真正的结构性差异在股权层面。

Tesla是单一股权公司，Musk持股仅13%。过去几年他在特拉华州法院、在股东集体诉讼里来回拉锯，几次薪酬方案被股东诉讼推翻，CEO权力跟股东信任的张力一直没消解。SpaceX是双层股权，Musk持股42%，控制79%投票权。

合并之后，Musk可以用SpaceX的双层股权架构整合Tesla的治理结构。SpaceX招股书里明确提到，Musk的去职需要Class B股东投票通过。这种创始人控制的双层股权在硅谷并不罕见——Google、Meta、Snap、Palantir、Snowflake都用过类似结构，背后的逻辑是让创始人能做长期决策不被短期股东压力打断。但实际效果是合并实体的治理由Musk长期主导，对短期股东的约束力大幅降低。

对相信Musk长期判断的投资人来说，这是优点。对希望保留股东治理参与权的投资人来说，这是需要权衡的代价。两种立场都有合理性，最终取决于投资人买这家公司是为了什么。

## 2.4 轨道数据中心的工程现实

并购公告里有一个抓眼球的承诺：未来Colossus将搬到轨道，做"太空数据中心"。Anthropic也在跟SpaceX谈未来部署多吉瓦的轨道AI算力。

但工程上，这件事在十年内很难实现。

太空有五个工程问题，没有一个被解决。

第一个是散热。地面数据中心靠空气和水带走废热。太空只能靠辐射散热，效率低一个数量级。Colossus 1的300兆瓦放上去，需要足球场大小的散热板，且不能折叠（折叠的散热板做不出来这种功率）。

第二个是能源。300兆瓦在地面可以接电网，在太空只能靠太阳能。300兆瓦相当于1.5平方公里的太阳能板，约210个标准足球场。把这种东西送上轨道，发射成本以亿美元计。

第三个是维修。GPU在轨道上的故障率比地面高10倍以上，主要是辐射诱发的位翻转。Colossus有22万张GPU，地面机房一年坏几千张是正常的，轨道上一年可能坏5万张，没有人能上去换。

第四个是辐射加固。H100这种现代GPU不是辐射加固设计的，必须从头设计芯片，性能至少倒退5到10年。NASA和SpaceX自己的航天器用的芯片普遍是几代之前的产品。

第五个是带宽和延迟。LLM训练对GPU之间的同步延迟极敏感（毫秒级），太空数据中心和地面之间的延迟是数百毫秒，这种节奏跑不动现代大模型训练。

这五件事每一件都是几十亿美元的工程难题，五件事叠加起来，没有任何2030年前能跑通的迹象。

但这跟IPO估值有关吗？有关。

Musk历史上有一类长周期承诺，工程兑现时间常常远超最初预告。Hyperloop 2013年承诺LA到SF 30分钟，12年过去了基本没进展。Mars殖民2024年载人，目前推迟到2030之后。Robotaxi 2019年承诺2020年100万辆无人车，6年后还在内测。FSD从2016年起每年承诺"明年实现完全自动驾驶"，承诺了9年。

但同样要承认，Musk在另一些项目上做到了别人没做到的事。Falcon 9可回收火箭做成了，把发射成本降了一个数量级。Tesla把电动车从富人玩具变成大众市场。Starlink让北极圈到撒哈拉都能连上互联网。这些当年也都被骂过画饼。

所以"轨道数据中心"这个承诺有两面性。短期看它对IPO估值是有帮助的。长期看它会不会兑现要拉更长的时间观察。买SpaceX IPO的投资人买的是Musk的复合记录：一部分长周期项目最终交付了，一部分至今没有。

# 三、Anthropic为什么突然成了战略伙伴

## 3.1 一组让审计师睡不着觉的数字

5月6日那条推文之所以让所有人意外，是因为它在Musk的修辞框架里完全说不通。但放进Colossus 1的财务现实里，它就是唯一能走的那条路。要看清这一层，得先回到2026年初的孟菲斯。

Colossus 1是xAI 2024到2025年砸出来的超算项目，部署在田纳西州孟菲斯郊外的一座废弃伊莱克斯工厂里。从立项到上线的速度被Musk反复在X上炫耀过，他认为这是SpaceX风格的硬件工程速度，跟传统AI实验室那种慢吞吞的研究节奏完全不一样。建好以后的Colossus 1是一头怪兽：555,000张GPU，180亿美元采购成本，300兆瓦满负载电力消耗，是2025年地球上单点算力最密集的设施之一。

盖这个东西的时候，xAI赌的是Grok要带着X的5亿用户冲消费AI市场，需要海量算力做分发。算力规划基于一个核心假设：Grok的日活用户在2025到2026年会爆炸式增长，模型推理算力需求会线性跟上。

但2026年初，The Information报了一个让所有人都没准备好的数字：xAI的Colossus 1实际算力利用率，只有11%。

11%是什么概念？意思是用180亿美元买的硬件，89%的时间在那儿空转。这不是某一周的低谷，是2025年第四季度整个quarter平均下来的数字。

对一家正常运营的公司，89%闲置只是浪费。但Colossus 1的拥有方SpaceX，要在2026年6月递交S-1，准备IPO。审计师面对这种闲置率，只有几条路可以选。

第一条是资产减值。会计准则要求long-lived assets按实际使用情况评估，如果utilization长期低于设计容量的某个阈值，就要按fair value减值。180亿美元的硬件按实际利用率打折，可能要减值几十亿。这一笔砸进招股书，IPO估值要被砍掉很大一块。

第二条是把闲置算力作为产能储备。但产能储备要写明用于哪个客户、哪个产品。xAI自己消化不了这89%的剩余产能，"为未来Grok增长留备"这个故事在审计师眼里不够具体。

第三条是把闲置算力签长期合同租出去，把"闲置资产"转成"已签约的长期收入流"。这是让财务报表好看的最直接方法。一份多年期的高利润hosting合同，能同时贡献ARR、毛利率、客户多元化全套指标。Colossus 1从"减值候选"立刻变成"signed revenue引擎"。

问题是租给谁。

## 3.2 全世界只剩一个买家

2026年初，全世界能消化22万张H100加300兆瓦电力、还付得起几十亿美元一年的客户，屈指可数。

OpenAI不需要。它跟Microsoft已经绑死，加上2025年跟Oracle、Crusoe一起搞的Stargate这种千亿美元算力项目，自己已经从algo客户变成了算力供应方。OpenAI现在缺的不是H100，是更多更便宜的GPU。

Google用自家的Trillium/TPU v6那条线，从来不外采H100这种规模。Google从2017年开始就有自己的硬件栈，Gemini训练完全跑在自家TPU上。Anthropic 2024年虽然拿过Google投资，但Google给Anthropic的算力是有ceiling的，核心TPU产能要先满足Google Search、Gemini、YouTube这些自家业务。

Microsoft早就跟OpenAI深度绑定。Azure的AI算力大头分给OpenAI优先消化，剩下的还要分给Azure外部企业客户。Microsoft直接租Colossus 1给Anthropic用，意味着跟自家OpenAI伙伴的关系会变得很尴尬。

Meta自己已经买了几十万张H100做内部Llama系列训练，多余产能极少。而且Meta跟Anthropic某种程度上是直接竞争，都做chatbot、都做企业AI、都瞄企业市场。Meta当hosting provider不现实。

Amazon也微妙。Amazon是Anthropic主要投资人之一，投资金额累计接近100亿美元，AWS也是Anthropic最大的hosting客户。但Amazon自家有Trainium芯片想推，给Anthropic增加H100等于跟自家芯片业务正面冲突。

剩下的只有Anthropic自己作为买方。

而Anthropic也确实缺算力，缺到这家公司在2025年下半年开始公开承认。Claude Code的5小时使用配额经常被开发者用爆，X、Reddit、HackerNews上各种"我刚开始vibe coding就被rate-limited了"的吐槽。Opus API的速率限制紧到企业客户开始抱怨。Cursor这种重度依赖Claude的产品反复反馈"高峰时段API不稳定"。

更要命的是时间窗口。Anthropic自己也准备2026年IPO，公开估值已经在9000亿美元路演阶段。它需要的不只是算力，是"未来一两年算力不会断"的那个保证。从AWS加产能、自建数据中心、跟新晋hosting厂签合同，每一条路在IPO路演的时间窗口里都来不及。

所以严格说，这单合作的实质是市场结构选择题。Anthropic在2026年初是市场上唯一能消化Colossus 1那89%闲置算力、还付得起30到40亿美元一年的客户。Musk没多少选择空间。Anthropic也没多少选择空间。

90天前还在X上互相批评的两家公司，因为各自的财务现实，走到了同一张合同上。这条合同5月6日早上签下来，下午Musk就发出了那条"邪恶探测器没响"的推文。

## 3.3 这笔交易对双方的真实价值

对Musk来说，第一层好处直接体现在IPO招股书上。

180亿美元的闲置硬件不再是负债，它转化成了一份多年期的高利润收入合同。审计师可以这么算账：Anthropic每年付30到40亿美元，签约期假设5年，total contract value在150到200亿美元区间。Hosting业务毛利率按AWS的标杆假设60%，光这一份合同就能给IPO贡献几百亿估值。Colossus 1从"减值候选"变成了"signed ARR引擎"。

第二层是法律层面。Musk 2024年起在加州法院告OpenAI和Sam Altman，主线指控是OpenAI"背叛了创始使命，从非营利转成赢利公司"。在诉讼里把Anthropic重新定位成"安全AI替代品"，能给他的指控加一层叙事支撑：你看，做AI不需要走OpenAI那条路，Anthropic就做得不错。同时合同里据报道有一条"Humanity Clause"，如果Musk认为Claude在做"危害人类"的事，可以切断算力。这条款给了Musk对竞争对手运营层面某种有限的影响力，虽然实际触发条件应该相当苛刻。

第三层是舆论。Musk从"骂Anthropic是邪恶AI"变成"我亲自审查了它的安全文化，邪恶探测器没响"。这是Musk一贯的修辞调整方式。一条tweet就把过去的所有指控翻篇，不需要解释中间的转变过程。X上的支持者会接受这种叙述，因为Musk本人的可信度是他们关注的中心。

对Anthropic来说，好处也分三层。

最直接的是算力解渴。签约公告之后第二天，Anthropic就公告Claude Code的5小时配额翻倍，Opus API上限大幅提高。开发者论坛立刻有人发"这次Anthropic真的把限额放开了"的截图。这是用户体验层面的具体改善，能直接缓解2025年下半年那波"Claude越来越不好用"的舆论压力。

第二层是独立性。Anthropic没有向OpenAI阵营（Microsoft / Oracle / Stargate）投降，也没有完全依赖Google那边的TPU。拿到OpenAI阵营之外的大宗算力，意味着Anthropic在战略上还能保持相对独立。这对一家强调"安全AI路线独立性"的公司很重要。

第三层是IPO路演弹药。9000亿估值的IPO路演里，最大的潜在风险就是"用户体验在崩"。把这个故事改写成"已锁定22万H100，未来一年半算力供给确定"，路演画风完全不一样。投资人评估Anthropic时，从"会不会因为算力被卡死"变成"算力可见，可以专注估值模型的其他变量"。

这笔交易在两边的财报和叙事上都是双赢。Musk解决IPO估值问题，Anthropic解决算力和路演问题。中间被牺牲的只有Musk 2024到2025年在X上对Anthropic的所有公开评价。这个代价对Musk来说，几乎为零。

## 3.4 Musk的修辞和商业决策从来都是两条线

如果你只追Musk在X上的发言，会被他批评的剧烈程度吓到。但如果只看他签的合同，他几乎没有什么"原则性"的对抗。

批评Bezos是常态，骂过"Jeff B... gone fishing again"那种话，但SpaceX跟Amazon Kuiper（亚马逊的卫星项目）在FCC频谱协调上既竞争也合作。批评广告主2023年那句著名的"go fuck yourself"在前，第二年（2024）跟Disney、Apple、Comcast这些被骂过的广告主重新签合同。批评中国制造常态化，但Tesla的上海工厂是全球最赚钱的Tesla工厂，他每年至少飞一次去签订单。批评OpenAI是"异端"，转身告OpenAI同时挖OpenAI高管来xAI，Babuschkin、Tony Wu这一批人当年都是OpenAI系。

Musk的修辞和商业决策几乎从不一致。他批评Claude时是在做舆论表达，他签Anthropic合同时是在做生意。两件事服务不同的目标。批评是面向X用户和支持者群体保持热度，签合同是面向董事会、投资人、审计师完成交付。这两个audience的反馈循环不交叉。

他的真实优先级排序大致是：自我利益高于公司整体利益，公司整体利益高于公开承诺。如果一笔生意能给SpaceX IPO估值多1000亿美元，他骂过的话翻篇成本几乎为零。发一条推文就够了。

这件事的更大含义是：少数几家AI公司控制着全行业的算力、电力、数据。台前他们怎么吵都行，台下他们必须互相租算力、互相买数据、互相挖人。Musk-Anthropic这笔交易在2026年很可能只是开始。AI行业整体已经进入"基础设施寡头"阶段，前5家公司的算力、模型、企业客户、数据集已经形成相互交叉的依赖网络。这是结构性事实，不针对某一家公司。

# 四、这件事到底意味着什么

## 4.1 三层理解

最浅的一层是媒体故事。Musk反转，xAI失败，Anthropic受益。三个新闻标题就能讲完。

中间一层是商业逻辑。xAI在消费AI路径上输给了企业基础设施路径，被迫并入SpaceX寻求重组。SpaceX需要AI业务拉高IPO估值，Colossus 1的闲置算力需要客户。Anthropic需要算力填补需求缺口。三方在各自的财务约束下走到一起，本质是约束条件的耦合。

最深一层是合并实体的资产组合管理。Musk通过两次反向收购（X归xAI、xAI归SpaceX），把三家原本不相关的公司整合成1.25万亿美元的合并实体。下一步可能是SpaceX跟Tesla的反向合并，最终在双层股权下形成一个统一的合并主体。资本结构是这场整合的主线，但xAI本身并不会消失，它会从独立AI实验室变成SpaceX体系里的AI产品和算力部门。

## 4.2 谁赢了，谁输了

Musk个人是受益方。SpaceX IPO之后他的净资产可能突破6000亿美元，而且通过双层股权获得了整合实体的长期主导权。这件事的金融价值远超过xAI在产品层面的失败。

Anthropic也是受益方。它拿到了关键算力，对OpenAI的领先在企业市场扩大。这家公司2026年的IPO走在最有利的时间窗口里。

SpaceX早期投资人是受益方。从2002年Musk自己掏钱开始，到2026年合并实体估值1.25万亿美元，回报相当可观。

承担成本的一方比较多。

xAI的11位联合创始人和80多位研究员被驱离。他们的行业声誉还在，但2023年那个"理解宇宙真实本质"的故事在他们手里已经结束了。

即将买SpaceX IPO的散户，需要明白自己买的资产组合既包括Starlink这种盈利业务，也包括xAI、X这种亏损业务，加上一些长周期工程承诺。双层股权意味着投票权有限。这个组合是否值得买，取决于个人投资判断。Tesla现有股东在反向收购真的发生时，股票可能被换成无投票权的Class A，相当于把Tesla这家公开公司的股权换成合并实体的股权。

AI行业的整体多元化趋势在这次合并后进一步收紧。前10大AI公司继续向几家超级实体集中，独立创业公司能拿到的算力、数据、人才都在变少。

## 4.3 xAI接下来会变成什么

xAI的角色已经变了。以前要证明自己能成为OpenAI、Anthropic那样的独立AI公司，现在要证明自己能给SpaceX合并实体的收入、估值和战略想象力加分。Grok不会消失，但它的优先级会让位给SpaceX体系的整体目标。

短期看，Grok会被更深地嵌进X、Starlink和SpaceX的政府客户体系。X给它用户入口和实时数据，Starlink给它全球终端入口，SpaceX给它政府和企业销售通道。这条路线如果跑通，Grok就从聊天机器人扩展成SpaceX体系里的软件层，客服、搜索、数据分析、舆情处理、战场文本分析都能往这一层上堆。但创始团队散掉、Colossus 1大半算力还要租给Anthropic消化，xAI自己继续做前沿研究的空间会比2023年小得多。

成功版本是xAI变成SpaceXAI这类平台层，给Starlink、政府业务、X和未来轨道数据中心提供AI能力，把通信、算力、模型、客户关系打包卖出去。失败版本是它只剩Grok一个流量产品和一座昂贵的Colossus，继续靠Starlink现金流补贴。这个差别会直接决定SpaceX IPO的质量。未来三到五年真正要看的是，Grok有没有进入Starlink账单、政府合同和企业客户的日常采购里。

## 4.4 SpaceX IPO本质上是什么

如果冷静地看，SpaceX IPO是把多个不同性质的业务打包成一个上市主体。

业务可以分两类。火箭发射和Starlink是现金流引擎，火箭项目制收入毛利高，Starlink订阅每年100亿美元。这两块加起来一年能产生几十亿美元自由现金流。

剩下的几块都在烧钱。Grok季度净亏14.6亿，X每年亏几十亿，Colossus的算力出租是把闲置变成收入但本金都还没收回。

SpaceX IPO的核心财务逻辑就是：用Starlink的现金流支撑xAI和X的亏损运营，让公开市场参与这个组合的整体估值。

这种模式在科技行业不算少见。Amazon长期用AWS的利润补贴零售业务的扩张。Meta用广告利润补贴Reality Labs的元宇宙投入。Google用搜索广告补贴YouTube、Cloud、Waymo。投资人买这些公司，本质都是接受"赚钱业务支持烧钱业务"的组合。SpaceX IPO的特殊性在于亏损业务的体量比较大、涉及行业更多元、双层股权下创始人主导权更强。

## 4.5 创始人控制的双层股权传统

SpaceX IPO后的治理结构延续的是硅谷过去20年的一种主流做法：创始人通过双层股权保留长期控制权。

Google 2004年IPO时引入双层股权，Page和Brin的Class B票一票顶十票。Facebook 2012年IPO同样是双层结构，Zuckerberg控制多数投票权。Snap 2017年走得更极端，IPO股票完全无投票权。Palantir、Airbnb、Snowflake、Coinbase都是类似设计。

这种结构的支持者认为：创始人不被短期股东压力打断，才能做长期投资、保护核心战略不被对冲基金扰乱。Page和Brin确实这样做出了Waymo和Brain。Zuckerberg在被投资人质疑的情况下坚持做Reality Labs和AI。Bezos写给股东信里反复说"我们做长期"。这些公司都跑出了不错的长期回报。

反对的声音则关注治理透明度：当创始人犯错时（Snap业绩不及预期、Meta元宇宙投资亏空数百亿），普通股东很难通过投票纠偏。WeWork当年的治理失败就被反复引用作为反面教材。

SpaceX的双层股权不算新鲜事物，但有几个特殊性。一是合并实体里的业务多元程度比硅谷一般科技公司更高（航天加AI加社交加未来可能的电动车）。二是Musk同时控制多家公司、有多重利益冲突。三是部分业务（轨道数据中心）的兑现时间在十年以上。

这种组合下的双层股权，对短期投资人和长期投资人的吸引力会有显著差异。

# 五、写在最后

xAI从一个意图理解宇宙的研究实验室，变成了一艘IPO母舰里的AI业务部门。它的11位顶尖研究员先用脚投票表达了对Musk重组的反对。整个公司接着被并入SpaceX充当IPO故事里的"AI拼图"。再然后，超额建的算力被打包租给一年前还在被Musk公开批评的竞争对手。

这条路径上每一步都符合各方的财务约束。它的解释更多在资本和供需结构上，跟AI技术本身关系不大。

Musk通过这次合并解决了几个具体问题：xAI的独立融资难题、Colossus 1的闲置算力、SpaceX IPO的估值故事。同时把竞争对手Anthropic变成了付费客户。一进一出，这是一次相对成功的资产整合。

对潜在投资人，这件事有两个层面的判断要做。一是相不相信这个合并实体在未来5到10年能把"AI加太空"叙事兑现成实际业务，特别是Grok能不能在企业市场翻身、轨道数据中心的工程难题能不能突破。二是接不接受双层股权下创始人长期主导的治理结构，并把它跟Google、Meta、Tesla等硅谷同行的同类结构做横向比较。

这两件事都没有标准答案。它们的答案取决于投资人对Musk长期复合记录的判断，以及对未来5到10年AI和太空行业格局的预期。

整件事最值得记住的，是2026年初这个时间点上一个事实。当Anthropic和SpaceX在5月6日同时签下合作公告时，更深层的信号其实在AI产业的资源结构上：算力、资本、人才已经集中到了少数几个超级实体手里。这种集中度在2026年还在继续上升。Musk-Anthropic这单合作，是2026年AI产业基础设施层面整合的一个公开样本。它后面会有更多类似的整合，方向都不会变。

---

## 作者其它文章

- [福特经济学和AI经济学](https://x.com/snowboat84/status/2052551731385602072)
- [数学照妖镜：AI能发现新的数学定理吗？](https://x.com/snowboat84/status/2052174034041995572)
- [手把手教你分析：你会被AI取代吗?](https://x.com/snowboat84/status/2051818364507688978)
- [一篇文章讲清大语言模型发展史](https://x.com/snowboat84/status/2051444935547912236)
- [气吞万里如虎：回顾十九世纪的数学英豪们](https://x.com/snowboat84/status/2050371067278143931)
- [Vibe Reading：AI时代读书的系统化方法](https://x.com/snowboat84/status/2050008577511973253)
- [长篇分析：Manus案折射出的中国AI创业生态](https://x.com/snowboat84/status/2049643679804248305)
- [别再被AI新词绕晕了：Prompt、Context、Agent背后的工程主线](https://x.com/snowboat84/status/2049286033427349809)
- [两万字科普：AI为什么会编程——原理、历史与未来](https://x.com/snowboat84/status/2048919554882215954)
- [兄弟们，真·Vibe Writing时代到来了](https://x.com/snowboat84/status/2047828585537548574)
- [全网最详细的AI学习路线图](https://x.com/snowboat84/status/2047457686070141051)
- [每个人都应该使用的三个最有用的Claude Skill](https://x.com/snowboat84/status/2047110768773197834)
- [SpaceX立志传（一）：赌上全部的最后一次发射](https://x.com/snowboat84/status/2046743964192276766)
- [估值290亿美元的套壳公司，正在被自己的房东杀死](https://x.com/snowboat84/status/2046380497627230607)
- [黄仁勋和主持人吵红了脸：芯片封锁中国，美国到底能不能打赢？](https://x.com/snowboat84/status/2046022377830801725)
- [AI将如何颠覆教育，普通人又应该如何抢夺教育新的生态位](https://x.com/snowboat84/status/2044932338262667509)
- [学物理的八方英雄们，物理学已死，请转行搞AI](https://x.com/snowboat84/status/2044584627046920278)
- [不会编程、没有融资、没有员工，他怎么一个人做到年入2000万](https://x.com/snowboat84/status/2044216044575998136)
- [兄弟们想清楚：究竟是你为X打工，还是X为你打工？](https://x.com/snowboat84/status/2043842017260908743)
- [一人公司盈利四亿美元：是骗子，还是可复制的红利？](https://x.com/snowboat84/status/2043493870265422223)
- [2026第一季度大裁员，AI是背锅侠吗？](https://x.com/snowboat84/status/2042766853404307931)
- [重返星辰大海：这次绕月飞行有意义吗？](https://x.com/snowboat84/status/2042405716380835998)
- [张雪峰在美国为什么无法成功](https://x.com/snowboat84/status/2042045634245746743)
- [2026企业尸检报告：不用AI，你的公司能活过今年吗？](https://x.com/snowboat84/status/2041672997959057517)
- [兄弟们，我创业失败了，人生完整了](https://x.com/snowboat84/status/2040948420391940272)

---

## 本文参考文献

- [xAI Raises $20B Series E](https://x.ai/news/series-e) - xAI官方公告，2026年1月6日
- [Elon Musk's xAI raises $20 billion from investors including Nvidia, Cisco, Fidelity](https://www.cnbc.com/2026/01/06/elon-musk-xai-raises-20-billion-from-nvidia-cisco-investors.html) - CNBC，xAI Series E估值2300亿
- [Anthropic, SpaceX Sign Deal to Boost AI Computing Power for Claude Software](https://www.bloomberg.com/news/articles/2026-05-06/anthropic-inks-computing-deal-with-spacex-to-meet-ai-demand) - Bloomberg，Anthropic-SpaceX算力交易
- [Anthropic, SpaceX announce compute deal that includes space development](https://www.cnbc.com/2026/05/06/anthropic-spacex-data-center-capacity.html) - CNBC，Colossus 1 220K GPU + 300MW
- [Musk's SpaceX has rented out access to its supercomputer's 220,000 Nvidia GPUs](https://www.tomshardware.com/tech-industry/artificial-intelligence/musks-spacex-has-rented-out-access-to-its-supercomputers-220-000-nvidia-gpus-and-300-megawatts-of-ai-compute-power-to-rival-anthropic-musk-says-no-one-set-off-my-evil-detector-antrhropic-also-interested-in-orbital-data-centers) - Tom's Hardware，Musk "evil detector" 推文
- [Musk's xAI loses second co-founder in two days as Jimmy Ba departs](https://www.cnbc.com/2026/02/10/musks-xai-loses-second-co-founder-in-two-days-as-jimmy-ba-departs.html) - CNBC，2026年2月10/11 Tony Wu + Jimmy Ba 24小时内连续辞职
- [All 11 xAI co-founders have now left Elon Musk's AI company](https://thenextweb.com/news/xai-all-cofounders-departed-musk-spacex-rebuild) - The Next Web，11位创始人全部离职
- [80+ AI Researchers Just Walked Out of xAI](https://www.metaintro.com/blog/xai-exodus-ai-talent-wars-2026) - Metaintro，80+ 研究员集体离开
- [xAI Co-Founder Exodus, SpaceX IPO & Musk's $1.25T Rebuild](https://almcorp.com/blog/xai-co-founders-exodus-spacex-ipo-elon-musk-rebuild-2026/) - ALM Corp行业分析，1.25万亿合并实体估值

---

## 附录：原始草稿

> # 马斯克把 xAI 并入 SpaceX，到底意味着什么？
>
> > 一场用资本运作掩盖产品执行失败的精心包装
>
> 2026 年 5 月 6 日，Elon Musk 在 X 上发了一条推文："我跟 Anthropic 的人见了几面。我的邪恶探测器没响。"
>
> 这句话在 90 天前是不可想象的。就在 2026 年 2 月，Musk 还在公开称 Anthropic 是 "misanthropic"、"hates Western civilization"、"evil AI"。但就在这条推文发布的同一天，Anthropic 宣布签下 SpaceX Colossus 1 的全部算力（220,000 张 GPU、300+ 兆瓦电力，年付 30 至 40 亿美元）；Musk 宣布 xAI 将作为独立公司解散，全部并入 SpaceX，改名为 SpaceXAI。
>
> 是什么让世界首富在 90 天内 180 度转弯？答案不在 AI 里，在资本里。要看懂这件事，必须从 xAI 自身的兴衰、SpaceX 的 IPO 野心、X 的真实角色、Tesla 的下一步、Anthropic 的供需缺口五个维度同时观察。
>
> 原稿后续详细展开了五个维度：xAI 创始团队（11 位联合创始人 2026 年 3 月全部离职）、Grok 的技术 benchmark 与变现失败、合并 SpaceX 的四个真实动机（资本套利、IPO 故事升级、政府渠道继承、避免独立融资）、SpaceX 的财务真相（2025 年营收 155 亿美元、EBITDA 80 亿、利润率 50%+）、X 在帝国里的归属变迁、SpaceX 反向收购 Tesla 的 80-90% 概率、轨道数据中心的五个工程问题、Colossus 1 闲置率 11% 与 IPO 审计师的供需困境、Musk 修辞与商业决策的长期不一致、19 世纪商业君主制的历史类比，最终落在"商业君主制在数字时代的一次完整演练"这个结论上。
