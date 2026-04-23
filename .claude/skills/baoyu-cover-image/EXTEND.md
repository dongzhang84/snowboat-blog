# 封面默认风格

## 触发

用户说"做封面"、"给 XX 做封面"、"来个封面"之类时，直接按下面动作，不问。

## 动作

1. 从上下文推断 `<slug>`（kebab-case，取自当前文章文件名，没有就向用户一句话要）
2. 从上下文或用户消息拿第一行、第二行文案（第一行是铺垫，第二行是文章主句）
3. 跑：
   ```bash
   python3 scripts/cover.py <slug> "第一行" "第二行"
   ```
4. 向用户报告输出路径 `cover-image/<slug>/cover.png`

## 原则

- 不要问维度（type、palette、rendering 等），默认风格已定
- 不要生成额外 prompt 文件、markdown、reference
- 不要去调 AI 图像后端，只跑这个 Python 脚本
- 只有用户明确说"换风格 / 换配色 / 换尺寸"才偏离
