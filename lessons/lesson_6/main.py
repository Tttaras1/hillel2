# # Legb rule
# # Local Enclosing Global Built it

# # • We can't definte variable After it was used
# def test_func():
#     # global my_var | For using my_var from global env. With that approach we can redefine it in a function
#     my_var = 20
#     print(my_var)

# my_var = 10
# test_func()


def test_func(*args):
    print(type(args))
    print(args)

test_func(1,2,3,4,5,6,7,8,9,0)

# def test_func2(**kwargs):
#     print(type(kwargs))
#     print(kwargs)

# test_func2(side_1 = 1, side_2 = 2, side_3 = 3, side_4 = 4)

from statistics import mean


def average_score(*scores):
    return mean(scores)


def average_score2(*scores):
    return sum(scores) / len(scores)


print(average_score(5, 6, 4, 7, 4, 3, 8))
print(average_score2(5, 6, 4, 7, 4, 3, 8))
