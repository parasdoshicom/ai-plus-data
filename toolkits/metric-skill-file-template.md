# Metric Skill File Template

Use this template to create a structured context file for an important metric or domain.

The goal is simple: give AI enough grounded context to answer recurring business questions consistently.

## Template

```yaml
metric_name: 
metric_group: 
business_definition: 
owner: 
status: official | draft | deprecated

source_of_truth:
  primary_table_or_model: 
  semantic_metric_name: 
  trusted_dashboard: 
  version_control_reference: 

calculation:
  numerator: 
  denominator: 
  grain: 
  aggregation_logic: 

required_filters:
  - 

common_exclusions:
  - 

time_rules:
  timezone: 
  business_week_definition: 
  partial_period_handling: 

known_gotchas:
  - 

approved_query_patterns:
  - question: 
    sql_or_reference: 
    notes: 

guardrails:
  never_do:
    - 
  join_warnings:
    - 
  interpretation_warnings:
    - 

lineage_context:
  upstream_dependencies:
    - 
  downstream_consumers:
    - 

validation:
  last_validated_at: 
  validated_by: 
  validation_method: 
```

## Guidance

A useful skill file should answer:

- What exactly does this metric mean?
- Which source should AI trust?
- Which filters are mandatory?
- What edge cases usually create bad answers?
- Which query patterns are already known to be correct?

## Tips

- Start with the top 10 recurring metrics, not the whole warehouse.
- Be explicit about exclusions and partial-period rules.
- Link to validated SQL whenever possible.
- Treat this like operational documentation, not prose.
- Review and update when business logic changes.

## Simple test

Ask the same business question five different ways.

If AI still gives five different answers after reading the skill file, the file is incomplete.
