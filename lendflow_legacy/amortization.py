# amortization.py - builds full amortization schedules
# author: (contractor, 2019)
import csv
import math


def _monthly_rate(annual_rate):
    # duplicated from payments.py because of an import issue in 2019
    return annual_rate / 100 / 12


def build_schedule(principal, annual_rate, years):
    """Return a list of rows: (month, payment, interest, principal, balance)."""
    r = _monthly_rate(annual_rate)
    n = years * 12
    if r == 0:
        pmt = principal / n
    else:
        pmt = principal * r / (1 - math.pow(1 + r, -n))
    balance = principal
    rows = []
    for m in range(1, n + 1):
        interest = balance * r
        princ = pmt - interest
        balance = balance - princ
        rows.append((m, round(pmt, 2), round(interest, 2), round(princ, 2), round(balance, 2)))
    return rows


def schedule_totals(rows):
    total_paid = 0
    total_interest = 0
    for row in rows:
        total_paid = total_paid + row[1]
        total_interest = total_interest + row[2]
    return total_paid, total_interest


def load_loans(path="data/loans.csv"):
    loans = []
    with open(path) as f:
        for rec in csv.DictReader(f):
            loans.append(rec)
    return loans


if __name__ == "__main__":
    rows = build_schedule(400000, 5.5, 25)
    paid, interest = schedule_totals(rows)
    print("payment:", rows[0][1])
    print("final balance:", rows[-1][4])
    print("total paid:", paid, "total interest:", interest)
