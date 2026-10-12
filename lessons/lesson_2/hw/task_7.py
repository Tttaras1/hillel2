print(True and False)
# False because of how and works ( it expects both truthy values)
print(True & False)
 # 1 & 0 -> 0 -> False

print(5 and 3)
# 3 -> and returns first falsy value or last true
print(5 & 3)
# 0101 & 0011 => 0001 => 1

print(0 or 7)
# 7 -> or returns last false or first true value
print(0 | 7)
# 0000 | 0111 => 0111 => 7

print(4 or 2)
# 4 # 4 -> or returns the first truthy value
print(4 | 2)
# 0100 | 0010 => 0110 => 6