---
name: development-learning
description: Use when a development task, debugging session, design discussion, code review, or skill-authoring session needs a retrospective, reusable learning notes, weakness/risk identification, a "复盘总览" overview, or a decision about creating or improving workflow skills.
---

# Development Learning

流程版本：v0.4

## Overview

Use this skill to turn development work into evidence-based learning records. Capture reusable thinking, observed process risks, and skill evolution candidates without storing full chat logs or making personality judgments.

Learning data lives under the agent's personal data root:

```text
<AGENTS_HOME>\data\development-learning\
```

Resolve `<AGENTS_HOME>` from the current agent environment. For Codex-style personal skills, it is usually the parent directory that contains `skills\`.

Read `references/usage.md` when the user asks how to use this skill, asks for the skill usage document, or needs examples of commands and expected behavior.

Read `references/test-scenarios.md` when validating this skill, modifying this skill, or checking whether future agents will follow the intended behavior.

## The Iron Law

```text
NO LEARNING RECORD WITHOUT EVIDENCE.
NO USER WEAKNESS CLAIM WITHOUT OBSERVED BEHAVIOR.
NO NEW SKILL CANDIDATE WITHOUT TRIGGER CONDITIONS.
NO EXTRA EVIDENCE WEIGHT FROM REPEATED REVIEW OF THE SAME HISTORY.
```

If there is no evidence, do not invent a lesson. If there is only weak evidence, record it as "观察中". If the content is project-specific, do not put it in this general skill.

When reviewing the same history more than once, repeated reading is not new evidence. It can only refine, correct, split, merge, downgrade, or revoke conclusions.

## Trigger Decision

If the user says exactly `复盘总览`, show the current overview from `index.md`. If the user asks to expand, read the relevant review files.

If a development task just ended, or the user says "复盘", "总结这次开发", "记录成学习论", or "沉淀经验", create or update a task retrospective.

If the user asks to create, optimize, or evaluate a skill, include skill evolution judgment. For actual skill creation or editing, use the relevant skill-authoring workflow after recording the candidate or evolution context.

If the user says "优化 development-learning", "修改这个复盘 skill", or reports that this skill behaved poorly, follow the self-modification protocol before editing the skill.

## Data Files

Maintain these files:

```text
<AGENTS_HOME>\data\development-learning\
  index.md
  skill-candidates.md
  development-learning-evolution.md
  reviews\
    YYYY-MM-DD-topic.md
```

- `index.md`: scannable overview of principles, observed risks, review list, and skill candidates.
- `skill-candidates.md`: candidate workflow skills and evidence for creating or improving them.
- `development-learning-evolution.md`: changes to this skill itself.
- `reviews\*.md`: one complete retrospective per meaningful task.

Create missing directories or files before writing. Preserve existing content and append/update only the relevant sections.

## Retrospective Workflow

1. State the goal and boundary in one sentence before writing files.
2. Gather evidence from the current discussion, changed files, decisions, verification output, and user constraints.
3. Create one review file under `reviews\YYYY-MM-DD-topic.md`.
4. Update `index.md` with only summaries and links, not full review content.
5. Update `skill-candidates.md` when the task suggests a new or improved skill.
6. If this skill itself changed, update `development-learning-evolution.md`.
7. Report the written or updated paths and the main learning points.

## Retrospective Gate Function

Before writing or updating a retrospective:

1. IDENTIFY: What task, discussion, decision, or failure is being reviewed?
2. COLLECT: What evidence exists from user constraints, decisions, file changes, verification, or explicit feedback?
3. CLASSIFY: Is each item a reusable principle, observed risk, normal task detail, or skill candidate?
4. FILTER: Remove chat logs, speculation, personality labels, and project-specific rules that belong elsewhere.
5. WRITE: Create or update only the relevant learning files.
6. VERIFY: Confirm `index.md`, `skill-candidates.md`, and evolution records still point to the right level of detail.

Skip any step and the retrospective is not reliable.

## Repeat Review Anti-Overfitting Protocol

Use this protocol when the requested review scope overlaps an existing review, such as the same month, same task, same exported history range, or the same source manifest.

1. DECLARE: State whether this is a first review, a repeated review, or a cross-scope synthesis.
2. COMPARE: Locate the existing review for the same scope before writing.
3. DELTA: Separate new evidence from reinterpretation of old evidence.
4. DEDUP: Do not count the same conversation, summary, stat, file change, or user feedback as additional frequency.
5. COUNTERCHECK: Ask what could weaken or contradict the previous conclusion.
6. WRITE: Prefer updating the existing review with a repeat-review section instead of creating a duplicate file for the same scope.
7. GRADE: Mark conclusion strength as single observation, same-scope repeated observation, cross-period observation, cross-project observation, or explicit user feedback.

Repeated reviews of the same evidence must not promote a skill candidate, strengthen a user weakness claim, or convert an observation into a stable pattern. Only independent new evidence can do that.

Use the repeat-review addendum only for repeated reviews or cross-scope syntheses. Do not add it to ordinary task retrospectives.

Use this review template:

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

Use this repeat-review addendum only when the requested scope overlaps existing evidence:

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

## Evidence Rules

Write observations as behavior and context, not labels.

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

Do not record private speculation. Do not convert one event into a permanent user trait. If evidence is weak, mark it as "观察中".

## Red Flags - STOP

- You are about to copy the full conversation into a review.
- You are about to describe the user with a trait instead of an observed behavior.
- You cannot point to evidence for a "暴露的问题" item.
- You want to put ordinary learning content into `SKILL.md`.
- You want to put project-specific rules into this general skill.
- You want to create a new skill from one event without explicit user instruction.
- You are handling `复盘总览` and about to expand every review file by default.
- You are modifying this skill without first deciding whether the problem is design gap or execution failure.
- You are reviewing the same history again and treating repeated reading as new evidence.

## Overview Output

For `复盘总览`, read `index.md` and show:

1. 当前思想学习论
2. 已识别的开发风险
3. 复盘记录
4. Skill 候选

Keep the output concise. Do not expand every review unless the user explicitly asks.

## Skill Candidate Rules

Recommend creating or improving a skill only when at least two conditions are true:

- 同类问题出现两次以上。
- agent 在这类任务中容易遗漏关键步骤。
- 该经验跨项目适用。
- 该经验是判断型流程，不能简单靠脚本或检查器替代。
- 用户明确要求沉淀为 skill。
- 该流程会影响代码质量、验证质量或需求理解质量。

If only one condition is true, record the item as "观察中".

Repeated reviews of the same history do not count as independent occurrences. A skill candidate can be strengthened only by new periods, new tasks, new projects, new verification failures, or explicit user instruction.

When a candidate should proceed, do not bypass skill-authoring discipline. Record the candidate first, then use the proper skill creation or skill editing workflow.

## Rationalization Prevention

| Excuse | Reality |
|---|---|
| "This was a small task, no review is needed." | Small tasks still require a quick trigger check when learning or risk evidence exists. |
| "The user's weakness is obvious." | Only observed behavior and context can be recorded; no labels. |
| "This lesson is useful, put it in SKILL.md." | `SKILL.md` is for process rules; lessons belong in `development-learning`. |
| "This would be a useful skill, create it now." | Unless explicitly requested or supported by enough evidence, record a candidate first. |
| "复盘总览 should show everything." | The overview shows `index.md`; expansion requires a request. |
| "The skill failed, so change the skill." | First decide whether the skill rule is missing or the current agent ignored it. |
| "I reviewed the same month three times, so the evidence is stronger." | Same-scope repetition is not new evidence; record only deltas, corrections, and confidence changes. |

## Self-Modification Protocol

Use this protocol before changing `development-learning` itself:

1. Restate the issue: trigger, output structure, judgment rule, storage rule, or usage documentation.
2. Decide whether the issue is a skill design gap or an execution failure by the current agent.
3. Propose the smallest rule change that addresses the evidence.
4. Update `SKILL.md` only for process rules. Put learning content in `index.md`, candidates in `skill-candidates.md`, and self-change history in `development-learning-evolution.md`.
5. Add an evolution entry with change, reason, evidence, and verification.
6. Create a normal retrospective if the modification reflects a reusable workflow lesson.

Do not modify this skill for a one-off preference, a project-specific lesson, or content that belongs in the learning index.

## Common Mistakes

| Mistake | Correction |
|---|---|
| Recording full conversation logs | Record only decisions, evidence, principles, and reminders. |
| Labeling the user | Describe observable process behavior and next reminders. |
| Growing SKILL.md with learning content | Keep SKILL.md to workflow rules; store learning in `development-learning`. |
| Creating a new skill after one event | Mark as "观察中" unless enough evidence or explicit user instruction exists. |
| Showing every review for `复盘总览` | Show the index first; expand only on request. |
| Repeating a history review and upgrading conclusions | Same evidence cannot increase frequency or confidence; require independent new evidence. |
