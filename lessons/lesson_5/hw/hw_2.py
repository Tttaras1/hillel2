
# Завдання 1: очищення списку від дублікатів та аналіз логів (set)

day1_users = ["alice", "bob", "charlie", "david", "alice", "eva"]
day2_users = ["bob", "frank", "eva", "george", "charlie", "charlie"]

# 1.
set1 = set(day1_users)
set2 = set(day2_users)

# 2. 

print("Uniq users: ", set1 | set2)

# 3.

print("Users visited in both days: ", set1 & set2)

# 4.

print("Users visited in first day: ", set1 - set2)

# Завдання 2: Пошук унікальних замовлень без урахування порядку (frozenset)

orders = [
    ["хліб", "молоко"],
    ["молоко", "хліб"],
    ["сік", "хліб"],
    ["хліб", "молоко"]
]

unique_orders = {frozenset(order) for order in orders}

print("Unique orders: ", len(unique_orders))

# Завдання 3: групування за категоріями (defaultdict)

from collections import defaultdict

orders_data = [
    ("Електроніка", "Ноутбук"),
    ("Їжа", "Яблуко"),
    ("Електроніка", "Смартфон"),
    ("Їжа", "Хліб"),
    ("Одяг", "Сорочка"),
    ("Їжа", "Молоко")
]

grouped = defaultdict(list)

for category, product in orders_data:
    grouped[category].append(product)

print(grouped)

# Завдання 4: аналіз частоти слів у тексті (Counter)
from collections import Counter

text = "python python java python c++ java python c++ javascript"

programming_languages_count = Counter(text.split(' '))

print("Languages in total: ", programming_languages_count)
print("Most common languages: ", programming_languages_count.most_common(2))
# OR
print("Most common languages without counting: ", [name for name, _ in programming_languages_count.most_common(2)])

# Завдання 5: налаштування програми з декількох джерел (ChainMap)

from collections import ChainMap

default_config = {"theme": "light", "language": "uk", "font_size": 12}
user_config = {"theme": "dark", "font_size": 16}

resulting_config = ChainMap(user_config, default_config)

print("User configuration: ", resulting_config)
print("Users theme: ", resulting_config['theme'])
print("Users font: ", resulting_config['font_size'])
print("Users language: ", resulting_config['language'])

# Завдання 6: робота з порядком та керування елементами (OrderedDict)

from collections import OrderedDict

data = OrderedDict([("a", 1), ("b", 2), ("c", 3), ("d", 4)])

data.move_to_end("a")
print(data)

first_item = data.popitem(last=False)

print("Deleted first key: ", first_item)
print("Keys left: ", list(data.keys())) 