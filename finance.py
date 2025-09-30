# finance.py
import math
import numpy as np

def future_value(P: float, r: float, t_years: int, m: int = 1) -> float:
    """
    Compound interest future value.
    P: principal, r: annual rate (decimal), t_years: years, m: compounds/year
    """
    if m <= 0: 
        raise ValueError("m must be positive")
    return P * (1 + r / m) ** (m * t_years)

def loan_payment(principal: float, annual_rate: float, years: int, m: int = 12) -> float:
    """
    Level-payment loan (EMI).
    """
    r = annual_rate / m
    n = years * m
    if r == 0:
        return principal / n
    return principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

def amortization_schedule(principal: float, annual_rate: float, years: int, m: int = 12):
    """
    Return a list of dicts with period, payment, interest, principal, balance.
    """
    pmt = loan_payment(principal, annual_rate, years, m)
    r = annual_rate / m
    n = years * m
    bal = principal
    sched = []
    for k in range(1, n + 1):
        interest = bal * r
        principal_paid = pmt - interest
        bal = max(0.0, bal - principal_paid)
        sched.append({
            "period": k,
            "payment": pmt,
            "interest": interest,
            "principal": principal_paid,
            "balance": bal
        })
    return sched

def npv(discount_rate: float, cash_flows: list[float]) -> float:
    """
    NPV of cash flows at t=0..N with constant discount rate.
    """
    return sum(cf / ((1 + discount_rate) ** t) for t, cf in enumerate(cash_flows))

def irr(cash_flows: list[float], guess: float = 0.1) -> float:
    """
    Compute IRR using numpy's solver as a helper if available; fallback to bisection.
    """
    try:
        return float(np.irr(cash_flows))  # may be deprecated in future numpy
    except Exception:
        low, high = -0.99, 10.0
        for _ in range(200):
            mid = (low + high) / 2
            val = npv(mid, cash_flows)
            if abs(val) < 1e-7:
                return mid
            if val > 0:
                low = mid
            else:
                high = mid
        return mid

def simple_returns(prices: list[float]) -> list[float]:
    return [(prices[i] / prices[i-1]) - 1 for i in range(1, len(prices))]

def log_returns(prices: list[float]) -> list[float]:
    return [math.log(prices[i] / prices[i-1]) for i in range(1, len(prices))]

def equity_curve_from_prices(prices: list[float]) -> list[float]:
    """
    Normalize to 1.0 then grow by simple returns cumulatively.
    """
    rets = simple_returns(prices)
    curve = [1.0]
    for r in rets:
        curve.append(curve[-1] * (1 + r))
    return curve
