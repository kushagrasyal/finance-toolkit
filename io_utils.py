# io_utils.py
import csv

def read_portfolio_csv(path: str):
    """
    CSV columns: ticker,shares,price
    Returns list[dict] with an extra 'value' key.
    """
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            shares = float(row["shares"])
            price = float(row["price"])
            value = shares * price
            rows.append({"ticker": row["ticker"], "shares": shares, "price": price, "value": value})
    return rows

def read_prices_csv(path: str) -> list[float]:
    """
    CSV columns: date,price (header required)
    Returns list of price floats in file order.
    """
    prices = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            prices.append(float(row["price"]))
    if len(prices) < 2:
        raise ValueError("Need at least 2 prices to compute returns.")
    return prices
