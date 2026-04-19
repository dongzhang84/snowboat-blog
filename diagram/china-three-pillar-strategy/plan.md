# Diagram Plan: 中国的三支柱策略

**Material**: 黄仁勋文章 第八节《中国该怎么打这场仗》
**Type**: structural (3 stacked sibling containers, rich interior)
**Slug**: china-three-pillar-strategy

## Reader need
"After seeing this diagram, the reader understands China's playbook is not 'accelerate indigenization at any cost', but a three-part strategy: anchor the home field, close the software-stack gap, and let the opponent's mistakes compound over time."

## Design consistency
Matches `diagram/chip-ban-three-channels/diagram.svg` visual template (3 stacked containers, same layout math). The two diagrams are mirror images: one about the US wall's three leaks, one about China's three strategic pillars.

## Color strategy
- Gray neutral for all three containers (pillars are complementary, not hierarchical)
- Accent on right-tag in each container (puts the punchy takeaway in accent)

## Three pillars

**一 · 守主场 (Anchor the Home Field)**
- Right tag: "→ 14 亿用户 · 完整闭环"
- Body 1: "抖音、微信、淘宝、美团 + 制造业 AI 需求"
- Body 2: "豆包 16.4 万亿 token/天；通义千问 6 亿下载、17 万衍生模型"
- Body 3: "把推理规模优势出海至东南亚、中东、拉美、非洲"

**二 · 补短板 (Close the Gaps)**
- Right tag: "→ 真瓶颈是软件栈，不是硬件"
- Body 1: "CUDA 惯性：PyTorch / vLLM / Megatron-LM 全 CUDA 原生"
- Body 2: "华为 CANN、国产 MUSA 在爬，速度还不够快"
- Body 3: "真正自主在编译器 toolchain、TVM 改造、GPU 无关中间层"

**三 · 掌握节奏和叙事 (Set Your Own Tempo)**
- Right tag: "→ "6 个月窗口期"是心理战"
- Body 1: "国产化分层：前沿训练合规英伟达，推理逐步迁国产"
- Body 2: "消费级 API 完全依赖国产生态，给国产厂商订单规模"
- Body 3: "时间站在中国这边，能源 + 中端芯片代际优势会继续变现"

## Footer
- Caption-strong: ""守住主场，补齐短板，然后等美国自己把手里的牌打坏。""
- Caption: "鹰派正在加速帮中国完成最后这件事。"

## Layout math (same as chip-ban-three-channels)
- viewBox 680 × 580
- Container height 125, stride 141
- Container 1: y 96-221
- Container 2: y 237-362
- Container 3: y 378-503
- Footer: caption-strong y=535, caption y=557
