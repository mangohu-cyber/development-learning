# development-learning 复盘规则

## 复盘门禁

写入或更新复盘前：

1. IDENTIFY: 明确被复盘的是任务、讨论、决策还是失败。
2. COLLECT: 收集来自用户约束、决策、文件变更、验证输出或明确反馈的证据。
3. CLASSIFY: 判断每条内容是可复用思想、风险、普通细节还是 skill 候选。
4. FILTER: 移除聊天流水、猜测、人格标签和项目专用规则。
5. WRITE: 只写相关学习文件。
6. VERIFY: 确认 `index.md`、`skill-candidates.md`、演化记录仍保持正确粒度。

## 质量自检

写入复盘后，完成前检查：

- Evidence: 每条可复用思想、风险和 skill 判断都有证据。
- Labels: “暴露的问题”描述可观察行为或流程风险，不贴人格标签。
- Scope: 项目专用规则没有写入通用 skill。
- Dedup: 重复复盘或跨范围总览没有重复计权。
- Index: `index.md` 只保留稳定摘要和指针。
- Candidates: `skill-candidates.md` 记录状态、证据、边界和下一步。
- Evolution: 修改本 skill 时已更新 `development-learning-evolution.md`。

任一项失败时，先修正学习文件，再报告完成。

## index 容量规则

`index.md` 是总览，不是第二份复盘全集。

- 保留稳定思想、活跃风险、复盘链接、skill 候选摘要和当前边界。
- 详细证据、长解释和历史叙事放入 `reviews\*.md`。
- 旧候选或撤销候选的细节放入 `skill-candidates.md`。
- 分区过长时，合并相似条目，只保留最新稳定表述。
- `复盘总览` 不能默认展开全部复盘细节。

## 重复复盘防过拟合

同一月份、同一任务、同一历史范围或同一 manifest 被再次复盘时，先声明这是重复复盘或跨范围总览。

重复复盘只能做：

- 补充新增证据
- 修正旧结论
- 合并或拆分旧结论
- 降级或撤销旧结论
- 输出跨范围总览

重复阅读同一批历史不能增加证据权重，不能把观察中事项升级为稳定缺点，也不能把 skill 候选直接推进为应创建。

### 重复复盘协议

1. DECLARE: 说明是首次复盘、重复复盘还是跨范围总览。
2. COMPARE: 写入前定位同范围已有复盘。
3. DELTA: 区分新增证据与旧证据重新解释。
4. DEDUP: 不把同一会话、摘要、统计、文件变更或用户反馈重复计数。
5. COUNTERCHECK: 检查什么信息会削弱或反驳旧结论。
6. WRITE: 优先更新已有复盘或追加重复复盘小节，不为同范围创建重复文件。
7. GRADE: 标记结论强度：单次观察、同范围重复观察、跨周期观察、跨项目观察、明确用户反馈。

## 普通复盘模板

```markdown
# YYYY-MM-DD 任务复盘：标题

## 任务目标
本次任务要解决的问题和边界。

## 关键上下文
仓库、模块、文件、约束、用户明确要求。

## 关键讨论
只记录影响判断的信息，不记录流水账。

## 关键决策
最终采用的方案，以及选择原因。

## 被放弃方案
放弃了哪些方案，原因是什么。

## 可复用思想
从本次任务抽象出的判断原则、方法或检查清单。

## 暴露的问题
基于证据描述开发过程中的问题，不贴人格标签。

## 下次提醒
后续遇到相似场景时，agent 应该如何提醒用户或约束自己。

## Skill 演化判断
- 结论：不需要 / 候选 / 应创建 / 应优化
- 证据：
- 建议：
```

## 重复复盘附加模板

仅在复盘范围与已有证据重叠时追加：

```markdown
## 重复复盘校验
- 复盘类型：重复复盘 / 跨范围总览
- 已存在的同范围复盘：
- 本轮新增证据：
- 本轮只是重新解释的旧证据：
- 未重复计权的证据：
- 被削弱、降级或撤销的结论：
- 结论强度：
```

## 证据规则

记录行为和上下文，不贴标签。

Good:

```text
本次在需求边界未完全明确前已经讨论实现路径，后续类似场景应先确认目标、非目标和验证方式。
```

Bad:

```text
用户需求不清楚。
用户不重视测试。
用户容易犯低级错误。
```

不要记录私下猜测。不要把一次事件变成长期用户特质。证据弱时标记为“观察中”。

## Skill 候选规则

只有至少两个条件成立时，才建议创建或优化 skill：

- 同类问题出现两次以上。
- agent 在这类任务中容易遗漏关键步骤。
- 该经验跨项目适用。
- 该经验是判断型流程，不能简单靠脚本或检查器替代。
- 用户明确要求沉淀为 skill。
- 该流程会影响代码质量、验证质量或需求理解质量。

只有一个条件成立时，记录为“观察中”。

重复复盘同一批历史不能算独立出现次数。候选只能被新周期、新任务、新项目、新验证失败或用户明确指令增强。

## 红旗

- 准备复制完整对话到复盘。
- 准备用人格标签描述用户。
- “暴露的问题”没有证据。
- 想把普通学习内容放进 `SKILL.md`。
- 想把项目规则写进通用 skill。
- 想从单次事件创建新 skill，且没有用户明确指令。
- 处理 `复盘总览` 时准备默认展开全部复盘。
- 修改本 skill 前没有判断是设计缺口还是执行偏差。
- 重复阅读同一历史时准备当成新证据。

## 反合理化

| Excuse | Reality |
|---|---|
| "This was a small task, no review is needed." | Small tasks still require a quick trigger check when learning or risk evidence exists. |
| "The user's weakness is obvious." | Only observed behavior and context can be recorded; no labels. |
| "This lesson is useful, put it in SKILL.md." | `SKILL.md` is for process rules; lessons belong in `development-learning`. |
| "This would be a useful skill, create it now." | Unless explicitly requested or supported by enough evidence, record a candidate first. |
| "复盘总览 should show everything." | The overview shows `index.md`; expansion requires a request. |
| "The skill failed, so change the skill." | First decide whether the skill rule is missing or the current agent ignored it. |
| "I reviewed the same month three times, so the evidence is stronger." | Same-scope repetition is not new evidence; record only deltas, corrections, and confidence changes. |
