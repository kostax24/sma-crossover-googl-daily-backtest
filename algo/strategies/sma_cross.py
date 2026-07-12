import pandas as pd


def sma_crossover_signals(
    prices: pd.DataFrame,
    short_window: int = 5,
    long_window: int = 20,
) -> pd.DataFrame:
    df = prices.copy()

    df["SMA_short"] = df["Close"].rolling(window=short_window).mean()
    df["SMA_long"] = df["Close"].rolling(window=long_window).mean()

    df["signal"] = 0
    df.loc[df["SMA_short"] > df["SMA_long"], "signal"] = 1
    df.loc[df["SMA_short"] < df["SMA_long"], "signal"] = -1

    return df