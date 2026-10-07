# Завдання 3.3. Обробка профілю користувача (методи рядків)
import string;

def process_name(typed_name):
    stripped_str = typed_name.strip()
    capped_str = string.capwords(stripped_str)
    surname_entry = capped_str.find(" ")
    display_name = capped_str if surname_entry == -1 else f"{capped_str[:surname_entry].strip()} {capped_str[surname_entry + 1:].strip()}"
    print(f"Вітаємо у системі, {display_name}! Профіль активовано!")

process_name(input('Type in your name: '))