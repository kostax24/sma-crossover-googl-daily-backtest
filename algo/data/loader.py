import os
from pathlib import Path

import yfinance as yf
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

# Path to the top-level data folder (../data from this file)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"

def load_prices(
    symbol: str = "GOOGL",
    start: str = "2020-01-01",
    end: str = "2021-01-01",
    save_csv: bool = True,
) -> pd.DataFrame:
    """
    Download daily price data from Yahoo Finance and return as a pandas DataFrame.
    Optionally save the data to data/<symbol>.csv.
    """
    print(f"Downloading {symbol} from Yahoo Finance...")
    df = yf.download(symbol, start=start, end=end)

    # Ensure we just have a Date index and a simple Close column
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]

    if "Adj Close" in df.columns:
        df = df.rename(columns={"Adj Close": "Close"})

    # Make sure we actually got some data
    if df.empty:
        print("No data downloaded. Check symbol or dates.")
        return df

    df = df[["Close"]]  # keep only Close

    # Ensure data folder exists
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    if save_csv:
        file_path = RAW_DIR / f"{symbol}.csv"
        df.to_csv(file_path)
        print(f"Saved data to {file_path}")


    print("Finished downloading.")
    return df