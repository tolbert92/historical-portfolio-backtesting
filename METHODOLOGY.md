# Methodology (Specification Phase)

The repository defines an intended historical backtesting skill. **No calculation engine is included in this package.**

## BT-001 reference case

Starting capital $10,000, allocated 60% to ASSET_A and 40% to ASSET_B. Total-return index values move from 100 to 110 and from 100 to 105 respectively. Without cash flows or costs, ending value is $6,600 + $4,200 = **$10,800**, total return **8%**.

## Return conventions

All return rates are decimal fractions. Prices in the reference fixture are synthetic total-return index levels, not tradable opening quotes. The fixture verifies simple valuation arithmetic only, not execution timing or actual trades.

TWR must isolate external cash flows; XIRR requires dated investor flows. Ratios with insufficient observations must be unavailable. A short two-date fixture is not sufficient to establish annualized volatility or Sharpe ratio.

## Compatibility

The visualization-handoff schema is local to this repository. Verify the receiver's schema before claiming compatibility with the 3D Portfolio Visualization skill.
