# Claims Ledger

This ledger maps important public claims to their evidence strength and caveats. It is more conservative than marketing copy by design.

## Evidence Strength

| Strength | Meaning |
| --- | --- |
| Direct repo artifact | Demonstrated directly by files in this repo |
| Public external source | Supported by a public third-party, professional-body, company-authored, or self-authored source |
| Inference | Reasonable conclusion from artifacts, but not independently proven |
| Not claimed | Deliberately excluded from public claims |

## Ledger

| Claim | Where it appears | Evidence | Strength | Caveat |
| --- | --- | --- | --- | --- |
| The repo contains a coherent operating thesis for AI-native data leadership | [`README.md`](../README.md), [`what-this-repo-proves.md`](./what-this-repo-proves.md) | README, CDO OS, playbooks, toolkits | Direct repo artifact | Quality still depends on reader judgment |
| The repo is public-safe by design | [`README.md`](../README.md), [`repo-privacy-policy.md`](./repo-privacy-policy.md) | Privacy policy, publication checklist, synthetic examples | Direct repo artifact | Manual ZIP/upload outside git could bypass safeguards |
| Paras has a long-running public writing archive | [`README.md`](../README.md), [`public-source-inventory.md`](./public-source-inventory.md) | Insight Extractor archive | Public external source | Archive metrics are self-published on the site |
| Paras has senior analytics/community recognition | [`external-proof-of-impact.md`](./external-proof-of-impact.md) | Institute of Analytics profile, Evanta page, Globee pages | Public external source | Recognition does not by itself prove current operating scope |
| There is externally visible outcome evidence beyond self-authored writing | [`external-proof-of-impact.md`](./external-proof-of-impact.md) | Select Star case study, Opendoor public article | Public external source | Vendor case studies and company articles are not audited financial proof |
| AI analytics needs trusted metric/context infrastructure before broad rollout | [`playbooks/semantic-layer-is-the-trust-layer.md`](../playbooks/semantic-layer-is-the-trust-layer.md), [`projects/ten-metric-trust-layer-pilot.md`](../projects/ten-metric-trust-layer-pilot.md) | Repo argument plus public research notes | Direct repo artifact | This is an operator thesis, not a universal law |
| A 10-metric trust layer is a practical first pilot | [`projects/ten-metric-trust-layer-pilot.md`](../projects/ten-metric-trust-layer-pilot.md) | Generalized pattern from adjacent work and repo playbooks | Direct repo artifact | Public repo does not claim a named customer deployed this exact pilot |
| Decision memos improve executive use of AI-assisted analysis | [`projects/decision-memo-operating-loop.md`](../projects/decision-memo-operating-loop.md), [`sample-monthly-cdo-review.md`](./sample-monthly-cdo-review.md) | Repo artifact and synthetic example | Direct repo artifact | Needs live reader adoption proof to become stronger |
| The repo proves current private company performance | Nowhere | Excluded by policy | Not claimed | Private/confidential results are intentionally not published |
| The repo contains customer data, internal SQL, private schemas, or confidential dashboards | Nowhere | Excluded by policy | Not claimed | Keep publishing from tracked files only |

## Review Rule

When adding a new strong claim to the README or executive packet, add it here first. If the claim cannot be supported by a public source, direct repo artifact, or clearly marked inference, do not make it.
