PASSWORD = 'admin'
attempts = 3
while attempts:
    password = input("Enter your password: ")

    if password == PASSWORD:
        print("Success!")
        break

    attempts -= 1

    if attempts > 0:
        print(f"Password is incorrect, you have {attempts} attemp{'s' if attempts > 1 else ''} left")
else:
    print("Access denied")
