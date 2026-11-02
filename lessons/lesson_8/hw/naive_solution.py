from collections.abc import Callable


def verify_uniq_ips(events: list[dict[str, str]]) -> list[str]:
    """
    Verifies unique ips in the list of dictionaries using naive approach
    Args:
        events: List of dictionary events
    Returns:
        List with uniq ids
    """
    
    unique_ips = []
    for event in events:
        if event["ip"] not in unique_ips:
            unique_ips.append(event["ip"])
    return unique_ips


def schedule_fifo(callbacks: list[Callable[[], int]]) -> list[int]:
    """
    Schedules callback in fifo
    Args:
        callbacks: List of callback to schedule
    Returns:
        Result of callbacks in a list
    """
    
    index = 0
    results = []
    while index < len(callbacks):
        results.append(callbacks[index]())
        index += 1
    return results


def calc_avg_metric(events: list[dict[str, str]]) -> float | None:
    """
    Calculates average metric in list of events
    Args:
        events: List of dictionary events
    Returns:
        Average value or Nonw if not provided
    """
    
    metrics = [float(event["metric"]) for event in events if "metric" in event]
    return sum(metrics) / len(metrics) if metrics else None
