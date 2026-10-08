# Завдання 3.2. Перевірка доступу (логічні операції)
age = int(input('Type in your age: '))
is_student = 'yes' == input('Are you a student? ( yes/no )').lower().strip()
discount_allowed = is_student and age < 25 or not (18 < age < 60)
if discount_allowed:
    print('You are allowed to get 25% discount')
else: 
    print('Unfortunately we can\'t provide you a discount')
