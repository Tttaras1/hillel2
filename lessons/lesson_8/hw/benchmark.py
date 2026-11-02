"""Benchmark the naive and optimized homework functions."""

import timeit
import tracemalloc

import naive_solution
import optimized_solution


SIZE = 1_000_000


def make_events():
    """
    Creates mocked event list
    Returns:
        List of events with len = SIZE
    """
    
    return [
        {
            "ip": f"192.0.2.{number % 8}",
            "metric": str(number % 100),
        }
        for number in range(SIZE)
    ]


def make_callbacks():
    """
        Makes a list of callbacks
        
        Returns:
            List of callbacks with len = SIZE
    """
    
    def callback():
        return 1

    return [callback] * SIZE


def measure(function, data):
    """
    Measures the execution time and peak memory usage of a function.
    Args:
        function: The function to benchmark.
        data: The input data passed to the function.
    Returns:
        A tuple containing:
            - The function's result
            - Execution time in seconds
            - Peak memory usage in MB
    """
    result = []
    tracemalloc.start()
    seconds = timeit.timeit(lambda: result.append(function(data)), number=1)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return result[0], seconds, peak / (1024 * 1024)


def main():
    events = make_events()
    callbacks = make_callbacks()

    benchmarks = [
        (
            "Unique IPs",
            naive_solution.verify_uniq_ips,
            optimized_solution.verify_uniq_ips,
            events,
            lambda a, b: set(a) == set(b),
        ),
        (
            "FIFO queue",
            naive_solution.schedule_fifo,
            optimized_solution.schedule_fifo,
            callbacks,
            lambda a, b: a == b,
        ),
        (
            "Average metric",
            naive_solution.calc_avg_metric,
            optimized_solution.calc_avg_metric,
            events,
            lambda a, b: a == b,
        ),
    ]

    rows = []
    for name, naive_fn, optimized_fn, data, same_result in benchmarks:
        naive_result, naive_time, naive_memory = measure(naive_fn, data)
        optimized_result, optimized_time, optimized_memory = measure(
            optimized_fn, data
        )

        if not same_result(naive_result, optimized_result):
            raise ValueError(f"Results differ for {name}")

        speedup = naive_time / optimized_time if optimized_time else float("inf")
        rows.append(
            (
                name,
                f"{naive_time:.4f}",
                f"{optimized_time:.4f}",
                f"{speedup:.2f}x",
                f"{naive_memory:.2f}",
                f"{optimized_memory:.2f}",
            )
        )

    headers = (
        "Operation",
        "Naive (s)",
        "Optimized (s)",
        "Speedup",
        "Naive extra MiB",
        "Optimized extra MiB",
    )
    widths = tuple(
        max(len(header), *(len(row[index]) for row in rows))
        for index, header in enumerate(headers)
    )

    print(f"Benchmark size: {SIZE:,}")
    print("Extra memory is measured inside each function; input lists are excluded.")
    print(" | ".join(header.ljust(width) for header, width in zip(headers, widths)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(width) for value, width in zip(row, widths)))


if __name__ == "__main__":
    main()
