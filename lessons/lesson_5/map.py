from collections import ChainMap
from collections import defaultdict

# defaults = {"theme": "light", "sidebar": True}
# user_settings = {"theme": "dark"}

# resulting_config = ChainMap(user_settings, defaults)
# print(resulting_config["theme"])
# print(resulting_config["sidebar"])
# print(resulting_config)
# my_config = defaults.copy()
# my_config.update(user_settings)
# print(my_config)


my_dict = defaultdict(list)

while True:
    print("Type in your command. 1 - Get current dict, 2 - take a book, 3 - Remove a book, 4 exit")
    command = int(input("Type in your command: "))

    match command:
        case 1:
            print(my_dict)
        case 2:
            surname = input("Type in authors surname: ")
            book_name = input("Type in book name: ")
            
            my_dict[surname].append(book_name)
        case 3:
            surname = input("Type in authors surname: ")
            book_name = input("Type in book name: ")

            if my_dict[surname]:
                my_dict[surname].remove(book_name)
            else:
                print("Book is not found!")
        case 4:
            break
        case _:
            print("Unknown command")
