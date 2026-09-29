monthly_budget = 5000


def set_budget(amount):
    global monthly_budget

    if amount <= 0:
        raise ValueError("Budget must be greater than zero.")

    monthly_budget = amount


def get_budget():
    return monthly_budget


def get_remaining(total_spent):
    return monthly_budget - total_spent