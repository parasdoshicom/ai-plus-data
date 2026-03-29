# Source log — AI productivity for top data teams

Date: 2026-03-28
Purpose: defensibility log for the operator memo

## Evidence standard used
- Tier 1: official product documentation / admin guidance / technical docs
- Tier 2: official vendor operator guidance or release material
- Tier 3: general market framing only if it supported, not drove, the recommendation

This packet was intentionally biased toward Tier 1 sources from active platforms used by serious data teams.

## Sources reviewed

### 1) Snowflake Cortex Analyst
- URL: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst
- Tier: 1
- Why it mattered: evidence that NL analytics is being built around governed semantic definitions and monitored admin surfaces.
- Key takeaways used:
  - natural-language analytics is tied to semantic modeling
  - enterprise implementation expects governance and observability

### 2) Snowflake Semantic Views overview
- URL: https://docs.snowflake.com/en/user-guide/views-semantic/overview
- Tier: 1
- Why it mattered: strongest evidence for semantic views as the abstraction layer between business language and physical schemas.
- Key takeaways used:
  - metrics/entities/relationships should be defined in the semantic layer
  - semantic abstraction improves AI accuracy and BI consistency

### 3) Power BI: Use Copilot with semantic models
- URL: https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models
- Tier: 1
- Doc date observed during fetch: 2025-04-15; updated 2026-02-24
- Why it mattered: strong explicit guidance that Copilot quality depends on model/data/user prep.
- Key takeaways used:
  - semantic model prep is a prerequisite, not optional polish
  - developers should test Copilot against models before broad rollout
  - poor prep leads to inaccurate/misleading outputs

### 4) Microsoft Fabric Copilot overview
- URL: https://learn.microsoft.com/en-us/fabric/get-started/copilot-fabric-overview
- Tier: 1
- Why it mattered: shows AI is embedded across the analytics platform rather than treated as a separate toy.
- Key takeaways used:
  - platform-native copilot is becoming standard
  - rollout should match enterprise governance boundaries

### 5) Fabric data warehouse Copilot
- URL: https://learn.microsoft.com/en-us/fabric/data-warehouse/copilot
- Tier: 1
- Why it mattered: evidence for AI assistance in warehouse-native authoring workflows.
- Key takeaways used:
  - productivity use cases center on authoring/explaining/generating warehouse assets

### 6) Databricks Genie Code
- URL: https://docs.databricks.com/aws/en/notebooks/code-assistant
- Tier: 1
- Why it mattered: direct evidence of AI inside notebook/SQL workflows.
- Key takeaways used:
  - generate/debug/optimize/explain SQL and Python
  - use Unity Catalog metadata for relevance
  - slash-command workflow standardization matters

### 7) Measure Genie Code impact
- URL: https://docs.databricks.com/aws/en/genie-code/impact
- Tier: 1
- Why it mattered: shows mature teams should measure workflow impact locally.
- Key takeaways used:
  - use specific operational metrics rather than generic productivity stories

### 8) Databricks AI assistive features trust and safety
- URL: https://docs.databricks.com/aws/en/databricks-ai/databricks-ai-trust
- Tier: 1
- Why it mattered: strongest source in this set on privacy/retention/permissions and execution controls.
- Key takeaways used:
  - zero-retention endpoints and permission-aware context are major governance themes
  - read-only vs executable AI behavior must be explicit
  - human review remains necessary

### 9) dbt Semantic Layer
- URL: https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl
- Tier: 1
- Why it mattered: evidence from analytics engineering that centralized metric definitions are core infrastructure.
- Key takeaways used:
  - semantic layers reduce duplicate logic and enforce consistency
  - downstream tool interoperability matters

### 10) GitHub Copilot overview
- URL: https://docs.github.com/en/copilot/get-started/what-is-github-copilot
- Tier: 1
- Why it mattered: broad evidence that AI coding assistance is now normal in engineering workflows, including data code.
- Key takeaways used:
  - coding copilots are table stakes for repetitive authoring work

## Synthesis note
This memo intentionally avoids hard ROI claims. The evidence base strongly supports the direction of travel and the concrete implementation patterns, but local impact still needs to be measured by workflow and domain.

## Confidence call
- High confidence: semantic grounding, metadata quality, native copilots, governance/review gates
- Medium confidence: which vendor surface will be best for a given team
- Medium confidence: agent-mode productivity upside without stronger strong governance controls
