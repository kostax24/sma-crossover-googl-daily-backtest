import pandas as pd
import numpy as np

def sharpe_ratio(returns: pd.Series, risk_free: float = 0.02, periods_per_year: int = 252) -> float:
    """
    Compute annualized sharpe ratio from a series of returns.
    returns: strategy returns per period (e.g. daily)
    risk_free: risk free rate per period (set now for 0)
    """
    risk_free_adj = (risk_free / 252) * np.sqrt(252)
    excess = returns - risk_free_adj
    mu = excess.mean()
    sigma = excess.std()
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

