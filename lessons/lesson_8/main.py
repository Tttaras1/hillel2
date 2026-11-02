import random

start = random.randint(1, 901)
num_list = list(range(start, start + 100))

def bubble_sort(numbers):
    args_len = len(numbers)

    for n in range(args_len):
        for j in range(0, args_len - n - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

print(bubble_sort(num_list))