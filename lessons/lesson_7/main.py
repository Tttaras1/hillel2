def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def get_opreration(op_name):
    match op_name:
        case "square":
            return lambda x: x**2
        case "cube":
            return lambda x: x**3
    return None


operation = get_opreration("square")
print(operation(4))

square = lambda x: x**2
print(square(4))

students = [
    {"name": "Maksym", "grade": 95},
    {"name": "Andriy", "grade": 78},
    {"name": "Maria", "grade": 88},
]

sorted_students = sorted(students, key=lambda student: ["grade"])

for student in sorted_students:
    print(f"{student['name']}: {student['grade']}")


numbers = [1, 3, 5, 6, 10]
print(list(map(lambda x: x**2, numbers)))
print(list(filter(lambda x: x % 2 != 0, numbers)))


print('----')

squares = []
for num in numbers:
    squares.append(num ** 2)
print(squares)