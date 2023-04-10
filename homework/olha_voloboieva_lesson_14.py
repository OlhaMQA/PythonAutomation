import random

# Decorator prints function name as soon as it is called
def func_name_print(func):
    def print_name(*args, **kwargs):
        func(*args, **kwargs)
        print(func.__name__)
    return print_name

# 3 functions to use the decorator on
@func_name_print
def add_one(number):
    return number + 1


@func_name_print
def add_two(number):
    return number + 2


@func_name_print
def complex_math(number_1, number_2):
    a = ((number_1 + number_2)**4)/(number_2**number_1)
    return a

'''
# call functions to demonstrate the decorator

add_two(10)
add_one(1)
complex_math(1, 1)
'''

# List comprehension task

list_of_integers = [random.randint(1, 10) for i in range(100)]               # List of 100 elements
count_elements = {k: list_of_integers.count(k) for k in list_of_integers}   # dictionary with each element's count

print(list_of_integers)
print(count_elements)
