# Plan: DPO 与开源后训练的简化路线（第四章）

## Type
Structural subsystem 左右对比。RLHF 三步 vs DPO 一步，底部 footer 加变体清单、工具栈、大厂 vs 开源选择逻辑。

## 布局
viewBox 680 × 540
- title y=42 "DPO 与开源后训练的简化路线"
- subtitle y=64 "RLHF 三步 → DPO 一步，工程门槛从大厂拉到开源"
- 左容器 RLHF (PPO): x=60, y=95, w=270, h=300
- 中间 "vs"
- 右容器 DPO: x=350, y=95, w=270, h=300
- 底部三块: 变体 / 工具栈 / 选择逻辑

## 左容器内容（RLHF/PPO）
- eyebrow "大厂路线"
- th "RLHF (PPO)"
- ts "几十人 RL 团队"
- right tag "→ 工程门槛极高"
- 三个 stacked pill: SFT / 训 reward model / PPO RL + KL 约束
- 末尾注脚: 灵活 / reward shaping / multi-stage

## 右容器内容（DPO）
- eyebrow "开源主流"
- th "DPO"
- ts "Stanford 2023"
- right tag "→ 4×H100 几天可跑"
- 两个 stacked pill: SFT / 直接对比损失训偏好数据
- 末尾注脚: 不需 reward model, 不需 PPO

## 底部内容
- DPO 变体: IPO (防过拟合) / KTO (单标签 OK) / ORPO (合并 SFT)
- 开源工具栈: TRL / Axolotl / Unsloth / LLaMA-Factory
- 选择逻辑: 大厂 PPO 灵活 / 开源 DPO 稳定; 2026 趋势两边收敛 (大厂测 DPO, 开源测 GRPO)

## Reader need
读者一眼看清第四章核心论点: DPO 把 RLHF 三步压成一步, 这是让开源后训练真正走得通的工程演化。
