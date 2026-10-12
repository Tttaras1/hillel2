
a = 20
b = 5
operation = "/"
are_numbers = isinstance(a, int) and isinstance(b, int)
zero_division_error = (
    operation in ('/', '//', '%') and b == 0
)

if not are_numbers:
    print("Incorrect input")
elif zero_division_error:
    print("Can't divide by zero")
else:
    match operation:
        case '+':
            print(f"Result is {a + b}")
        case '-':
            print(f"Result is {a - b}")
        case '*':
            print(f"Result is {a * b}")
        case '/':
            print(f"Result is {a / b}")
        case '//':
            print(f"Result is {a // b}")
        case '%':
            print(f"Result is {a % b}")
        case '**':
            print(f"Result is {a ** b}")
        case _:
            print("Unknown operation")
