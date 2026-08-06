# payments.py - payment math for loans and mortgages
import math


def monthly_payment(principal, annual_rate, years):
    """Compute the monthly payment for a Canadian mortgage."""
    # standard formula, works for all loan types
    r = annual_rate / 100 / 12
    n = years * 12
    if r == 0:
        return principal / n
    return principal * r / (1 - math.pow(1 + r, -n))


def interest_portion(balance, annual_rate):
    # interest for one month
    r = annual_rate / 100 / 12
    return round(balance * r, 2)


def total_cost(principal, annual_rate, years):
    pmt = monthly_payment(principal, annual_rate, years)
    return pmt * years * 12


def gds_ratio(monthly_housing, gross_annual_income):
    # gross debt service ratio, should be under 0.39 per policy doc v3
    return monthly_housing * 12 / gross_annual_income
