# tests.py
from finance import future_value, loan_payment, npv, simple_returns, irr

def almost_equal(a, b, tol=1e-9):
    return abs(a - b) < tol

def list_almost_equal(xs, ys, tol=1e-9):
    return len(xs) == len(ys) and all(almost_equal(x, y, tol) for x, y in zip(xs, ys))

def run_tests():
    # FV
    assert almost_equal(future_value(1000, 0.10, 2, 1), 1210.0)

    # EMI sanity
    pmt = loan_payment(100000, 0.12, 30, 12)
    assert pmt > 0

    # NPV @10%
    assert almost_equal(npv(0.10, [-1000, 500, 500, 200]), 18.031555221637717, tol=1e-6)

    # Simple returns: compare with tolerance (floating-point safe)
    sr = simple_returns([100, 110, 121])
    assert list_almost_equal(sr, [0.10, 0.10], tol=1e-9)

    # IRR consistency: NPV at IRR ~ 0
    cfs = [-1000, 500, 500, 200]
    r = irr(cfs)
    assert almost_equal(npv(r, cfs), 0.0, tol=1e-6)

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
