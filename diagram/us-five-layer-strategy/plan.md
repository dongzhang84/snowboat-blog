# Diagram Plan: 五层框架 · 美国真正该打的仗

**Material**: 黄仁勋文章 第七节《回到五层框架：美国到底该怎么打这场仗》
**Type**: structural (5 stacked layers, rich interior)
**Slug**: us-five-layer-strategy

## Reader need
"After seeing this diagram, the reader understands that the US cannot win all five layers, and that the current hawk strategy is sacrificing the US's strongest moats (Layer 3 CUDA, Layer 5 apps) to marginally delay Layer 4 (models)."

## Design consistency
Use the same 5-layer stacking as `diagram/huang-ai-five-layers/diagram.svg`. Two diagrams in the same article should share visual language.

## Color strategy
- Gray neutral for Layers 1, 2, 4, 5
- Accent (rose/coral) for **Layer 3** — the critical moat being destroyed by embargo
- Right-tag in each layer uses accent text for Layer 3 only; others use soft eyebrow

## Layout

- viewBox 680 × 720
- Layer stacking (top = Layer 5, bottom = Layer 1), matching huang diagram
- Container height 100, stride 112 (12 gap)
  - Layer 5: y 96–196
  - Layer 4: y 208–308
  - Layer 3: y 320–420 (accent background)
  - Layer 2: y 432–532
  - Layer 1: y 544–644
- Footer: caption-strong y=680, caption y=702

## Per-layer content

**Layer 5 · 应用 (Applications)**
- Right tag: "深耕主场 · 出海第三方"
- Body 1: "消费 AI 中美分市场；企业 SaaS 美国仍有地盘"
- Body 2: "深耕 Fortune 500 / 盟友；在东南亚、中东反入侵"

**Layer 4 · 模型 (Models)**
- Right tag: "持续投入 · 不靠封锁"
- Body 1: "领先缩到 3-6 个月（2024 年还是 12 个月）"
- Body 2: "真正护城河是 OpenAI / Anthropic 的资本开支"

**Layer 3 · 基础设施 (Infrastructure)** ← ACCENT
- Right tag: "开门卖 · 留住开发者"
- Body 1: "CUDA 是 20 年开发者生态，技术可复制，生态不能一夜搬家"
- Body 2: "禁运把全球一半开发者推向 CANN / MUSA，亲手拆城墙"

**Layer 2 · 芯片 (Chips)**
- Right tag: "守 3nm 以下 · 放 7nm 以上"
- Body 1: "3nm 以下美国联盟领先 10-15 年，EUV 是真卡点"
- Body 2: "7-28nm 中端中国实质自给，继续管制没有边际收益"

**Layer 1 · 能源 (Energy)**
- Right tag: "接受落后 · 走侧门"
- Body 1: "中国发电量 2× 美国，新增装机仍在翻"
- Body 2: "侧门：能效优化、SMR 核电、加拿大 / 中东盟友能源"

## Footer
- Caption-strong: ""不要为了第 4 层，亲手把第 3 层和第 5 层送走。""
- Caption: "鹰派当前的交换比率是灾难性的。"
