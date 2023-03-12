from functools import reduce


# Напишіть програму на Python для знаходження перетину двох заданих масивів за допомогою лямбда.
test_array = [1, 2, 3, 4, 5, 6, 7, 8]
test_array_2 = [2, 4, 6, 8, 10]

intersection = filter(lambda x: x in test_array, test_array_2)  # Filters the digits present in both lists

print(list(intersection))           # [2, 4, 6, 8]

# Напишіть програму на Python, щоб перевірити, чи є заданий рядок числом, за допомогою лямбда
test_string = input('Enter a digit: ')

is_number = lambda x: x.isdigit()       # Checks if the string is digit

print(is_number(test_string))           # True

# Напишіть програму на Python, щоб знайти список із максимальною та мінімальною довжиною за допомогою лямбда.
test_array_3 = [[1, 2, 3], [2], [2, 3], [3, 4, 0, 0], []]

minimal_len = list(reduce(lambda x, y: x if len(x) < len(y) else y, test_array_3))    # Finds the shortest list

maximal_len = list(reduce(lambda x, y: x if len(x) > len(y) else y, test_array_3))    # Finds the longest list

print(f'longest - {maximal_len}')           # longest - [3, 4, 0, 0]
print(f'shortest - {minimal_len}')          # shortest - []

# Напишіть програму на Python для обчислення добутку заданого списку чисел за допомогою лямбда.
test_array_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

product = int(reduce(lambda x, y: x*y, test_array_4))       # Multiplies all numbers in the list

print(product)
