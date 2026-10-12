# Рівень 1. Логічний тип даних та логічні вирази
# Завдання 1. Визначення результатів виразів

print(10 > 5) # True
print(10 == 5) # False
print(7 != 3) # True
print(12 <= 12) # True
print(15 < 10) # False

print(True and False) # False
print(True or False) # True
print(not True) # False
print(not False) # True

print(5 > 3 and 10 < 20) # True
print(5 > 3 and 10 > 20) # False
print(5 < 3 or 10 < 20) # True
print(not (5 > 3)) # False
print(5 > 3 or 10 / 0 > 1) # True

print(0 or 15) # 15
print(10 and 20) # 20
print("" or "Python") # Python
print([] and [1, 2, 3]) # []

1. Чому останні чотири вирази не обов'язково повертають True або False?
    • Вони повертають одне зі значень, вони не конвертують це значення в Boolean; В python [] репрезентує falsy значення
2. Чому останній вираз із діленням на нуль не викликає помилку?
    • До нього код просто не доходить так як одразу повертає 5>3 що є True. Якби було 5<3 то була би поимлка 
3. Які вирази використовують коротке замикання?
    • or, and, not; or - якщо зустрічається truthy то далі виконання не йде; and - те саме але з Falsy значенням;
        not - в свою чергу завжди виконується так як йому треба "перевернути" значення. Результат завжди True or False
4. Чим відрізняються and та or за поведінкою?
    • and виконується до першого False, or до першого True

# Завдання 2. Таблиці істинності

1 + 2 ( A and B, A or B)
[A, B] [AND, OR]
[0, 0] [ 0 ,  0]
[0, 1] [ 0 ,  1]
[1, 0] [ 0 ,  1]
[1, 1] [ 1 ,  1]

3 ( not A )
[A] [not]
[0] [1]
[1] [0]

4 ( not A and B )
[A, B] []
[0, 0] [0]
[0, 1] [1]
[1, 0] [0]
[1, 1] [0]

5 (A or B) and not A

0,0 -> (0 or 0) and not 0 -> 0 and not 0 -> 0 and 1 -> 0
0,1 -> (0 or 1) and not 0 -> 1 and not 0 -> 1 and 1 -> 1
1,0 -> (1 or 0) and not 1 -> 1 and not 1 -> 1 and 0 -> 0
1,1 -> (1 or 1) and not 1 -> 1 and not 1 -> 1 and 0 -> 0

[A, B]
[0, 0] [0]
[0, 1] [1]
[1, 0] [0]
[1, 1] [0]


6 ( not (A and B) )
[A, B]
[0, 0] [1]
[0, 1] [1]
[1, 0] [1]
[1, 1] [0]

7 ( (A and B) or C )
[A, B, C]
[0, 0, 0] [ 0 ]
[0, 0, 1] [ 1 ]
[0, 1, 0] [ 0 ]
[0, 1, 1] [ 1 ]
[1, 0, 0] [ 0 ]
[1, 0, 1] [ 1 ]
[1, 1, 0] [ 1 ]
[1, 1, 1] [ 1 ]

Завдання 3. Істинність об'єктів
values = [
    0,
    1,
    -1,
    0.0,
    "",
    "0",
    [],
    [0],
    (),
    (0,),
    {},
    {"x": None},
    None,
    False,
    True
]

for value in values:
    print(repr(value), bool(value))

0 False
1 True
-1 True
0.0 False
'' False
'0' True
[] False
[0] True
() False
(0,) True
{} False
{'x': None} True
None False
False False
True True

