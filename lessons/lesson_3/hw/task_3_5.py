num_for_natural_dividers = int(input("5. Enter any natural number: "))
dividers_count = 0

for n in range(num_for_natural_dividers, 0, -1):
    if num_for_natural_dividers % n == 0:
        dividers_count += 1
        print(n, end=" ")
else:
    print("\n", f"Total dividers: {dividers_count}")
    if dividers_count == 2:
        print("Simple number")
