# Decision Memo Operating Loop

## Purpose

AI-assisted data work should not end as a clever answer in a chat thread. Important investigations should become decision memos that executives, managers, and data owners can review, forward, reopen, and improve.

This project turns recurring analysis into an operating loop:

1. question
2. evidence
3. implication
4. decision
5. owner
6. follow-up
7. reusable answer path

## Use This When

- a metric moved and the team needs to decide what to do
- an executive review keeps revisiting the same question
- an AI answer needs to be trusted beyond the original chat
- analysts are repeating the same explanation work
- the organization needs a reusable path from evidence to action

## Memo Template

```markdown
# Decision Memo: [Question]

## Decision Needed
[The decision or tradeoff the team must resolve.]

## Current Read
[The shortest useful answer, including confidence and caveats.]

## Evidence Path
- Metric or KPI:
- Trusted source:
- Freshness:
- Query, dashboard, model, or artifact:
- Validation check:
- Known caveats:

## Business Implication
[What this changes about prioritization, risk, investment, or operating focus.]

## Options
1. [Option A]
2. [Option B]
3. [Option C]

## Recommendation
[Recommended path and why.]

## Owner And Next Step
- Owner:
- Next step:
- Review date:

## Reusable Answer Path
[What should be saved so the next version of this question starts from a stronger baseline.]
```

## Quality Bar

A strong decision memo:

- names the actual decision, not just the topic
- separates known facts from inference
- cites the trusted source path
- includes freshness, caveats, and validation status
- makes the business implication explicit
- assigns an owner and next step
- leaves behind reusable operating knowledge

## Related Reads

- [`docs/ai-adoption-board-brief.md`](../docs/ai-adoption-board-brief.md)
- [`playbooks/ai-war-room-briefing.md`](../playbooks/ai-war-room-briefing.md)
- [`playbooks/plan-review-execute-review.md`](../playbooks/plan-review-execute-review.md)
- [`docs/cdo-operating-system.md`](../docs/cdo-operating-system.md)
