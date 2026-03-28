# Synthetic Funnel Walkthrough

This example is a public-safe walkthrough of the workflow this repo recommends: ingest safe data, clarify the question, run AI-assisted analysis, validate the output, and translate it into a manager-ready recommendation.

Everything here is synthetic. The data is made up for demonstration and does not represent any private company, customer, or internal system.

## What This Example Proves

- AI can accelerate a recurring analysis without needing production data
- reliability comes from question framing and validation, not just generation
- the final output should be a decision-ready explanation, not just a query

## Files

- `seller_funnel.csv`: toy weekly funnel data
- `analysis.sql`: baseline DuckDB queries for decomposition and weekly change

## End-To-End Workflow

### 1. Ingest Safe Data

Load the CSV into DuckDB:

```bash
duckdb demo.duckdb
```

```sql
CREATE TABLE seller_funnel AS
SELECT * FROM read_csv_auto('seller_funnel.csv');
```

### 2. Frame The Question

Use a prompt that pins down the task before analysis begins:

```text
You are helping analyze a weekly funnel.

The table has one row per week and includes:
- visitor_count
- lead_count
- qualified_count
- demo_count
- contract_count

Before analyzing:
- restate the business question
- confirm the grain
- identify the conversion stages you plan to inspect
- call out any assumptions

Then:
1. calculate stage conversion rates
2. compare the latest week to the prior week
3. identify the biggest source of decline
4. suggest the next two questions to investigate
```

### 3. Run AI-Assisted Analysis

- ask the model for a first-pass diagnosis
- compare its logic to `analysis.sql`
- if the output is wrong or incomplete, feed back the exact issue and iterate

### 4. Validate Against Trusted Logic

Run:

```sql
.read analysis.sql
```

Check:

- one row really means one week
- stage conversion math matches expectations
- the reported driver of decline matches the SQL output
- no stage is skipped in the explanation

### 5. Turn It Into A Manager-Ready Readout

Do not stop at query output. Convert the result into a short operating brief:

- headline: what moved
- diagnosis: which stage drove the change
- confidence: why you trust the answer
- next step: what to investigate next

Example:

> Weekly conversion declined primarily because later-stage conversion weakened, not because top-of-funnel traffic collapsed. The SQL tie-out supports that diagnosis, so the next step is to inspect qualification-to-demo and demo-to-contract changes before changing acquisition spend.

## What To Look For

This toy dataset is designed so the biggest drop in the final week is not traffic volume. It is later-stage conversion. That makes it useful for practicing decomposition instead of stopping at headline volume.

## Related Next Reads

- [`../../playbooks/self-correcting-sql-loop.md`](../../playbooks/self-correcting-sql-loop.md)
- [`../../playbooks/ask-before-building.md`](../../playbooks/ask-before-building.md)
- [`../../toolkits/data-team-ai-rollout-checklist.md`](../../toolkits/data-team-ai-rollout-checklist.md)
