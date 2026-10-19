# dict = key -> value pairs. Keys are unique; order = insertion order.
my_dict = {1}
print(len(my_dict))  # number of keys

# d[key] = value adds a new key...
my_dict['key'] = 'value'
print(my_dict)  # {'key': 'value'}
my_dict['key2'] = 'value2'
print(my_dict)  # {'key': 'value', 'key2': 'value2'}

# ...or overwrites an existing one (never a duplicate key)
my_dict['key'] = 'value' * 5
print(my_dict)  # {'key': 'valuevaluevaluevaluevalue', 'key2': 'value2'}

# del removes a key (KeyError if missing)
del my_dict['key']
print(my_dict)  # {'key2': 'value2'}

# re-added key goes to the end, not its old spot
my_dict['key'] = 'value'
print(my_dict)  # {'key2': 'value2', 'key': 'value'}

# pop removes the key and returns its value
print(my_dict.pop('key'))  # value
print(my_dict)  # {'key2': 'value2'}

# d[key] raises KeyError if missing; d.get(key, default) returns default instead
print(my_dict["key2"])  # value2
print(my_dict.get("key", 0))  # 0, 'key' was popped


my_dict['key'] = 'value' * 5
print(my_dict)
del my_dict['key']
print(my_dict)
my_dict['key'] = 'value'
print(my_dict)

"'""..."""

for key, value in my_dict.items():
    print(f"{key}: {value}")

squares = {x ** 2 for x in range(10)}
squares2 = {x: x ** 2 for x in range(10)}
print (squares)
print(squares2)