import pandas as pd
import numpy as np
from pandas.io.formats.format import return_docstring


def sharpe_ratio(returns: pd.Series, risk_free: float = 0.02, periods_per_year: int = 252) -> float:
    """
    Compute annualized sharpe ratio from a series of returns.
    returns: strategy returns per period (e.g. daily)
    risk_free: risk free rate per period (set now for 0)
    """
    risk_free_adj = risk_free / periods_per_year
    excess = returns - risk_free_adj
    mu = excess.mean()
    sigma = returns.std()
    if sigma == 0:
        return np.nan # cannot divide by 0
    return (mu / sigma) * np.sqrt(periods_per_year)

def max_drawdown(equity: pd.Series) -> float:
    """
    Compute maximum drawdown (as a negative fraction).
    """
    running_max = equity.cummax()
    drawdown = (equity - running_max) / running_max
    max_dd = drawdown.min()
    return max_dd

def profit_factor(returns: pd.Series) -> float:
    """
    Profit factor = sum of positive returns / abs(sum of negative returns).
    """
    gains = returns[returns > 0].sum()
    losses = returns[returns < 0].sum()
    if losses == 0:
        return np.nan
    pf = gains / abs(losses)
    return pf

def cagr(equity: pd.Series) -> float:
    """
    CAGR (Compound Annual Growth Rate)
    It takes start and end values to calculate the annualized growth rate.
    """
    start = equity.iloc[0]
    end = equity.iloc[-1]
    years = (equity.index[-1] - equity.index[0]).days / 365.25
    if years <= 0:
        return np.nan
    cagr = (end / start) ** (1 / years) - 1
    return cagr

def volatility(return_strategy: pd.Series, periods_per_year: int = 252) -> float:
    """
    Standard deviation of annualized periodic returns.
    """
    annual_vol = return_strategy.std() * np.sqrt(periods_per_year)
    return annual_vol

def number_of_trades(return_strategy: pd.Series) -> int:
    mask_trades = return_strategy != 0
    trades = mask_trades.sum()
    return trades

def win_rate(return_strategy: pd.Series) -> float:
    mask_win = return_strategy > 0
    mask_loss = return_strategy < 0

    wins = mask_win.sum()
    losses = mask_loss.sum()
    trades = wins + losses

    wr = wins / trades
    return wr

def expectancy(return_strategy: pd.Series) -> float:
    mask_win = return_strategy > 0
    mask_loss = return_strategy < 0

    wins = mask_win.sum()
    losses = mask_loss.sum()
    trades = wins + losses

    win_rate = wins / trades
    loss_rate = losses / trades
    avg_win = return_strategy[mask_win].mean()
    avg_loss = -return_strategy[mask_loss].mean()

    exp = (win_rate * avg_win) - (loss_rate * avg_loss)
    return exp




