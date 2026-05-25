# Analysis Close-The-Loop Template

Use this template at the end of any analysis that makes a recommendation. If the work is only monitoring or exploration, use a lighter note. If it asks someone to act, use the full template.

```markdown
# Close The Loop: [Recommendation]

## Decision

- **Recommendation:**
- **Decision owner:**
- **Decision deadline:**
- **Decision needed:** approve / reject / defer / choose option

## Success Tracking

- **Success metric:**
- **Metric definition:**
- **Current baseline:**
- **Target:**
- **Measurement window:**
- **Trusted source:**
- **Validation check:**

## Guardrails

- **Guardrail metric:**
- **Acceptable range:**
- **What would make this a tradeoff instead of a win:**

## Follow-Up

- **Follow-up owner:**
- **Check-back date:**
- **If successful:**
- **If unsuccessful:**
- **If inconclusive:**

## Provenance

- **Analysis date:**
- **Analyst / system:**
- **Source path or artifact:**
- **Confidence:** high / medium / low
- **Key assumptions:**
- **What would change the recommendation:**
```

## Lightweight Version

Use this when writing an action item inside a meeting note or daily log:

```markdown
- [ ] [Action] -- Owner: [name]. Metric: [metric]. Baseline: [value]. Target: [value]. Check: [date]. Fallback: [what happens if it fails].
```

## Field Rules

| Field | Rule |
| --- | --- |
| Decision owner | One person or role that can decide. Not a team. |
| Success metric | The metric closest to the recommended change. |
| Baseline | The pre-action value. If unknown, the first action is to establish it. |
| Target | A numeric threshold or observable state. |
| Measurement window | Long enough for the action to show up, short enough to keep accountability. |
| Guardrail | The metric that prevents a local optimization from becoming a system loss. |
| Fallback | Revert, escalate, pivot, or accept the status quo. Do not leave it blank. |

## Red Flags

Rewrite the action item if it contains any of these without a metric and date:

- monitor
- look into
- follow up
- circle back
- explore
- investigate
- by end of quarter
- product to own
- team to decide

## Example

```markdown
- [ ] Fix the onboarding drop-off after step 3 -- Owner: Growth PM. Metric: step-3-to-activation conversion. Baseline: 41%. Target: 48% within 4 weeks of launch. Check: 2026-07-15. Guardrail: support tickets must not rise more than 5%. Fallback: revert the flow and run moderated user research on the failed step.
```
