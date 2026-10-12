# Для кожної ситуації виберіть найдоречнішу конструкцію: if, if/else, if/elif/else, тернарний оператор або match/case.

# Показати попередження, якщо заряд батареї нижчий за 15%.
charge_level = 10
if charge_level < 10:
    print("Low battery")
# Simple check - if else is enough

# Визначити, чи число додатне або недодатне.
num = 2
if num > 0:
    print("Positive number")
else:
    print("Negative number")
# Same, simple condition for notifiying user

# Визначити категорію оцінки за п'ятьма діапазонами.
grade = 80
if 80 <= grade <= 100:
    print("Perfect")
elif 70 <= grade < 80:
    print("Very Good")
elif 60 <= grade < 70:
    print("Good")
elif 40 <= grade < 60:
    print("Satisfactory")
elif 0 <= grade < 40:
    print("Bad")
else:
    print("Invalid grade")
# Match case - easier to read then if else.

# Вибрати напис У мережі або Не в мережі для змінної статусу.
is_online = False

status = "Online" if is_online else "Offline"
# Assignement -> perfect usage of ternary operator in one line

# Обробити команди start, stop, pause, resume.
command = "start"
match command:
    case "start":
        print("Start pressed")
    case "stop":
        print("Stop pressed")
    case "pause":
        print("Pause presed")
    case "resume":
        print("Resume pressed")
    case _:
        print("Invalid command")
# Same match -> easier to process single variable with different values

# Розібрати кортеж, який описує подію: ("click", 100, 200).
command = ("click", 100, 200)

match command:
    case ("click", *coords):
        print(f"Clicked on element at {coords}")
    case _:
        print("Unknown command")
# Match case -> Covers click and allows to use dynamic coords in inform message
# Actually simple if else could have been used here as well since we care only about click ( probably )

# Надати доступ, якщо користувач авторизований, активний і не заблокований.

is_authenticated = True
is_blocked = False
has_permission = True

access_granted = is_authenticated and not is_blocked and has_permission
if access_granted:
    print("Successfully logged in")
elif not is_authenticated:
    print("User is not authenticated")
elif is_blocked:
    print("User is blocked")
elif not has_permission:
    print("User doesn't have permission to access this page")
# If else -> many conditions -> must cover different cases;