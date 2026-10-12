# Why the order of conditions matters:
# elif stops at the first true condition, so the conditions are checked top to bottom.
# 1. The range check goes first. Otherwise 150 would match `score >= 90` and get A, and -5 would fall through to else and get F.
# 2. Grade goes from highest to lowest, so each branch only needs a lower bound: reaching `elif score >= 80` already means the score is below 90.
# If `score >= 60` came first, 95 would match it and get D.

scores = [0, 59, 60, 69, 70, 79, 80, 89, 90, 100, -1, 101]

for score in scores:
    if score < 0 or score > 100:
        print(f"{score}: score should be between 0 and 100")
    elif score >= 90:
        print(f"{score}: A")
    elif score >= 80:
        print(f"{score}: B")
    elif score >= 70:
        print(f"{score}: C")
    elif score >= 60:
        print(f"{score}: D")
    else:
        print(f"{score}: F")
