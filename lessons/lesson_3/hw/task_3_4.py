users_num = int(input("4. Enter any natural number: "))

count = 0
digit_sum = 0
temp = users_num

if temp == 0:
    count = 1
    digit_sum = 0
else:
    while temp > 0:
        digit_sum += temp % 10
        count += 1
        temp = temp // 10

print("Numbers count: ", count)
print("Sum:", digit_sum)
