# development-learning

`development-learning` is a local agent skill for evidence-based development retrospectives.

It helps agents turn development work, debugging sessions, design discussions, code reviews, and skill-authoring work into reusable learning records without copying full chat logs or making personality judgments.

## What It Does

- Creates concise task retrospectives from concrete evidence.
- Maintains a lightweight learning index.
- Tracks observed development risks without labeling the user.
- Records workflow skill candidates and their trigger evidence.
- Supports the short `复盘总览` overview command.
- Separates process rules from personal learning data.

## Local Usage

Place this directory under the agent skills root as:

```text
<AGENTS_HOME>/skills/development-learning
```

`<AGENTS_HOME>` is the agent's personal data root. For Codex-style setups, it is usually the directory that contains `skills/`.

Ask the agent to use the skill during or after development work:

```text
使用 development-learning，复盘这次任务。
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

The skill stores learning data outside the skill directory:

```text
<AGENTS_HOME>/data/development-learning/
```

Expected data files:

```text
index.md
skill-candidates.md
development-learning-evolution.md
reviews/
```

## Privacy Rules

The skill is designed around four rules:

```text
NO LEARNING RECORD WITHOUT EVIDENCE.
NO USER WEAKNESS CLAIM WITHOUT OBSERVED BEHAVIOR.
NO NEW SKILL CANDIDATE WITHOUT TRIGGER CONDITIONS.
NO EXTRA EVIDENCE WEIGHT FROM REPEATED REVIEW OF THE SAME HISTORY.
```

Do not store raw chat logs as learning records. Store only decisions, evidence, reusable principles, risks, and next reminders.

## Contents

```text
SKILL.md
agents/openai.yaml
references/review-rules.md
references/usage.md
references/test-scenarios.md
scripts/validate_development_learning.py
```

## Validation

Run the standard skill validation script when available:

```bash
python <SKILL_CREATOR>/scripts/quick_validate.py <AGENTS_HOME>/skills/development-learning
```

Run the data consistency validator:

```bash
python <AGENTS_HOME>/skills/development-learning/scripts/validate_development_learning.py
```
