
# Historical Portfolio Backtesting

A comprehensive, reusable AI agent skill for historical investment portfolio backtesting, strategy simulation, benchmark comparison, performance attribution, transaction-cost modeling, and structured financial reporting.

Part of the **AI Portfolio Optimization Agent** project.

## Overview

Historical Portfolio Backtesting evaluates how hypothetical investment portfolios and strategies would have performed using historical market data.

The skill supports independent analysis and integration with other AI portfolio management skills through validated, versioned JSON contracts.

## Key Capabilities

- Buy-and-hold portfolio simulation
- Periodic and threshold-based rebalancing
- Multiple portfolio and strategy comparisons
- Historical benchmark comparisons
- Total return and compound annual growth rate (CAGR)
- Sharpe, Sortino, and Calmar ratios
- Maximum drawdown and rolling performance analysis
- Time-weighted and money-weighted returns
- Transaction costs, commissions, and slippage
- Portfolio performance attribution
- Historical data validation and bias controls
- Structured JSON, CSV, HTML, and PDF reporting
- Visualization integration with Plotly-based dashboards

## Six-Phase Workflow

1. **Initialize** — Load portfolio definitions, historical data, and simulation parameters.
2. **Validate** — Verify input integrity, historical availability, and bias controls.
3. **Simulate** — Execute historical portfolio strategies and track transactions.
4. **Analyze** — Calculate performance metrics, benchmarks, and attribution.
5. **Verify** — Reconcile portfolio accounting and validate calculations.
6. **Deliver** — Generate reports, structured results, and visualization outputs.

## Integration Architecture

Designed to integrate with:

- [Individual Investment Profile Builder](https://github.com/tolbert92/individual-investment-profile-builder)
- [Market Data Analyst](https://github.com/tolbert92/market-data-analyst)
- [Portfolio Optimization](https://github.com/tolbert92/portfolio-optimization)
- [Portfolio Risk Assessment](https://github.com/tolbert92/portfolio-risk-assessment)
- [3D Portfolio Visualization](https://github.com/tolbert92/3d-portfolio-visualization)

Additional planned integrations include Strategy Comparison and Decision Support.

## Validation and Quality Controls

The skill specification establishes three validation tiers:

- **Critical:** Block invalid simulations.
- **Warning:** Permit qualified results with disclosed limitations.
- **Informational:** Document assumptions and methodology.

Controls address look-ahead bias, survivorship bias, historical data quality, transaction accounting, and reproducibility.

## Development Status

**Current status: Specification published — implementation pending.**

The architecture and ten design decisions are complete.

Development follows three acceptance gates:

| Gate | Description | Status |
|---|---|---|
| 1 | GitHub publication and contract verification | In progress |
| 2 | Standalone calculation engine verification | Pending |
| 3 | Agent integration verification | Pending |

The repository does not yet contain a verified operational backtesting engine.

## Documentation

See [SKILL.md](SKILL.md) for the complete technical specification, including:

- Approved design decisions
- Input and output contract requirements
- Historical simulation methodology
- Performance calculation definitions
- Six-phase execution workflow
- Validation and bias controls
- Testing requirements
- Acceptance criteria

## Important Disclaimer

Historical backtesting results are hypothetical and do not guarantee future investment performance.

This skill is intended for financial analysis, research, and educational purposes. It does not execute live trades or provide personalized investment advice.

## Version

**Specification Version:** 1.0.0

**Project:** AI Portfolio Optimization Agent

**Skill:** Historical Portfolio Backtesting
