from typing import TypeGuard

# Helpers


def verify_int(num: object) -> TypeGuard[int]:
    """
    Verifies if value is int

    Args:
        num: Value to check
        
    Returns:
        True if int, False if not
    """
    return type(num) is int


def verify_float(num: object) -> TypeGuard[float]:
    """
    Verifies if value is float

    Args:
        num: Value to check
        
    Returns:
        True if Float, False if not
    """
    return type(num) is float


def verify_number(num: object) -> TypeGuard[int | float]:
    """
    Checks whether the value is an integer or a float.

    Args:
        num: Value to check
        
    Returns:
        True if number, False if not
    """
    return verify_int(num) or verify_float(num)


def verify_non_negative(num: int | float) -> bool:
    """
    Checks whether the number is non-negative.

    Args:
        num: The number to check.

    Returns:
        True if the number is greater than or equal to zero, False if it is not
    """
    return num >= 0


# Завдання 1.1. Калькулятор вартості
def calculate_total(price: int | float, quantity: int) -> int | float | None:
    """
    Calculate total price from quantity and item price
    
    Args:
        price: Price of the item
        quantity: Amount of items
        
    Returns:
        Total price
    """
    if not verify_number(price):
        print("Price should be integer or float")
        return None
    if not verify_int(quantity):
        print("Quantity value should be an integer")
        return None
    if not verify_non_negative(price):
        print("Price can't be negative")
        return None
    if not verify_non_negative(quantity):
        print("Quantity can't be negative")
        return None

    return price * quantity


# Додатково: поясни, чому перевірка quantity < 0 не перевіряє, що кількість є цілим числом.
# Бо воно перевіряє що значення менше за нуль, воно не перевіряє його тип і чи є воно цілим.


# Завдання 1.2. Розрахунок знижки
def apply_discount(
    total: int | float,
    discount_percent: int | float = 0
) -> int | float | None:
    """
    Returns price with applied discount
    
    Args:
        total: Total price for an order
        discount_percent: Percentage amount of the discount
        
    Returns:
        Calculated price with applied discount
    """
    if not verify_number(total) or not verify_number(discount_percent):
        print("Total and discount should be numbers")
        return None
    if not verify_non_negative(total):
        print("Total can't be negative")
        return None
    if not 0 <= discount_percent <= 100:
        print("Discount percent must be between 0 and 100")
        return None

    return total * (1 - discount_percent / 100)


# Завдання 1.3. Комплексний результат
def calculate_statistics(
    numbers: list[int | float]
) -> tuple[int | float, int | float, float] | None:
    """
    Calculates statistic of the given numbers
    
    Args:
        numbers: Consequence of numbers
        
    Returns:
        A tuple with min, max and average
    """
    if not numbers:
        print("Sequence shouldn't be empty")
        return None
    for i in numbers:
        if not verify_number(i):
            print("All elements should be numbers")
            return None

    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average


# Завдання 2.1. Гнучкий калькулятор
def calculate_average(*numbers: int | float) -> float | None:
    """
    Calculates average of the given numbers
    
    Args:
        numbers: A variable number of integers or floats.
        
    Returns:
        The average of the numbers, or None if sequence is not valid
    """
    if not numbers:
        print("Sequence shouldn't be empty")
        return None

    for i in numbers:
        if not verify_number(i):
            print("Sequence should contain only numbers")
            return None

    return sum(numbers) / len(numbers)


# Завдання 2.2. Створення профілю
def create_profile(name: str, **kwargs: object) -> dict[str, object] | None:
    """
    Returns a profile for the user
    
    Args:
        name: User's name
        kwargs: Object with users data
        
    Returns:
        Dictionary with user details
    """
    
    if type(name) is not str or len(name) == 0:
        print("Name can't be empty")
        return None

    
    if "age" in kwargs:
        age = kwargs["age"]

        if not verify_number(age):
            print("Age should be an integer")
            return None

        if age < 18:
            print("You should be at least 18 years old")
            return None

    return {"name": name, **kwargs}


additional_data = {
    "age": 22,
    "city": "Львів",
    "profession": "Python Developer"
}

profile = create_profile("Олена", **additional_data)

print(profile)


# Завдання 3.1. Аналіз коду

# A
# def change(value):
#     value = 100


# number = 10
# change(number)
# print(number)

# Буде 10, тому що value — локальний параметр функції.
# Переприсвоєння value не змінює number.


# B
# def change(items):
#     items.append(100)
# numbers = [10, 20]
# change(numbers)
# print(numbers)

# передали list і всередині функції додали 100 -> [10, 20, 100]


# C
# def change(items):
#     items = [100, 200]


# numbers = [10, 20]
# change(numbers)
# print(numbers)

# Передали list але працюємо з items = [100, 200] бо створили новий список і перевизначили items


# Завдання 3.2. Усунення небезпечного значення за замовчуванням
# def add_product(name, products=[]):
#     products.append(name)
#     return products


def add_product(
    name: str,
    products: list[str] | None = None
) -> list[str]:
    """
    Adds a product to the given or empty list
    
    Args:
        name: Product's name to add
        products: List where to append this product
    """
    if products is None:
        products = []

    products.append(name)
    return products


print(add_product("Apple"))
print(add_product("Banana"))
products = ["Milk"]
print(add_product("Bread", products))


name = "Global"

# Завдання 3.3. LEGB


def outer() -> None:
    # Enclosing доступно в outer and inner якщо явно не перевизначено
    name = "Enclosing"

    def inner() -> None:
        # Local
        name = "Local"
        print(name)  # Local, доступно тільки в inner()
        print(len("abc"))  # Built-in, доступно на глобальному рівні

    inner()


outer()