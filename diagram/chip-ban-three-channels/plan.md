# Diagram Plan: 美国芯片封锁的三条漏风口

**Material**: 黄仁勋文章 第四节《美国为什么封不住：三条都堵不上的通道》
**Type**: structural (three vertical sibling containers, rich interior)
**Slug**: chip-ban-three-channels

## Reader need
"After seeing this diagram, the reader understands why US export controls leak through three distinct, structurally different channels — and that each leak is the US's own design failure."

## Mermaid sketch

```mermaid
flowchart TD
  subgraph Ch1["通道一 · 合法"]
    C1T["境外租赁<br/>Offshore Rental"]
    C1B1["阿里、字节把 AI 训练搬到新加坡、马来西亚"]
    C1B2["字节经马来西亚运营商接入数据中心 / 云算力"]
    C1B3["AI Diffusion Rule 被川普一纸行政令撤回"]
  end
  subgraph Ch2["通道二 · 灰色"]
    C2T["走私渠道<br/>Gray Market"]
    C2B1["壳公司在新加坡、香港登记，经东南亚转口至深圳"]
    C2B2["DOJ 查获 1.6 亿，SemiAnalysis 估实际 10 亿+"]
    C2B3["中国 60%+ 前沿 AI 训练仍用英伟达硬件"]
  end
  subgraph Ch3["通道三 · 合规"]
    C3T["降级合规版<br/>Compliance Downgrade"]
    C3B1["H20：训练砍到阈值以下，推理几乎完整"]
    C3B2["部分推理基准比 H100 还快；华为昇腾同逻辑"]
    C3B3["美国盯训练，中国商业飞轮已转向推理"]
  end
  Ch1 -.-> Ch2 -.-> Ch3
  Ch3 -.-> Footer["美国想封没完全封，中国想买也没完全敞。一场怪异的双人舞。"]
```

## Layout math

- viewBox 680 × 580
- Outer margin x=60, content width 580
- Each container: height 125, stride 141 (16 gap)
  - Container 1: y 96–221
  - Container 2: y 237–362
  - Container 3: y 378–503
- Inside container: divider at x=220 splits left col (label) and right col (body)
  - eyebrow at +22, th at +54, ts at +74
  - body 1/2/3 at +54, +76, +98
- Header: title y=42, subtitle y=64
- Footer: caption-strong y=535, caption y=557

## Color strategy
- All three containers use neutral gray (they are structurally equivalent leaks)
- Accent used only on the right-aligned "leak magnitude" tag in each container (pulls the eye to the scale of each leak)

## Right-tag data points
- Ch 1: "→ 字节 36000 片 Blackwell"
- Ch 2: "→ 估算 10 亿美元 / 年"
- Ch 3: "→ 中国推理算力主力"
