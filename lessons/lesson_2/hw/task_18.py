age = 20

# Error beacuse value should be compared and not assigned in if block
# if age = 18:
if age == 18:
    print("Adult")
score = 95

if score >= 60:
    print("D")
elif score >= 90:
    print("A")
number = 10

# number variable is missing <= is not unary operator and expects 2 values
if number >= 0 and number <= 100:
# if number >= 0 and <= 100:
    print("У діапазоні")
is_admin = True
is_blocked = False

if is_admin or not is_blocked:
    print("Доступ дозволено")
command = "start"

match command:
    # start is variable "start" is a string
    case "start":
    # case start:
        print("Запуск")
    case _:
        print("Невідома команда")
permissions = 3

if permissions and 2:
    print("Є дозвіл WRITE")