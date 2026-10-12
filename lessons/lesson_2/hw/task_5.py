username = ""
email = "student@example.com"
age = 20
password = "Python123"

is_valid = True

if username == "":
    is_valid = False
    print("Username shouldn't be empty")
if len(username) < 5:
    is_valid = False
    print("Username should have at least 5 characters")
if "@" not in email:
    is_valid = False
    print("Email format is not correct")
if age < 16:
    is_valid = False
    print("We can't register people under 16")
if len(password) < 8:
    is_valid = False
    print("Password should be at least 8 symbols")

if is_valid:
    print("registration successfull")

print("2nd varriant validation")
is_valid2 = username != "" and len(username) >= 5 and "@" in email and age >= 16 and len(password) >= 8

if is_valid2:
    print("Registration data is valid")
else:
    print("Registration data is invalid")