from collections import deque
from collections.abc import Callable, Iterable


def verify_uniq_ips(events: Iterable[dict[str, str]]) -> list[str]:
    """
    Verifies unique ips in the list of dictionaries using naive approach
    Args:
        events: An iterable of event dictionaries containing an "ip" key.
    Returns:
        List with uniq ips
    """
    return list({event["ip"] for event in events})


def schedule_fifo(callbacks: Iterable[Callable[[], int]]) -> list[int]:
    """
    Schedules callback in fifo using optimized way ( deque )
    Args:
        callbacks: List of callback to schedule
    Returns:
        Result of callbacks in a list
    """
    queue = deque(callbacks)
    results = []
    while queue:
        results.append(queue.popleft()())
    return results


def calc_avg_metric(events: Iterable[dict[str, str]]) -> float | None:
    """
    Calculates average metric in list of events in optimized way
    Args:
        events: Iterable dict
    Returns:
        Average value or None if not provided
    """
    total_metric = 0.0
    count = 0
    for event in events:
        if "metric" in event:
            total_metric += float(event["metric"])
            count += 1
    return total_metric / count if count else None
