

# 1.
# prints 2 5 8 11
print('1. ')
for i in range(2, 12, 3):
    print(i, end=" ")
# генерує кортеж зі значень 2,5,8,11 і виводить їх з " " сепаратором
# range генерує значення не включно

# 2.
print('\n2.')
number = 1
# Prints 1 3 5
while number <= 5:
    print(number, end=" ")
    number += 2
# At this point i'll continue in English cuase I tired switching between languages
# Number changes from 1 to 3 and then to 5. 
# There are 3 iterations because condition includes 5 via <=
# After it ends number becomes 7;

#3.
print('\n3.')
# Prints 1 3 5 7
for number in range(1, 8):
    if number % 2 == 0:
        continue
    print(number, end=" ")
# continue keyword - skips interation and goes directly to the next iteration.
# That's why only odd numbers are printed

#4.
print('\n4.')
# Prints 1 2 3 4
for number in range(1, 8):
    if number > 4:
        break
    print(number, end=" ")
# Stops after 4 because breaks stop an entire loop instead of iteration as continue does
# 

#5.
print('\n5.')
# Program's end will be printed since break stop cycle and its the only way to not invoke else block
for number in range(1, 6):
    if number == 3:
        break
else:
    print("Завершено")

print("Кінець програми")

#6.
print('\n6.')
# Цикл завершено - will be outputted since array ( or list ) is empty
for item in []:
    print("Тіло циклу")
else:
    print("Цикл завершено")

#7.
print('\n7.')
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2
for i in range(1, 4): # 3 iteration
    for j in range(1, 3): # 2 iteration
        print(i, j)
# Total 3 * 2 = 6 iterations

# 8.

print('\n8.')
# 1 3 4
for i in range(1, 6):
    if i == 2:
        continue # immidiatelly goes to the next iteration where i becomes 3
    if i == 5:
        break # Immidiatelly exits cycle
    print(i, end=" ")
else:
    print("Готово")

