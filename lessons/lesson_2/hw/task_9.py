temperatures = [-10, -1, 0, 5, 25]

# Incomplete branching
for t in temperatures:
    if t < 0: 
        print(f"{t}C is below zero")

print('\n -------- \n')

# Complete branching
for t in temperatures:
    if t < 0: 
        print(f"f{t}C is below zero")
    else:
        print("It's ok")

# Complete branching - covers both cases, incomplete branching - covers only true condition, otherwise - nothing