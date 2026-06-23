---
name: development-learning
description: Use when a development task, debugging session, design discussion, code review, or skill-authoring session needs a retrospective, reusable learning notes, weakness/risk identification, a "复盘总览" overview, or a decision about creating or improving workflow skills.
---

# Development Learning

流程版本：v0.6

## Overview

Use this skill to turn development work into evidence-based learning records. Capture reusable thinking, observed process risks, and skill evolution candidates without storing full chat logs or making personality judgments.

Learning data lives under the agent's personal data root:

```text
<AGENTS_HOME>\data\development-learning\
```

Resolve `<AGENTS_HOME>` from the current agent environment. For Codex-style personal skills, it is usually the parent directory that contains `skills\`.

Read `references/review-rules.md` before writing or updating retrospectives, handling repeated reviews, judging user weaknesses, updating skill candidates, or validating review quality.

Read `references/usage.md` when the user asks how to use this skill, asks for the skill usage document, or needs examples of commands and expected behavior.

Read `references/test-scenarios.md` when validating this skill, modifying this skill, or checking whether future agents will follow the intended behavior.

Run `scripts/validate_development_learning.py` after changing learning data structure or when checking index/candidate consistency.

## The Iron Law

```text
NO LEARNING RECORD WITHOUT EVIDENCE.
NO USER WEAKNESS CLAIM WITHOUT OBSERVED BEHAVIOR.
NO NEW SKILL CANDIDATE WITHOUT TRIGGER CONDITIONS.
NO EXTRA EVIDENCE WEIGHT FROM REPEATED REVIEW OF THE SAME HISTORY.
```

If there is no evidence, do not invent a lesson. If there is only weak evidence, record it as "观察中". If the content is project-specific, do not put it in this general skill.

Repeated reading of the same history is not new evidence. It can only refine, correct, split, merge, downgrade, or revoke conclusions.

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

Before writing, read `references/review-rules.md` and apply its gate function, templates, evidence rules, repeated-review protocol, candidate rules, quality self-check, and index capacity rules.

1. State the goal and boundary in one sentence before writing files.
2. Gather evidence from the current discussion, changed files, decisions, verification output, user constraints, or sanitized exported stats.
3. Create or update one relevant review file under `reviews\YYYY-MM-DD-topic.md`.
4. Update `index.md` with summaries and links only.
5. Update `skill-candidates.md` when the task suggests a new or improved skill.
6. If this skill itself changed, update `development-learning-evolution.md`.
7. Run the retrospective quality self-check from `references/review-rules.md`.
8. Report written or updated paths and the main learning points.

## Overview Output

For `复盘总览`, read `index.md` and show:

1. 当前思想学习论
2. 已识别的开发风险
3. 复盘记录
4. Skill 候选

Keep the output concise. Do not expand every review unless the user explicitly asks.

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
