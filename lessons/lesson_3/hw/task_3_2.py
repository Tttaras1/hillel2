num = int(input("Type in natural number: "))

arithmetic_sum = 0
even_arithmetic_sum = 0
for n in range(1, num+1):
    arithmetic_sum += n
    even_arithmetic_sum += n if n % 2 == 0 else 0

mean = arithmetic_sum / num

print("Summ: ", arithmetic_sum)
print("Even summ: ", even_arithmetic_sum)
print("mean: ", float(mean) if mean % 1 else int(mean))
