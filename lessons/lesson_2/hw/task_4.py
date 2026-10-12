age = 21
is_authenticated = True
is_blocked = False
has_permission = True

# age, is_authenticated, is_blocked, has_permission = 21, False, False, True  # not authenticated
# age, is_authenticated, is_blocked, has_permission = 21, True, True, True  # blocked
# age, is_authenticated, is_blocked, has_permission = 17, True, False, True  # under 18
# age, is_authenticated, is_blocked, has_permission = 21, True, False, False  # no permission
# age, is_authenticated, is_blocked, has_permission = 18, True, False, True  # exactly 18
# age, is_authenticated, is_blocked, has_permission = 16, False, True, False  # all fail

access_granted = is_authenticated and not is_blocked and age >= 18 and has_permission
if access_granted:
    print("Successfully logged in")
elif not is_authenticated:
    print("User is not authenticated")
elif is_blocked:
    print("User is blocked")
elif age < 18:
    print("Access restricted for users under 18")
elif not has_permission:
    print("User doesn't have permission to access this page")
