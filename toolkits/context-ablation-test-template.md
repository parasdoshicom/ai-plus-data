# Context Ablation Test Template

Use this test to learn which context bundles change an analytics agent's answer, safety, latency, or stability. Do not keep a bundle merely because it sounds relevant.

## Test Setup

- **Golden question:**
- **Expected answer state:**
- **Expected result or range:**
- **Source snapshot:**
- **Model and version:**
- **Temperature:**
- **Tool permissions:**
- **Run count per condition:**
- **Reviewer:**

Keep every field above fixed across conditions.

## Context Bundles

| Bundle | Contents | Owner | Review status | Tokens |
| --- | --- | --- | --- | --- |
| Metric definition |  |  |  |  |
| Approved answer path |  |  |  |  |
| Caveats and corrections |  |  |  |  |
| Source and lineage note |  |  |  |  |
| Prior evidence record |  |  |  |  |

## Conditions

Run at least these conditions:

1. minimal approved context
2. full approved context
3. full context minus each bundle, one at a time
4. one-bundle-added runs when a bundle's contribution remains unclear

## Results

| Condition | Correct state | Correct result | Quietly wrong | Tokens | Latency | Source calls | Stable across runs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Minimal |  |  |  |  |  |  |  |
| Full |  |  |  |  |  |  |  |
| Minus metric definition |  |  |  |  |  |  |  |
| Minus answer path |  |  |  |  |  |  |  |
| Minus caveats |  |  |  |  |  |  |  |
| Minus source note |  |  |  |  |  |  |  |
| Minus prior evidence |  |  |  |  |  |  |  |

## Decision

For each bundle, choose one action:

- Keep: material quality or safety gain
- Rewrite: useful idea, poor structure or excessive size
- Narrow: useful only for certain questions or risk tiers
- Remove: no measurable gain or creates conflict
- Escalate: owner conflict or unclear precedence

Record the decision:

| Bundle | Action | Evidence | Owner | Follow-up date |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Guardrail

Do not remove a bundle based on token savings alone. A bundle earns its place when it reduces decision risk, improves the correct answer state, or prevents quietly wrong output.
