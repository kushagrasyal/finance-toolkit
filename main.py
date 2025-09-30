# main.py
from finance import (
    future_value, loan_payment, amortization_schedule,
    npv, irr, simple_returns, log_returns
)
from io_utils import read_portfolio_csv, read_prices_csv

MENU = """
Mini Finance Toolkit
1) Future value (compound interest)
2) Loan payment (EMI) + amortization schedule
3) NPV & IRR of cash flows
4) Returns from prices (simple & log)
5) Portfolio snapshot from CSV
6) Plot equity curve from returns (optional)
0) Exit
Choose: """

def main():
    while True:
        choice = input(MENU).strip()
        if choice == "1":
            principal = float(input("Initial amount: "))
            rate = float(input("Annual rate (e.g., 0.08 for 8%): "))
            periods = int(input("Years: "))
            freq = int(input("Compounds per year (e.g., 12): "))
            print("Future value:", round(future_value(principal, rate, periods, freq), 2))
        elif choice == "2":
            loan = float(input("Loan amount: "))
            annual_rate = float(input("Annual rate (e.g., 0.09): "))
            years = int(input("Years: "))
            pmt = loan_payment(loan, annual_rate, years, 12)
            print("Monthly payment:", round(pmt, 2))
            show = input("Show first 6 lines of amortization? (y/n): ").lower().startswith("y")
            if show:
                sched = amortization_schedule(loan, annual_rate, years, 12)
                for row in sched[:6]:
                    print(row)
        elif choice == "3":
            print("Enter cash flows separated by commas (e.g., -1000,300,400,500):")
            cfs = [float(x) for x in input().split(",")]
            disc = float(input("Discount rate (e.g., 0.1): "))
            print("NPV:", round(npv(disc, cfs), 2))
            print("IRR (approx):", round(irr(cfs), 4))
        elif choice == "4":
            path = input("Path to prices CSV (default prices.csv): ").strip() or "prices.csv"
            prices = read_prices_csv(path)
            print("Simple returns:", simple_returns(prices)[:5], "...")
            print("Log returns:", log_returns(prices)[:5], "...")
        elif choice == "5":
            path = input("Path to portfolio CSV (default portfolio.csv): ").strip() or "portfolio.csv"
            snapshot = read_portfolio_csv(path)
            total_value = sum(item['value'] for item in snapshot)
            print(f"Total portfolio value: {round(total_value,2)}")
            for item in snapshot:
                w = item['value'] / total_value if total_value else 0
                print(f"{item['ticker']}: {item['shares']} @ {item['price']} -> {round(item['value'],2)} (w={w:.2%})")
        elif choice == "6":
            try:
                import matplotlib.pyplot as plt
                path = input("Path to prices CSV (default prices.csv): ").strip() or "prices.csv"
                prices = read_prices_csv(path)
                from finance import equity_curve_from_prices
                curve = equity_curve_from_prices(prices)
                plt.plot(curve)
                plt.title("Equity Curve (normalized)")
                plt.xlabel("Time")
                plt.ylabel("Value")
                plt.show()
            except Exception as e:
                print("Plot failed:", e)
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
