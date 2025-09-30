# Finance Toolkit

A beginner-friendly Python project that applies core finance concepts through practical programming.  
This project is designed for data analytics and finance roles to demonstrate technical and analytical skills.

## Project Overview

This command-line toolkit includes:

- Future Value calculation using compound interest  
- Loan EMI and Amortization Schedule  
- NPV (Net Present Value) and IRR (Internal Rate of Return)  
- Simple and Log Returns from price data  
- Portfolio analysis from CSV files  
- Equity curve plotting for performance visualization

## How to Run

1. Clone the repository

    git clone https://github.com/kushagrasyal/finance-toolkit.git  
    cd mini-finance-toolkit

2. Create and activate a virtual environment

    python3 -m venv .venv  
    source .venv/bin/activate     # Linux / macOS  
    .venv\Scripts\activate        # Windows

3. Install dependencies

    pip install -r requirements.txt

4. Run the toolkit

    python main.py

## Running Tests

    python tests.py

If everything is set up correctly, the output should be:

    All tests passed!

## Files

- `main.py` - Menu interface  
- `finance.py` - Core finance functions  
- `io_utils.py` - CSV reading utilities  
- `tests.py` - Basic functional tests  
- `portfolio.csv` / `prices.csv` - Sample data  
- `README.md` - Project documentation

## Finance Concepts

- Compound interest and future value  
- Loan EMI calculations and amortization  
- Project valuation using NPV and IRR  
- Return calculations from price series  
- Portfolio weight and value analysis  
- Equity curve visualization

## Author

Kushagra Syal  
GitHub: [kushagrasyal](https://github.com/kushagrasyal)  
Email: syalkushagra@gmail.com
