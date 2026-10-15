# Analytics platform review exercise

This is an original hypothetical exercise, not a report of a real company's results. It replaces the former employer-specific case read-through while keeping the existing file path useful. No historical outcome figures are presented as synthetic evidence.

## Situation

Imagine a team planning to replace a reporting platform. The team has overlapping dashboards, unclear metric definitions, and users who do not know which asset to trust. Your task is to decide what to migrate, what to retire, and what must be fixed first.

## Work through the decision

1. Inventory the recurring decisions and dashboards that support them.
2. Assign each candidate asset a status: retain, repair, retire, or investigate.
3. For retained assets, record the source, metric definition, downstream use, and reviewer.
4. Capture the current cost, review effort, and reliability baseline using actual evidence from your own environment.
5. Move one bounded workflow, verify its outputs and user path, and test the fallback before expanding.

## Questions for the review

- Which asset can be retired without removing a decision-critical capability?
- Which conflicting definitions need a decision before migration?
- How will the team detect a correct-looking answer built from the wrong source?
- What evidence would justify continuing, repairing, or stopping the migration?
- Who will operate the workflow after the project team leaves?

## Evidence to produce

| Artifact | What it should establish |
| --- | --- |
| Asset inventory | What exists and which decision depends on it |
| Definition record | Which meaning and source the team approved |
| Baseline and comparison | What changed, with counts, windows, and caveats |
| Verification record | Whether the real output and user path passed |
| Support handoff | Who can detect a miss and recover safely |

No improvement is assumed. Record a failed check or an unchanged measure as observed, and separate a reduced software bill from the total cost of operating the workflow.

## Related tools

[Dashboard governance](../../playbooks/dashboard-governance-for-ai-analytics.md) · [Metric trust packet](../../toolkits/metric-trust-packet-template.md) · [Workflow investment brief](../../toolkits/workflow-investment-brief.md) · [AI leadership operating guide](../ai-leadership-operating-guide.md)
