# Maven AI Analyst Video Source Log

This source log captures public lesson pages and transcript-backed notes from the AI analyst and Claude Code analytics learning cluster. It does not store raw transcripts. The useful public lesson is the operating pattern: analysis should move through framing, validation, narrative, decision, owner, and follow-up.

## Source Cluster

| # | Source | Course / cluster | Encoded operating pattern |
| --- | --- | --- | --- |
| 1 | [Turn Insights to Action in Claude Code](https://maven.com/p/213eab) | Claude Code Analytics Bootcamp | End every recommendation with decision owner, success metric, baseline, target, check-back date, and fallback. |
| 2 | [Design Product Analysis with Claude Code](https://maven.com/p/66f451) | AI Analytics for Builders | Start with an analysis design spec before touching data: decision, scope, cohorts, hypotheses, methods, outputs, risks, and thresholds. |
| 3 | [Root Cause Analysis in Claude Code](https://maven.com/p/cddd45/measure-ai-impact-with-causal-inference) | Claude Code Analytics Bootcamp | Define the metric change precisely, find the largest driver, then drill down until the cause is actionable. |
| 4 | [Analyze Product Data w/ Claude Code Opus 4.6](https://maven.com/p/c56895/analyze-product-data-w-claude-code-opus-4-6) | Claude Code Analytics Bootcamp | Use AI to accelerate mechanics, but keep the human as validator for business context, metric interpretation, and actionability. |
| 5 | [Build Slide Decks in Claude Code](https://maven.com/p/bdf395) | Claude Code Analytics Bootcamp | Treat decks as a pipeline: data, story structure, slide content, charts, theme, final review. |
| 6 | [Storytelling & Presentation Building Using Claude Code](https://maven.com/p/e698e2) | AI Analytics for Builders | Convert findings into a narrative with a clear so-what, evidence, audience fit, and ask. Cut charts that do not change a decision. |
| 7 | [Design a Geo-Experiment in 30 Minutes with Claude Code](https://maven.com/p/e8fd98/design-a-geo-experiment-in-30-minutes-with-claude-code) | Marketing Science Bootcamp | Use AI for experiment design, but force power, market selection, confounders, guardrails, and decision rules up front. |
| 8 | [Crack Product Sense & Analytics Interviews with AI](https://maven.com/p/7c6b28/crack-product-sense-analytics-interviews-with-ai) | AI Analytics for Builders | Use AI as a structured practice partner that probes scoping, metric trees, tradeoffs, and decision quality. |
| 9 | [Practice for Product Sense PM Interviews with AI](https://maven.com/p/d8e439/practice-for-product-sense-pm-interviews-with-ai) | Product sense interview prep | Encode reusable interview practice loops: prompt, answer, critique, score, retry. |
| 10 | [Product Sense in the Age of AI: What Changes, What Doesn't](https://maven.com/p/d85f6c/product-sense-in-the-age-of-ai-what-changes-what-doesn-t) | Agentic AI Product Management | AI product sense still depends on judgment: scope the user problem, define success, reason through failure modes, and steer ambiguity. |
| 11 | [Why technical excellence isn't enough for AI products](https://maven.com/p/204b68/mastering-ai-product-sense) | AI Product Management | Technical quality does not rescue weak product judgment. AI products fail under ambiguity without guardrails, feedback loops, and user-grounded structure. |

## Open-Source Reference

The strongest implementation reference is [ai-analyst-lab/ai-analyst](https://github.com/ai-analyst-lab/ai-analyst). The repo describes an AI product analyst built on Claude Code with specialized agents, skills, commands, DAG-based execution, validation, deck generation, and close-the-loop behavior.

High-value implementation ideas to borrow in public-safe form:

- An analysis design spec before non-trivial work starts.
- A question-framing ladder from goal to decision to metric to hypothesis.
- Separate agents or checkpoints for source tie-out, validation, opportunity sizing, story architecture, deck creation, and close-the-loop.
- A correction log so repeated mistakes become reusable operating knowledge.
- A close-the-loop checklist at the end of any recommendation.

## Net-New Standards To Encode

1. **No analysis starts without a decision.** If no decision exists, classify the work as monitoring, reporting, or exploration.
2. **No recommendation ships without a measurement contract.** Every recommendation needs owner, metric, baseline, target, window, check date, and fallback.
3. **No win ships without a guardrail.** If the success metric improves but the guardrail degrades, call it a tradeoff.
4. **No deck ships without an ask.** The story must move the audience toward a decision or prioritization choice.
5. **No AI output becomes trusted until validated.** Tie out sources, denominators, freshness, and caveats before stakeholder use.

## How This Should Change Future Work

For AI+Data, this becomes a public-safe operating pattern for data leaders. For private operating systems, it becomes a default behavior: after any meaningful analysis, create a close-the-loop block instead of leaving recommendations as loose bullets.
