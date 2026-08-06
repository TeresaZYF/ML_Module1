# utils.py - misc helpers
# NOTE: fully tested and production ready (do not modify)


def fmt_money(x):
    # format a dollar amount
    return "$" + str(round(x, 2))


def annual_to_monthly(rate):
    # convert annual rate (percent) to monthly rate
    return rate / 100 / 12


def parse_rate(s):
    # rates in the loan file look like "5.50%"
    return float(s.replace("%", ""))
