# 《AI Agent 时代的审查瓶颈》事实核查

核查日期：2026-08-16

结论：文章主线成立。开源、安全、学术、招聘、教育都确实出现了“生成端变便宜，审查端没同步扩容”的公开案例。但正文里有几处数字和口径需要改，否则容易被抓。

## 需要优先修改

| 位置 | 原文说法 | 核查结论 | 建议改法 |
| --- | --- | --- | --- |
| 开头 Rust 政策 | “2026 年 8 月 5 日，rust-lang/rust 的五个团队通过了一份 LLM 使用政策” | 高风险。能查到的是 2026 年 5 月底 Socket 报道“政策仍是 PR / proposed policy”，7 月 Rust 官方博客还在说要成立 LLM committee。没有查到 8 月 5 日官方通过公告。Socket 支持“3000 多条 Zulip 讨论”和草案内容，但不支持“已经通过”。 | 改成“2026 年春夏，rust-lang/rust 围绕 LLM 贡献政策展开正式讨论；草案覆盖 compiler、libs、types、rustdoc、bootstrap 等团队相关工作”。如果必须写“通过”，需要补官方链接。 |
| 1.1 token 价格 | “Gemini 3.1 Flash 每百万输入 0.1 美元、输出 0.4 美元” | 错。Google 当前价格里，Gemini 3 Flash 是 $0.50 / $3.00，Gemini 3.1 Flash-Lite 是 $0.25 / $1.50。$0.10 / $0.40 更像 Gemini 2.0 Flash 或 2.5 Flash-Lite 这一档。 | 改成“Gemini 2.5 Flash-Lite / 2.0 Flash 这一档低到每百万输入 0.1 美元、输出 0.4 美元”，或者用官方 Gemini 3.1 Flash-Lite 的 $0.25 / $1.50。 |
| 1.2 编码 agent 成本 | “主流模型落在 0.03 到 0.13 美元之间” | 口径偏窄。SSOJet 的计算里便宜模型确实有 $0.028、$0.033、$0.059、$0.075、$0.078，但 Claude Haiku 4.5 是 $0.150，GPT-5.1 是 $0.239，Claude Opus 4.5 是 $0.680。 | 改成“便宜和中档模型可低到 0.03 到 0.08 美元，闭源旗舰可到 0.2 到 0.7 美元”。 |
| 3.2 AAAI-26 | “AAAI-26 超过 30,000 份初始投稿，上一届 AAAI-25 是 12,957 份” | 需要统一口径。AI Review Pilot 支持 22,977 篇进入完整评审、24 小时生成 AI review、每篇低于 1 美元；一些报道说初始投稿超过 30,000。但 AAAI-26 主技术轨公开统计也有 23,680 这个口径。12,957 是 AAAI-25 main track 口径。 | 改成“AAAI-26 初始投稿据试点论文和报道超过 30,000；其中 22,977 篇进入完整评审。若按 main technical track 统计，AAAI-26 与 AAAI-25 的口径要另行说明。” |
| 3.2 法律幻觉数据库 | “8 月 8 日 1,868 起” | 当前可查 live page 显示 2026-07-29 更新为 1,812 起；7 月 2 日 1,668 起、653 执业律师、975 自行诉讼者有二手统计支持。没有核到 8 月 8 日 1,868。 | 改成“截至 2026 年 7 月底约 1,800 起；7 月 2 日统计为 1,668 起，其中 653 起涉及执业律师、975 起涉及自行诉讼者。” |
| 5.5 NSF | “NSF 现在允许提案只收到最少一份外部评审，此前下限是三份” | 很可能错。可查到的说法是：最低外部评审从 3 份降到 2 份，其中一份可由 NSF staff 内部完成；panel review 可选；摘要缩到 3 到 5 句。 | 改成“NSF 把完整提案的最低评审数从三份降到两份，并允许其中一份由 NSF 内部人员完成，同时减少常规 panel 使用。” |

## 基本成立的关键事实

| 位置 | 结论 | 依据 |
| --- | --- | --- |
| curl 赏金关闭 | 成立。Daniel Stenberg 2026-01-26 宣布 curl bug bounty 于 1 月底结束；87 个确认漏洞、超过 10 万美元奖金、2025 年确认率跌到 5% 以下都能核到。1 月 16 日邮件也支持“16 小时 7 份报告、2026 年已 20 份、真实漏洞为 0”。 | Daniel Stenberg 博客与邮件列表 |
| curl 回 HackerOne | 成立。2026-02-25 博客说 3 月 1 日回 HackerOne；4 月复盘说 slop 问题缓解，但报告频率更高。 | Daniel Stenberg 博客 |
| GitHub PR 量 | 成立。GitHub 2026-06-18 官方博客写明，2023 年 1 月每月约 2500 万 merged PR，现在超过 9000 万，约 3.6 倍，并推出 PR limits。 | GitHub Blog |
| GitHub PR limits | 成立。非写权限用户可被限制同时打开的 PR 数，可信贡献者可豁免，AI agent PR 也计入。 | GitHub Blog |
| Node.js Signal 1.0 | 成立。Node.js 2026-02-19 公告要求 HackerOne Signal >= 1.0，低于门槛者走 OpenJS Slack。 | Node.js 官方公告 |
| GitHub bug bounty VIP 分层 | 成立。GitHub 2026-07-22 公告，7 月 27 日生效；public critical 固定 $10,000，VIP critical $30,000+。 | GitHub Blog |
| Organization Science | 成立。论文摘要支持投稿量自 ChatGPT 后增 42%、写作质量下降，AI 生成写作解释了几乎全部趋势。 | Organization Science |
| NeurIPS 2025 | 成立。官方博客支持 21,575 有效投稿、5,290 录取、24.52%；也明确否认主会录取数受场地容量约束。 | NeurIPS 官方博客 |
| Princeton 监考 | 成立。2026-05-11 教授会几乎一致通过，7 月 1 日生效，结束 1893 年以来线下考试免监考传统，只有 1 票反对。 | Princeton Alumni Weekly |
| Ashby 招聘数据 | 成立。Ashby 2026-05-07 公告支持 1 亿+申请、20 万+岗位、applications per hire 自 2021 年以来翻三倍、平均超过 300、进入面试概率约为五年前一半。 | Ashby / PRNewswire |
| DORA 2025 trust | 成立。DORA 相关页面支持 30% 开发者对 AI 生成输出只有 little/no trust，也支持“验证税”的叙述。 | DORA |
| METR RCT | 成立但要保留时间口径。早 2025 实验支持 16 名资深开源开发者、246 个任务、AI 组慢 19%、事前预期快约 24%、事后仍感觉快约 20%。METR 2026-02 又说后续实验信号不可靠，早 2026 可能已有提升。 | METR |
| GitClear | 大方向成立，但数字要精确。211M lines 成立；copy-pasted lines 从 8.3% 到 12.3%、refactored/moved lines 从约 24.1% 到 9.5% 有二手复述。正文“克隆代码块八倍”需要直接对照 GitClear 原报告，二手来源更多说四倍或八倍不一。 | GitClear press / 二手复述 |
| tldraw | 成立。2026-01-15 issue 宣布自动关闭外部 PR，1 月 17 日博客解释低质量 AI PR。 | tldraw GitHub issue / blog |
| OpenAI Erdős 单位距离 | 成立。OpenAI 2026-05-20 公告说内部模型推翻 Erdős 单位距离猜想，外部数学家检查，使用代数数论工具。Erdős Problems 页面标为 DISPROVED (LEAN)。 | OpenAI / Erdős Problems |
| GNoME | 成立。DeepMind 支持 220 万新晶体、38 万稳定候选、736 个外部并行实验实现、A-Lab 合成 41 个新材料。 | Google DeepMind |
| GNoME disorder 风险 | 成立。Advanced Materials 论文支持 GNoME set 中 80% 到 84% 可能有 substitutional disorder。 | Wiley / Advanced Materials |

## 建议补强或降调

1. “一个开源项目公开给自己的贡献流量设断路器，此前没有先例”这句太绝对。可以保留意思，但改成“这在主流开源项目里已经很罕见”，避免被人拿其它项目政策反例打。

2. “AI 评审意见与编辑最终决定不相关”需要从 Organization Science 正文或附录确认。摘要支持 AI 写作和评审质量问题，但“不相关”这个统计结论需要更精确出处。

3. “Anthropic 用 Claude Opus 4.6 在 Firefox 两周找出 22 个漏洞，其中 14 个高危，112 份唯一崩溃报告，Mozilla 148.0 修复”目前主要依赖 TechCrunch。建议补 Mozilla Bugzilla、Anthropic 技术博客或 Mozilla 安全公告，否则写成“据 TechCrunch 报道”。

4. “IBB 3 月 27 日暂停、80% 支出发现 / 20% 修复”需要尽量找 HackerOne 或 IBB 官方原文。现在可以用 InfoWorld 等媒体，但这是文章核心案例之一，最好有一手链接。

5. “CPU 跑几分钟替代专家审一年”这句有感染力，但 Lean formalization 这例子实际是 100 万到 120 万行 Lean 代码，Kevin Buzzard 也提醒代码不等于可读数学证明。建议改成“可验证性从相信专家转成相信 proof checker，但把证明整理成可读、可维护的数学仍然是另一件事”。

## 可直接改正文的几句

- Rust 开头：  
  “2026 年春夏，rust-lang/rust 围绕一份 LLM 使用政策草案展开了持续讨论。Socket 报道称，这场讨论在 Zulip 上超过三千条消息，草案试图把 LLM 私下辅助和公开署名创造分开。”

- token 价格：  
  “2026 年，Gemini 2.5 Flash-Lite / 2.0 Flash 这一档已经低到每百万输入 token 0.1 美元、输出 0.4 美元；即使用 Gemini 3.1 Flash-Lite，价格也只是 0.25 / 1.50 美元。”

- AAAI：  
  “AAAI-26 初始投稿据报道超过 30,000 份，其中 22,977 篇进入完整评审阶段，并全部收到一份明确标注的 AI 评审。”

- NSF：  
  “NSF 的变化不能简单归因于 AI。它把完整提案的最低评审数从三份降到两份，并允许其中一份由 NSF 内部人员完成，同时压缩 panel 和评审摘要。这更像行政与人力收缩造成的同型现象。”

## 主要来源

- Rust draft policy and discussion: https://socket.dev/blog/rust-moves-to-restrict-llm-use-in-contributions
- Rust LLM committee update: https://blog.rust-lang.org/inside-rust/2026/07/14/program-management-update--june-2026/
- curl bug bounty end: https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/
- curl January reports: https://lists.haxx.se/pipermail/daniel/2026-January/000143.html
- curl back to HackerOne: https://daniel.haxx.se/blog/2026/02/25/curl-security-moves-again/
- GitHub PR limits: https://github.blog/open-source/maintainers/how-pull-request-limits-are-cutting-down-the-noise/
- Node.js Signal requirement: https://nodejs.org/en/blog/announcements/hackerone-signal-requirement
- GitHub bounty restructuring: https://github.blog/security/next-chapter-restructuring-githubs-bug-bounty-program/
- Organization Science peer review paper: https://pubsonline.informs.org/doi/10.1287/orsc.2026.ed.v37.n3
- AAAI AI review pilot: https://www.alphaxiv.org/overview/2604.13940
- NeurIPS 2025 review process: https://blog.neurips.cc/2025/09/30/
- Princeton proctoring: https://paw.princeton.edu/article/after-133-years-princeton-going-back-proctoring-exams
- Ashby hiring data: https://www.prnewswire.com/news-releases/new-data-from-ashby-reveals-surge-in-applications-rising-selectivity-and-shifting-recruiter-workloads-302765846.html
- DORA 2025: https://dora.dev/research/2025/dora-report/
- METR productivity experiment update: https://metr.org/blog/2026-02-24-uplift-update/
- OpenAI Erdős unit distance: https://openai.com/index/model-disproves-discrete-geometry-conjecture/
- Erdős Problems Lean status: https://www.erdosproblems.com/search_bib/Er83c/solved
- GNoME: https://deepmind.google/en/blog/millions-of-new-materials-discovered-with-deep-learning/
- GNoME disorder analysis: https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/adma.202514226
