# Why AI Analytics Agents Need a Metric Store

**Thesis:** A semantic layer defines meaning, but conversational analytics also needs a store of approved answer paths for recurring business questions.

## Use This When

- an agent gives plausible but unofficial answers
- multiple valid query paths exist and the system picks inconsistently
- the same executive or KPI question is asked over and over

## Core Operating Pattern

For each recurring business question, store the approved answer path:

1. approved metric definition
2. preferred source model or table
3. approved SQL pattern or retrieval method
4. required filters and exclusions
5. caveats, freshness expectations, and interpretation notes
6. owner and status

The metric store sits between raw discovery and final answers.

## How The Layers Fit Together

- **Semantic layer:** what does the metric mean?
- **Skill file / domain context:** what should AI watch out for?
- **Catalog:** where are the relevant assets and lineage?
- **Metric store:** which answer path is officially approved?
- **Agent:** how do we turn that into a usable experience?

## Why The Semantic Layer Is Not Enough

It may not capture:

- query recipes analysts actually trust
- context-specific exclusions
- approved behavior for recurring executive questions
- which valid source should win when more than one exists

That is where the metric store becomes valuable.

## Common Failure Modes

- trying to encode every possible question before focusing on recurring ones
- storing definitions but not query behavior
- omitting caveats and freshness rules
- assuming the agent will infer the approved source on its own

## What To Store First

Start with:

- top executive questions
- top recurring KPI questions
- metrics tied to real decisions
- metrics with known ambiguity or historical disagreement

## Related Next Reads

- [`semantic-layer-is-the-trust-layer.md`](./semantic-layer-is-the-trust-layer.md)
- [`fix-ai-analytics-inputs-not-prompts.md`](./fix-ai-analytics-inputs-not-prompts.md)
- [`../toolkits/metric-skill-file-template.md`](../toolkits/metric-skill-file-template.md)
