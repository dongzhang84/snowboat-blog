
## 写作设定

|项|内容|
|---|---|
|读者|想了解 / 想转行 / 想学这个方向的人|
|预估篇幅|5500 字上下（可压到 4000）|
|结构|引子 + 六章 + 结语。引子和结语不编号|
|基调|先讲清楚，再泼冷水。不写"风口快上车"，写"这东西是什么、你现在该干嘛"|
|全文主线|**FDE 不是因为 AI 不好用才出现的岗位，而是因为 AI 开始被允许动真格的，才必须有人去把责任边界画出来**|
|差异化|别人写"定义 + 职责清单"，我们写因果链、组织位置、能力保质期、以及能不能单干|

---

## 引子（不编号，约 400 字）

> 功能：一段之内让读者知道这不是又一个热词

- 开篇先用一句话把定义压住：FDE 是驻扎在客户现场、把产品从"能演示"做到"能上生产"的工程师（不单列小节，一句带过即可）
- 现象：2026 年这个岗位确实在升温，但数字要降级写。可引用口径一：FDE Pulse 在 2026 年 4 月 30 日追踪到 249 个活跃 FDE 岗位，覆盖 137 家公司；可引用口径二：Plank Research 写到 2026 年 4 月同比增长 729%，但这是第三方报告，不是一手招聘平台
- 名单里不只有 AI 实验室。OpenAI、Anthropic、Adobe、Databricks、AWS 都有一手材料可支撑；Stripe、Notion、GitLab 若要写，发稿前必须逐个找到公司官网招聘页或删掉
- 不要写"两年前几乎没人提它"这种无法稳健证明的话。更稳的写法：2023 年那波企业 AI 的主角是 chatbot 和 API 接入，FDE 还不是主叙事
- 这个时间差就是全文要解释的东西。亮出主线，预告结构

---

## 第一章　它是什么时候来的

> 功能：用一条时间轴同时回答"从哪来"和"为什么现在火" 约 900 字

### 1.1 起源：涉密数据逼出来的组织设计

- Palantir 早期客户是情报和国防机构
- 硬约束：数据不能带出、工作流没有文档全在老员工脑子里
- 只能反过来，把工程师送进去
- Forward Deployed 直接借用军事术语（前线部署单位），客户群本身说军语

### 1.2 命门不是驻场，是经验回流

- 驻场本身不新鲜，实施顾问干了几十年
- 真正的设计是两条：FDE 与核心工程团队协同，现场反复出现的东西被收回主干产品
- **驻场不是成本，是产品需求的采集管道**，这条是 FDE 区别于外包的分界线
- 本节是全文的地基，第三章和第六章都要回扣

### 1.3 沉寂：2023 年 AI 最热的时候，它没火

- 那一波是 chatbot，企业接个 API 自己就能上
- 产出是挂在业务旁边的问答框，答错了没后果
- **不需要派人驻场**，这是最有力的反证

### 1.4 爆发：模型从"说话"变成"动手"

- Agent 时代 = 多步工作流 = 模型拿到真实系统的**写权限**
- 它能发邮件、改工单、触发流程、动钱
- 问题从"效果好不好"变成"我敢不敢让它动"
- 而"敢不敢"这件事，**信任没法远程交付**
- 收尾：所以"FDE 是 AI 新岗位"这个说法本身就是错的，它只是被 AI 重新激活了
- 补一句各家叫法：OpenAI 用 Forward Deployed Engineer / Forward Deployed Software Engineer；Anthropic 同时出现 Applied AI Engineer 和 Forward Deployed Engineer, Applied AI；Adobe 有 Forward Deployed AI Engineer；Databricks 有 AI Forward Deployed Engineering 团队

---

## 第二章　FDE 到底在做什么

> 功能：全文最"实"的一章。读者读完要能想象出这个人每天在干嘛 约 1600 字

### 2.1 不是"安装"，是流程重构

- 安装的前提是成品已存在，只需搬进去配置。AI agent 没有这个成品
- 你到客户那儿，手里只有一个模型 API 和一堆框架
- 客户说"我们客服效率低"，离一个能跑的 agent 之间隔着： 工单实际长什么样 / 哪些字段是脏的 / 知识库三年没更新 / 什么情况必须转人工 / 转了之后责任算谁 / 出错谁兜底
- **没有一条是技术问题，但每一条不定下来，agent 就没法写**
- 推论：这个岗位不会被"部署工具变好了"消灭

### 2.2 不是一个人去

- 中文文章基本都把 FDE 写成孤胆英雄，实际是小队作战
- 典型配置：FDE（动手造）+ 部署策略/客户经理（管关系与优先级）+ 客户侧的领域专家（唯一知道流程真相的人）
- **领域专家不是"配合方"，是最关键的信息源**，第四章讲的 eval 体系就是跟这个人一起定出来的
- 客户侧还有几个必须打交道的角色：IT 管权限、安全管边界、法务管责任、业务方管验收
- 说明为什么这岗位不是"技术好就行"：**你要同时让四拨利益不一致的人点头**
- 一句可用：FDE 的一半工作，是在客户内部找到那个真正能拍板的人

### 2.3 一个项目的完整链路

六个环节，每个配一句真实场景，这是本章篇幅最重的一节：

1. **需求解构**，把"提升效率"翻译成"哪一个具体动作、由谁做、现在耗时多少"
2. **摸真实数据与权限**，这一步最常翻车：数据在五个系统里、字段含义没人说得清、想要的表申请不下来
3. **搭 workflow**，真正写代码的部分，也是耗时最短的部分
4. **建 eval**，跟领域专家一起过样本，定义什么叫"做对了"（呼应 4.3）
5. **灰度上线**，先只读不写、先小流量、先人工复核，把写权限一点点放开（呼应 1.4）
6. **沉淀回流**，把可复用的部分收回产品（呼应 1.2）

- 强调节奏：前两步往往占掉一半时间，而它们跟 AI 无关

### 2.4 走的时候留下什么

- 这一节回答"交付物到底是什么"，也是区分 FDE 与外包的实操证据
- 留给客户：能跑的系统、一套评估集、运维手册、以及客户团队自己能改的能力
- 带回公司：可复用的组件与脚手架、产品需求清单、以及模型在真实场景里的失败样本
- **最后一项是很多人忽略的资产**，实验室里造不出真实企业的脏数据和边界情况
- 一句可用：如果一个项目结束后客户离不开你，那不是成功，是外包

### 2.5 时间都花在哪

- AI 相关工作大概只占三成，其余是数据接入、身份权限、对接 legacy、合规、开会
- 不写具体比例。更稳的说法是：大量时间花在数据接入、身份权限、legacy 系统对接、合规和沟通上，真正围绕模型本身的工作只是一部分
- 直接反驳"我把 agent 框架学会就能去做 FDE"
- 承上启下：既然只有三成是 AI，那另外七成是从哪继承来的？引出第三章

---

## 第三章　它跟哪些工种重叠

> 功能：全文承重墙。这章立住，第四章的能力清单是自动推出来的 约 800 字

### 3.1 五个前身

|前身|传承了什么|差在哪|
|---|---|---|
|FAE 现场应用工程师|最直接的祖宗，厂商派人住进客户产线|只管用对，不管造新的|
|ERP 实施 / 驻场开发|驻场、脏数据、跟业务对齐、需求变更|交付即终点，经验不回流|
|Solutions Architect / 售前 SE|业务解构、方案设计、跟技术负责人对话|签单前的活，交完就撤|
|Professional Services / TAM|客户关系、长期陪跑|成本中心，按人天计价，天然反对产品化|
|管理咨询|需求逆向、跟高层沟通、模糊中定方向|不写代码，交付物是建议|

### 3.2 并集，去掉各自的天花板

- FDE 同时具备咨询的视角、售前的方案、实施的耐性、工程师的手
- 一块技能都不新
- 那新的到底是什么？**组织位置**。它被放在研发侧，因此有改产品的权力（回扣 1.2）
- 关键一句：前面五个岗位的天花板长得各不相同，但根源是同一个，**都不在研发侧，都改不了产品**
- 本节是第三章的收口，也是第六章"单干就掉回表里"的伏笔，值得写足

### 3.3 推论：谁天然占优

- 表里任何一格干过的人都有半张船票
- ToB 交付 / 会写代码的顾问 / 行业专家转技术，各自的优势与短板
- 纯算法、纯研究背景反而一格不占（这条会得罪人，但要写）

---

## 第四章　需要什么基础：三层能力，保质期不同

> 功能：全文最有实操价值的一章 约 900 字

### 4.1 底座层（继承自 SWE）

- 全栈够用、API 集成、数据管道、读懂别人的烂代码、上线流程
- 没有捷径。**这是"FDE 不是入门岗"的根本原因**
- 保质期：长，但会被工具持续拉低门槛

### 4.2 交付层（继承自实施 / 售前 / 咨询）

- 需求解构、跟非技术方沟通、项目推进
- 一个特别具体的能力：**判断什么该定制、什么该推回产品路线图**
- 保质期：中。只能在真实交付里长出来

### 4.3 翻译层（唯一没有前身的一层）

- 传统软件要么跑通要么报错，验收标准是现成的
- LLM 系统"大部分时候对"，那**"多对算对"本身得先被设计出来**
- 这就是 eval 体系：把模糊的业务期待翻译成可测量的验收标准
- 佐证：Anthropic 岗位描述和招聘镜像都把 evaluation frameworks 与 agent 开发、prompt 工程、规模化部署并列。OpenAI 另有 evals 企业文章，明确把 evals 解释为把模糊业务目标变成可测量标准。John Deere 官方案例能支撑"AI 进入真实客服、经销商和农机运营流程"，但不能支撑具体样本量和定制 eval 体系，这个细节不要写
- 保质期：**最长，也最稀缺**

### 4.4 权重比清单重要

- 照着"并集"去学，人会本能先啃最像技术的部分（agent 框架、RAG、向量库）
- 而那恰恰是最容易替代、半年换一茬的
- 落点：**那些栈两个月能学完，学不完的是"在没人告诉你对错的时候，自己定义对错"**

---

## 第五章　想入门的人该怎么走

> 功能：给读者可执行的东西，也是转发动力所在 约 700 字

### 5.1 先破一个幻想：这是横向移动，不是入口

- 能力是叠加式的，不存在初级台阶
- 没在生产环境被 on-call 折磨过的人，到客户现场只会被业务方牵着走
- 直说：**你现在不该盯 FDE，该先把工程基本功补到能独当一面**

### 5.2 四类人的不同起跑线

- 承接 3.3，给每类人一句"你缺的是什么"

### 5.3 自己造交付场景

- 光刷课学不到交付层和翻译层
- 折中方案：给一家真实小企业免费做一个 AI 工作流，从摸脏数据开始，到上线、被吐槽、改需求、建评估
- **这段经历在面试里的分量，胜过十个 GitHub demo**

### 5.4 面试大概考什么

- 不要写成确定的"不是算法题"。更稳的写法：公开岗位要求更强调模糊情境下的部署判断、系统设计、客户沟通和 production rollout
- 可给 2-3 个"可能被问到的工作样题"，不要声称来自某家公司真实面试

---

## 第六章　能不能自己干

> 功能：读者里一定有一批人在想这件事。只给判断和方向，控制在全文 15% 以内 约 600 字

### 6.1 一单干，就不叫 FDE 了

- FDE 的命门是"坐在研发组织里、有改产品的权力"（回扣 1.2 与 3.2）
- 个体没有产品可推，造的东西只能是一次性的
- **于是掉回第三章那张表里**，成了装备 LLM 技术栈的实施顾问，天花板一起回来
- 一句话：**FDE 是一种雇佣形态，不是一种技能。技能能单干，形态不行**

### 6.2 平台提供的四样东西，第四样是死结

- 获客：FDE 不做销售，合同是公司签的
- 信任背书
- 经济结构：厂商贴钱派人是因为后端有 token 收入；个体只能按人天，回到咨询老账本
- **责任**，回扣 1.4 的写权限：agent 出事谁兜？甲方法务要的是能签 MSA、有责任上限、能买职业责任险的实体。个体户过不了采购和法务，不是能力问题

### 6.3 个体的三样反向优势

- 大厂根本不去的市场（中端与小微，前沿实验室这辈子不会派人去）
- 模型中立
- **垂直复利**：厂商横着摊经验，个体可以死磕一个行业，第三个客户开始资产复用
- 结论：**个体不该模仿 FDE，该反着来。厂商靠横向规模，个体靠纵向纵深**

### 6.4 "有多少人在做"，这个数字不存在

- 分类学问题：独立从业者不自称 FDE，散落在"AI 顾问""自动化""agency"标签下
- 只能看代理指标，且**这个领域的数据几乎全是咨询公司和招聘平台的营销内容，务必打折**
- 最硬的信号：OpenAI 在 2026 年 5 月 11 日宣布成立 OpenAI Deployment Company，并同意收购 Tomoro；OpenAI 官方说这会带来约 150 名 Forward Deployed Engineers 和 Deployment Specialists

### 6.5 顺序建议

- 不是学会技能就能单干，而是先在有平台的地方干几年、攒够一个行业的纵深再出来
- 落点：**你从大厂 FDE 出来单干，带走的不是技术栈，是你在某个行业里踩过的所有坑**

---

## 结语（不编号，约 400 字）

> 功能：不做鼓吹式收尾，给读者一个可以自己判断的框架

- 一个不太好听的观察：**FDE 的招聘量，某种程度上是产品成熟度的倒数**
- 产品够好，客户自己就能上手，不需要派人。Palantir 当年一直被质疑是"伪装成软件公司的咨询公司"
- 两边都有道理：技术层门槛确实会随工具变好而下降，但**"客户不知道自己要什么"这件事永远不会被工具解决**
- 所以 FDE 不会消失，但重心会持续从"能把东西做出来"漂移到"能定义该做什么"
- 呼应 4.4：底座层和交付层会贬值，翻译层会升值
- 用主线那句话收口

---

## 附录 A　事实核查结果

- [x] Palantir 起源：Palantir 官方文档没有给出"正式启用 FDE title 的年份"，但官方承认其平台通过 Forward Deployed Engineering 方法持续从客户任务中塑形。a16z 文章给出"2011 年 Palantir 把 solutions / integration engineers 改名为 forward-deployed engineer"的说法，属于可信二手来源。正文可写"Palantir 普及了这个 title"，不要写死"某年正式启用"。
- [x] 2026 年招聘量：FDE Pulse 在 2026 年 4 月 30 日追踪到 249 个活跃岗位、137 家公司。Plank Research 写到截至 2026 年 4 月同比增长 729%。二者都是第三方口径。正文建议写"第三方追踪显示，岗位已经到数百个、一百多家公司量级"，不要把"八倍"当官方事实。
- [x] OpenAI：OpenAI 在 2026 年 5 月 11 日宣布成立 OpenAI Deployment Company，并同意收购 Tomoro；官方写明 Tomoro 会带来约 150 名 Forward Deployed Engineers 和 Deployment Specialists。这个可以写。
- [x] Anthropic：Anthropic 官网招聘页能确认 Applied AI、Applied AI Engineer、Forward Deployed Engineer, Applied AI 等岗位存在。没有找到 Anthropic 官方公告确认"2026 年 5 月成立 1.5B 独立 FDE 业务单元"。这条只能写成媒体报道，或直接删。
- [x] AWS：AWS 官方在 2026 年 6 月宣布创建 AWS Forward Deployed Engineering 组织，背后是 10 亿美元投资，并称会把数千名专家嵌入客户团队。可作为"大厂开始把 FDE 组织化"的强证据。
- [x] Adobe / Databricks：Adobe 招聘页和 Adobe 官方文章能确认 Forward Deployed AI Engineer 叫法；Databricks Data + AI Summit 讲者页能确认 AI Forward Deployed Engineering 团队和 AI FDE 叫法。
- [x] OpenAI / Anthropic 岗位描述：OpenAI 官网 FDE 岗位明确写 production deployment、embed with customer teams、eval-driven feedback、roadmap input。Anthropic 官网招聘页能确认岗位名称，具体职责可用岗位镜像或招聘页抓取材料，但正文要标明这是岗位描述，不要当公司战略公告。
- [x] John Deere：OpenAI 官方 John Deere 案例能支撑 AI 用于客户成功、经销商诊断、农机运营建议、See & Spray 价值证明等场景，也能支撑"生产流程复杂、需要业务知识"。没有看到"几百个样本、定制 eval 体系"的一手证据，这个细节删掉。
- [x] 薪资区间：OpenAI 官网 FDE Seattle 岗位写 16.2 万到 28 万美元基础薪资加 equity，Gov FDE 写 14.58 万到 28 万美元基础薪资加 equity。第三方高薪汇编可作背景，不要当权威。
- [x] 时间分配："1/4 写码、1/2 集成、1/4 沟通"没有找到一手来源。正文只写"大量时间花在数据接入、权限、安全、合规、沟通上"，不要写比例。

## 附录 A.1　核查来源

- [OpenAI launches the OpenAI Deployment Company](https://openai.com/index/openai-launches-the-deployment-company/) - OpenAI 官方，2026 年 5 月 11 日
- [Forward Deployed Engineer (FDE) - Seattle](https://openai.com/careers/forward-deployed-engineer-%28fde%29-seattle-seattle/) - OpenAI Careers
- [Forward Deployed Engineer, Gov](https://openai.com/careers/forward-deployed-engineer-gov-washington-dc/) - OpenAI Careers
- [Jobs - Applied AI](https://www.anthropic.com/careers/jobs?aff=YpJLo) - Anthropic Careers
- [AWS invests $1 billion to embed AI forward deployed engineers with customers](https://www.aboutamazon.com/news/aws/aws-1-billion-forward-deployed-ai-engineers) - Amazon / AWS 官方，2026 年 6 月
- [AI FDE overview](https://www.palantir.com/docs/foundry/ai-fde/overview) - Palantir 官方文档
- [Architecture center overview](https://www.palantir.com/docs/foundry/architecture-center/overview) - Palantir 官方文档
- [Forward-deployed Job Titles](https://a16z.com/forward-deployed-job-titles/) - a16z，2026 年 1 月 27 日
- [Forward Deployed Engineer Hiring Trends 2026](https://fdepulse.com/insights/fde-hiring-trends-2026/) - FDE Pulse，2026 年 4 月 30 日
- [The state of FDE as a service](https://joinplank.com/state-of-fde) - Plank Research，2026 年 6 月 11 日，7 月 24 日更新
- [AI helps John Deere transform agriculture](https://openai.com/index/john-deere-justin-rose/) - OpenAI 官方，2025 年 5 月 6 日
- [How evals drive the next chapter in AI for businesses](https://openai.com/index/evals-drive-next-chapter-of-ai/) - OpenAI 官方，2025 年 11 月 19 日
- [Forward Deployed AI Engineer](https://careers.adobe.com/us/en/job/R164040/Forward-Deployed-AI-Engineer) - Adobe Careers
- [The rise of the new Creative Technologist](https://business.adobe.com/resources/sdk/the-rise-of-the-new-creative-technologist.html) - Adobe 官方
- [Max Marcussen speaker profile](https://www.databricks.com/dataaisummit/speaker/max-marcussen) - Databricks 官方

## 附录 B　可用金句

1. FDE 不是因为 AI 不好用才出现的岗位，而是因为 AI 开始被允许动真格的，才必须有人去把责任边界画出来。（主线）
2. 不是 AI 火了所以 FDE 火了，是 AI 从"说话"变成"动手"了，FDE 才火。
3. 它是那五个岗位的并集，去掉各自的天花板。
4. 驻场不是成本，是产品需求的采集管道。
5. 那些技术栈两个月能学完，学不完的是"在没人告诉你对错的时候，自己定义对错"。
6. FDE 是一种雇佣形态，不是一种技能。
7. 厂商靠横向规模，个体靠纵向纵深。
8. FDE 的招聘量，某种程度上是产品成熟度的倒数。
