# Diagram Plan: 退款 agent 的 8 层壳

**Material**: 《别再被 AI 新词绕晕了：Prompt、Context、Agent 背后的工程主线》5.2 小节
**Type**: flowchart (8-layer harness pipeline)
**Slug**: refund-agent-harness

## Reader need
"After seeing this diagram, the reader understands that a production refund agent is not just an LLM call; it is an 8-layer harness where only Layer 3 runs the model and the other 7 layers are traditional engineering controls."

## Mermaid sketch

```mermaid
flowchart TD
  A["用户邮件"]
  L1["1. 入口验证<br/>sanitize + classifier"]
  L2["2. 上下文准备<br/>客户 / 订单 / 政策 / 物流"]
  L3["3. 结构化输出约束<br/>LLM 输出 JSON"]
  L4["4. 输出验证<br/>金额 / 置信度 / reason / action"]
  L5["5. 执行<br/>退款 API + 幂等 key + 人工审批"]
  L6["6. 执行后验证<br/>支付系统复查 + 对账"]
  L7["7. 可观测性<br/>logs / trace / metrics"]
  L8["8. 熔断 + 人工介入<br/>失败率 / 异常流量 / oncall"]
  Z["退款或转人工"]
  A --> L1 --> L2 --> L3 --> L4 --> L5 --> L6 --> L7 --> L8 --> Z
```

## Layout math

- viewBox: 680 × 1000
- Outer margin x=60, content width 580
- 9 compact containers, each 82 px high, 8 px gap
  - Input: y 96–178
  - Layer 1: y 186–268
  - Layer 2: y 276–358
  - Layer 3: y 366–448
  - Layer 4: y 456–538
  - Layer 5: y 546–628
  - Layer 6: y 636–718
  - Layer 7: y 726–808
  - Layer 8: y 816–898
- Footer: y=938 / 960
- Left column x=82–220; right column x=238–640; divider x=220

## Color strategy

- Layer 3 uses accent because it is the only LLM step.
- Other layers are neutral, emphasizing that the harness is mostly traditional backend / SRE work.
- Right tags categorize each layer: gate, context, LLM, validator, API, reconciliation, observability, breaker.

## Text compression

- No raw code or JSON in SVG.
- Keep each right body line short.
- Footer takeaway: "只有第 3 层是 LLM，其余 7 层都是工程壳。"
