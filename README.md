# development-learning

`development-learning` is an agent skill for evidence-based development retrospectives.

It helps agents turn development work, debugging sessions, design discussions, code reviews, and skill-authoring work into reusable learning records without copying full chat logs or making personality judgments.

## What It Does

- Creates concise task retrospectives from concrete evidence.
- Maintains a lightweight learning index.
- Tracks observed development risks without labeling the user.
- Records workflow skill candidates and their trigger evidence.
- Supports a short "复盘总览" overview command.
- Separates process rules from personal learning data.

## Install

Clone this repository into your agent skills directory as `development-learning`.

```bash
git clone https://github.com/mangohu-cyber/development-learning.git <AGENTS_HOME>/skills/development-learning
```

`<AGENTS_HOME>` is the agent's personal data root. For Codex-style setups, it is usually the directory that contains `skills/`.

## Usage

Ask the agent to use the skill during or after development work:

```text
使用 development-learning，复盘这次任务
```

Show the current overview:

```text
复盘总览
```

Use it after:

- debugging sessions
- feature implementation
- design or refactoring discussions
- code review
- skill creation or skill updates
- historical agent conversation reviews

## Data Location

The skill stores learning data outside the skill repository:

```text
<AGENTS_HOME>/development-learning/
```

Expected data files:

```text
index.md
skill-candidates.md
development-learning-evolution.md
reviews/
```

This repository should contain the reusable skill instructions only, not private retrospective records.

## Privacy Rules

The skill is designed around three rules:

```text
NO LEARNING RECORD WITHOUT EVIDENCE.
NO USER WEAKNESS CLAIM WITHOUT OBSERVED BEHAVIOR.
NO NEW SKILL CANDIDATE WITHOUT TRIGGER CONDITIONS.
```

Do not store raw chat logs as learning records. Store only decisions, evidence, reusable principles, risks, and next reminders.

## Repository Contents

```text
SKILL.md
agents/openai.yaml
references/usage.md
references/test-scenarios.md
```

## Validation

If you have the standard skill validation script available, run it against this directory:

```bash
python <SKILL_CREATOR>/scripts/quick_validate.py <AGENTS_HOME>/skills/development-learning
```

Also check that the repository does not include private learning data before publishing:

```bash
git status --short
```
