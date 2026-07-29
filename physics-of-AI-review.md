# AI 的物理学:从微观到宏观的还原论纲领——批判性文献综述

> **纲领背景**:物理学有一条经典的**从微观到宏观的还原论链**——
> **微观(牛顿力学,粒子)→ 中观(玻尔兹曼方程,统计力学)→ 宏观(纳维-斯托克斯,流体力学)**。
> 每一层都有一个**自治的闭合方程**,层与层之间通过严格极限相连(粒子→玻尔兹曼靠 propagation of chaos;玻尔兹曼→流体靠 Chapman–Enskog 展开)。
> 本文问:**这条还原论链能不能搬到 AI 上?** 对齐关系:
> - **微观 = SGD**(单权重更新)
> - **中观 = ?**
> - **宏观 = ?**
> 并综述学术界用**物理方法**把这条链建到了什么程度。
>
> **可信度分层**(决定你能信到什么程度):
> - **[已核验]**:经多智能体 deep-research 抓取一手文献、三票对抗核验、全票存活的结论。
> - **[未核验]**:引文经检索确认存在、但**未过对抗验证**,由整理者凭领域知识补全。
> - **[已证否]**:被对抗核验以 0-3 判否的说法,单独标出以免误传。
>
> 两轮 deep-research 共:220 个子智能体、~400 万 token、66 篇一手源、282 条论断、48 条三票核验。
> 生成/更新日期:2026-07-15

---

## 0. 总判 **[已核验]**

把物理的梯子摆到 AI 上,当前状态是:

| 层 | 物理 | AI(对应) | 学术界现状 |
|---|---|---|---|
| **微观** | 牛顿力学(粒子) | **SGD**:$w\leftarrow w-\eta\nabla L$ | ✅ 已有,平凡——定律已知、精确 |
| **微观→中观** | propagation of chaos → 玻尔兹曼 | **同一个 propagation of chaos** → mean-field PDE | ✅ 已严格建成,**仅在极限里**(无限宽、浅层) |
| **中观** | 玻尔兹曼方程(单粒子分布 $f$) | **三个竞争候选**(见 §2) | ⚠️ 存在,但分裂、无典范共识 |
| **中观→宏观** | Chapman–Enskog 展开 | **DMFT / Volterra 闭合 → scaling 指数** | ✅ **已建成,但仅限可解模型**(本轮修正:非空白) |
| **宏观** | 纳维-斯托克斯($\rho,u,T$) | scaling law(指数已可推导);涌现、泛化 | ⚠️ 指数可从谱/动力学推出,但两端假设仍需第一性化 |

**一句话**:梯子的**下半截(微观→中观)和上半截的横档(中观→宏观)都已经在可解模型里搭起来了**;真正未打通的是**"数据几何 → 谱"这最后一段**,以及**把这些结果从可解模型推广到真实特征学习的 Transformer**。

**对物理学家最本质的一条**:AI 更像一个**"有序参量、无守恒律"**的系统。它的慢变量(overlap、内积核、谱指数)是**高维集中**逼出来的统计对象,不是像物理那样**由守恒律**逼出来的。这是本纲领与物理最深的结构差异,也是"宏观闭合方程是否存在"这个问题至今没有干净答案的根源。

> **勘误(相对本文档上一版)**:上一版判"中观→宏观基本空白"。**此判被本轮核验推翻,已收回。** 见 §3。

---

## 1. 微观 → 中观:**已严格建成(极限意义下)** **[已核验]**

**AI 的"玻尔兹曼方程"已经存在,而且是用一模一样的数学造出来的。**

- 物理:粒子 → 单粒子分布 $f(x,v,t)$ → 玻尔兹曼方程,靠 **propagation of chaos** 闭合。
- AI(mean-field 理论,Mei–Montanari–Nguyen PNAS 2018;Chizat–Bach NeurIPS 2018):**神经元 = 粒子**,神经元分布 $\mu(w,t)$ = $f$,满足 **Wasserstein 梯度流 / McKean–Vlasov PDE**,靠的**也是 propagation of chaos**。

神经元↔粒子,权重分布↔$f$,那个 PDE↔玻尔兹曼方程。**这是同一套机器,不是类比。**

**前沿正在做的,恰是"短时间 → 长时间"那一步**(即气体里 Lanford → 长时间推导的 AI 版):Glasgow–Wu–Bruna(2025, arXiv:2504.13110)把 propagation of chaos 的时间跨度从 $O(\log d)$ 推进到**多项式 in $d$**。

**代价**:只对**一到两层、无限宽极限**;有限宽要多宽、收敛多快仍开放(Chizat–Bach 的全局收敛只是**定性、有条件**的:需 2-齐次激活、全支撑初始化、凸损失,不给速率)。

---

## 2. 中观:**存在,但分裂成三个候选** **[已核验]**

物理只有**一个**中观变量($f$),因为它由守恒律+尺度分离唯一确定。AI 有**三个竞争候选,无共识**:

1. **神经元分布 $\mu(w,t)$**(mean-field)——最像玻尔兹曼的 $f$。
2. **序参量 + 记忆核**(DMFT,Mignacco/Gerbelot)——更像 Mori–Zwanzig 广义 Langevin 约化;**离散 SGD 已被严格证明**(Gerbelot 等 2210.06591)。
3. **内积核(NTK 及其演化)**(Jacot 1806.07572;Bordelon–Pehlevan 2205.09653)——核作为中观变量,后者给出核演化的自洽闭合。

**"该用哪个中观变量"没有定论,本身就是 AI 还原不如物理干净的信号**:物理的 $f$ 有典范地位,AI 这三个都只是高维极限下的方便选择。

**NTK/lazy 极限**给出最干净的**闭合宏观方程**(最小二乘下的线性 ODE),但**代价是冻结了核、排除了特征学习**——闭合恰好存在于"无趣"处,在"有趣"(特征学习)处失效。Bordelon–Pehlevan 是冲出 lazy 区、让核演化起来的动态桥。

---

## 3. 中观 → 宏观:**已建成,但仅限可解模型(本轮核心修正)** **[已核验]**

物理靠 Chapman–Enskog 从玻尔兹曼推出纳维-斯托克斯。**AI 里,这根横档已经有多家搭起来了**——这是本轮把上一版错判纠正过来的关键结论。它们**真的是"推导",不是唯象拟合**:

| 工作 | 怎么搭的横档 | 类型 | 力度 |
|---|---|---|---|
| **Bordelon–Atanasov–Pehlevan**《A Dynamical Model of Neural Scaling Laws》(ICML 2024, arXiv:2402.01092) | 从梯度下降/SGD 动力学出发,闭合一个 **DMFT**(关联/响应函数),傅里叶域精确解,**推出**时间/模型/数据三个不同指数 $L\sim t^{-(a-1)/b}$、$L\sim N^{-\min\{a-1,2b\}}$、$L\sim P^{-\min\{a-1,2b\}}$,机制为 $k^*\approx\min\{t^{1/b},N,P\}$;并给出**非对称 compute-optimal 规则**(训练时间比模型规模长得快) | **动态**(非平衡),真·中观闭合方程→宏观指数 | **最接近"真横档"** |
| 其特征学习续作《How Feature Learning Can Improve Neural Scaling Laws》(ICLR 2025 Spotlight, arXiv:2409.17858) | 冲出静态核:对"难任务"(目标在初始 NTK 的 RKHS 之外),**特征学习把训练时间指数从 $t^{-\beta}$ 提到 $t^{-2\beta/(1+\beta)}$**($\beta<1$ 时近乎翻倍);易任务(in-RKHS)指数不变 | 动态+特征学习 | 可解模型推导 |
| **Paquette–Paquette–Xiao–Pennington**《4+3 Phases of Compute-Optimal Neural Scaling Laws》(NeurIPS 2024, arXiv:2405.15074) | 三参数可解模型,**one-pass SGD**,用 homogenized SGD / **Volterra 积分方程**(确定性等价闭合),**带数学证明**地推出各相指数,并证明相平面存在 **4+3 个相**、**真正的相边界(相变)**;单一幂律不足以描述整个 compute-optimal 前沿 | **微观 SGD → 宏观,证明级** | **最严格** |
| **Bahri–Dyer–Kaplan–Lee–Sharma**《Explaining Neural Scaling Laws》(PNAS 2024, arXiv:2102.06701) | replica 理论:分**四区**(variance-limited / resolution-limited × 数据/宽度);resolution-limited 区由核特征谱 $\lambda_i=i^{-(1+\alpha_K)}$ 推出 $L(D)\propto D^{-\alpha_K}$、$L(P)\propto P^{-\alpha_K}$,即 $\alpha_D=\alpha_P=\alpha_K$ | **静态/谱**(偏平衡) | 谱端推导 |
| **Maloney–Roberts–Sully**《A Solvable Model of Neural Scaling Laws》(arXiv:2210.16859) | 随机矩阵:联合生成数据+随机特征模型,在"大数据×大参数"对偶极限解出;数据协方差的幂律谱**经非线性随机特征映射延展**,translated 成 test loss 的幂律 | 静态/谱 | 谱端推导 |

**判定**:横档**建成了**,而且分两端——**动态端**(Bordelon–Atanasov–Pehlevan DMFT,最接近完整;Paquette–Pennington 最严格、证明级)和**静态谱端**(Bahri;Maloney–Roberts–Sully)。**平衡(谱)与非平衡(DMFT/SGD)两条路都能推出 scaling 指数。**

### 但"建成"要打两个折 **[已核验]**

1. **全是可解模型**:random-feature / lazy-kernel / 高维极限。**没有一个是关于"真实特征学习的 Transformer + 自然数据"的定理。** Bordelon–Atanasov–Pehlevan 的核心可解模型仍是线性化/lazy 的,特征学习主要靠经验补充;作者自己承认真实 compute-optimal 指数"需要一个核演化的机制理论"。
2. **谱指数 $a,b,\alpha_K$ 是"输入",不是第一性原理推出来的**。横档目前是"**核谱 → 指数**";"**数据几何 → 核谱**"这最后一段**尚未打通**。

**因此真正剩下的开放问题(也是最像"把假设变成定理"的活)**:
- (i) 对真·特征学习网络(非 lazy)自洽闭合 DMFT;
- (ii) 把谱指数本身从数据流形几何推导出来。

---

## 4. 宏观:涌现是不是真相变? **[已核验为"非纯假象" + 未核验细节]**

- **[已证否]** Schaeffer–Miranda–Koyejo 那个**强命题——"能力涌现纯粹是度量不连续造成的假象"——被 3 票判否(0-3)。** 即:把涌现**全部**归为度量假象,站不住;它至多是**部分**解释。
- **[已核验]** Paquette–Pennington 在可解模型里**证明了真相变(相边界)存在**。
- **综合当前最佳答案**:**涌现里有真东西,不全是海市蜃楼。** 至少在可解模型层面,存在带证明的相变;度量选择会放大/制造表观的突变,但不能解释全部。
- **[未核验]** Michaud–Tegmark 的 quantization 模型(离散"技能量子"按幂律频率叠加成光滑宏观幂律)、grokking 作为相变(Nanda;Liu omnigrok;Power)——这些提供了"微观尖锐涌现 → 宏观光滑幂律"的机制图景,但本轮未过对抗核验,列为待核实。

> **[已证否]** 另:有说法称 Bahri 等"从数据流形维数 $d$ 推出 $L\sim D^{-1/d}$、$4/\alpha_D=d$"——被 3 票判否(0-3),原文并无此推导。勿传。

---

## 5. 尚未核实的三块(留待定向核验) **[未核验]**

以下三块两轮 deep-research 均"源抓到、论断未过对抗核验",下述内容系整理者凭知识补写,**未经验证**:

- **守恒量 / 慢变量(纲领的结构核心)**:Kunin《Neural Mechanics》——对称(尺度/旋转)→ 梯度流下的严格守恒量,SGD/动量/weight-decay 会"破缺"之;Marcotte–Gribonval——独立守恒律数目的完整刻画。**关键判断(待核实):这些守恒量目前只约束微观轨迹,尚无工作把它们抬升为闭合的宏观理论。** 故"AI 有守恒量吗"最诚实的答案仍是:**有一些微观守恒量,但组织宏观理论的是序参量与记忆核,不是守恒律。**
- **奇异学习理论(SLT)/ 自由能**:Watanabe——自由能渐近由 **RLCT / 局部学习系数(LLC)** 控制,是"AI 的热力学"最有力的候选;贝叶斯相变、developmental interpretability(Lau–Murfet–Wei 等对 LLC 的估计)。**局限:贝叶斯后验 vs 真实 SGD 的系综差异**(见 §6)。
- **RG / 有效场论**:Roberts–Yaida–Hanin《Principles of Deep Learning Theory》(1/width 微扰、深宽比临界性);Greg Yang 的 Tensor Programs 与 muP/muTransfer(跨宽度的标度/RG 式结果);Mehta–Schwab 的 RG↔RBM 精确映射;信息瓶颈(Tishby)及 Saxe 的质疑。**判定(待核实):哪些是真 RG(粗粒化+不动点+普适),哪些只是名义类比。**

---

## 6. 头号开放问题:平衡与非平衡是同一枚硬币吗? **[已核验为开放问题]**

> **平衡系综(Gibbs)与非平衡稳态(DMFT),是不是同一个对象的两个极限?平衡描述是不是就是非平衡的 $t\to\infty$ 不动点?** mean-field Langevin 在长时间**确有一个自由能极小化子**;那 SGD 稳态究竟收敛到它,还是停在**没有自由能势的真·非平衡稳态**上?

**等价表述**:*SGD 稳态的权重分布,离玻尔兹曼–Gibbs 后验 $e^{-\beta L}$ 有多远?* 在可解模型(线性网、随机特征、单层感知机)里**可以真算**。它同时裁决"AI 该用热力学(SLT/自由能)还是动理学(DMFT)":
- 若近似成立 → AI 真有热力学,直接用统计力学收割宏观律;
- 若偏差显著 → 该偏差**就是**"AI 必须用动理学而非热力学"的精确度量。

本轮还发现一个相关的核验级开放问题:**§3 里静态谱端(Bahri、Maloney–Roberts–Sully)与动态端(Bordelon–Atanasov–Pehlevan、Paquette–Pennington)在重叠区间给出的指数是否一致?谁更根本?**——尚无定论。

---

## 7. 往上接:三个最有台阶可踩的落点

1. **[跨尺度,最像 Deng–Hani–Ma] 补横档的最后一段:从数据几何推出谱指数。**
   现有横档是"核谱 → 指数";把 $a,b,\alpha_K$ 本身从**数据流形几何 / 真实数据集性质**推出来,就把"数据 → 宏观律"整条打通。这是把可解模型里的"输入假设"变成"定理"的活。
2. **[非平衡,前沿在推] 对真·特征学习网络自洽闭合 DMFT。**
   Bordelon–Atanasov–Pehlevan 已把横档搭到"随机特征+可解";下一步是非 lazy 的机制性核演化理论——作者自己点名的缺口。
3. **[平衡侧,最扎实] 把 SLT(自由能/LLC)做实为"AI 的热力学",并回答 §6 那枚硬币。**
   在可解模型里直接测"SGD 稳态 vs Gibbs 后验"的距离,同时裁决平衡 vs 非平衡两条路线。

---

## 8. 参考文献(引文经检索确认存在)

**微观→中观(mean-field / propagation of chaos)**
- Mei, Montanari, Nguyen, *A mean field view of the landscape of two-layer networks*, PNAS (2018). arXiv:1804.06561
- Chizat & Bach, *On the global convergence of gradient descent for over-parameterized models*, NeurIPS (2018)
- Glasgow, Wu, Bruna, *propagation of chaos to poly-in-d time* (2025). arXiv:2504.13110

**中观(DMFT / NTK / 核演化)**
- Mignacco, Krzakala, Urbani, Zdeborová, *DMFT for SGD* (NeurIPS 2020 / JSTAT 2021). arXiv:2006.06098
- Gerbelot, Troiani, Mignacco, Krzakala, Zdeborová, *Rigorous DMFT for SGD* (2022). arXiv:2210.06591
- Jacot, Gabriel, Hongler, *Neural Tangent Kernel*, NeurIPS (2018). arXiv:1806.07572
- Bordelon & Pehlevan, *Self-consistent dynamical field theory of kernel evolution* (NeurIPS 2022 / JSTAT 2023). arXiv:2205.09653

**中观→宏观(scaling law 的推导)**
- Bahri, Dyer, Kaplan, Lee, Sharma, *Explaining Neural Scaling Laws*, PNAS (2024). arXiv:2102.06701
- Maloney, Roberts, Sully, *A Solvable Model of Neural Scaling Laws* (2022). arXiv:2210.16859
- Bordelon, Atanasov, Pehlevan, *A Dynamical Model of Neural Scaling Laws*, ICML (2024). arXiv:2402.01092
- Bordelon, Atanasov, Pehlevan, *How Feature Learning Can Improve Neural Scaling Laws*, ICLR (2025 Spotlight). arXiv:2409.17858
- Paquette, Paquette, Xiao, Pennington, *4+3 Phases of Compute-Optimal Neural Scaling Laws*, NeurIPS (2024). arXiv:2405.15074

**平衡侧统计力学(replica,背景)**
- Zdeborová & Krzakala, *Statistical physics of inference*, Adv. Phys. (2016). arXiv:1511.02476
- Abbara, Aubin, Krzakala, Zdeborová, *Rademacher complexity and spin glasses* (2020). arXiv:1912.02729

**宏观 / 涌现(部分未核验)**
- Wei et al, *Emergent Abilities of Large Language Models* (2022). arXiv:2206.07682
- Schaeffer, Miranda, Koyejo, *Are Emergent Abilities of LLMs a Mirage?* (2023). arXiv:2304.15004 —— 强命题被本综述核验判否
- Michaud, Liu, Girit, Tegmark, *The Quantization Model of Neural Scaling* (2023). arXiv:2303.13506 —— 未核验
- Nanda et al, *Progress measures for grokking* (2023). arXiv:2301.05217 —— 未核验

**守恒律 / SLT / RG(均未核验)**
- Kunin et al, *Neural Mechanics* (2020). arXiv:2012.04728
- Marcotte, Gribonval et al, *Conservation laws in gradient flows* (2023–24). arXiv:2307.00144, arXiv:2405.12888
- Watanabe, *Algebraic Geometry and Statistical Learning Theory* (CUP, 2009);LLC 近作 arXiv:2308.12108, arXiv:2402.02364
- Roberts, Yaida, Hanin, *The Principles of Deep Learning Theory* (CUP, 2022). arXiv:2106.10165
- Yang et al, *Tensor Programs / muTransfer*. arXiv:2011.14522, arXiv:2203.03466
- Mehta & Schwab, *Exact mapping between Variational RG and deep learning* (2014). arXiv:1410.3831
- Shwartz-Ziv & Tishby, *Information Bottleneck* (2017). arXiv:1703.00810;Saxe et al 质疑 (2018)

---

## 9. 覆盖状态与诚实边界

- **[已核验]**(两轮共 48 条三票通过,绝大多数基于 PNAS/ICML/NeurIPS/ICLR/JSTAT 同行评审):微观→中观(§1)、中观三候选(§2)、中观→宏观横档(§3)、涌现"非纯假象"(§4)、§6 开放问题。
- **[已证否]**(0-3):"涌现纯为度量假象"强命题;"Bahri 从流形维数推 $L\sim D^{-1/d}$"。
- **[未核验]**:守恒量、SLT/自由能、RG/有效场论(§5),及涌现的 quanta/grokking 机制细节(§4)——引文确认存在,论断待定向核验。
- **时效**:§3 为 2024–2025 活跃文献,可能已有更新的推广(超出 2026-01 知识截止)。

---

*本综述由两轮 deep-research 多智能体流程(共 220 个子智能体、~400 万 token、66 篇一手源、282 条论断、48 条三票核验)+ 领域知识整理生成。可信度分层见开头;§3 的结论纠正了本文档上一版"中观→宏观空白"的错判。*
