# AI+Data

Public playbooks and hands-on toolkit for Chief Data Officers, heads of data, and high-agency data teams adopting AI without giving up rigor.

This repo is for:

- Chief Data Officers who need an operator-grade AI adoption system, not another prompt list
- heads of data and analytics leaders who are turning isolated experiments into a team habit
- analysts, analytics engineers, and data scientists working inside a leader-led AI adoption motion
- builders who want public-safe patterns for increasing leverage without losing trust

The core thesis is simple: AI should help data organizations ship more, learn faster, and create more business impact, but only when paired with strong validation, clear operating habits, and practical governance.

The sharper wedge behind this repo is also simple: the best AI adoption programs in data do not start with tooling. They start with a high-leverage data leader who can translate business context, analytical standards, and operating judgment into repeatable team workflows. This repo is designed around that CDO-to-CDO transfer.

## What You'll Find

This repo is organized around three layers of adoption:

1. Individual workflow
   Move from one-off prompting to repeatable analysis patterns.
2. Team operating model
   Turn scattered experiments into shared habits, review loops, and rollout checklists.
3. Leader operating cadence
   Help CDOs, heads of data, and analytics leaders create leverage while preserving quality, trust, and analytical judgment.

## Repo Map

- [`playbooks/`](./playbooks): reusable AI-native ways of working for data teams
- [`playbooks/why-agents-need-a-metric-store.md`](./playbooks/why-agents-need-a-metric-store.md): the missing layer between semantic definitions and reliable agent answers
- [`playbooks/semantic-layer-and-skill-files.md`](./playbooks/semantic-layer-and-skill-files.md): why governed definitions and practical guardrails solve different problems
- [`playbooks/semantic-layer-is-the-trust-layer.md`](./playbooks/semantic-layer-is-the-trust-layer.md): why governed metric definitions are foundational trust infrastructure for AI analytics
- [`playbooks/validate-at-ingestion.md`](./playbooks/validate-at-ingestion.md): why data quality should be caught upstream before it hits dashboards, models, and AI workflows
- [`playbooks/fix-ai-analytics-inputs-not-prompts.md`](./playbooks/fix-ai-analytics-inputs-not-prompts.md): a practical rollout for making AI answers more reliable
- [`playbooks/dashboard-governance-for-ai-analytics.md`](./playbooks/dashboard-governance-for-ai-analytics.md): how to reduce dashboard sprawl into a trusted layer for AI
- [`playbooks/ai-native-data-catalog-foundation.md`](./playbooks/ai-native-data-catalog-foundation.md): why catalogs and metric layers are foundational for AI analytics
- [`toolkits/`](./toolkits): rollout tools, scorecards, and checklists
- [`toolkits/metric-skill-file-template.md`](./toolkits/metric-skill-file-template.md): a structured template for top-metric AI context files
- [`examples/`](./examples): synthetic, public-safe examples only
- [`docs/`](./docs): founder context, source inventory, privacy policy, and publication safety checks

## Start Here

If you're new to this repo, start in this order:

1. Read [`playbooks/self-correcting-sql-loop.md`](./playbooks/self-correcting-sql-loop.md)
2. Read [`playbooks/ask-before-building.md`](./playbooks/ask-before-building.md)
3. Run the synthetic example in [`examples/synthetic-funnel/`](./examples/synthetic-funnel/)
4. Use [`toolkits/data-team-ai-rollout-checklist.md`](./toolkits/data-team-ai-rollout-checklist.md) to assess where your team is today
5. Use [`toolkits/manager-ai-adoption-scorecard.md`](./toolkits/manager-ai-adoption-scorecard.md) to review progress and risk

## Recommended First Workflow

For most teams, the fastest safe win is:

1. pick a recurring analysis you already know well
2. run it through an AI-assisted workflow on local or sampled data
3. keep a human validation loop at the end
4. document the corrections
5. repeat until the workflow becomes reliable

That is usually a better starting point than trying to deploy an "AI analyst" across the whole company on day one.

## Why This Exists

AI adoption in data teams is often stuck in one of two bad states:

- shallow prompt tips with no operating model
- tool-first rollouts with weak trust, weak review habits, and weak governance

This repo aims at the gap in the middle: practical operator-grade patterns that help data leaders and their teams compound their impact with AI.

Another way to say it: this is a public working repo for the kind of CDO who wants to help other CDOs adopt AI well.

## About Paras

This work is curated by Paras Doshi (`parasdoshi`), a data leader and operator writing about analytics, AI, and high-impact data teams.

The point of view here is intentionally operator-led: take what a very high-leverage data leader would actually use to move a team, then rewrite it into a public, reusable form.

Public references:

- [High Signal episode: Why Your Data Team Doesn't Have a Seat at the Table (And How to Earn It)](https://highsignal.fireside.fm/27)
- [Insight Extractor](https://insightextractor.com/)
- [GitHub profile](https://github.com/parasdoshicom)
- [LinkedIn](https://www.linkedin.com/in/doshiparas/)

More context lives in [`docs/founder.md`](./docs/founder.md) and [`docs/public-source-inventory.md`](./docs/public-source-inventory.md).
