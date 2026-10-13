menu_text = """
1 — Вивести привітання
2 — Показати числа від 1 до 10
3 — Обчислити суму від 1 до N
0 — Вихід
"""
while True:
    print(menu_text)

    typed_text = input("Type in your command: ").strip()
    match typed_text:
        case '0':
            print('Exit')
            break
        case '1':
            print('Hello world!')
        case '2':
            print('Numbers from 1 to 10: ', end = ' ')
            for n in range(1, 11):
                print(n, end = ' ')
            print('\n')
        case '3':
            summarise_to = int(input('Type in value you would like to summarise to: '))
            temp = 0
            for n in range(1, int(summarise_to) + 1):
                temp += n
            print(f"Summ from 1 to typed number: {temp}")
        case _:
            print('Unknown command')
