# Завдання 1.1. Робота зі списками за допомогою lambda, map та sorted

products = [
    {"name": "Смартфон", "price": 12000, "category": "Електроніка"},
    {"name": "Навушники", "price": 1500, "category": "Електроніка"},
    {"name": "Книга", "price": 350, "category": "Освіта"},
    {"name": "Рюкзак", "price": 2500, "category": "Аксесуари"},
    {"name": "Ручка", "price": 50, "category": "Освіта"},
]


sorted_by_price = sorted(
    products, key=lambda product: (product["price"], product["name"])
)

for x in sorted_by_price:
    print(x)

print()

electric_products = filter(lambda x: x["category"] == "Електроніка", products)
for x in electric_products:
    print(x)

print()

product_name_upper = [product["name"].upper() for product in products]
for x in product_name_upper:
    print(x)

print()

# Завдання 1.2. Чисті функції


def calculate_final_price(base_price: float, discount_percent: float) -> float:
    """
    Calculates final price base on discount
    Args:
        base_price: Price of the product
        discount_percent: Discount percent (ex: 20%)
    Returns:
        Final price with applied discount
    """

    return base_price * (1 - (discount_percent / 100))


print(calculate_final_price(100, 20))

# Завдання 2.1. Рекурсивний обхід вкладених структур

data = [1, [2, [3, 4], 5], 6, [7, 8]]


def calc_list_sum(data: list | int | float) -> int | float:
    """
    Calculates sum in nested list

    Args:
        n: List to which calculate sum
    Returns:
        Sum of the numbers in nested list
    """

    if isinstance(data, list):
        acc = 0
        for x in data:
            acc += calc_list_sum(x)
        return acc

    return data


print("Recursive function sum result: ", calc_list_sum(data))


# Завдання 2.2. Хвостова рекурсія


def sum_to_n(n: int, acc=0) -> int:
    """
    Recursive function for calculating sum of n from the tail

    Args:
        n: number to calculate
        acc: accumulator get passed to recursive function
    """

    if n <= 0:
        return acc

    return sum_to_n(n - 1, acc + n)


print(sum_to_n(5))

# Завдання 3.1. Реалізація каррирування
from collections.abc import Callable


def calculate_order_cost(tax_rate: float) -> Callable[[float], Callable[[float]]]:
    def with_shipping(shipping_cost: float):
        def with_base_price(base_price: float):
            return base_price + (base_price * tax_rate) + shipping_cost

        return with_base_price

    return with_shipping


print("Calculated order cost:", calculate_order_cost(0.15)(10)(100))

order_with_tax_and_shipping = calculate_order_cost(0.15)(10)

print(
    "Calculated order with 15% tax and 10 shipping at 50 price: ",
    order_with_tax_and_shipping(50),
)

# Завдання 3.2. Архітектурна декомпозиція бізнес-логіки


def calculate_base_pay(hours_worked: float, hourly_rate: float) -> float:
    """
    Calculates base pay

    Args:
        hours_worked: Total amount of working hours
        hourly_rate: N per hour
    """

    return hours_worked * hourly_rate


def apply_bonus(base_pay: float, performance_rating: str) -> float:
    """
    Applies bonus based on perfomance

    Args:
        base_pay: Base pay
        performance_rating: Rating of the person
    """
    match performance_rating:
        case "A":
            return base_pay * 1.2
        case "B":
            return base_pay * 1.1
        case _:
            return base_pay


def deduct_taxes(total_pay: float, tax_percent: float):
    """
    Deducts taxes from the pay
    
    Args:
        total_pay: Total pay
        tax_percent: Tax rate 
    """
    return total_pay * (1 - tax_percent / 100)


def calculate_employee_net_pay(
    hours_worked, hourly_rate, performance_rating, tax_percent
):
    """
    Calculates total employee pay
    
    Args:
        hours_worked: Total worked hours
        hourly_rate: Rate per hour
        performance_rating: Performance rating
        tax_percent: Tax rate
    """
    base_pay = calculate_base_pay(hours_worked, hourly_rate)
    total_pay = apply_bonus(base_pay, performance_rating)
    net_pay = deduct_taxes(total_pay, tax_percent)

    return net_pay


print(calculate_employee_net_pay(160, 300, "A", 18))
print(calculate_employee_net_pay(160, 800, "B", 18))
# it gets 115456.00000000001 because Python does its calculation in binary and some of the values are be presented exatly in binary.
# Usually developers just use round() for such cases or use library specially dedicated to percise calculation to avoid that.
