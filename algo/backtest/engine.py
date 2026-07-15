import pandas as pd
import matplotlib
matplotlib.use("Agg")  # using non-GUI backend
import matplotlib.pyplot as plt


def run_backtest(strat_df: pd.DataFrame, initial_capital: float = 10_000.0) -> pd.DataFrame:
    df = strat_df.copy()

    if "Close" not in df.columns:
        raise ValueError(f"'Close' column missing. Columns are: {list(df.columns)}")

    df["return_asset"] = df["Close"].pct_change()
    df["position"] = df["signal"].shift(1).fillna(0)
    df["return_strategy"] = df["position"] * df["return_asset"]
    df["equity"] = initial_capital * (1 + df["return_strategy"]).cumprod()

    return df

def plot_equity_vs_price(backtest_df: pd.DataFrame, title: str = "Strategy vs Price") -> None:
    df = backtest_df.dropna(subset=["Close", "equity"])

    fig, ax_price = plt.subplots(figsize=(10, 5))

    ax_price.plot(df.index, df["Close"], color="tab:blue", label="Price")
    ax_price.set_xlabel("Date")
    ax_price.set_ylabel("Price", color="tab:blue")
    ax_price.tick_params(axis="y", labelcolor="tab:blue")

    ax_equity = ax_price.twinx()
    ax_equity.plot(df.index, df["equity"], color="tab:orange", label="Equity")
    ax_equity.set_ylabel("Equity", color="tab:orange")
    ax_equity.tick_params(axis="y", labelcolor="tab:orange")

    plt.title(title)
    fig.tight_layout()

    # Save instead of show
    fig.savefig("GOOGL_equity_vs_price.png")
    print("Saved plot to equity_vs_price.png")