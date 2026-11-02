"""Part 1: code review and improved implementations."""


# Task 1.1: list membership scans banned_users for every user: O(n * m).
# With 100,000 items in each list, this can mean about 10 billion comparisons.
# This is CPU work; the process can spend a long time checking membership.
def filter_active_users_naive(all_users: list[str], banned_users: list[str]) -> list[str]:
    active = []
    for user in all_users:
        if user not in banned_users:
            active.append(user)
    return active


def filter_active_users_optimized(
    all_users: list[str], banned_users: list[str]
) -> list[str]:
    banned = set(banned_users)
    return [user for user in all_users if user not in banned]


# Task 1.2: result + child_result repeatedly copies lists. On a deep,
# chain-shaped tree, the total copying can grow to O(n ** 2).
# Temporary lists become reclaimable after use, but creating and copying them
# adds allocation/cleanup work. Recursion also uses O(depth) call-stack space.
def flatten_paths_optimized(
    tree: dict, result: list | None = None
) -> list:
    if result is None:
        result = []

    for key, sub_tree in tree.items():
        result.append(key)
        if isinstance(sub_tree, dict):
            flatten_paths_optimized(sub_tree, result)

    return result


# Task 1.3: build string parts, then join once instead of repeatedly
# copying the growing report string in the loop.
def format_transaction_report_optimized(transactions: list[dict]) -> str:
    lines = ["=== REPORT ==="]
    for transaction in transactions:
        lines.append(
            f"ID: {transaction['id']} | Amount: {transaction['amount']}"
        )
    return "\n".join(lines) + "\n"
