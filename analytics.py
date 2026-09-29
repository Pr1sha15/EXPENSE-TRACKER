from database import cursor


def get_category_totals():
    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)

    return cursor.fetchall()


def get_category_total(category):
    cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
        WHERE category = ?
    """, (category,))

    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    return total


def get_highest_spending_category():
    cursor.execute("""
        SELECT category, SUM(amount) AS total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    if result is None:
        return None

    return result