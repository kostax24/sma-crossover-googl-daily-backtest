# SMA Crossover GOOGL Daily Backtest

A simple Python backtesting project that downloads daily historical data from Yahoo Finance, runs on it a basic SMA crossover strategy, evaluates performance, and plots stock price vs portfolio equity.

## Features

- Downloads daily historical price data for GOOGL (2020-2021) by default
- Can be adapted in code for other stocks and time periods
- Saves downloaded market data as a CSV file (optional)
- Runs a 5-day vs 20-day SMA crossover strategy using default stock
- Long and short positions are allowed
- Uses a default starting portfolio value of 10,000 USD
- Reports key backtest metrics
- Saves a chart comparing stock price and portfolio equity

## Backtest metrics

- Number of trades
- Win rate
- Expectancy per trade
- Volatility
- Sharpe ratio
- Max drawdown
- Profit factor
- CAGR

## Project structure

```text
algo/
  backtest/
    engine.py
    performance.py
  data/
    loader.py
  strategies/
    sma_cross.py
main.py
README.md
requirements.txt
```

## Installation

```bash
git clone https://github.com/kostax24/sma-crossover-googl-daily-backtest.git
cd sma-crossover-googl-daily-backtest
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Notes

This project is intentionally simple and modular. It can be extended to test other assets, different date ranges, different moving average windows, different starting capital values, or additional strategies and evaluation metrics.