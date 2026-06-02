## 引子

最近，我把2024到2026年美国和欧洲的早期AI创业公司过了一遍。挑选的范围是pre-seed、seed、Series A阶段，融资额超过100万美元，集中在四个垂直领域：法律、医疗 / 临床、销售 / 客服、金融 / 会计。再加一个补充的横切领域：AI agent和工作流自动化。

总共看下来25家核心公司，加上agent领域里另外几家代表性玩家。这份名单是公开报道里能查到的代表性样本，远谈不上全市场普查，但已经够大到看出一些规律。

我感兴趣的是创业方法论的问题：在大模型commodity化的今天，什么样的人能成功做垂直AI？做这件事需要什么资源、走什么路径、避免什么坑？

提前剧透一句话核心结论：**圈外人是这个赛道的主流玩家，但完全没有资源的纯素人在这份名单里找不到成功案例**。圈外人能跑出来，靠的是某种"非行业但稀缺"的入场券：技术血统（前Google / OpenAI / Meta）、连续创业积累、加速器背书、或者顶级投资人人脉。零起点的人不在这个赛道。

文章按两段式走。前半部分按领域过25家公司，每个领域列全样本，挑两三家代表性公司展开讲故事。后半部分把所有观察合并，给出六条核心规律。读到第二部分时，前面铺过的具体公司会作为证据反复出现。

# 一、法律（10 家）

法律是垂直AI创业数量最多的赛道。原因有两个：律师工作严重依赖文本（合同、起诉状、证据、研究），是LLM天然适用的场景。美国律师行业又是出了名的高收费、低效率、对工具买单意愿强，付费意愿高。

| 公司         | 累计融资      | 阶段               | 做什么               |
| ---------- | --------- | ---------------- | ----------------- |
| Eve        | 1.5亿（含B轮） | Series B（已毕业出早期） | 给原告律所做AI          |
| Spellbook  | 约8000万    | Series B（已毕业）    | 嵌在Word里的合同起草      |
| Paxton     | 2800万     | Series A         | 法律研究与起草           |
| Crosby     | 2580万     | seed + A         | agentic律所做合同审查    |
| AttiFin AI | 约670万     | seed             | 英国法律科技            |
| Parambil   | 600万      | seed             | 大规模侵权 / 人伤 / 医疗事故 |
| Theo AI    | 420万      | seed             | 诉讼结果预测            |
| GitLaw     | 300万      | pre-seed         | 给创业公司做合同          |
| Soxton AI  | 250万      | pre-seed         | AI法律支持            |
| Jurisage   | 约200万     | pre-seed         | 法律研究              |

这10家里挑三家详细讲，分别对应"圈外人+大资本"、"PLG自助式"、"圈内人+人脉"三条典型路径。

## 1.1 Eve：圈外人 + 大资本路径

Eve现在已经不算严格意义的早期了。2025年9月拿了Spark Capital领投的1.03亿美元Series B，估值10亿美元，成了独角兽。但它的起点很早期，2020年成立时叫Butler Labs，做的是通用文档处理API（document extraction APIs），帮开发者从合同、发票、表单里抽取结构化数据。2023年才转型法律市场，公司改名Eve。

创始团队三个人：Jay Madheswaran（CEO）、Matt Noe（CPO）、David Zeng（工程负责人）。三人都来自一家叫Rubrik的数据公司，Jay是Rubrik第一位工程师兼产品工程负责人，另两人是Rubrik早期明星工程师。这是典型的"技术血统"团队。但Jay还多一层资源：他创业前在Lightspeed做过早期企业AI投资人，既懂技术又懂投资。

融资节奏：Butler Labs时期有一笔Menlo Ventures等参与的seed VC（具体金额和日期未公开）。2023年10月公司转型法律改名Eve时拿了1400万美元扩展融资。a16z做Series A 4700万美元（2025年1月），理由是Eve当时年增长率800%，Lightspeed和Menlo Ventures参投。Spark Capital做Series B 1.03亿（2025年9月），估值10亿，理由是不到两年服务了450多家律所，每年处理20万 + 法律案件，帮律所回收和解金和判决金合计35亿美元。

**怎么打通律师渠道，不是网上分发**：Eve走的是**典型的企业直销**，跟Spellbook那种"个人律师信用卡自助订阅"完全相反。98人团队里相当大比例是销售、客户成功、实施工程师，挨家律所跑demo、谈合同、做实施。打通这条渠道靠四件事叠加：

- 第一，**顶级VC资本背书是销售工具**。"Lightspeed、a16z、Spark Capital投了这家公司"本身就是律所合伙人愿意接电话的理由
- 第二，**专攻一个窄场景：原告律所**。原告律师事务所多是个体执业或小所（不像BigLaw那种几千人多层级采购），decision-maker通常就是合伙人本人，决策快
- 第三，**从elite律所开始打**。早期客户里有Mike Morse Law Firm、James Scott Farrin、Atlanta Personal Injury Law Group这些原告圈知名律所，做出标杆案例
- 第四，**同行口碑放大**。一家知名原告律所用了之后，附近 / 同领域的同行会跟。Series A之后8个月新增350家客户，主要是这种口碑传导

产品定位上：从案件受理评估开始，覆盖医疗记录梳理、起草需求函、应对证据开示，把律所改造成AI-native律所。

**对应的方法论**：圈外人 + 技术血统 + 资本人脉 + 大钱直推 + 选一个高ARPU的垂直niche专攻 + 重销售GTM（不是PLG）。这条路径成功率取决于资本和人脉，不是任何人都能复制。Spellbook的PLG路径对应"个人能下单"的产品形态，Eve的企业直销路径对应"机构买单"的形态，同一个行业里的两种GTM，差距大到像两种生意。

## 1.2 Spellbook：PLG 自助路径

Spellbook的故事跟Eve完全相反。它是2017到2018年加拿大成立的，最初叫Rally，做的是律所合同模板自动化。创始人Scott Stevenson本科学的是计算机工程，跟律师行业完全没关系，做Spellbook之前在加拿大纽芬兰开过乐器公司、做过音乐和电子游戏，再之前是一家网络监测创业公司的工程总监。整个履历跟"传统精英创业者画像"完全相反。

Rally时期磨了五年，律师反复反馈说模板对初级律师有用，但抓不住高级起草的细微差别，痛点没解决。转折点在2022年9月，趁着GPT-3和ChatGPT爆发，Spellbook推出了市场上**第一款生成式AI合同起草工具**。几个月内6万人加入候补名单，需求远超预期。公司从Rally改名Spellbook，拿了1090万美元（Moxxie Ventures领投，Thomson Reuters等参投）。

之后是2000万美元Series A，再到2025年10月Khosla Ventures（Keith Rabois个人领投）的5000万美元Series B，估值3.5亿美元，累计融资超过8000万美元。客户包括Nestlé、eBay、Kennedys等，平台上累计审查过1000万 + 合同。

产品形态是嵌在Microsoft Word里的AI合同副驾驶，能起草新条款、给修改建议、列谈判要点、生成条款摘要。最重要的事是它的销售模式：**个人律师用私人信用卡自助订阅，自下而上渗透到企业法务**。这条路完全绕开了"卖给大律所合伙人"那条传统销售路径。到2025年底，约一半收入来自大所和企业法务，是从个人订阅自然生长上来的。

**对应的方法论**：圈外人 + 多年连续创业积累 + 选一个"个人能直接下单"的产品形态（Word插件）+ 抓住generative AI的时机窗口 + 候补名单做冷启动 + 后期自然上移到企业。这条路对资本要求低、对产品判断力要求高。

## 1.3 Crosby：圈内人 + 顶级人脉路径

Crosby是第三种打法。它2024年纽约成立，做的事跟其它家不一样，**自己开了一家律所**，雇律师 + 配上内部AI，对外提供合同审查服务。这是一个混合型AI律所，融资额按"律所"看大得离谱（早期阶段累计2580万美元）。

创始人Ryan Daniels（CEO）本人是律师，父母都是法学教授，毕业后在科技圈头部律所Cooley起步，之后差不多干了十年创业公司的法务。他在上一家公司是唯一的法务，发现合同谈判成了公司增长的瓶颈，这就是Crosby的由来。CTO John Sarihan是技术联合创始人。这是典型的"行业人 + 技术人"组合。

但Crosby真正打动VC的是人脉路径。2025年6月Sequoia做了580万美元的seed轮（Josephine Chen和Alfred Lin领投），原因之一是Sequoia的内部律师Cindy Lee跟Daniels都从Cooley出来，认识多年。同年10月Index Ventures又领投2000万美元Series A，Bain Capital、Sequoia、Elad Gil、Patrick Collison、Cooley律所自己参投。客户里有Cursor这种明星创业公司。

产品形态是通过Slack原生界面交付合同审查，团队直接把合同发给Crosby，通常一小时内拿到专业法律意见。

**对应的方法论**：圈内人（律师 + 顶级律所 + 法学教授背景）+ Cooley同门人脉 + 顶级VC私交。这条路靠的是身份和关系，不是产品PMF的胜利。Daniels的律师身份和Cooley履历是别人买不到的入场券。

## 1.4 Paxton：圈外人 + MIT + 资本经历的路径

Paxton 2023年成立，俄勒冈州Bend / Portland。最初做的是给大银行的监管合规方案，后来转型法律。

创始人Tanguy Chau（CEO）和Michael Ulin（CTO），两人都是AI工程师，十年前在麦肯锡共事认识。Chau在MIT拿了硕士、博士、MBA，之前在硅谷做了约七年Series A基金的风险投资，早年就投过Ironclad、Casetext这些法律AI公司。Paxton是他创立的第三家公司。

团队参加了Unusual Ventures的Unusual Academy加速器，在那里完成了从大银行合规到法律市场的关键转向。2023年9月seed 600万美元，2025年1月Series A 2200万美元由Unusual Ventures领投，总融资2800万美元。

产品是法律研究与起草平台，主打准确和可溯源，每句话都能链接回原始法条，在Stanford法律幻觉基准上有94%的非幻觉率。面向单人执业者和小型律所。

**对应方法论**：圈外人 + 顶级名校血统（MIT博士）+ 资本人脉（自己当过7年VC）+ 加速器背书（Unusual Academy）。to C为主（单人执业者和小所，公开定价、信用卡自助开通、7天试用）。

## 1.5 Parambil：医疗 + 法律交叉的少见圈内人案例

Parambil seed 600万美元，Bling Capital领投。创始团队为Sara Cordrey、Liam Gordon和医学博士Ralph Horwitz。

产品专注一类很具体的法律业务：大规模侵权（mass tort）、人身伤害、医疗事故案件。这些案件的特点是医学事实和法律事实交织，需要懂医疗的人才能高效梳理证据。Parambil用AI把法律、医疗、专家数据结构化分析，帮诉讼团队更快更可靠地评估高风险案件。

**对应方法论**：偏圈内人（创始团队有医学博士，懂医疗事故案件的特殊性）+ 法律科技圈的战略天使背书。to B（卖给诉讼团队和律所）。这是这份样本里少见的"跨行业内人"配置。

## 1.6 Theo AI：诉讼结果预测的早期玩家

Theo AI 2023年加州成立，seed 420万美元。CEO为Patrick Ip。

产品做诉讼结果预测：用AI给进来的法律索赔按预测风险敞口和可能的和解价值排序。这是给律所、诉讼基金、保险公司用的，帮他们决定哪些案件值得投入资源。

**对应方法论**：圈外人技术团队 + 产品驱动 + to B（卖给法律团队）。公开信息有限，处于很早期。

## 1.7 GitLaw：给创业公司的自助合同工具

GitLaw pre-seed 300万美元，Jackson Square Ventures领投。2025年由连续创业者Nick Holzherr创立。

产品基于一个免费的、社区贡献的1000多个律师审核过的模板库，AI agent帮用户起草、修订、审查合同，面向创业公司和小企业。这条线跟Spellbook走的是同一条PLG路径，只是更聚焦"小企业自助"这个细分。

**对应方法论**：圈外人（连续创业者，不是律师）+ 连续创业者本身就是资源（有创业经验和资本通道）+ 产品驱动（面向创业公司自助使用）+ to C为主。

## 1.8 AttiFin AI：英国早期玩家

英国法律科技公司，2025年宣布seed约500万英镑（约670万美元），计划2026年上线平台，资金用于招募AI工程、平台工程和数据人才。

属于刚起步阶段，公开信息有限，无法判断创始团队画像。值得记录的是英国和欧洲市场也开始有可观的早期法律AI资金进来，跟美国市场有时间差但量级相当。

## 1.9 Soxton AI：刚起步的法律支持工具

Soxton AI pre-seed 250万美元，做AI法律支持。处于很早期，公开信息有限。

## 1.10 Jurisage：加拿大早期法律研究工具

Jurisage pre-seed约200万美元（加拿大），做法律研究工具，由CiteRight等关联机构孵化。处于很早期，公开信息有限。

**这三家（AttiFin AI / Soxton AI / Jurisage）一起看**：都是pre-seed级别、几百万美元、信息有限。在这份名单里属于"还没到能下判断"的阶段。它们的存在本身说明早期法律AI赛道密度很高，几十家在同时尝试。

# 二、医疗 / 临床（6 家，合计约 8400 万美元）

医疗AI的早期玩家集中在"减轻医生行政负担"这个具体场景，最典型的就是AI病历记录（ambient scribe）。医院系统采购周期长、决策慢，所以早期赢家都绕开医院，直接卖给个体医生和小诊所。

| 公司 | 累计融资 | 阶段 | 做什么 |
|---|---|---|---|
| Freed | 3400万 | Series A | AI病历记录 |
| Valerie Health | 3000万 | Series A | 医生的AI前台 |
| Cascala Health | 860万 | seed | 急性后期护理临床智能 |
| Auxira Health | 780万 | seed | 虚拟心脏病学 |
| YC诊所agent | 540万 | seed | 诊所电话 / 排班自动化 |
| WorkDone | 180万 | pre-seed | EHR文档合规 |

## 2.1 Freed：纯 PLG 的典范案例

Freed 2023年1月加州Santa Rosa成立，两位创始人都是前Facebook工程师。Erez Druk（CEO）数学和计算机出身，2013年到美国进Facebook，干了快四年，2017年创了第一家公司UrbanLeap，2022年关掉。Andrey Bannikov（CTO）在Facebook待了十年。这是典型的"大厂技术血统"团队。

创业灵感的来源很具体：Druk的妻子Gabi Meckler是加州一家社区诊所的家庭医生，常年被病历文书淹没。有一天Druk问她想要什么，她说"帮我写病历"，于是有了Freed。这是founder-market fit的一个微妙变种：创始人本人不是医生，但有一个非常近的医生家属，能持续输入真实痛点。

2025年3月Series A 3000万美元由Sequoia领投，累计融资3400万美元。但真正惊人的是它的增长数据：到融资时已经有1.7万付费医生（很快涨到2万），覆盖96个专科，每月处理200万次门诊。从0长到几千付费医生主要靠口碑，增长率像Slack、Zoom这种消费级SaaS。它**刻意绕开医院的漫长采购流程，直接卖给个体医生和小诊所**，每月 $99单医生订阅。

产品形态是AI病历记录：看诊时打开app按开始，AI听医患自然对话，自动生成SOAP病历，还会学习每个医生的措辞和模板偏好。

**对应的方法论**：圈外人技术团队 + 一个懂行的家属持续输入痛点 + 选一个"个人医生能直接下单"的形态（绕开医院采购）+ $99自助订阅 + 完全靠口碑增长。这是这份名单里PLG玩法的标杆案例。

## 2.2 Valerie Health：成立当年拿 A 轮的速度异常案例

Valerie Health 2024年纽约成立，Series A 3000万美元。做医生的AI前台，覆盖诊所前台电话、排班、患者沟通这一整套行政工作。

值得注意的是融资速度：2024年成立当年就拿A轮3000万美元，这在医疗AI早期赛道里属于异常快。能这么快拿到A轮，通常意味着创始团队本身有强背书（前大厂、前知名医疗AI公司管理层、或顶级VC早期backing），但公开创始人信息较少，难以精准定位。

**对应方法论**：速度异常快说明团队有较强背书。倾向圈外人 + 顶级资本路径。to B（诊所前台是机构采购）。

## 2.3 Cascala Health：机构孵化模式

Cascala Health 2024年初成立，seed 860万美元，由Redesign Health孵化、Flare Capital Partners早期投资。

做急性后期护理（post-acute care）的临床智能平台，把实时洞察嵌进临床医生现有的工作流。**Redesign Health是一家专门孵化医疗公司的venture studio**，它会自己组团队、起项目、配资金，孵化好了再找其它VC接力。这条路径在医疗领域很常见，因为医疗行业的复杂度需要专业孵化器降低初创难度。

**对应方法论**：偏信任驱动（有机构孵化背书）+ Redesign Health这种venture studio模式。to B（卖给护理机构）。这条路对个人创业者意味着：可以应聘venture studio的entrepreneur-in-residence角色，让他们配资源帮你创业，而不是从零开始。

## 2.4 Auxira Health：早期虚拟心脏病学

Auxira Health seed 780万美元，马里兰州。做虚拟心脏病学（virtual cardiology），通过远程方式提供心脏病专科服务。处于早期，公开信息有限。

**对应方法论**：信息不足，难以精准评估。但这家公司选的niche（远程心脏病专科）反映了一个普遍趋势：医疗AI早期玩家越来越多地选"窄但深"的专科，而非通用平台。

## 2.5 YC 诊所 agent：YC + 医疗创始人天使背书

这家公司seed 540万美元，投资来自Accel、YC、Sequoia scout以及多位医疗创始人。

产品是诊所电话和工作流自动化：AI agent处理诊所每天大量的来电和消息，从排班到计费到续药，已服务数万患者。这条线跟Valerie Health重叠（都是诊所前台AI），区别在于YC诊所agent走的是YC + 医疗创始人天使的路径，规模更小但路径更标准。

**对应方法论**：圈外人技术团队 + 加速器背书（YC）+ 医疗创始人天使背书。to B（卖给诊所和虚拟医疗公司）。这是YC路径在医疗赛道的标准玩法。

## 2.6 WorkDone：YC 出来的 EHR 合规工具

WorkDone pre-seed 180万美元（2025年4月），YC支持。CEO为Dmitry Karpov。

做EHR文档合规copilot：直接接进医院EHR系统，实时监测临床工作流，在理赔被拒或合规审计之前发现并解决文档问题。这是个相对窄但刚需的场景，医疗机构对"避免被拒赔"的付费意愿很强。

**对应方法论**：圈外人技术团队 + 加速器背书（YC）+ Pioneer Fund等早期投资人。to B（接进医院EHR系统）。这条YC pre-seed路径在医疗赛道里比较典型，融资量级小但门槛低。

# 三、金融 / 会计（5 家，合计约 2.55 亿美元）

会计行业的早期AI玩家少但单笔融资大。原因是会计行业**集中度高**（Top 100事务所占大头）、客单价高（一家事务所付费意愿强）、报税合规又是个绝对刚需。卖给一家中型事务所一年的ARR可能就是六位数。

| 公司 | 累计融资 | 阶段 | 做什么 |
|---|---|---|---|
| Digits | 9700万 + | 较成熟 | AI会计平台 |
| Accrual | 6500万 - 7500万 | 种子级大额 | Top 100所报税准备审核 |
| Numeric | 3800万 + | 累计 | 财务结账与对账自动化 |
| Basis | 3800万（早期）→ 现估值11.5亿 | seed→A | 会计agent |
| Juno | 1200万 | seed | AI报税 |

## 3.1 Juno：圈内人 + 行业身份案例

Juno是这份名单里最干净的"圈内人创业"案例。2023年圣地亚哥成立，创始人David Haase本人就是注册会计师，创立Juno之前自己创办并做大了一家湾区区域性会计师事务所Golden State Accounting，服务过数千客户，还有Stanford MBA。

Haase的原话是："我做这个不是因为爱AI。我做这个是因为我厌倦了错过孩子的足球赛、想回家吃晚饭。" 他在自己的事务所里把Juno迭代了一年多，去年卖掉事务所全职做Juno。

2026年4月seed 1200万美元由Bonfire Ventures领投。投资人明确说打动他们的是创始人本人就经历过这个痛点，**founder-market fit** 是关键。Juno已有近500家事务所采用，软件自动化90% 的数据录入，让CPA每单报税少花50% 时间。核心理念是AI做不到100% 准确，所以人在环里，**人类报税师是开车的人，AI是副驾驶**。

**对应的方法论**：圈内人（CPA + 自己开过事务所的几千客户网络）+ 在自己事务所里磨产品一年多 + Stanford MBA加持。卖事务所专心做产品这一步是关键。

## 3.2 Basis：圈外人 + 顶级资本案例

Basis跟Juno完全相反，是技术背景的圈外人团队。2023年成立，seed 360万美元，2024年12月Series A 3400万美元，Vinod Khosla投。现在估值11.5亿美元，严格说已经毕业出早期阶段。

产品是会计agent，做"长周期agent"（long-running agent），自主完成跨越数小时的复杂任务，覆盖客户账务、税务、审计。已被全美前25大会计师事务所里的30% 采用。

**对应的方法论**：圈外人 + 顶级VC（Khosla）+ 选一个数据天然结构化的高ARPU行业（会计事务所对自动化付费意愿高）。Basis的速度比Juno快得多，但靠的是资本不是行业身份。

## 3.3 Digits：已毕业出早期的连续创业者作品

Digits AI会计平台，累计融资9700万美元以上，投资人有GV、Benchmark。相对其它几家更成熟，已接近或超出严格意义的早期阶段。

创始人Jeff Seibert是连续创业者。Digits在PLG路径上走得比较早，最初面向创业公司和小企业自助使用，后来逐步扩展。这条路径跟Spellbook和Freed类似，都是"个人或小团队能直接下单"的形态。

**对应方法论**：圈外人（连续创业者血统）+ 大钱（GV、Benchmark）+ 先to C后扩展。是PLG在会计领域的代表。

## 3.4 Accrual：种子级大额直攻 Top 100 所

Accrual 2026年2月带着6500万至7500万美元出场，General Catalyst投。做AI-native会计平台，专攻Top 100会计师事务所在报税准备和审核环节的瓶颈。

属于种子阶段就拿大额的类型，这种融资模式在6.4节会专门讲，本质上是把融资当成销售工具。种子级别就拿General Catalyst几千万美元，本身就是Top 100会计所采购部门愿意接电话的理由。

**对应方法论**：种子级大额融资 + 顶级VC（General Catalyst）+ 直攻大客户。to B大单路径。公开创始人信息有限，但能拿到General Catalyst这种backing的团队通常有强背书。

## 3.5 Numeric：财务结账与对账的早期玩家

Numeric做财务结账与对账自动化，累计融资3800万美元以上。处于成长早期，公开创始人信息有限。

产品场景是企业财务团队每个月的"closing the books"流程，传统上要财务人员对一堆账目、做调整分录、生成报表。Numeric用AI自动化这套流程的大部分动作。

**对应方法论**：信息不足，倾向产品驱动 + to B（卖给企业财务团队）。

# 四、销售 / 客服（4 家，合计约 1.48 亿美元）

销售客服是AI agent落地最直接的场景之一：呼叫中心 + 客服文本 + 邮件本身就是大量重复劳动，对自动化的渴望和付费意愿都极高。这块的4家公司分布相对极端，一家拿了1.34亿，另外几家都在几百万级别。

| 公司 | 累计融资 | 阶段 | 做什么 |
|---|---|---|---|
| Wonderful | 1.34亿 | Series A | 多语言客服agent |
| Rime | 550万 | seed | 语音模型 |
| Leaping AI | 470万 | seed | 呼叫中心语音agent |
| Instruct | 340万 | seed | 大白话搭建agent |

## 4.1 Wonderful：异类大额

Wonderful是这份名单里最不像"早期"的早期公司。Series A 1亿美元，累计1.34亿美元，出stealth仅4个月就冲到这个量级。做多语言客服agent，覆盖语音、聊天、邮件，针对每个市场做语言、文化、监管的微调。已扩张到意大利、瑞士、荷兰等多国。AI agent每天处理数万次客户请求，解决率80%。

公开的创始人信息有限，但这个量级的种子级融资基本只能来自"早就被资本盯上的明星创始人"，否则一般融不到。

**对应的方法论**：未知。这是这份名单里"信息最不透明、融资最异常"的案例。值得留意但不能复制。

## 4.2 Leaping AI：最接近"零资源素人"的案例

Leaping AI是这份名单里最接近"完全没资源硬拼"的案例。2023年德国成立，创始人Kevin Wu（CEO）的灵感来自他在Amazon实习时去呼叫中心干了一天，意识到这是个未被自动化的大场子。

但他和CTO Arkadiy Telegin早期在德国融不到钱，**被两次拒绝**。转折是他们进了YC 2025冬季批次，搬到旧金山。YC背书加湾区network之后，收入快速增长，seed一周内就关掉，470万美元。

产品是呼叫中心语音agent，覆盖零售、电信、旅游、保险、地产，自动化率90% 以上。

**对应的方法论**：技术背景的圈外人 + 一开始没钱没资源 + **YC是救命的入场券**。Leaping AI印证了一个反面事实：纯粹零资源是不行的，**至少需要YC这种背书**才能起来。

## 4.3 Rime：做语音基础设施而非应用

Rime seed 550万美元（2025年5月），Unusual Ventures领投。做语音模型，主打的差异化是"语音质量是商业结果而非技术细节"。它的Arcana模型能产生自然的笑声、叹气、呼吸，这些细节决定了客户在电话里能不能被骗过去。

数据上Rime每月支撑1亿多次电话对话，企业客户包括Domino's、Wingstop这种连锁餐饮。它做的是基础设施层，而不是直接面对终端用户的应用。

**对应方法论**：圈外人技术团队 + 资本（Unusual Ventures）+ 选基础设施层（语音模型）而不是应用层。to B（卖给企业，做语音基础设施）。这条路差异化清晰，但跟OpenAI、ElevenLabs这种巨头直接竞争。

## 4.4 Instruct：大白话搭 agent 的横向平台

Instruct seed 340万美元，Lakestar和Creandum投，2024年融资、2025年10月公开上线。

产品定位是"让人用大白话搭建自主AI agent"，不需要技术背景，用户描述任务、连接应用，AI agent就跨多个平台执行工作。这条线跟Relevance AI、H Company重叠（都是横向agent平台），区别在于Instruct更聚焦"非技术用户自助搭建"。

**对应方法论**：圈外人技术团队 + 顶级欧洲VC（Lakestar、Creandum）+ 横向平台路线。to C为主（个人用大白话搭agent，自助）。Instruct同时算在销售客服和agent两个领域，因为它既能搭客服agent也能搭别的。

# 五、AI Agent / 工作流自动化（补充领域，9 家）

这是一个横切前面四个领域的新赛道：用AI agent替企业里某个具体工种干活。2025到2026年，垂直agent是整个AI agent赛道里融资最多的细分，单是2025年的统计就有17笔交易、合计约8.1亿美元。

赛道里分两类玩家。一类是横向平台（让用户自己搭agent），一类是垂直agent（替某个具体工种干活）。横向平台PLG友好但护城河浅，垂直agent重要客户大但销售周期长。

| 公司 | 累计融资 | 阶段 | 做什么 | 类型 |
|---|---|---|---|---|
| H Company | 2.2亿 | seed（欧洲史上最大） | 企业自动化action agent | 横向平台 |
| Eudia | 1.05亿 | Series A | Fortune 500法务agent | 垂直（法律） |
| Relevance AI | 3700万 | 累计到B | 让任何人搭AI agent团队 | 横向平台 |
| 8Flow | 1660万 | Series A | 业务流程编排agent | 横向平台 |
| Worktrace AI | 900万 | seed | 研究公司工作流再自动化 | 横向平台 |
| Mindoo | 约540万 | seed | 医院行政与临床工作流agent | 垂直（医疗） |
| Instruct | 340万 | seed | 大白话搭agent | 横向平台 |
| Gentek AI | 86万 | seed | 企业定制agent | 横向平台 |
| Rebar | 信息有限 | seed | 建筑承包商估算agent | 垂直（建筑） |

## 5.1 H Company：DeepMind 系顶级技术血统

H Company 2023年法国巴黎成立，前身叫Holistic。2024年5月一次拿了2.2亿美元seed，是欧洲历史上最大的AI种子轮。

创始人5位：Karl Tuyls、Laurent Sifre、Julien Perolat、Daan Wierstra都是前DeepMind研究员，CEO Charles Kantor是Stanford计算数学背景。其中Laurent Sifre是DeepMind的principal scientist，AlphaGo、AlphaFold、AlphaStar的核心贡献者之一，最近还做了Google的Gemini和Gemma。这是一个高度DeepMind血统的团队。

投资人包括Accel、Amazon、Samsung、UiPath、Creandum、Elaia Partners、FirstMark Capital、Visionaries Club，以及Eric Schmidt、Xavier Niel、Yuri Milner、Bernard Arnault等一线大佬个人参投。2026年发布Holo 3计算机操作AI模型。

**对应的方法论**：顶级技术血统（多位DeepMind研究员，AlphaGo贡献者）+ 巨额资本。这条路对普通创业者几乎完全不可复制。

## 5.2 Worktrace AI：OpenAI 系

Worktrace是2025年成立的早期公司，seed 900万美元，投资方包括Conviction（Sarah Guo）、8VC、OpenAI、Mira Murati个人参投。

创始人Angela Jiang是前OpenAI员工，参与过ChatGPT的发布，是典型的OpenAI系。Deepak Vasisht是资深研究员和学者。公司成立才八个月就给五个设计合作伙伴提供agent。

产品思路是先研究一家公司的内部工作流，再帮他们用AI把这些流程自动化。这是OpenAI系常见的打法：先建关系、找客户深度合作、再做产品。

**对应的方法论**：顶级AI厂血统（OpenAI系，参与过ChatGPT发布）+ 顶级投资人人脉（Mira Murati个人参投）。跟H Company是同一档的稀缺入场券。

## 5.3 Rebar：少见的行业人 agent 创业案例

Rebar是agent领域里少见的"行业人创业"案例。2024年10月成立，创始人Evan Brown是前HVAC（暖通空调）估算员，亲历过承包商估算工作的痛苦。

产品是给建筑承包商做估算的agent，自动化投标和估算这类繁琐工作。2026年头六周ARR就翻倍，资金用于把agent平台扩展到电气和管道等垂直领域。

公开融资信息有限（属于早期seed），但增长指标说明产品真的解决了行业痛点。

**对应的方法论**：圈内人（前HVAC估算员）+ 解决自己干过的痛点。这是agent领域里少见的非技术血统、非顶级资本的路径。

## 5.4 Eudia：直攻 Fortune 500 法务的重 toB 模式

Eudia 2023年加州Palo Alto成立。Series A高达1.05亿美元（2025年2月，General Catalyst领投），总融资1.05亿美元。ARR超过1000万、年底冲2000万。已收购爱尔兰法律服务公司Johnson Hana来加强欧洲业务。

产品是给Fortune 500法务团队的agentic AI平台：每个企业定制一个法律大脑，人在环里增强，覆盖文档分析、合同红线、合规自动化。客户有Cargill、DHL、Duracell、Coherent这些Fortune 500名字。

跟Eve和Spellbook比，Eudia的客户画像完全不同。它不卖给律所，卖给企业法务部。这条线的特点是单客户年合同金额几十万到上百万美元，但销售周期6到12个月，需要重销售团队。

**对应方法论**：信息不足倾向圈外人（技术 + 企业服务团队）+ 信任驱动偏企业销售（直攻Fortune 500法务）+ 大钱（General Catalyst 1.05亿Series A）+ 企业销售能力。这是toB大单路径的代表。

## 5.5 Relevance AI：澳大利亚出身的横向 agent 平台

Relevance AI 2020年前后成立，澳大利亚出身。累计融资3700万美元（含2400万美元Series B），投资方King River Capital、Insight Partners、Peak XV。2025年1月单月就有4万个AI agent注册到平台。客户包括Qualified、Activision、SafetyCulture。

产品是让任何人搭建AI agent团队的平台。竞争对手包括Retell、SmythOS、微软等。

横向agent平台是个拥挤赛道，因为入门门槛低、巨头自己也在做。Relevance AI能跑出来靠的是早期就有客户验证 + 多年积累的销售渠道，不是靠产品差异化。

**对应方法论**：圈外人技术团队 + 资本（Insight、Peak XV）+ 横向平台路径 + 偏to C（任何人都能自助搭agent）后服务企业。

## 5.6 8Flow：业务流程编排 agent

8Flow 2022年美国成立。Series A 1660万美元（2025年4月）。做AI驱动的工作流自动化，编排业务流程、整合数据，让团队通过智能agent更高效地管理工作。公开的创始人细节较少。

**对应方法论**：信息不足，倾向圈外人技术团队 + 产品驱动 + to B（企业流程）。

## 5.7 Mindoo：医院工作流 agent 的欧洲玩家

Mindoo是一家欧洲公司，seed约500万欧元（约540万美元），Index Ventures和a16z领投，参投的天使里有Mistral的Arthur Mensch和Hugging Face的Thomas Wolf。

做面向医院和医护人员的AI agent平台，自动化行政和临床工作流，比如患者数据录入和预约排班，对抗医护人员的职业倦怠。重点是接进现有的EHR系统。

值得记录的是天使阵容：Mistral创始人 + Hugging Face创始人参投，这是欧洲AI创业圈最顶级的人脉背书。这种背书对企业销售很有用，因为客户能感受到"这家公司被欧洲AI圈认证过"。

**对应方法论**：圈外人技术团队 + 顶级AI圈天使背书（Mistral、Hugging Face创始人参投）+ a16z / Index资本 + to B（卖给医院，接EHR）。是欧洲AI圈"贵族化"打法的代表。

## 5.8 Instruct：横向 agent 平台

Instruct在第四章4.4节已经详细介绍过。它的产品同时算在销售客服和agent两个领域。这里不重复展开。

## 5.9 Gentek AI：英国早期玩家

英国公司，成立2024年，seed 86万美元（2024年12月）。做企业定制agent。处于很早期，刚过百万门槛，公开信息有限。

**对应方法论**：信息不足，倾向产品驱动 + to B（企业定制）。值得记录的是融资量级：86万美元seed在这份名单里是最低的，几乎是angel round级别。但在英国，这个级别已经够让团队跑一年了。

# 六、几个学到的东西

把34家公司放到一起看，规律比单独看每家清楚得多。下面六条是我从这份样本里读出来的东西。

## 6.1 圈外人是主流，但几乎没有真正的素人

最直接的观察：34家里**真正的行业内人只有4家**：Juno（CPA + 开过事务所）、Crosby（律师 + Cooley）、Parambil（医学博士联创）、Rebar（前HVAC估算员）。其余30家全是技术背景的圈外人。

这推翻了一个常见担忧："做垂直AI必须是行业内人，否则做不进去。" 数据上不成立。**圈外人是这个赛道的主流**，他们靠产品打开市场，不靠行业关系。

但**圈外人几乎全都不是真素人**。把"圈外人"细看下去，他们都至少自带一种稀缺资源：

- **顶级技术血统**：Eve（Rubrik三联创）、Freed（前Facebook两人）、H Company（DeepMind多人）、Worktrace（前OpenAI）、Spellbook（多年连续创业）
- **资本人脉**：Eve（Jay当过Lightspeed投资人）、Paxton（Tanguy自己当过7年VC）
- **顶级VC早期backing**：Crosby（Sequoia + Index）、Basis（Khosla）、H Company（Accel + Amazon）、Worktrace（OpenAI + Mira Murati个人）
- **加速器背书**：Leaping AI（YC）、YC诊所agent（YC）、WorkDone（YC）
- **机构孵化**：Cascala Health（Redesign Health）、Paxton（Unusual Academy）
- **大佬天使背书**：Mindoo（Mistral创始人 + Hugging Face创始人参投）

整份名单里，**完全孤立、零资源、纯靠硬拼的纯素人找不到成功案例**。最接近的Leaping AI也是被德国VC拒了两次之后靠YC才起来。这意味着"创业不需要资源、有idea就行"在2024到2026年这份样本里不成立。

## 6.2 PLG + 先 toC 后 toB 是圈外人最好的入场打法

圈外人没有行业关系，怎么打进一个充满内行的行业？最稳定的答案是**产品驱动**（Product-Led Growth）+ **优先toC路径**。

具体看几个标杆：

**Spellbook**：早期是个人律师用私人信用卡自助订阅Word插件，自下而上渗透。到2025年底约一半收入来自大所和企业法务，是从个人订阅自然生长上来的。一个圈外的工程师不需要认识任何大律所合伙人，靠产品本身就能起量。

**Freed**：刻意绕开医院的漫长采购流程，直接卖给个体医生（$99 / 月），靠口碑从0长到2万付费医生。一个圈外的工程师不需要打通医院IT部门，靠产品本身就能起量。

**Paxton、GitLaw、Instruct、Relevance AI**：都是类似的"个人或小团队能直接下单"的形态。

反过来看，**纯toB、必须打通机构采购的场景对圈外人不友好**。卖给大医院IT、Fortune 500法务、大型律所合伙人，需要信任和关系。Eudia是这条路径的代表，但它早期就拿了General Catalyst 1.05亿美元Series A，本质上靠资本背书打通了关系。普通圈外人没有这种资本。

这也解释了为什么医疗领域早期赢家集中在卖给个体医生的临床记录工具（Freed），而不是卖给医院系统的产品。

## 6.3 圈内人靠"亲历痛点 + 行业人脉"突围，路径不同

少数行业人创业的案例不靠PLG，靠的是"亲历痛点 + 行业身份带来的信任"。

**Juno** 的David Haase在自己开的会计事务所里磨了Juno一年多，去年卖掉事务所专心做。投资人明确说打动他们的是founder-market fit。500家事务所采用，靠的是Haase在会计师圈的口碑和人脉。

**Crosby** 的Ryan Daniels律师身份 + Cooley出身 + Sequoia内部律师Cindy Lee同门人脉。这条路完全靠身份和关系，不是产品胜利。

**Rebar** 的Evan Brown前HVAC估算员，解决自己干过的痛点。

**Parambil** 创始团队含医学博士，懂医疗事故案件。

行业人创业的优势：天然有founder-market fit、不需要花时间理解行业、自带客户网络、容易拿到行业里的VC（懂这个行业的VC）。劣势：行业人通常不懂技术，需要找技术联创。且行业人的ceiling受行业大小限制（卖给100家会计事务所跟卖给100个国家用户是两种生意）。

整份名单里行业人路径占少数，但单家成功率不低（Juno、Crosby都在快速增长）。

## 6.4 toB 大单需要资本和关系背书，不是产品

有一部分公司从一开始就走重toB路径，目标客户是Fortune 500或大型律所 / 医院 / 银行。这条路有共同特征：**早期就拿大额融资，靠资本和关系打通客户**。

- **Eudia**（Series A 1.05亿）：直攻Fortune 500法务
- **Wonderful**（累计1.34亿）：企业级多语言客服
- **Accrual**（6500-7500万seed）：Top 100会计所
- **H Company**（seed 2.2亿）：企业自动化
- **Eve**（Series B 1.03亿）：原告律所

注意这些公司的融资模式：种子轮就拿巨额或者Series A直接破亿。这种融资规模本身就是销售工具。"Sequoia / a16z / Khosla投了这家公司"是Fortune 500采购部门愿意听电话的理由。

**对普通创业者的提示**：如果你的产品天然只能卖给大客户、机构采购周期长、单笔ARR高，那这条路一开始就需要顶级VC背书。没有顶级VC，做这条路非常困难。反过来，如果产品能让个人或小团队直接下单，PLG路径成本低得多。

## 6.5 垂直 agent 比横向平台更被资本看好

Agent领域内部，资本明显在垂直agent这边重注。

2025到2026年的统计显示，**17笔垂直agent交易拿了约8.1亿美元**，远超横向平台。Eudia（1.05亿）、Mindoo（540万 + 顶级天使）、Rebar（早期但增长快）都属于垂直派。横向平台里融资最大的Relevance AI累计也才3700万。

逻辑很直接：**通用agent工具拼不过深度，agent必须懂某个具体工种的工作流才有护城河**。一个通用的"让你用大白话搭agent"的平台，使用门槛高、用户留存差、且面对OpenAI / Anthropic这种巨头自己出agent工具的直接挤压。垂直agent因为有具体行业know-how和工作流深度，护城河深得多。

这一条对接下来想做agent创业的人很关键：**别做通用agent平台，做某个具体工种的agent**。

## 6.6 数据口径提醒

最后一条算是一条caveat，不是规律。

这34家是2024到2026年公开报道里能查到的代表性样本，不是全市场普查。还有大量更小、信息不公开的pre-seed公司没进这份名单。少数公司创始人信息不全。

融资数字截至2026年6月，部分公司可能在文章发布后又有新一轮融资。具体数字可能小幅波动，但整体规律（圈外人主流、PLG优先、垂直胜过横向）应该比较稳定。

另外这份样本偏向美国和西欧，不包含中国、印度、东南亚的早期AI公司。中国的早期AI创业有自己的特点（更卷B端定制、客户更难付费、政策环境更敏感），不能直接套用这份名单的规律。

# 七、收尾：给想做垂直 AI 的人的几条话

如果你看完这份名单想做垂直AI创业，下面是从这34家公司里能直接拿走的几条话：

第一，**承认起点**。你属于哪一类？是技术背景的圈外人，还是有行业身份的内行？是有顶级VC朋友的，还是从零起步的？这份名单里30家圈外人 + 4家内行 + 0家纯素人成功案例。先想清楚自己的入场券是什么。

第二，**没有入场券就先攒**。如果连技术血统、连续创业积累、加速器背书、行业身份都没有，做垂直AI之前先想办法拿一个。最现实的可能是YC这种顶级加速器（参考Leaping AI路径）。

第三，**优先选PLG路径**。能让个人或小团队直接下单的产品形态，比必须打通机构采购的产品形态启动成本低一个数量级。Spellbook和Freed是教科书案例。

第四，**别做通用工具，做具体工种的agent**。垂直深度是2025到2026年这个时点最稀缺的护城河。

第五，**找一个懂行的家属或合伙人**。Freed的妻子是医生、Crosby的父母是法学教授、Juno自己开过事务所。从外面想象一个行业的痛点，远不如有一个人天天跟你抱怨真实痛点。

最后想说一件事：这份名单里看到的"圈外人路径"和"圈内人路径"，**没有哪条更对**。两条都跑出来过成功案例。重要的是诚实承认自己有哪些资源、缺哪些资源，然后选一条能用自己资源走通的路。

---

## 作者其它文章

- [什么是 Diffusion Model？图片视频生成模型全网最详细介绍](https://x.com/snowboat84/status/2061598950944305295)
- [美国税收制度完全指南](https://x.com/snowboat84/status/2060511915617779821)
- [当物理遇上AI：深度学习里的物理元素（上）](https://x.com/snowboat84/status/2060145538922844179)
- [一文看懂美国的法律系统](https://x.com/snowboat84/status/2059795010330251568)
- [教宗良十四世论人工智能（精华版）](https://x.com/snowboat84/status/2059434342745866391)
- [廉颇老矣，尚能饭否：现代数学史（下）](https://x.com/snowboat84/status/2059071134738620606)
- [一篇文章讲清楚美国的移民系统](https://x.com/snowboat84/status/2057980486501433383)
- [大航海时代2的逆向工程实验](https://x.com/snowboat84/status/2057264254319993332)
- [量子计算机有前途吗？](https://x.com/snowboat84/status/2056895775578456417)
- [一文讲清楚美国医疗系统](https://x.com/snowboat84/status/2055081426744422697)
- [一篇文章看懂美国教育全生态](https://x.com/snowboat84/status/2054359249917210633)
- [一篇文章讲清大语言模型发展史](https://x.com/snowboat84/status/2051444935547912236)
- [不会编程、没有融资、没有员工，他怎么一个人做到年入2000万](https://x.com/snowboat84/status/2044216044575998136)

---

## 本文参考文献

### 法律 AI 公司

- [Eve Raises $103 Million at $1 Billion Valuation (Series B)](https://www.prnewswire.com/news-releases/eve-raises-103-million-at-1-billion-valuation-to-help-plaintiff-firms-deliver-justice-through-ai-transformation-302570807.html) - PRNewswire 2025年9月30日
- [Eve's Series B - Lightspeed Venture Partners](https://lsvp.com/stories/eves-series-b-another-milestone-as-eve-rapidly-transforms-legal-firms-with-ai/) - Lightspeed 关于 Eve 的官方介绍
- [Spellbook Raises $50M Series B led by Khosla Ventures](https://www.spellbook.legal/blog/series-b) - Spellbook 2025年10月官方公告
- [Spellbook 50M Series B + CEO Interview - Artificial Lawyer](https://www.artificiallawyer.com/2025/10/09/spellbook-raises-50m-ceo-scott-stevenson-interview/) - Scott Stevenson 访谈
- [Crosby launches a new kind of AI-powered law firm - TechCrunch](https://techcrunch.com/2025/06/17/sequoia-backed-crosby-launches-a-new-kind-of-ai-powered-law-firm/) - Crosby seed 轮
- [Hybrid AI Law Firm Crosby Raises $20m - Cooley Invests - Artificial Lawyer](https://www.artificiallawyer.com/2025/10/08/hybrid-ai-law-firm-crosby-raises-20m-cooley-invests/) - Crosby Series A
- [Sequoia: Partnering with Crosby](https://sequoiacap.com/article/partnering-with-crosby-a-law-firm-at-the-speed-of-ai/) - Sequoia 对 Crosby 的官方背书介绍

### 医疗 AI 公司

- [Freed raises $30 million led by Sequoia - CNBC](https://www.cnbc.com/2025/03/05/freed-raises-30-million-led-by-sequoia-to-tackle-clinician-burnout.html) - Freed Series A 报道
- [Freed Secures $30M Series A - BusinessWire](https://www.businesswire.com/news/home/20250305397400/en/Freed-Secures-$30M-Series-A-Led-by-Sequoia-Capital-to-Free-Clinicians-from-Administrative-Burdens-with-AI-Assistant) - Freed 官方融资公告
- [Freed says 20,000 clinicians are using its medical AI - VentureBeat](https://venturebeat.com/ai/freed-says-20000-clinicians-are-using-its-medical-ai-transcription-scribe-but-competition-is-rising-fast) - Freed 增长数据

### 金融会计 AI 公司

- [Juno Raises $12M Seed - Crunchbase News](https://news.crunchbase.com/fintech/cpa-founded-ai-tax-return-startup-juno-seed-funding/) - Juno seed 轮
- [Juno Raises $12M to Scale AI Tax Preparation - CPA Practice Advisor](https://www.cpapracticeadvisor.com/2026/04/13/juno-raises-12m-seed-to-scale-ai-tax-preparation-platform-that-automates-90-of-busy-work/181502/) - 产品细节
- [Tax Prep Co. Juno Lands $12M - San Diego Business Journal](https://www.sdbj.com/technology/tax-prep-co-juno-lands-12m-seed/) - 创始人 David Haase 访谈

### Agent / 工作流 AI 公司

- [French AI startup H raises $220M seed round - TechCrunch](https://techcrunch.com/2024/05/21/french-ai-startup-h-raises-220-million-seed-round/) - H Company 创纪录 seed
- [Ex-DeepMind scientists raise $220m to launch H - Sifted](https://sifted.eu/articles/h-raises-220m-seed-round) - H Company DeepMind 背景
- [H (company) - Wikipedia](https://en.wikipedia.org/wiki/H_(company)) - 创始人和投资人完整名单

### 行业整体数据

- [Crunchbase News - AI Startup Funding Tracker](https://news.crunchbase.com/) - 早期 AI 融资数据来源
- [TechCrunch Startups](https://techcrunch.com/category/startups/) - 创业公司新闻
- [Artificial Lawyer](https://www.artificiallawyer.com/) - 法律 AI 行业报道

---

## 附录：原始草稿

> 本文基于原始研究笔记扩写而成。原始笔记包含 25 家核心公司 + 9 家 Agent 领域公司的详细资料，按四个维度标注（圈外人/圈内人、是否产品驱动、自带资源、toC/toB），数据来源为 Crunchbase、TechCrunch、Sequoia、Law.com 及公司公告，时间窗口 2024 至 2026 年。原始笔记另存。
