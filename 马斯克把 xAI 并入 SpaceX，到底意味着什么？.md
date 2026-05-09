2026年5月6日早上，Elon Musk在X上发了一条推文：

> "我跟 Anthropic 的人见了几面。我的邪恶探测器没响。"

读到这条推文的人都愣了一下。

90天前，Musk还在公开骂Anthropic是"misanthropic"（厌恶人类的）、"hates Western civilization"（憎恨西方文明）、"evil AI"。再往前一年，他嘲讽过Anthropic的Constitutional AI是"enforced diversity"，强加的多元主义。在这之前的两三年里，Musk嘴里几乎没有说过一句Anthropic的好话。

但就在这条推文发出来的同一天，两条新闻从两个方向砸了过来。Anthropic宣布签下SpaceX的Colossus 1超算，22万张GPU、300多兆瓦电力，全部用来跑Claude，年付30到40亿美元。同一天，Musk宣布xAI将作为独立公司解散，全部并入SpaceX，新名字叫SpaceXAI。

世界首富在90天里从骂街到合作，发生了什么？

要说清这件事，必须从五条线一起看：xAI这家公司这两年是怎么活过来又怎么撑不下去的；SpaceX为什么需要它；X在Musk帝国里到底扮演什么角色；Tesla可能就是下一个；以及Anthropic的算力缺口在2026年大到什么程度。把这五条线接起来，你会发现这次合并跟AI技术本身关系不大，跟资本结构关系很大。

# 一、xAI这家公司是怎么走到这一步的

## 1.1 从一份招聘清单开始

故事的起点在2023年初。Musk跟OpenAI已经闹翻——那个他参与创办的非营利组织变成了估值千亿的盈利公司，主导权落在Sam Altman手里。Musk嘴上的指控是OpenAI"背叛了创始使命"，账本上的逻辑很简单：他要造一个新的对抗性AI公司。

2023年3月9日，xAI在内华达州悄悄注册。4个月后正式对外亮相，使命写得很大：理解宇宙的真实本质（understand the true nature of the universe）。但xAI真正吓人的部分在它的初始名单上，口号本身意义不大。Musk把12个人从OpenAI、DeepMind、Google Brain、Microsoft Research一个一个挖了出来。

Igor Babuschkin，前DeepMind和OpenAI工程师，挂首席工程师。Yuhuai "Tony" Wu，前Google DeepMind。Christian Szegedy，前Google，深度学习里搞GAN和inception那一拨人。Jimmy Ba，多伦多大学副教授，整个深度学习行业每天都在用他和合作者2014年那篇论文里的Adam优化器。Greg Yang，前Microsoft Research。Kyle Kosic等另外几个人，也都是顶尖实验室出身。

Musk给他们的承诺是研究自由加影响力。你来这里造的是"理解宇宙"的AI，做产品只是顺带的事。对一群泡在论文堆里的人来说，这是Big Tech之外最有诱惑力的故事。

后面发生的事情比所有人预料的都快。2023年公司估值6.7亿美元；2024年涨到240亿；2025年涨到500亿；2026年1月Series E一轮融资20亿美元，估值2300亿；2月并入SpaceX，合并实体估值1.25万亿。3年里估值翻342倍。这个速度，连2010年代那批最热的AI公司加起来都没跑出来过。

## 1.2 Grok打榜成绩很猛，但企业不买账

技术上Grok也确实给力。2025年底到2026年初，Grok 4和4.1在LMArena的Text Elo榜上排到1483，全球第一。Humanity's Last Exam这种被设计成模型很难做对的考题，Grok做到50.7%，依然第一。AIME数学题91.7%。一个常常被Musk称为"理论物理级"的模型，benchmark上的表现确实够看。

但代码这一项Grok输给了Claude，SWE-bench Verified Grok 75% vs Claude 87.6%。这一项之所以致命，是因为代码是2025到2026年企业市场的核心场景。Cursor、Claude Code、GitHub Copilot这一类工具的兴起，让"AI写代码能不能用"直接挂钩到了模型的企业付费率。

把xAI跟Anthropic的财务并排放，差距大到不需要解释。xAI 2025年的年化收入大概3亿美元，季度净亏14.6亿，每月烧10亿美元。Anthropic 2026年初的年化收入是300亿美元，已经接近盈亏平衡。Anthropic Claude的企业订阅可以做到211美元一个月一个用户，OpenAI的ChatGPT普通版25美元一周。同样的token，Anthropic能多收三五倍的钱。

xAI赌的是"AI是消费/分发战争"——Grok直接嵌进X的5亿用户里靠免费流量做分发。Anthropic赌的是"AI是企业基础设施战争"——卖token给开发者，让Claude Code在程序员的工作流里上瘾。两条路都有人押。结果押第二条的赢得彻底。Anthropic用5%于ChatGPT的用户量，做到了OpenAI 40%以上的收入。

Grok的问题不在模型本身。问题在路线。Musk选的那条消费战争的路，在2025到2026年的市场结构里跑不出钱来。

## 1.3 11位联合创始人是怎么一个一个走的

到2026年3月，xAI的11位联合创始人全部离职。算上80多名研究员和工程师集体出走。一家不到3年的公司，初始团队走得一个不剩，这在AI行业是少见的事。

故事真正的转折点是2026年2月10日和11日。

2月10日下午，Tony Wu在内部Slack发了一封告别信。他没说去哪，只说"AI这件事，要按它本来的节奏做"。第二天，2月11日，Jimmy Ba也走了。

Jimmy Ba离职这一刻很关键。他不是普通员工。他是Adam优化器的作者之一，整个深度学习行业每天都在用他论文里的算法做训练。一个写出来基础工具的人离开一家AI公司，意味着的是这家公司在他眼里已经无可救药了。

接下来一个月，瀑布效应开始。Babuschkin走，他没去别的实验室，自己开了家VC基金，等于"我看好AI赛道，但不看好这家公司"。Dai走、Zhang走、Pohlen走、Kroiss走、Nordeen走。到3月底，11个人一个不剩。一位还没走的xAI工程师对外说了一句被反复引用的话：

> "AI开发那种流动的、探索性的本质，被Starship和Starlink项目里那种刚性的、里程碑式的指标取代了。"

这句话把所有问题点穿了。

xAI当初按"研究实验室"招的人。这些人习惯长实验周期、试错驱动、论文导向、自由探索。但2026年初合并SpaceX之后，Musk把他在火箭和工厂那一套硬件文化整套搬过来：每天12到16小时工作；任何时间消息要30分钟内回复；产品决策不在xAI内部Slack谈，而是在X上一个300人的大群里拍板；内部把xAI重组成"模块化、产品驱动的组织"，参照Starship和Starlink的里程碑式管理。

Starship可以这么管，因为火箭工程的目标足够具体——要把多少吨送上轨道，落在哪里。AI研究不是这个性质，它的产出常常需要几个月的探索才会有方向感，而且你做不到的事情AI模型自己也做不到。把火箭那套节奏搬到AI研究里，等于让一群本来要画地图的人天天写日报。这群人留下的概率几乎为零。

Musk自己罕见地公开承认了这件事。他在X上发的原话是：

> "xAI was not built right first time around, so is being rebuilt from the foundations up."（xAI第一次没建对，正在从基础重建。）

这是过去十年Musk最罕见的一句承认错误的话。但他没把xAI拆掉重新雇人——他把xAI整个塞进了SpaceX。

## 1.4 为什么必须塞进SpaceX

对外说的理由很大：轨道数据中心，垂直整合AI。听起来非常Musk。

但拆开看真实动机，在四个层面上都说得通。

第一个是资本套利。月烧10亿美元的亏损单独立着是个炸弹，藏进Starlink 80亿美元利润的母舰里就只是一行注脚。独立公司每12到18个月要融一轮，每轮要给投资人讲一个新故事；塞进SpaceX之后，这些麻烦消失。

第二个是IPO故事升级。SpaceX单独上市，按Starlink的SaaS估值倍数算大概5000到8000亿美元。加上"AI加 太空"这个故事，估值跳到1.5到2万亿。多出来的7000亿到1.2万亿，全部来自叙事溢价。

第三个是政府渠道。Anthropic 2025年被五角大楼定为"供应链风险"，丢了一份2亿美元的合同。SpaceX跟五角大楼、NASA、情报机构关系深得多，Grok借SpaceX的渠道直接拿政府合同，比xAI单独申请要快很多。

第四个最现实：xAI如果继续独立，下一轮根本融不到钱。季度亏14.6亿，月烧10亿，11位联合创始人全走光，这种公司在2026年的市场上拿不到Series F。

合并对Musk个人是好事。对xAI这家公司本身则是被吞掉、被肢解、被改造。"xAI"作为独立AI实验室的品牌，从那天起就消失了。

# 二、合并之后的SpaceX

## 2.1 表面上的赢家

SpaceX的财务在2025年是亮眼的。营收155亿美元，比2024年涨18%；EBITDA利润80亿，利润率超过50%。这里面Starlink贡献大头，约100亿美元，每年增长又快又稳。这是全球商业航天里唯一真正赚钱的公司。

但合并完xAI之后，SpaceX的资产负债表就变得复杂了。账面上多出一个年亏60亿美元的AI公司，外加一个年亏几十亿、还在还120亿美元收购债务利息的X。Starlink的现金流要先去喂这两个无底洞，剩下的才能继续投星舰、星链卫星。

监管包袱也跟着传染。xAI在印尼和马来西亚被国家级封禁，欧盟有一系列调查，深度伪造的集体诉讼还在审。这些原本跟SpaceX没关系，合并之后全都进了同一份招股书。

招股书是这场IPO的核心文件。SpaceX计划2026年6月递交S-1。审计师面对一份"火箭+卫星+AI+社交"的混合资产，要给一个估值，要回答董事会和监管机构上百个尖锐问题。"这家公司到底是干什么的"，将变成IPO路演里反复被问的问题。

但市场可能愿意忽略这些复杂度。叙事溢价的本质就是：只要故事够大，投资人会主动忽视冲突。"AI加太空"这个组合在2026年的资本市场是黄金叙事，估值多打一万亿都有人接。

## 2.2 X在帝国里走过的奇怪路径

X这家公司的归属变迁是一条曲折到搞笑的路径。

2022年10月，Musk以440亿美元个人收购Twitter，私有化后改名X。2025年3月，Musk把X卖给xAI，估值330亿美元，缩水25%。2026年2月，SpaceX收购xAI（连带X一起），这一次xAI整体估值从800亿跳到2500亿。2026年5月，xAI法律实体解散，X直接归SpaceX/SpaceXAI。

注意中间一个细节。2025年3月律所Sullivan & Cromwell给X的估值是330亿，比2022年Musk的440亿收购价缩水了25%。但11个月后SpaceX收购xAI（含X）时，xAI整体估值从800亿跳到2500亿。X在账面上贬值了，作为"xAI的一部分"被打包卖给SpaceX时，又被以更高估值算了进去。

这种通过反复打包来注入估值的玩法，是Musk帝国资本运作最核心的套路。一份资产，单独看没什么人买；放进一个更大的故事里，估值能涨好几倍。

X的真实角色其实是为Grok服务的：实时数据训练Grok、用户对话做RLHF、社交分发渠道。给SpaceX的火箭和卫星业务则没有直接帮助。但作为故事，X是Musk帝国"全栈互联网"叙事不可或缺的一块拼图。没有X，Musk的帝国就只是火箭加AI；有了X，他就能讲"轨道发射、卫星连接、内容分发、AI推理"这条端到端的产品链。

## 2.3 真正的下一步：SpaceX反向收购Tesla

很多人以为合并xAI是Musk的终局。其实这只是中场。下一步分析师们已经在公开下注：SpaceX反向收购Tesla。

Tesla和SpaceX的财务对比放在一起看，会让你重新思考这两家公司谁是谁的母舰。

Tesla 2025年营收948亿美元，是SpaceX的6倍。但Tesla的GAAP利润是38亿，同比下降46.5%；增长是负的2.9%，史上第一次年度营收下降。SpaceX只有155亿营收，但EBITDA利润80亿，利润率50%以上，增长18%。Tesla市值1.5万亿，市盈率343到364倍；SpaceX如果按合并实体估值1.5到2万亿IPO，市盈率反而会比Tesla低。

把这件事翻译成大白话：Tesla营收大但赚不到钱，SpaceX营收小但赚钱凶猛。如果两家合并，财务上是SpaceX在救Tesla，而不是反过来。

Wedbush的Dan Ives给SpaceX反向收购Tesla的概率打到80%到90%，时间窗口2027年上半年。前Tesla总裁Jon McNeill估的概率是50%以上。

但财务只是表层原因。真正的关键是股权结构。

Tesla是单一股权公司，Musk持股仅13%，几乎没有正式控制权。过去几年他在特拉华州法院、在股东集体诉讼里来回拉锯，每一次都是因为他作为CEO的权力跟股东信任之间的冲突。SpaceX是双层股权，Musk持股42%，控制79%投票权。

合并之后，Musk可以用SpaceX的双层股权架构，把Tesla原本公众股东的影响力永久消除。SpaceX招股书里有一句话很关键：Musk只能由Class B持有人投票才能被解雇。简单翻译过来，只有Musk自己能解雇Musk。

这才是Musk这十年所有资本运作的真正终局。整个Musk帝国（火箭、卫星、AI、X、Tesla、Optimus）锁进一个他永久控制的合并实体，公开股东出钱但没有发言权。

19世纪的铁路大亨也用过这套玩法，那时候叫"trust company"（控股信托公司）。后来美国搞了反托拉斯法把这套东西拆掉。一百多年后，Musk在数字时代用一套现代化的双层股权重新组装出来。

## 2.4 轨道数据中心是个故事，不是工程项目

并购公告里有一个很出彩的承诺：未来Colossus将搬到轨道，做"太空数据中心"。Anthropic也在跟SpaceX谈未来部署多吉瓦的轨道AI算力。

听上去非常Musk。但工程上，这件事在十年内基本不可能。

太空有五个工程问题，没有一个被解决。

第一个是散热。地面数据中心靠空气和水带走废热。太空只能靠辐射散热，效率低一个数量级。Colossus 1的300兆瓦放上去，需要足球场大小的散热板，且不能折叠（折叠的散热板做不出来这种功率）。

第二个是能源。300兆瓦在地面可以接电网，在太空只能靠太阳能。300兆瓦相当于1.5平方公里的太阳能板，约210个标准足球场。把这种东西送上轨道，发射成本以亿美元计。

第三个是维修。GPU在轨道上的故障率比地面高10倍以上，主要是辐射诱发的位翻转。Colossus有22万张GPU，地面机房一年坏几千张是正常的，轨道上一年可能坏5万张，没有人能上去换。

第四个是辐射加固。H100这种现代GPU不是辐射加固设计的，必须从头设计芯片，性能至少倒退5到10年。NASA和SpaceX自己的航天器用的芯片普遍是几代之前的产品。

第五个是带宽和延迟。LLM训练对GPU之间的同步延迟极敏感（毫秒级），太空数据中心和地面之间的延迟是数百毫秒，这种节奏跑不动现代大模型训练。

这五件事每一件都是几十亿美元的工程难题，五件事叠加起来，没有任何2030年前能跑通的迹象。

但这跟IPO估值有什么关系吗？有，而且很大。

Musk商业模式的精髓就是：讲一个20年才能证伪的故事，但金融价值今天就兑现。Hyperloop 2013年承诺LA到SF 30分钟，12年过去了基本破产。Boring Company承诺改变城市交通，结果是拉斯维加斯一段单线隧道。Mars殖民2024载人，推迟到2030+。Robotaxi 2019年承诺2020年100万辆无人车，6年后还在内测。FSD从2016年起每年承诺"明年实现完全自动驾驶"，承诺了9年。

这些故事每一个都没兑现。但每一个故事在被吹的那个年代，都给Tesla或SpaceX的估值贡献了几百亿到几千亿美元。等市场反应过来时，早期投资人已经套现走人。

轨道数据中心很可能是这个名单的下一个。SpaceX招股书里写一句"未来部署多吉瓦的轨道AI算力"，对短期估值的拉动可能就是几百亿美元。十年后兑现不兑现，那是十年后的事。

外行听到"AI加太空"会激动；工程师听到"AI加太空"会摇头；只有华尔街听到"AI加太空"会签支票。Musk对这三类人的反应了若指掌。

# 三、Anthropic为什么突然成了战略伙伴

## 3.1 一组让审计师睡不着觉的数字

5月6日的合作公告之所以让所有人意外，是因为它在Musk的修辞框架里完全说不通。但放进Colossus 1的财务现实里，它就是唯一能走的那条路。

Colossus 1是Musk2024到2025年砸出来的超算项目，部署在田纳西州的孟菲斯。一共555,000张GPU，180亿美元采购成本。盖这个东西的时候，xAI赌的是Grok要带着X的5亿用户冲消费AI市场，需要海量算力做分发。

但2026年初，The Information报了一个数字：xAI的Colossus 1实际算力利用率，只有11%。

11% 是什么概念？意思是用180亿美元买的硬件，89%的时间在那儿空转。

对一家正常运营的公司，89%闲置只是浪费。但Colossus 1的拥有方SpaceX要在2026年6月递交S-1，准备IPO。审计师面对这种闲置率，只有几条路可以选。

第一条是资产减值。把180亿美元的硬件按实际利用率打折，可能要减值几十亿。这一笔砸进招股书，IPO估值要被砍掉很大一块。

第二条是把闲置算力作为产能储备。但产能储备要写明用于哪个客户、哪个产品。xAI自己消化不了，这个故事讲不通。

第三条是把闲置算力签长期合同租出去，把"闲置资产"变成"已签约的长期收入流"。这是唯一能让财务报表好看的方法。

问题是租给谁。

## 3.2 全世界只剩一个买家

2026年初，全世界能消化22万张GPU的客户屈指可数。

OpenAI不需要——它跟Microsoft已经绑死，加上跟Oracle合作的"Stargate"计划，自己就是算力供应方。

Google用自家的TPU，从来不外采H100这种规模。

Microsoft早就跟OpenAI深度绑定，多余的算力还要分给Azure客户。

Meta自己已经买了几十万张H100做内部用，不缺。

Amazon有Trainium和自己的Anthropic投资，关系微妙。

剩下的只有Anthropic。

Anthropic 2025年下半年开始在公开场合抱怨"用户体验在崩"——Claude Code的5小时使用配额经常被开发者用爆，Opus API的速率限制紧到企业客户开始流失。这家公司缺算力到什么程度？它在2025年Q4就已经在跟AWS、Google Cloud谈一切可能的算力来源。但这两家都跟自己的AI业务有冲突，给Anthropic的算力都是有保留的。

Anthropic IPO在即，2026年初公开估值已经到9000亿美元路演阶段。它需要的不只是算力，是"未来一两年算力不会断"的那个保证。

所以严格说，这不是Musk选了Claude。是Anthropic在2026年初是市场上唯一能消化Colossus 1闲置产能、还付得起30到40亿美元一年的客户。Musk没什么选择空间。Anthropic也没什么选择空间。

90天前还在互相骂街的两家公司，因为各自的财务现实，走到了同一张合同上。

## 3.3 这笔交易对双方的真实价值

对Musk的好处直接体现在招股书上。180亿美元的闲置硬件不再是负担，变成了一份多年期的高利润收入合同。审计师可以算这笔账：Anthropic每年付30到40亿美元，毛利率假设60%，光这一份合同就能给IPO贡献几百亿估值。

舆论层面，Musk也有套话术可以用。从"骂Anthropic是邪恶AI"变成"我亲自审查了它的安全文化，邪恶探测器没响"。这是Musk一贯的修辞翻篇方式——发条推文圆回来，过去的话当作风。

法庭上Musk还有更隐性的好处。他正在加州法院告OpenAI和Sam Altman。在诉讼里把Anthropic定位成"安全AI替代品"，能给他的指控加一层叙事支撑。同时合同里据说有一条"Humanity Clause"——如果Musk认为Claude在做"危害人类"的事，可以切断算力。这给了Musk对竞争对手运营层面某种否决权，理论上他可以在关键时刻威胁Anthropic。

对Anthropic的好处也很清楚。算力解渴最直接，签约公告之后第二天Claude Code的5小时配额翻倍，Opus API上限大幅提高。它没有向OpenAI阵营投降，也没有向Google让步。最关键的是IPO路演弹药——把"用户体验在崩"的故事改写成"已锁定22万GPU"。

这笔交易在两边的财报和叙事上都是双赢。中间被牺牲的只是2024到2025年Musk在社交媒体上对Anthropic的所有评价。

## 3.4 Musk的修辞和商业决策从来都是两条线

如果你只追Musk在X上的发言，会被他骂街的剧烈程度吓到。但如果只看他签的合同，他几乎没有什么"原则性"的对抗。

骂Bezos是常态，但跟Amazon Kuiper（亚马逊的卫星项目）既竞争也合作。骂广告主"go fuck yourself"，第二年又求他们回来。骂中国制造，但Tesla的上海工厂是全球最赚钱的Tesla工厂，他每年要去签订单。骂OpenAI是"异端"，转身告OpenAI，同时挖OpenAI的高管来xAI。

Musk的修辞和商业决策几乎从不一致。他骂Claude时是在打舆论战；他签Anthropic合同时是在做生意。这两件事在他那里不矛盾，因为它们服务的是不同的目标。骂街是打舆论战，让自己在Twitter上保持热度，让股东相信他在战斗。签合同是赚钱，让股东相信他能交付。

他的真实优先级排序大致是：自我利益高于Musk帝国利益，Musk帝国利益高于公开承诺。如果一笔生意能给SpaceX IPO估值多1000亿美元，他骂过的话翻篇成本几乎为零。

这件事的更大含义是：少数几家AI公司控制着全行业的算力、电力、数据。台前他们怎么吵都行，台下他们必须互相租算力、互相买数据、互相挖人。Musk-Anthropic这笔交易在2026年很可能只是开始，AI行业整体已经进入"基础设施寡头"阶段。

# 四、这件事到底意味着什么

## 4.1 三层理解

最浅的一层是媒体故事。Musk反转，xAI失败，Anthropic受益。三个新闻标题就能讲完。

中间一层是商业逻辑。xAI输掉了消费战略，被迫并入SpaceX寻求续命。SpaceX需要AI故事拉高IPO估值。Anthropic需要算力填补需求缺口。三方在各自的财务约束下走到一起，本质是约束条件的耦合。

最深一层是资本运作。Musk用4年时间，通过两次反向收购（X归xAI、xAI归SpaceX），把三家原本不相关的公司捏成1.25万亿美元的合并实体。下一步可能是SpaceX反向吃Tesla，最终在双层股权下永久锁住整个Musk帝国。这是一场跟AI关系不大、跟资本结构关系很大的游戏。

## 4.2 谁赢了，谁输了

Musk个人是最大赢家。SpaceX IPO之后他的净资产可能突破6000亿美元，而且通过双层股权获得了整个帝国的永久控制权。这件事的金融价值远超过xAI的失败。

Anthropic也赢了。它拿到了关键算力，对OpenAI的领先在企业市场扩大。这家公司2026年的IPO走在最有利的时间窗口里。

SpaceX早期投资人是大赢家。从2002年Musk自己掏钱开始，到2026年合并实体估值1.25万亿美元，回报是天文数字。

输的一方比较多。

xAI的11位联合创始人和80多位研究员被驱离。他们的行业声誉还在，但2023年那个"理解宇宙真实本质"的故事死掉了。

即将买SpaceX IPO的散户用真金白银养Musk的多个亏损资产，加上双层股权剥夺投票权。他们买的是火箭加卫星加一个画的饼加没有发言权。

Tesla现有股东在反向收购真的发生时，股票可能被换成无投票权的Class A。从持有Tesla公司变成持有Musk帝国的某个分股，二者价值不一样。

AI行业的多元化也输了。前10大AI公司继续向几家超级实体集中，独立创业公司能拿到的算力、数据、人才都在变少。

## 4.3 SpaceX IPO的本质是什么

如果冷静地看，SpaceX IPO是一场精心设计的财务魔术。

帝国里有两类业务。火箭发射和Starlink是现金流引擎，火箭项目制收入毛利高，Starlink订阅每年100亿美元。这两块加起来一年能产生几十亿美元自由现金流。

剩下的几块都是烧钱。Grok季度净亏14.6亿，X每年亏几十亿，Colossus的算力出租是把闲置变成收入但本金都还没收回。

SpaceX IPO的本质就是：让Starlink那100亿美元现金流，去喂养xAI和X这两个无底洞，同时让公开市场的股东接盘这个组合。

而Musk通过双层股权（持股42%、控制79%投票权），让股东出钱但管不了钱怎么花。

这就是合并的金融逻辑。它不是为了"垂直整合AI"——这只是对外说辞。它是为了把帝国里所有亏损的资产藏进一个赚钱的母舰，然后通过IPO把账面问题转移给公开市场。

## 4.4 19世纪的旧戏，21世纪的新外壳

借用一个历史类比。

19世纪后半期到20世纪初，美国出现过一批"商业君主"——Cornelius Vanderbilt（铁路）、John D. Rockefeller（石油）、Andrew Carnegie（钢铁）、J.P. Morgan（金融）。这些人的玩法都是"控股公司套娃"加"双层股权"，控制从原料到运输到销售的整条产业链。Standard Oil最高峰时控制美国90%以上的炼油产能。

后来美国搞反托拉斯法，把这些垂直垄断的帝国一个一个拆掉。这是上个世纪初进步主义运动的核心议题。

100多年后，Musk把同样的玩法装在21世纪科技公司的外壳里。从Starlink（互联网基础设施），到X（内容），到xAI/Grok（AI），到Colossus（算力），到Terafab（芯片），到Starship（发射），到Tesla和Optimus（具身智能）。这是一个垂直整合到端到端的科技帝国。

跟100年前相比，这次的差别有两个。一是科技公司的双层股权架构在法律上是被允许的，反托拉斯法对这种垂直整合的约束很弱。二是合并实体里的某些业务还在亏损，但通过叙事溢价，IPO估值仍然能撑起来。这套打法在19世纪做不到。

历史不会重复，但有时候会押韵。Musk这次玩的，是一套加了科技外壳的19世纪商业君主制。

# 五、写在最后

xAI的故事没有"被并入SpaceX"这么平淡。它是被Musk的资本野心吞噬了。

它从一个意图理解宇宙的研究实验室，变成了一艘IPO母舰里的AI调味剂。它的11位顶尖研究员先用脚投票，表达了对Musk改造的反对。整个公司接着被并入SpaceX充当IPO故事的"AI拼图"。再然后，超额建的算力被打包租给一年前还在被Musk公开辱骂的竞争对手。

每一步都是商业策略的"表演"。表演底下是用资本运作掩盖产品执行失败的精心包装。

真正的赢家是Musk个人。他用xAI的失败把自己最难管的资产（亏损的AI公司）藏进了最容易包装的母舰（即将IPO的SpaceX）。同时把自己最大的对手（Anthropic）变成了自己的付费客户。一进一出，他没付什么代价，反而把帝国的总估值往上推了一个台阶。

而我们作为旁观者或潜在投资人，要看清的是：当一个人用一套资本架构同时控制了火箭、卫星、AI、社交媒体、芯片厂和电动车的时候，"商业"两个字已经容纳不下他真正在做的事情了。

这是商业君主制在数字时代的一次完整演练。它会不会成功，要看SpaceX IPO之后这十年。它会不会被拆掉，要看下一个进步主义时代什么时候到来。

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
