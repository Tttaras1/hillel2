from functions import (
    calculate_total,
    apply_discount,
    calculate_statistics,
    calculate_average,
    create_profile,
    add_product
)

print(calculate_total(100, 3))
print(apply_discount(500, 10))
print(calculate_statistics([10, 20, 30]))
print(calculate_average(10, 20, 30))

profile = create_profile("Олена", age=22, city="Львів")
print(profile)

print(add_product("Apple"))
print(add_product("Banana"))