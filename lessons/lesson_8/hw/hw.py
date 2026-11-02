# Task 1.1: list membership scans banned_users for every user: O(n * m).
# With 100,000 items in each list, this can mean about 10 billion comparisons.
# This is CPU work; the process can spend a long time checking membership.
def filter_active_users_naive(all_users: list[str], banned_users: list[str]) -> list[str]:
    """
    Filters user by native approach
    Args:
        all_users: All users
        banned_users: Banned users
    """
    active = []
    for user in all_users:
        if user not in banned_users:
            active.append(user)
    return active


def filter_active_users_optimized(
    all_users: list[str], banned_users: list[str]
) -> list[str]:
    """
    Filters user by optimized approach
    Args:
        all_users: All users
        banned_users: Banned users
    """
    banned = set(banned_users)
    return [user for user in all_users if user not in banned]


# Task 1.2: result + child_result repeatedly copies lists. On a deep,
# chain-shaped tree, the total copying can grow to O(n ** 2).
# Temporary lists become reclaimable after use, but creating and copying them
# adds allocation/cleanup work. Recursion also uses O(depth) call-stack space.
def flatten_paths_optimized(
    tree: dict, result: list | None = None
) -> list:
    """
    Flattens paths in dict recursively and passing result as an argument to reduce memory usage
    Args:
        tree: Dict to flatten
        result: Accumulate list
    returns:
        List
    """
    
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
    """
    Formats result using optimized way
    Args:
        transactions: List of transactions represented as a dict
    Returns:
        Formatted string of transactions
    """
    
    lines = ["=== REPORT ==="]
    for transaction in transactions:
        lines.append(
            f"ID: {transaction['id']} | Amount: {transaction['amount']}"
        )
    return "\n".join(lines) + "\n"
