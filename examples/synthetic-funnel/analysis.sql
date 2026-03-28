WITH base AS (
  SELECT
    week_start,
    visitor_count,
    lead_count,
    qualified_count,
    demo_count,
    contract_count,
    ROUND(100.0 * lead_count / NULLIF(visitor_count, 0), 2) AS visitor_to_lead_pct,
    ROUND(100.0 * qualified_count / NULLIF(lead_count, 0), 2) AS lead_to_qualified_pct,
    ROUND(100.0 * demo_count / NULLIF(qualified_count, 0), 2) AS qualified_to_demo_pct,
    ROUND(100.0 * contract_count / NULLIF(demo_count, 0), 2) AS demo_to_contract_pct
  FROM seller_funnel
)
SELECT * FROM base ORDER BY week_start;

WITH weekly AS (
  SELECT
    week_start,
    visitor_count,
    lead_count,
    qualified_count,
    demo_count,
    contract_count,
    LAG(visitor_count) OVER (ORDER BY week_start) AS prev_visitor_count,
    LAG(lead_count) OVER (ORDER BY week_start) AS prev_lead_count,
    LAG(qualified_count) OVER (ORDER BY week_start) AS prev_qualified_count,
    LAG(demo_count) OVER (ORDER BY week_start) AS prev_demo_count,
    LAG(contract_count) OVER (ORDER BY week_start) AS prev_contract_count
  FROM seller_funnel
)
SELECT
  week_start,
  visitor_count - prev_visitor_count AS delta_visitors,
  lead_count - prev_lead_count AS delta_leads,
  qualified_count - prev_qualified_count AS delta_qualified,
  demo_count - prev_demo_count AS delta_demos,
  contract_count - prev_contract_count AS delta_contracts
FROM weekly
ORDER BY week_start;
