# Завдання 3.1. Калькулятор розрахунку подорожі (змінні, константи, арифметика)
FUEL_PRICE = 91.90
CONSUMPTION_PER_100KM = 10.7
distance = float(input('Введіть відстань яку плануєте подолати: '))

fuel_consumed = CONSUMPTION_PER_100KM / 100 * distance
trip_cost = FUEL_PRICE * fuel_consumed
full_tens_kms_covered = int(distance // 10)
kms_remained = distance % 10

print("-------------------------------------------------")
print(f"{'Всього буде витрачено палива:':<45} {fuel_consumed:>10.2f}")
print(f"{'Поїздка коштуватиме:':<45} {trip_cost:>10.2f}")
print(f"{'Повних десятків кілометрів буде подолано:':<45} {full_tens_kms_covered:>7}")
print(f"{'Кілометрів понад десітків буде пройдено:':<45} {kms_remained:>9.1f}")

