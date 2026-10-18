
# my_var = b'abc'
# print(type(my_var))
# my_var = my_var.decode()
# print(my_var)
# print(type(my_var))
# my_var = my_var.encode()
# print(my_var)
# print(type(my_var))



# # ---------

# my_list = [1, 1.5, "123", (1,2,3), [1,2,3]]
# print(my_list)
# print(len(my_list))
# my_list.extend("add")
# print(my_list)
# print(len(my_list))
# my_list.insert(-1, "add2")
# my_list.insert(99, "add2")
# print(my_list)
# print(len(my_list))
      
# # --------

# my_list.remove(1.5)
# print(my_list)
# print(len(my_list))


# my_tuple = tuple(range(10))
# print(my_tuple, my_tuple[::-1])


grades = []
sum_of_grades = 0

for n in range(0, 10):
    grades.append(int(input('Type in your numbers: ')))

for grade in grades:
    sum_of_grades += grade


print(f"Mean grade: {sum_of_grades / len(grades)}")


from collections import namedtuple
user_tuple = ("Олексій", 25, "Київ")
print(f"Ім'я: {user_tuple[0]}, Місто: {user_tuple[2]}")

User = namedtuple('User', ['name', 'age', 'city'])
user_named = User(name="Олексій", age=25, city="Київ")
print(f"IM'я: {user_named.name}, Mico: {user_named.city}")
print(f"Вік за індексом: {user_named[1]}")