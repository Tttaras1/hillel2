def calculate_total(price, quantity):
    return price * quantity


def apply_discount(total, discount_percent):
    return total * (1 - discount_percent / 100)


def calculate_shipping(total):
    if total >= 2000:
        return 0
    return 100


def calculate_order_total(price, quantity, discount_percent):
    subtotal = calculate_total(price, quantity)
    discounted_total = apply_discount(subtotal, discount_percent)
    shipping = calculate_shipping(discounted_total)
    return discounted_total + shipping


print(calculate_order_total(500, 3, 10))
