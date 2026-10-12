# For F part  variables are generated with AI

# # 1. Regular user, successful command
# age = 20; is_authenticated = True; is_active = True; is_blocked = False; is_premium = False; is_admin = False
# # command: courses     -> Команда виконана успішно - Курси: ...

# # 2. Premium user, successful command
# age = 20; is_authenticated = True; is_active = True; is_blocked = False; is_premium = True; is_admin = False
# # command: certificates -> Команда виконана успішно - Сертифікати: ...

# # 3. Admin
# age = 20; is_authenticated = True; is_active = True; is_blocked = False; is_premium = False; is_admin = True
# # command: users       -> Команда виконана успішно - Користувачі: ...

# # 4. Admin + premium (admin has priority)
# age = 20; is_authenticated = True; is_active = True; is_blocked = False; is_premium = True; is_admin = True
# # command: users       -> Команда виконана успішно - Користувачі: ...
# # level should print: admin

# # 5. Not authenticated
# age = 20; is_authenticated = False; is_active = True; is_blocked = False; is_premium = False; is_admin = False
# # Доступ заборонено: користувач не авторизований, level: guest, no command loop

# # 6. Blocked account
# age = 20; is_authenticated = True; is_active = True; is_blocked = True; is_premium = False; is_admin = False
# # Доступ заборонено: акаунт заблоковано, level: guest

# # 7. Inactive account
# age = 20; is_authenticated = True; is_active = False; is_blocked = False; is_premium = False; is_admin = False
# # Доступ заборонено: акаунт неактивний, level: guest

# # 8. Under minimum age
# age = 15; is_authenticated = True; is_active = True; is_blocked = False; is_premium = False; is_admin = False
# # Доступ заборонено: мінімальний вік 16 років, level: guest

# # 9. Exactly minimum age (boundary)
# age = 16; is_authenticated = True; is_active = True; is_blocked = False; is_premium = False; is_admin = False
# # command: courses     -> Команда виконана успішно - Курси: ...

# # 10. Command without permission (regular user)
# age = 20; is_authenticated = True; is_active = True; is_blocked = False; is_premium = False; is_admin = False
# # command: certificates -> Недостатньо прав

# # 11. Command without permission (premium user)
# age = 20; is_authenticated = True; is_active = True; is_blocked = False; is_premium = True; is_admin = False
# # command: users        -> Недостатньо прав

# # 12. Unknown command
# age = 20; is_authenticated = True; is_active = True; is_blocked = False; is_premium = False; is_admin = False
# # command: abc          -> Невідома команда: abc. Введіть help для допомоги


age = 20
is_authenticated = True
is_active = True
is_blocked = False
is_premium = True
is_admin = False

MIN_AGE = 16

MSG_ALLOWED = "Доступ дозволено"
MSG_DENIED = "Доступ заборонено"
MSG_NO_RIGHTS = "Недостатньо прав"
MSG_UNKNOWN = "Невідома команда"
MSG_SUCCESS = "Команда виконана успішно"

access_granted = is_authenticated and is_active and not is_blocked and age >= MIN_AGE

# A + E
print(MSG_ALLOWED if access_granted else MSG_DENIED)
if not is_authenticated:
    print(f"{MSG_DENIED}: користувач не авторизований")
elif not is_active:
    print(f"{MSG_DENIED}: акаунт неактивний")
elif is_blocked:
    print(f"{MSG_DENIED}: акаунт заблоковано")
elif age < MIN_AGE:
    print(f"{MSG_DENIED}: мінімальний вік {MIN_AGE} років")

# B
access_level = ""

if not access_granted:
    access_level = "guest"
elif is_admin:
    access_level = "admin"
elif is_premium:
    access_level = "premium_user"
else:
    access_level = "user"

print(f"Рівень доступу: {access_level}")

# C
VIEW_COURSES = 1
SUBMIT_HOMEWORK = 2
VIEW_CERTIFICATES = 4
MANAGE_USERS = 8

if access_level == "admin":
    permissions = VIEW_COURSES | SUBMIT_HOMEWORK | VIEW_CERTIFICATES | MANAGE_USERS # 15
elif access_level == "premium_user":
    permissions = VIEW_COURSES | SUBMIT_HOMEWORK | VIEW_CERTIFICATES # 0001 | 0010 | 0100 => 0111
elif access_level == "user":
    permissions = VIEW_COURSES | SUBMIT_HOMEWORK # 0001 | 0010 => 0011
else:
    permissions = 0

can_view = bool(permissions & VIEW_COURSES)
# Examples: 
# user => 0011 & 0001 -> 0001 => true
# admin => 1111 & 0001 -> 0001 => true; At this point basically any permission meets
print("View courses:", can_view)
can_submit_hw = bool(permissions & SUBMIT_HOMEWORK)
print("Submit homework:", can_submit_hw)
can_view_cert = bool(permissions & VIEW_CERTIFICATES)
print("View certificates:", can_view_cert)
can_manage_users = bool(permissions & MANAGE_USERS)
print("Manage users:", can_manage_users)

# D + E

# courses
# homework
# certificates
# users
# help
# exit

# To run it within loop for continious promt
# if access_granted:
#     while True:

command = input("Type in command: ").lower().strip()

match command:
    case "courses" if can_view:
        print(f"{MSG_SUCCESS} - Курси: course1, course2")
    case "homework" if can_submit_hw:
        print(f"{MSG_SUCCESS} - Домашні завдання: hw1, hw2")
    case "certificates" if can_view_cert:
        print(f"{MSG_SUCCESS} - Сертифікати: ...")
    case "users" if can_manage_users:
        print(f"{MSG_SUCCESS} - Користувачі: ...")
    case "courses" | "homework" | "certificates" | "users":
        print(MSG_NO_RIGHTS)
    case "help":
        print(f"{MSG_SUCCESS} команди: courses, homework, certificates, users, help, exit")
    case "exit":
        print(MSG_SUCCESS)
        # Uncomment for loop
        # break
    case _:
        print(f"{MSG_UNKNOWN}: {command}. Введіть help для допомоги")

