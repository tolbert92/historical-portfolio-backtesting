# Testing and acceptance plan

## Gate 1: publication and contract verification

- Validate all three JSON schemas against Draft 2020-12.
- Validate all three example files against their corresponding schemas.
- Verify invalid input fails contract validation.
- Verify BT-001 expected arithmetic from the independently specified fixture.
- Fail GitHub Actions if zero tests are discovered.

## Gate 2: standalone engine verification — NOT IMPLEMENTED

Add simulation engine tests for buy-and-hold, periodic and threshold rebalancing, execution timing, cash flows, fees, corporate actions, numerical performance metrics, bias controls, and accounting reconciliation. Contract tests alone do not establish this gate.

## Gate 3: agent integration — NOT VERIFIED

Validate actual upstream market/portfolio contracts and downstream risk/visualization contracts, with end-to-end reconciliation and failure isolation.
