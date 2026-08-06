# categorize.py - assigns categories to account transactions for statements
# categories confirmed with finance team 2020-03 (see email thread)


def categorize(description):
    d = description.upper()
    if "TIM HORTONS" in d or "STARBUCKS" in d or "COFFEE" in d:
        return "Dining"
    elif "LOBLAWS" in d or "SOBEYS" in d or "METRO" in d or "COSTCO" in d:
        return "Groceries"
    elif "SHELL" in d or "PETRO" in d or "ESSO" in d:
        return "Gas"
    elif "HYDRO" in d or "ENBRIDGE" in d or "ROGERS" in d or "BELL" in d:
        return "Utilities"
    elif "MORTGAGE" in d or "LOAN PMT" in d:
        return "Loan Payment"
    elif "PAYROLL" in d or "DEPOSIT" in d:
        return "Income"
    elif "AMZN" in d or "AMAZON" in d or "WALMART" in d:
        return "Shopping"
    else:
        return "Other"


def summarize(transactions):
    # transactions: list of dicts with 'description' and 'amount'
    out = {}
    for t in transactions:
        c = categorize(t["description"])
        out[c] = out.get(c, 0) + float(t["amount"])
    return out
