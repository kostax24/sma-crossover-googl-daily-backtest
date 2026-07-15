from algo.data import loader
from algo.strategies import sma_cross
from algo.backtest import engine, performance


if __name__ == "__main__":
    prices = loader.load_prices(
        symbol="GOOGL", # adjust the ticker to work with other stocks
        start="2020-01-01", # adjust for other dates
        end="2020-12-31",
)

strat_df = sma_cross.sma_crossover_signals(prices)
backtest_df = engine.run_backtest(strat_df, initial_capital=10_000.0)

engine.plot_equity_vs_price(backtest_df, title="GOOGLE SMA Crossover strategy 2020")

valid = backtest_df["SMA_long"].notna()
rets = backtest_df.loc[valid, "return_strategy"].dropna()
equity = backtest_df.loc[valid, "equity"].dropna()

# print(backtest_df.head(25).to_string()) # check the dataframe
# print(backtest_df.tail(10).to_string())

print("Number of trades:", performance.number_of_trades(rets))
print("Win rate:", round(performance.win_rate(rets), 4))
print("Expectancy per trade:", round(performance.expectancy(rets), 4))

print("Volatility:", round(performance.volatility(rets), 4))
print("Sharpe:", round(performance.sharpe_ratio(rets), 4))
print("Max drawdown:", round(performance.max_drawdown(equity), 4))
print("Profit factor:", round(performance.profit_factor(rets), 4))
print("CAGR:", round(performance.cagr(equity), 4))