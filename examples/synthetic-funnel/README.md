# Synthetic Funnel Example

This example shows how to use AI on a small, public-safe funnel dataset.

Everything here is synthetic. The data is made up for demonstration and does not represent any private company, user, or customer.

## Files

- `seller_funnel.csv`: toy weekly funnel data
- `analysis.sql`: simple DuckDB queries for stage conversion and weekly change

## Suggested Workflow

1. Load the CSV into DuckDB.
2. Ask an AI assistant to explain the funnel and write a first-pass query.
3. Compare the AI output to `analysis.sql`.
4. Ask the model for a short diagnosis and next-step recommendation.

## Quick Start With DuckDB

```bash
duckdb demo.duckdb
```

Then run:

```sql
CREATE TABLE seller_funnel AS
SELECT * FROM read_csv_auto('seller_funnel.csv');
```

And:

```sql
.read analysis.sql
```

## Example Prompt

```text
You are helping analyze a weekly funnel.

The table has one row per week and includes:
- visitor_count
- lead_count
- qualified_count
- demo_count
- contract_count

Please:
1. calculate stage conversion rates
2. compare the latest week to the prior week
3. identify the biggest source of decline
4. suggest the next two questions to investigate
```

## What to Look For

This toy dataset is designed so that the biggest drop in the final week is not top-of-funnel traffic. It is later-stage conversion. That makes it useful for practicing decomposition instead of stopping at headline volume.
