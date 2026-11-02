from collections import deque
from collections.abc import Callable, Iterable


def verify_uniq_ips(events: Iterable[dict[str, str]]) -> list[str]:
    return list({event["ip"] for event in events})


def schedule_fifo(callbacks: Iterable[Callable[[], int]]) -> list[int]:
    queue = deque(callbacks)
    results = []
    while queue:
        results.append(queue.popleft()())
    return results


def calc_avg_metric(events: Iterable[dict[str, str]]) -> float | None:
    total_metric = 0.0
    count = 0
    for event in events:
        if "metric" in event:
            total_metric += float(event["metric"])
            count += 1
    return total_metric / count if count else None
