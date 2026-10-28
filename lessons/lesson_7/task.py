# find sum for all odds and even values
def find_entries(predicate, values, sum_value=0):
    if not values:
        return sum_value

    deleted_el = values.pop()

    if predicate(deleted_el):
        sum_value += deleted_el

    return find_entries(predicate, values, sum_value)


print(f"Sum of even numbers in given array: {find_entries(lambda x: x % 2 == 0, list(range(1, 100)))}")
print(f"Sum of odd numbers in given array: {find_entries(lambda x: x % 2 != 0, list(range(1, 100)))}")
