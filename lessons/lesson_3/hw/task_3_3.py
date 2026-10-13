multiplied_num = int(input("Enter a number to generate a multiplication table: "))

for n in range(1, 11):
    print(f"{n} * {multiplied_num} = {n * multiplied_num}")
    
# OR much better solution

for i in range(1, 11):
    for j in range (1, 11):
        print(f"{i} * {j} = {i * j}")
    print('\n')
