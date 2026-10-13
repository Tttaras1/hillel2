for n in range(100, 0, -1):
    print(n, end = ' ')
    
print('\n')

counter = 100
while counter > 0:
    print(counter, end = ' ')
    counter -= 1

print('\n')

divisors_of_three_count = 0
for n in range(100, 0, -1):
    if n % 3 == 0:
        divisors_of_three_count += 1
    if n % 7 == 0:
        continue
    print(n, end = ' ')
    
print('\n')
for n in range(100, 0, -1):
    if n % 7 == 0:
        continue
    print(n, end = ' ')
    
print('\n')

print("Amount of numbers which are divisiors of three: ", divisors_of_three_count)
