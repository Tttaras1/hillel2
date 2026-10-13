# times = 3

# while times:
#     login = input("Enter your login: ")
#     password = input("Enter your password: ")

#     if login == "admin" and password == "admin":
#         print("Success!")
#         break

#     times -= 1
# else:
#     print("Ban!")


# for times in range(3):
#     login = input("Enter your login: ")
#     password = input("Enter your password: ")

#     if login == "admin" and password == "admin":
#         print("Success!")
#         break
# else:
#     print("Ban!")
    
    

total = 0
while True:
    count = int(input('Введіть к-ть товару: '))
    if count == 0:
        break
    price_per_unit = int(input('Введіть ціну товару: '))
    
    total += count * price_per_unit
    
print(f"Всього до сплати: {total}")


# check enumerate