# development-learning 使用文档

## 用途

这个 skill 用于开发任务后的半自动复盘。它帮助 agent 把一次开发讨论或实现过程沉淀为可复用思想、可观察风险、后续提醒，以及是否需要创建或优化新 skill 的判断。

它不保存完整聊天记录，不替代项目规范，也不根据单次事件给用户贴长期标签。

## 常用口令

| 你说 | agent 应该做什么 |
|---|---|
| `复盘一下这次开发` | 生成一条任务复盘，并更新总览索引。 |
| `记录成学习论` | 抽象本次可复用思想，写入复盘和 `index.md`。 |
| `复盘总览` | 展示当前所有复盘摘要、思想、风险和 skill 候选。 |
| `展开复盘总览` | 在总览基础上展开更多细节。 |
| `展开某条复盘` | 读取并展示指定复盘文件内容。 |
| `这类问题以后做成 skill` | 更新 `skill-candidates.md`，并判断是否进入 skill 创建流程。 |
| `优化 development-learning` | 先执行自我修改协议，再决定是否修改该 skill。 |

## 输出内容

一次标准复盘包含：

- 任务目标
- 关键上下文
- 关键讨论
- 关键决策
- 被放弃方案
- 可复用思想
- 暴露的问题
- 下次提醒
- Skill 演化判断

只有重复复盘或跨范围总览才追加“重复复盘校验”。普通任务复盘不需要该小节。

## 详细规则

写入或更新复盘前，agent 必须读取：

```text
<AGENTS_HOME>\skills\development-learning\references\review-rules.md
```

详细规则集中维护在 `review-rules.md`，包括质量门禁、质量自检、索引容量、重复复盘防过拟合、复盘模板、证据规则、skill 候选规则、红旗和反合理化表。

`index.md` 必须保持可扫读。长期细节应留在 `reviews\*.md` 或 `skill-candidates.md`，不要把总览变成第二份复盘全集。

## 数据位置

```text
<AGENTS_HOME>\data\development-learning\
  index.md
  skill-candidates.md
  development-learning-evolution.md
  reviews\
```

`<AGENTS_HOME>` 表示当前 agent 的个人配置根目录，通常是包含 `skills\` 目录的上一级目录。

## 使用建议

在一次任务完成后使用：

```text
复盘一下这次开发，沉淀学习论。
```

当你想查看长期积累时使用：

```text
复盘总览
```

当你觉得某类问题反复出现时使用：

```text
这类问题以后做成 skill。
```

## 修改该 skill 的规则

修改 `development-learning` 前，agent 必须先判断问题来源：

- skill 规则确实缺失
- 当前 agent 没按规则执行
- 用户偏好变化
- 某个项目的局部经验不适合写入通用 skill

只有第一类和稳定的第三类适合修改 `SKILL.md`。项目局部经验写入项目文档或普通复盘，不能塞进通用 skill。

修改或验证该 skill 时，可读取：

```text
<AGENTS_HOME>\skills\development-learning\references\test-scenarios.md
```

修改学习数据结构或检查索引、候选项一致性时，运行：

```bash
python <AGENTS_HOME>\skills\development-learning\scripts\validate_development_learning.py
```
