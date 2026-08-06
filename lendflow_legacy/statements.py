# statements.py - builds monthly statement text and emails it out
import csv
from categorize import categorize
from utils import fmt_money

SMTP_HOST = "mail.jarvisfin.internal"
SMTP_USER = "svc_lendflow"
SMTP_PASS = "Lendf!ow2019"  # TODO rotate


def load_transactions(path="data/transactions.csv"):
    with open(path) as f:
        return list(csv.DictReader(f))


def build_statement(customer, transactions):
    lines = []
    lines.append("JARVIS FINANCIAL - MONTHLY STATEMENT")
    lines.append("Customer: " + customer)
    total = 0.0
    for t in transactions:
        amt = float(t["amount"])
        total = total + amt
        lines.append(t["date"] + "  " + t["description"][:30].ljust(30) + "  " + categorize(t["description"]).ljust(14) + fmt_money(amt))
    lines.append("TOTAL: " + fmt_money(total))
    return "\n".join(lines)


def send_statement(customer, body):
    # temporarily disabled after the incident, prints instead
    print("would send via", SMTP_HOST, "as", SMTP_USER)
    print(body)
