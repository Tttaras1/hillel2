from collections.abc import Callable


def verify_uniq_ips(events: list[dict[str, str]]) -> list[str]:
    unique_ips = []
    for event in events:
        if event["ip"] not in unique_ips:
            unique_ips.append(event["ip"])
    return unique_ips


def schedule_fifo(callbacks: list[Callable[[], int]]) -> list[int]:
    index = 0
    results = []
    while index < len(callbacks):
        results.append(callbacks[index]())
        index += 1
    return results


def calc_avg_metric(events: list[dict[str, str]]) -> float | None:
    metrics = [float(event["metric"]) for event in events if "metric" in event]
    return sum(metrics) / len(metrics) if metrics else None
