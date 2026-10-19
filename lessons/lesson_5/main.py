# Set = unordered collection of unique items. Both sets share 5, 7, 9:
#
#   ┌─ A ─────────────────┐
#   │             ┌───────┼────── B ─────┐
#   │    3  10    │ 5 7 9 │              │
#   │             │       │     6  8     │
#   └─────────────┼───────┘              │
#                 └──────────────────────┘
#
# ░ in the pictures below = what the operation returns.
A = {3, 5, 7, 9, 10}
B = {5, 6, 7, 8, 9}
print(A, B)

# Intersection: items in A AND in B -> {5, 7, 9}
#
#   ┌─ A ─────────────────┐
#   │             ┌───────┼────── B ─────┐
#   │    3  10    │░5 7 9░│              │
#   │             │░░░░░░░│     6  8     │
#   └─────────────┼───────┘              │
#                 └──────────────────────┘
#
print('A & B: ')
print(A & B)
print(A.intersection(B))

# Union: items in A OR in B (or both); duplicates kept once -> {3, 5, 6, 7, 8, 9, 10}
#
#   ┌─ A ─────────────────┐
#   │░░░░░░░░░░░░░┌───────┼────── B ─────┐
#   │░░░░3  10░░░░│░5 7 9░│░░░░░░░░░░░░░░│
#   │░░░░░░░░░░░░░│░░░░░░░│░░░░░6  8░░░░░│
#   └─────────────┼───────┘░░░░░░░░░░░░░░│
#                 └──────────────────────┘
#
print('A | B: ')
print(A | B)
print(A.union(B))

# Difference: items in A that are NOT in B -> {3, 10}
#
#   ┌─ A ─────────────────┐
#   │░░░░░░░░░░░░░┌───────┼────── B ─────┐
#   │░░░░3  10░░░░│ 5 7 9 │              │
#   │░░░░░░░░░░░░░│       │     6  8     │
#   └─────────────┼───────┘              │
#                 └──────────────────────┘
#
print('A - B:')
print(A - B)
print(A.difference(B))

# Order matters: B - A keeps B's own items -> {6, 8}
#
#   ┌─ A ─────────────────┐
#   │             ┌───────┼────── B ─────┐
#   │    3  10    │ 5 7 9 │░░░░░░░░░░░░░░│
#   │             │       │░░░░░6  8░░░░░│
#   └─────────────┼───────┘░░░░░░░░░░░░░░│
#                 └──────────────────────┘
#
print('B - A:')
print(B - A)
print(B.difference(A))

# Symmetric difference: items in exactly one set (everything except the overlap)
# -> {3, 6, 8, 10}. Two ways to build it by hand:
#   (A | B) - (A & B)  = everything, minus the middle
#   (A - B) | (B - A)  = left part + right part
#
#   ┌─ A ─────────────────┐
#   │░░░░░░░░░░░░░┌───────┼────── B ─────┐
#   │░░░░3  10░░░░│ 5 7 9 │░░░░░░░░░░░░░░│
#   │░░░░░░░░░░░░░│       │░░░░░6  8░░░░░│
#   └─────────────┼───────┘░░░░░░░░░░░░░░│
#                 └──────────────────────┘
#
print((A | B) - (A & B))
print((A - B) | (B - A))

# Built-in shortcut for the same thing -> {3, 6, 8, 10}
print(A ^ B)
print(A.symmetric_difference(B))

# Dictionary
print('-')

my_var = {}
print(my_var)
print(type(my_var))


my_frozen_set = frozenset([1, 5, 10])
print(my_frozen_set)
print(type(my_frozen_set))
my_frozen_set.add(2) 
print(my_frozen_set)