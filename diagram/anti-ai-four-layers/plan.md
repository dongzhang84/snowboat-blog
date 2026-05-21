# Plan: 反感的四层叠加

## Mermaid sketch

```mermaid
flowchart TD
    subgraph Layers["四层叠加（同一个 22 岁毕业生身上）"]
        L1["LAYER 1 · 最直接<br/>生计层 / 应届就业崩盘<br/>大科技裁员 10 万 · 应届招聘 -50%<br/>42% Gen Z 担心被 AI 夺工作"]
        L2["LAYER 2<br/>制度层 / 学校 AI 双标<br/>老师用 AI 备课，学生用 AI 算作弊<br/>检测工具误判率 20% · 一边开 AI 主修一边罚学生"]
        L3["LAYER 3<br/>尊严层 / 创作者身份被冲击<br/>创作者身份不能外包 · 训练数据未经同意<br/>200 位音乐人公开信 · 1000 位英国艺术家抗议"]
        L4["LAYER 4 · 最弥散<br/>消费层 / AI 被塞进每个角落<br/>Google AI 总结错 37% · AI 客服转不到真人<br/>社交媒体 AI slop · 用得越多越讨厌"]
    end
    L1 --> L2 --> L3 --> L4
```

## Type

Illustrative — stack of four labeled layers visualizing how four layers of resentment co-occur in one person.

## Template reference

Closest match: `huang-ai-five-layers` (5 layers, 96 height, layer-top accent).
This diagram: 4 layers, 96 height, **LAYER 1 (生计层) marked as layer-key** (article calls it "最直接的一层").

## Layout math

- viewBox: 680 × 600
- Title region: y=42 (title), y=64 (subtitle)
- LAYER 1: y=96–192 (height 96), `class="layer-key"`
- LAYER 2: y=202–298
- LAYER 3: y=308–404
- LAYER 4: y=414–510
- Caption-strong: y=540
- Caption: y=572

Inside each layer:
- eyebrow at y_top + 22
- th at y_top + 50 (left), body t1 at y_top + 50 (right)
- ts at y_top + 70 (left), body t2 at y_top + 70 (right)
- divider y_top+14 to y_top+82

## Color budget

1 accent ramp (coral, default). LAYER 1 = layer-key + eyebrow-accent + divider-accent. LAYER 2–4 = neutral.
