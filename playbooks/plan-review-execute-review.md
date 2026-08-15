# Plan, Review, Execute, Review

For non-trivial analysis, I prefer a short loop over one large AI run:

1. plan the work
2. review the plan
3. execute one meaningful step
4. review the output
5. repeat

## Why the Loop Works

- It catches bad framing before heavy computation or narrative work.
- It keeps the human involved at the moments that matter.
- It creates a lightweight audit trail.
- It reduces the risk of a polished but wrong answer.

## Use Cases

- root cause investigations
- experiment readouts
- funnel analysis
- forecasting work
- board or executive prep
- any analysis that will influence a real business decision

## Suggested Rhythm

### Step 1: Plan

Ask AI to create a short execution plan:

- question to answer
- data needed
- checks and tie-outs
- likely segmentation cuts
- decision checkpoints

### Step 2: Review

Review whether the plan makes sense before running it.

Questions to ask:

- Is the logic sound?
- Are we missing a benchmark?
- Are we using the right grain?
- What would disprove the working hypothesis?

### Step 3: Execute

Run only the next meaningful step, such as:

- loading the data
- generating the first summary table
- building the first trend cut
- validating the denominator

### Step 4: Review Again

Before moving on, review:

- whether the result is plausible
- whether the output introduces new questions
- whether the next step should change

## A Good Rule

If the cost of being wrong is high, the review interval should be short.

That usually means:

- shorter loops for executive-facing work
- longer loops for low-stakes internal exploration

## Example Prompt

```text
Create a step-by-step analysis plan for investigating a conversion decline.
Keep it to 6 steps maximum.
After each step, pause for review rather than continuing automatically.
Include the tie-outs you would run before sharing findings.
```

## What This Looks Like in Practice

The reviewer does not need to micromanage every query. They do need to control the framing, interpretation, and threshold for sharing the result.
