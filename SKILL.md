
---
name: historical-portfolio-backtesting
description: >
  Comprehensive, reusable AI agent skill for historical portfolio
  backtesting, strategy simulation, benchmark comparison, performance
  attribution, transaction-cost modeling, bias controls, and
  structured financial reporting. Supports standalone and
  agent-orchestrated execution through validated, versioned contracts.
version: 1.0.0
---

# Historical Portfolio Backtesting

## 1. Purpose

Historical Portfolio Backtesting is a reusable, platform-independent
AI agent skill for evaluating hypothetical investment portfolio
performance using historical financial market data.

The skill simulates portfolio holdings and transactions over time,
calculates performance and risk-adjusted metrics, compares results
against appropriate benchmarks, and generates auditable outputs.

The skill must distinguish:

1. Retrospective historical replay.
2. Point-in-time historically executable strategy simulation.
3. In-sample strategy development.
4. Out-of-sample historical evaluation.

Historical results are hypothetical and do not guarantee future
investment performance.

This skill does not authorize live trading, portfolio transactions,
or personalized investment recommendations.

## 2. Approved Design Architecture

The following ten design decisions are authoritative.

| # | Design Area | Approved Decision |
|---|---|---|
| 1 | Backtesting Scope | C — Comprehensive Historical Backtesting |
| 2 | Input Architecture | C — Hybrid Input Architecture |
| 3 | Simulation Methodology | C — Hybrid Simulation Engine |
| 4 | Performance Metrics | C — Comprehensive Performance Analytics |
| 5 | Benchmark Comparison | C — Multi-Benchmark & Dynamic Comparison |
| 6 | Transaction Costs | C — Comprehensive Execution & Cost Modeling |
| 7 | Reporting | C — Modular Reporting & Visualization Architecture |
| 8 | Validation | C — Tiered Validation with Critical Quality Gates |
| 9 | Execution | C — Dual-Mode Execution with Six-Phase Workflow |
| 10 | Testing | C — Comprehensive Testing + Integration Verification |

These decisions must be preserved unless an explicitly approved
future version supersedes them.

## 3. Skill Responsibilities

The skill SHALL:

- Accept validated portfolio definitions and historical market data.
- Support standalone and agent-orchestrated execution.
- Simulate buy-and-hold and configurable rebalancing strategies.
- Track positions, cash, transactions, fees, and portfolio valuation.
- Process contributions, withdrawals, and supported corporate actions.
- Calculate portfolio performance and risk-adjusted metrics.
- Compare performance against multiple compatible benchmarks.
- Support blended and rules-based dynamic benchmarks.
- Calculate rolling statistics and supported performance attribution.
- Detect and prevent invalid historical execution assumptions.
- Enforce critical data integrity and bias controls.
- Generate human-readable and machine-readable outputs.
- Preserve assumptions, methodology, provenance, and validation results.
- Produce reproducible results for identical validated inputs.

The skill SHALL NOT:

- Invent historical prices, transactions, or performance results.
- Present historical replay as a historically executable strategy.
- Use future information in historical investment decisions.
- Silently substitute missing critical data.
- Double-count dividends or investment expenses.
- Claim statistical significance without appropriate evidence.
- Treat successful schema validation as proof of numerical correctness.
- Execute real financial transactions.

## 4. Supported Execution Modes

### 4.1 Standalone Mode

Inputs may be supplied through:

- JSON portfolio definitions.
- CSV or JSON historical market data.
- Configuration files.
- User-provided strategy parameters.
- Validated benchmark datasets.

Standalone execution must not require another AI agent.

### 4.2 Agent-Orchestrated Mode

The skill may receive structured inputs from:

- Individual Investment Profile Builder.
- Market Data Analyst.
- Portfolio Optimization.
- Other contract-compatible upstream components.

Results may be passed to:

- Portfolio Risk Assessment.
- 3D Portfolio Visualization.
- Strategy Comparison.
- Decision Support.
- Other compatible downstream components.

The orchestration layer must validate schema compatibility.

### 4.3 Shared Calculation Engine

Both execution modes SHALL use the same:

- Input normalization rules.
- Validation gates.
- Portfolio accounting engine.
- Historical simulation logic.
- Performance metric definitions.
- Benchmark calculation methods.
- Reporting data model.

Execution mode must not change numerical results when inputs
and assumptions are identical.

## 5. JSON Input Contract

The authoritative input schema is:

`schemas/backtest-input.schema.json`

The contract SHALL use JSON Schema Draft 2020-12 or a documented,
equivalent supported version.

Required top-level properties:

- schema_version
- execution
- portfolio
- market_data
- simulation
- assumptions

Optional top-level properties:

- benchmarks
- integration
- metadata

### 5.1 Conceptual Input Example

```json
{
  "schema_version": "1.0.0",
  "execution": {
    "mode": "standalone",
    "run_id": "bt-example-001",
    "validation_policy": "tiered"
  },
  "portfolio": {
    "portfolio_id": "hypothetical-60-40",
    "currency": "USD",
    "initial_capital": 100000,
    "positions": [
      {
        "asset_id": "ASSET_A",
        "target_weight": 0.60
      },
      {
        "asset_id": "ASSET_B",
        "target_weight": 0.40
      }
    ]
  },
  "market_data": {
    "frequency": "daily",
    "price_type": "adjusted_close",
    "return_convention": "total_return",
    "series": [],
    "provenance": {
      "source": "hypothetical_fixture",
      "retrieved_at": "2026-11-16T00:00:00Z",
      "data_version": "fixture-1"
    }
  },
  "simulation": {
    "start_date": "2020-01-02",
    "end_date": "2025-12-31",
    "strategy_type": "periodic_rebalancing",
    "rebalancing_frequency": "annual",
    "execution_model": "next_available_open"
  },
  "assumptions": {
    "fractional_shares": true,
    "allow_short_selling": false,
    "allow_leverage": false,
    "commission_fixed": 0,
    "commission_rate": 0,
    "slippage_bps": 0,
    "cash_return_annual": 0,
    "risk_free_rate_annual": 0.03
  },
  "benchmarks": [],
  "integration": {
    "generate_visualization_handoff": true,
    "include_audit_manifest": true
  }
}
```

This example is a structural illustration, not an executable
backtest: the market-data series is empty.

### 5.2 Input Contract Requirements

The implemented schema SHALL define:

- Required fields and supported data types.
- Permitted execution modes and strategy types.
- Supported schema versions.
- Valid portfolio identifiers.
- Asset identifier uniqueness.
- Allocation sum constraints.
- Date and timestamp formats.
- Historical data observation structures.
- Currency and return conventions.
- Execution timing configuration.
- Transaction-cost configuration.
- Benchmark definitions.
- Data provenance requirements.
- Conditional requirements for optional calculations.

Initial portfolio weights must sum to 1.0 within a documented
numerical tolerance, unless an explicit cash allocation or
supported leverage policy explains the difference.

Historical observations must have unique, ordered timestamps
within each series after normalization.

Data normalization must preserve original source identifiers
and source provenance.

## 6. Historical Market Data Requirements

Supported data inputs may include:

- Historical adjusted prices.
- Raw prices with validated corporate-action data.
- Total-return indices.
- Historical dividends and distributions.
- Split adjustment factors.
- Trading calendars.
- Historical benchmark observations.
- Point-in-time asset eligibility information.

The engine must identify the return convention used for every
series.

Total-return-adjusted data must not receive additional dividend
credits that would duplicate distributions.

Fund expense ratios must not be automatically subtracted again
when already reflected in historical fund prices.

Missing critical observations must not be silently forward-filled.

Any permitted imputation must be explicitly configured, justified,
logged, and excluded from unsupported execution claims.

## 7. Hybrid Historical Simulation Engine

The simulation engine SHALL support:

### 7.1 Buy-and-Hold

- Allocate initial capital.
- Purchase permitted positions.
- Track share quantities.
- Allow allocation weights to drift.
- Process supported distributions and cash flows.
- Calculate portfolio value over time.

### 7.2 Periodic Rebalancing

Supported schedules may include:

- Monthly.
- Quarterly.
- Semiannual.
- Annual.
- Configurable custom schedules.

Rebalancing must use historically available information.

### 7.3 Threshold Rebalancing

Rebalancing may be triggered when allocation drift exceeds
a configured threshold.

The threshold definition and calculation timing must be recorded.

### 7.4 Cash Flows

Support:

- Scheduled contributions.
- Scheduled withdrawals.
- Dividend reinvestment.
- Dividend cash accumulation.
- Uninvested cash balances.
- Configurable cash returns.

External cash flows must be separated from investment performance.

### 7.5 Portfolio Accounting

For every simulated observation, maintain:

- Position quantities.
- Position market values.
- Available cash.
- Accrued or assessed fees.
- Executed transactions.
- External cash flows.
- Total portfolio equity.
- Actual allocation weights.

The portfolio accounting identity must reconcile:

Portfolio Equity = Holdings Market Value + Cash
                   - Outstanding Liabilities

Any liability treatment must be explicitly supported and
validated. Leverage is disabled by default.

## 8. Transaction Costs and Execution Modeling

Supported configurable costs:

- Fixed commissions.
- Percentage-based commissions.
- Bid-ask spread assumptions.
- Slippage in basis points.
- Transaction-size-dependent slippage.
- Advisory fees.
- Portfolio management fees.
- Fund expenses when not already embedded in returns.

Execution controls:

- Point-in-time price availability.
- Next eligible trading session execution.
- Configurable open/close execution assumptions.
- Fractional or whole-share policy.
- Insufficient-cash handling.
- Trading calendar validation.
- Configurable liquidity limits.
- Trade rejection or resizing.
- Transaction-level audit records.

A decision generated using a closing price must not be executed
at that same closing price unless a defensible execution model
establishes that the order could have been submitted in time.

Historical liquidity or spread data must not be represented as
observed when supplied through assumptions.

Gross and net results must be distinguishable and reconcile
to the underlying cost records.

## 9. Performance Analytics

The skill SHALL calculate applicable metrics using documented
definitions, units, and observation frequencies.

### 9.1 Growth Metrics

- Total return.
- Compound annual growth rate (CAGR).
- Ending portfolio value.
- Annual and calendar-period returns.
- Time-weighted return (TWR).
- Money-weighted return (XIRR), when mathematically defined.

### 9.2 Risk Metrics

- Annualized volatility.
- Maximum drawdown.
- Drawdown duration.
- Rolling volatility.
- Downside deviation.

### 9.3 Risk-Adjusted Metrics

- Sharpe ratio.
- Sortino ratio.
- Calmar ratio.
- Other explicitly supported risk-adjusted measures.

### 9.4 Trading and Attribution Metrics

- Portfolio turnover.
- Transaction costs.
- Gross-to-net performance impact.
- Asset-level contribution to performance.
- Allocation drift.
- Rebalancing activity.

### 9.5 Calculation Rules

Simple periodic returns:

r_t = (V_t - F_t) / V_(t-1) - 1

This expression is valid only under the documented convention
that F_t is the net external cash flow occurring at the end of
the measurement period, after investment performance.

For intraperiod flows, use an appropriate valuation-based
time-weighted methodology rather than assuming the same formula.

Compound growth:

V_T / V_0 = PRODUCT(1 + r_t)

CAGR:

CAGR = (V_T / V_0)^(1 / Y) - 1

For portfolios with external flows, the CAGR calculation must
use an appropriate flow-neutral investment growth series,
not raw beginning and ending account balances.

Annualized volatility:

sigma_annual = sigma_periodic * SQRT(P)

where P is the documented annualization factor.

Maximum drawdown:

MDD = MIN(V_t / running_peak_t - 1)

Sharpe ratio:

Sharpe = annualized_mean_excess_return /
         annualized_excess_return_volatility

Sortino ratio:

Sortino = annualized_excess_return /
          annualized_downside_deviation

All annualization conventions must be explicit.

Undefined or statistically unsupported ratios must be marked
unavailable rather than replaced with zero.

XIRR must use dated investor cash flows, an appropriate
sign convention, and a documented root-selection policy.

## 10. Multi-Benchmark Comparison

The skill SHALL support:

- Broad-market benchmarks.
- Asset-class benchmarks.
- Blended benchmarks.
- Custom benchmark portfolios.
- Configurable benchmark rebalancing.
- Multiple benchmarks per simulation.
- Rules-based dynamic benchmarks.

Supported relative metrics:

- Absolute and annualized return differences.
- Active returns.
- Tracking error.
- Information ratio.
- Beta.
- Alpha under a specified model.
- Up-market capture.
- Down-market capture.
- Rolling relative performance.
- Relative drawdown.
- Supported benchmark attribution.

Benchmark series must use compatible:

- Observation dates.
- Return frequencies.
- Currency treatment.
- Dividend conventions.
- Historical availability rules.

Benchmark-dependent metrics must be disabled if required
comparison data is unavailable or incompatible.

Benchmark selection and methodology must be disclosed.

A benchmark must not be presented as objectively appropriate
merely because it is commonly used.

## 11. Performance Attribution

The skill may calculate:

- Asset-level contribution to portfolio return.
- Sector or asset-class contributions.
- Allocation effects.
- Security-selection effects.
- Interaction effects.
- Transaction-cost effects.
- Rebalancing effects.

Each attribution method must specify:

- Required inputs.
- Return convention.
- Time aggregation methodology.
- Benchmark dependencies.
- Reconciliation requirements.

Allocation and selection attribution must not be calculated
without sufficient benchmark and holdings information.

Attribution results must reconcile to the appropriate
portfolio or active return within documented tolerances.

## 12. Six-Phase Execution Workflow

The authoritative workflow is:

Initialize -> Validate -> Simulate -> Analyze -> Verify -> Deliver

### Phase 1 — Initialize

1. Determine standalone or agent-orchestrated mode.
2. Read input configuration.
3. Verify supported contract versions.
4. Assign or validate run identifier.
5. Record execution parameters.
6. Establish data and configuration fingerprints.
7. Initialize execution and audit context.

Outputs:

- Execution manifest.
- Normalized configuration.
- Run identifier.
- Input references.

### Phase 2 — Validate

1. Validate JSON contracts.
2. Normalize portfolio definitions.
3. Validate historical market data.
4. Check asset and benchmark identifiers.
5. Verify historical date coverage.
6. Validate portfolio weights.
7. Enforce point-in-time availability.
8. Check execution assumptions.
9. Identify potential bias conditions.
10. Apply critical quality gates.

Outputs:

- Validated input package.
- Critical errors.
- Warnings.
- Disabled capabilities.
- Assumption manifest.

Critical errors block the affected simulation.

### Phase 3 — Simulate

1. Initialize positions and cash.
2. Process historical observations chronologically.
3. Evaluate permitted strategy signals.
4. Generate proposed transactions.
5. Apply execution constraints.
6. Calculate transaction costs.
7. Execute eligible simulated trades.
8. Process cash flows and corporate actions.
9. Update holdings and cash.
10. Record portfolio valuation and transaction ledger.

Outputs:

- Historical portfolio equity series.
- Holdings history.
- Transaction ledger.
- Cash-flow history.
- Cost records.

### Phase 4 — Analyze

1. Calculate portfolio growth metrics.
2. Calculate risk and drawdown metrics.
3. Calculate risk-adjusted performance.
4. Calculate cash-flow-adjusted returns.
5. Evaluate multiple benchmarks.
6. Calculate rolling statistics.
7. Calculate supported attribution.
8. Compare gross and net results.
9. Prepare structured analytical findings.

Outputs:

- Performance metrics.
- Benchmark comparison results.
- Rolling statistics.
- Attribution results.
- Cost diagnostics.

### Phase 5 — Verify

1. Reconcile holdings and cash.
2. Reconcile transactions and costs.
3. Verify portfolio valuation identities.
4. Validate performance calculations.
5. Verify benchmark alignment.
6. Check attribution reconciliation.
7. Confirm metric sufficiency.
8. Validate deterministic result generation.
9. Apply final critical quality gates.
10. Assign final execution status.

Outputs:

- Verification report.
- Final validation status.
- Disabled metrics.
- Numerical reconciliation evidence.

### Phase 6 — Deliver

1. Generate canonical results JSON.
2. Generate human-readable executive report.
3. Generate technical report.
4. Export supported CSV datasets.
5. Prepare visualization handoff.
6. Include assumptions and validation disclosures.
7. Include provenance and audit manifest.
8. Validate all required output contracts.
9. Return structured execution status.

Outputs:

- Backtesting report.
- Technical report.
- Canonical results JSON.
- CSV exports.
- Visualization handoff JSON.
- Validation and audit manifest.

## 13. Validation Severity Model

Three validation tiers are mandatory.

### Tier 1 — Critical: BLOCK

Examples:

- Invalid required input schema.
- Unsupported required schema version.
- Invalid or unreconcilable portfolio allocations.
- Missing essential historical prices.
- Impossible historical execution timing.
- Confirmed look-ahead leakage in an executable backtest.
- Invalid corporate-action treatment materially affecting returns.
- Portfolio accounting reconciliation failure.
- Unsupported leverage or short-selling activity.
- Unrecoverable numerical calculation failure.

Critical errors invalidate affected simulations.

### Tier 2 — Warning: QUALIFY

Examples:

- Limited historical coverage.
- Assumed spreads or slippage.
- Incomplete optional benchmark history.
- Potential survivorship bias.
- Uncertain historical universe completeness.
- Limited sample size.
- Overfitting or repeated strategy selection concerns.
- Missing optional attribution inputs.

Warnings must identify affected claims and metrics.

### Tier 3 — Informational: DOCUMENT

Examples:

- Rebalancing schedule.
- Return convention.
- Selected benchmark.
- Fractional-share policy.
- Risk-free rate.
- Reporting currency.
- Execution price convention.

Information-level findings must be retained in the audit manifest.

## 14. Historical Bias Controls

### 14.1 Look-Ahead Bias

Historically executable strategies must use only information
available at the decision timestamp.

Confirmed future-data leakage blocks the affected simulation.

### 14.2 Survivorship Bias

Historical investment universes must reflect historical
eligibility when such claims are made.

Survivor-only datasets must be disclosed.

### 14.3 Selection Bias

The methodology for selecting assets and strategies must be
documented.

Retrospective selection must not be misrepresented as
historical investment decision-making.

### 14.4 Data Snooping and Overfitting

Record, when available:

- Strategy variants tested.
- Parameter selection procedures.
- Training periods.
- Validation periods.
- Out-of-sample periods.
- Repeated testing and selection activity.

Do not label an in-sample result as out-of-sample evidence.

### 14.5 Historical Replay Classification

Historical replay using a portfolio selected with future
information is permitted only when explicitly classified as
retrospective hypothetical analysis.

It must not receive a historically executable designation.

## 15. Partial Results and Failure Isolation

Permitted statuses:

- completed
- partial
- blocked
- failed

`completed` means required calculations and verification passed.

`partial` means the core simulation is valid, but one or more
independent optional analyses are unavailable.

`blocked` means a critical validation gate prevented execution.

`failed` means execution or verification failed after processing
began.

Missing optional benchmark data may disable benchmark-relative
metrics without invalidating the portfolio simulation.

Missing essential prices or failed accounting reconciliation
must not be bypassed by labeling results partial.

In multi-strategy runs, independent strategies may complete
even if another strategy fails.

A shared critical data failure blocks all dependent strategies.

## 16. JSON Output Contract

The authoritative output schema is:

`schemas/backtest-output.schema.json`

Required top-level properties:

- schema_version
- skill
- run_id
- status
- simulation
- performance
- validation
- provenance

Additional supported properties:

- benchmarks
- attribution
- transaction_costs
- portfolio_timeseries
- transactions
- holdings_history
- cash_flows
- rolling_metrics
- artifacts
- audit_manifest

### 16.1 Conceptual Output Example

```json
{
  "schema_version": "1.0.0",
  "skill": "historical-portfolio-backtesting",
  "run_id": "bt-example-001",
  "status": "partial",
  "simulation": {
    "strategy": "annual_rebalancing",
    "currency": "USD"
  },
  "performance": {
    "total_return": null,
    "cagr": null,
    "annualized_volatility": null,
    "maximum_drawdown": null,
    "sharpe_ratio": null,
    "sortino_ratio": null,
    "time_weighted_return": null,
    "money_weighted_return": null
  },
  "benchmarks": [],
  "attribution": {},
  "transaction_costs": {},
  "portfolio_timeseries": [],
  "transactions": [],
  "validation": {
    "critical_errors": [],
    "warnings": [],
    "disabled_metrics": [],
    "assumptions": []
  },
  "provenance": {},
  "audit_manifest": {}
}
```

This is a contract skeleton, not a completed calculation.

In an actual `completed` or `partial` run, all required core
results must be populated with verified values. Unavailable
optional metrics must have explicit reasons.

A run without a valid core simulation must use `blocked` or
`failed`, not `completed` or `partial`.

## 17. Reporting and Visualization

The skill SHALL use a single authoritative results dataset
for all reporting outputs.

### 17.1 Human-Readable Reports

Supported formats:

- HTML.
- PDF.

Reports should contain:

- Executive summary.
- Simulation objective.
- Portfolio strategy description.
- Historical period.
- Data provenance.
- Performance metrics.
- Benchmark comparisons.
- Drawdown analysis.
- Trading costs.
- Attribution.
- Validation findings.
- Limitations and assumptions.

### 17.2 CSV Exports

Supported datasets:

- Portfolio equity and return history.
- Benchmark return history.
- Transaction ledger.
- Holdings history.
- External cash flows.
- Rolling metrics.
- Attribution results.

### 17.3 Visualization Handoff

The skill SHALL generate a versioned JSON handoff for
compatible visualization components.

Supported visualization data may include:

- Equity curves.
- Drawdown series.
- Rolling returns.
- Rolling volatility.
- Portfolio allocation changes.
- Benchmark-relative returns.
- Strategy comparison data.
- Risk-return relationships.

The handoff must comply with the receiving visualization
skill's validated schema.

No compatibility may be assumed without contract verification.

## 18. Provenance and Audit Requirements

Every execution SHALL record:

- Skill version.
- Input schema version.
- Output schema version.
- Run identifier.
- Execution mode.
- Data source identifiers.
- Data retrieval timestamps when supplied.
- Historical coverage.
- Data version or fingerprint.
- Strategy configuration.
- Execution assumptions.
- Cost assumptions.
- Benchmark definitions.
- Validation results.
- Calculation methodology version.
- Output artifact references.
- Final execution status.

Where deterministic fingerprints are generated, use a
documented canonical serialization method.

Do not expose secrets or sensitive credentials in audit outputs.

## 19. Testing Requirements

Testing must cover:

### 19.1 Contract Tests

- Valid input acceptance.
- Invalid input rejection.
- Required fields.
- Unsupported schema versions.
- Output schema compliance.
- Visualization handoff compliance.

### 19.2 Numerical Reference Tests

- Buy-and-hold portfolio returns.
- Periodic rebalancing.
- Threshold rebalancing.
- CAGR.
- Annualized volatility.
- Maximum drawdown.
- Sharpe ratio.
- Sortino ratio.
- Time-weighted return.
- XIRR.
- Benchmark relative metrics.

Expected results must be independently calculated.

### 19.3 Accounting Tests

- Position valuation.
- Cash balance.
- Trade execution.
- Contributions.
- Withdrawals.
- Dividends.
- Transaction costs.
- Gross/net reconciliation.

### 19.4 Bias and Validation Tests

- Look-ahead leakage.
- Invalid execution timing.
- Survivor-only universe disclosures.
- Missing prices.
- Duplicate timestamps.
- Corporate-action inconsistencies.
- Insufficient observations.
- Incompatible benchmarks.
- Unsupported leverage.
- Critical gate enforcement.

### 19.5 Reporting Tests

- Canonical JSON consistency.
- CSV reconciliation.
- HTML/PDF numerical consistency.
- Visualization handoff schema validity.
- Missing metric disclosures.
- Audit manifest completeness.

### 19.6 Reproducibility Tests

- Identical input reproducibility.
- Deterministic transaction ordering.
- Stable calculation conventions.
- Stable output fingerprints.
- Independence of standalone and agent execution modes.

### 19.7 Integration Tests

Verify compatibility with:

- Market Data Analyst.
- Portfolio Optimization.
- Portfolio Risk Assessment.
- 3D Portfolio Visualization.
- Strategy Comparison, when implemented.
- Decision Support, when implemented.

Contract integration must be tested separately from
numerical integration.

## 20. Numerical Acceptance Test — BT-001

Scenario:

- Initial portfolio value: $10,000.
- Equity allocation: 60%.
- Bond allocation: 40%.
- Equity return: +10%.
- Bond return: +5%.
- No external cash flows.
- No dividends beyond the specified returns.
- No transaction costs.

Expected ending values:

- Equities: $6,600.
- Bonds: $4,200.
- Portfolio: $10,800.

Expected total return:

0.60 * 0.10 + 0.40 * 0.05 = 0.08

Acceptance:

- Ending portfolio value equals $10,800.
- Total return equals 8%.
- Holdings reconcile to portfolio equity.
- Numerical differences remain within documented tolerances.

Additional reference tests must cover multiple periods,
rebalancing, costs, cash flows, and benchmark calculations.

## 21. Automated Testing

GitHub Actions SHOULD run on:

- Push.
- Pull request.
- Manual workflow dispatch.

The workflow should:

1. Check out repository contents.
2. Configure the supported Python environment.
3. Install declared dependencies.
4. Validate JSON schemas and fixtures.
5. Run contract tests.
6. Run numerical tests when the engine exists.
7. Run validation and reconciliation tests.
8. Run available integration tests.
9. Report actual executed test counts.
10. Fail when required tests fail or zero tests are discovered.

Unimplemented test categories must be explicitly reported
as not implemented, not silently marked successful.

## 22. Three Acceptance Gates

### Gate 1 — GitHub Publication Verified

Requirements:

- Complete SKILL.md.
- Methodology documentation.
- Versioned JSON schemas.
- Valid hypothetical examples.
- Test plan.
- Automated contract tests.
- Successful GitHub Actions run.
- Confirmed nonzero test count.

Passing Gate 1 establishes specification publication,
not operational calculation readiness.

### Gate 2 — Standalone Engine Verified

Requirements:

- Working simulation engine.
- Verified reference calculations.
- Portfolio accounting reconciliation.
- Bias and validation controls.
- Transaction-cost modeling.
- Performance metric verification.
- Valid reporting outputs.
- Deterministic execution.
- All required standalone tests passing.

Passing Gate 2 establishes standalone operational readiness.

### Gate 3 — Agent Integration Verified

Requirements:

- Upstream input compatibility.
- Downstream output compatibility.
- Versioned contract verification.
- End-to-end execution tests.
- Error and failure isolation.
- Cross-skill numerical consistency.
- Successful required integration tests.

Passing Gate 3 establishes verified agent integration.

## 23. Acceptance Standards

The following standards are mandatory:

- 100% of required contract tests pass.
- 100% of critical numerical reference tests pass.
- Zero unresolved critical validation failures in accepted results.
- Portfolio accounting reconciles within documented tolerances.
- Unsupported metrics are explicitly unavailable.
- Identical validated inputs produce identical numerical results.
- All required outputs pass their schemas.
- Required reports reconcile with canonical results.
- Executed test counts are visible.
- Integration readiness is not claimed before Gate 3 passes.

Numerical tolerances must be defined by calculation type
and justified in the test documentation.

## 24. Operational Constraints

The implementation SHALL:

- Apply configurable historical-data limits.
- Apply configurable strategy-count limits.
- Avoid unbounded memory consumption.
- Avoid unnecessary repeated calculations.
- Validate external data before use.
- Prevent unsupported execution assumptions.
- Fail safely when critical inputs are invalid.
- Keep calculation logic independent from presentation logic.
- Preserve backward compatibility where feasible.
- Use explicit schema versioning for breaking changes.

## 25. Financial Analysis Limitations

Every material report must communicate that:

- Backtested performance is hypothetical.
- Past performance does not guarantee future results.
- Market conditions may differ from historical observations.
- Transaction costs and execution assumptions affect outcomes.
- Historical datasets may contain gaps or biases.
- Strategy optimization may introduce overfitting.
- Results are not a substitute for professional financial advice.

The skill must not claim that a historical strategy will
achieve comparable future returns.

## 26. Recommended Repository Structure

```text
historical-portfolio-backtesting/
├── README.md
├── SKILL.md
├── docs/
│   ├── METHODOLOGY.md
│   └── VALIDATION_RULES.md
├── schemas/
│   ├── backtest-input.schema.json
│   ├── backtest-output.schema.json
│   └── visualization-handoff.schema.json
├── examples/
│   ├── hypothetical-input.json
│   ├── hypothetical-output.json
│   └── hypothetical-visualization-handoff.json
├── tests/
│   ├── test_contracts.py
│   ├── test_reference_cases.py
│   └── TEST_PLAN.md
└── .github/
    └── workflows/
        └── test.yml
```

The source-code implementation of the simulation engine
will be added during Gate 2 development.

## 27. Definition of Done

This skill is considered fully operational and integrated only when:

1. All ten approved design decisions are implemented.
2. Input and output contracts are validated.
3. The historical simulation engine is operational.
4. Required performance calculations are independently verified.
5. Critical validation and bias controls function correctly.
6. Portfolio accounting reconciles.
7. Reporting artifacts are numerically consistent.
8. Reproducibility tests pass.
9. Upstream and downstream integration tests pass.
10. Gates 1, 2, and 3 have been independently verified.

A published specification without a working calculation
engine must be labeled specification-complete only.

---

Version: 1.0.0

Status: Specification complete; implementation and integration pending.

Project: AI Portfolio Optimization Agent

Skill: Historical Portfolio Backtesting
