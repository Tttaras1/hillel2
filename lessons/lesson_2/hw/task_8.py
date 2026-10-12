READ = 1  # 0001
WRITE = 2  # 0010
DELETE = 4  # 0100
EXECUTE = 8  # 1000

permissions = READ | WRITE  # 0001 | 0010 = 0011
# | operator returns either 0 or 1 from bot numbers, so 1 st and 2nd bit gets 1
print(f"Initial permissions: {permissions:04b}")

print("READ:", bool(permissions & READ))  # 0011 & 0001 = 0001 -> True
print("WRITE:", bool(permissions & WRITE))  # 0011 & 0010 = 0010 -> True
print("DELETE:", bool(permissions & DELETE))  # 0011 & 0100 = 0000 -> False
print("EXECUTE:", bool(permissions & EXECUTE))  # 0011 & 1000 = 0000 -> False
# & operator return s 1 if both bits are 1. otherwise - 0
permissions = permissions | EXECUTE  # 0011 | 1000 = 1011
print(f"After adding EXECUTE: {permissions:04b}")

permissions = permissions & ~WRITE  # 1011 & 1101 = 1001
# ~ operator inverts all bits so 0010 becomes 1101
print(f"After removing WRITE: {permissions:04b}")

print("Final permissions:")
print("READ:", READ)  # 1001 & 0001 = 0001 -> True
print("WRITE:", WRITE)  # 1001 & 0010 = 0000 -> False
print("DELETE:", DELETE)  # 1001 & 0100 = 0000 -> False
print("EXECUTE:", EXECUTE)  # 1001 & 1000 = 1000 -> True
