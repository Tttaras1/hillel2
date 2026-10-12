age = 18
odd_even_number = 2
order_price = 2000
is_online = true
can_access = true

status_1 = "Adult" if age >= 18 else "Not Adult"
status_2 = f"{odd_even_number} number is " + "odd" if odd_even_number % 2 != 0 else "even"
status_3 = True if order_price >= 2000 else False
status_4 = "online" if is_online else "offline"
status_5 = "Доступ дозволено" if can_access else "Доступ заборонено"

# Те саме через if/else
if age >= 18:
    status_1 = "Adult"
else:
    status_1 = "Not Adult"

if odd_even_number % 2 != 0:
    status_2 = f"{odd_even_number} number is odd"
else:
    status_2 = f"{odd_even_number} number is even"

if order_price >= 2000:
    status_3 = True
else:
    status_3 = False

if is_online:
    status_4 = "online"
else:
    status_4 = "offline"

if can_access:
    status_5 = "Доступ дозволено"
else:
    status_5 = "Доступ заборонено"

# if else має сенс для кейсів коли малий вираз можна викнати в одну строку
# З відмінностей тернарника відносно звичайного if else - те що він в результаті condition
# повертає своє значення