from algo.data import loader
from algo.strategies import sma_cross
from algo.backtest import engine, performance


if __name__ == "__main__":
    prices = loader.load_prices(
        symbol="AAPL",
        start="2020-01-01",
        end="2020-12-31",
    )

    strat_df = sma_cross.sma_crossover_signals(prices)
    backtest_df = engine.run_backtest(strat_df, initial_capital=10_000.0)

    print(backtest_df[["Close", "signal", "position", "equity"]].tail(100))

    engine.plot_equity_vs_price(backtest_df, title="AAPL SMA Crossover 2020")

    rets = backtest_df["return_strategy"].dropna()
    equity = backtest_df["equity"].dropna()

    print("Sharpe:", performance.sharpe_ratio(rets))
    print("Max drawdown:", performance.max_drawdown(equity))
    print("Profit factor:", performance.profit_factor(rets))
