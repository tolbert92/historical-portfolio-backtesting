# Validation rules

## Tier 1 — Block

Malformed contracts, unsupported schema versions, missing essential prices, invalid strategy timing, look-ahead leakage for executable claims, unsupported leverage, or accounting reconciliation failures must block the affected simulation.

## Tier 2 — Qualify

Insufficient optional benchmark coverage, limited samples, assumed spreads, uncertain historical constituent membership, and data-snooping concerns must produce explicit warnings or disable dependent metrics.

## Tier 3 — Document

Record frequency, risk-free rate, rebalancing schedule, price convention, transaction assumptions, data provenance, and run identifiers.

## Checks beyond JSON Schema

The eventual engine must enforce weights summing to 1 within a documented tolerance; unique asset IDs; sorted, unique observation dates; complete price coverage; start date before end date; no look-ahead; and cash/holdings reconciliation. JSON Schema alone does not establish these invariants.
