# Task 1
import random

min = random.randrange(60)
quarter = 0

if min in range(15):
    quarter = 1
elif min in range(15, 30):
    quarter = 2
elif min in range(30, 45):
    quarter = 3
else:
    quarter = 4

print(f'{min} is in {quarter} quarter')


# Task 2
try:
    birth_month = int(input('В якому місяці ти народився (1-12): '))

    if 0 < birth_month <= 2 or birth_month == 12:
        print('За вікном падав сніг.')
    elif 3 <= birth_month <= 5:
        print('Все довкола розцвітало.')
    elif 6 <= birth_month <= 8:
        print('Діти насолоджувались літніми канікулами.')
    elif 9 <= birth_month <= 11:
        print('Все довкола загоралось яскравими фарбами.')
    else:
        print('Тільки цілі числа від 1 до 12')
except ValueError:
    print('Тільки цілі числа від 1 до 12')


# Task 3 - SOLUTION 1
number = random.randint(0, 999)

hundreds = number // 100
tens = (number % 100) // 10
ones = number % 10

digits_sum = hundreds + tens + ones

if digits_sum % 3 or ones % 2:
    print(f'Число {number} не ділиться на 6')
else:
    print(f'Число {number} ділиться на 6')


# Task 3 - SOLUTION 2
number_iterable = str(random.randint(0, 999))
digits_sum = sum([int(i) for i in number_iterable])

if digits_sum % 3 or int(number_iterable[-1]) % 2:
    print(f'Число {number_iterable} не ділиться на 6')
else:
    print(f'Число {number_iterable} ділиться на 6')


# Task 4
x = float(input('Enter x: '))
y = float(input('Enter y: '))

if x > 0 and y > 0:
    print(f'({x}, {y}) - I quadrant')
elif x > 0 and y < 0:
    print(f'({x}, {y}) - II quadrant')
elif x < 0 and y < 0:
    print(f'({x}, {y}) - III quadrant')
elif x < 0 and y > 0:
    print(f'({x}, {y}) - IV quadrant')
elif x == 0 and y == 0:
    print(f'({x}, {y}) - Origin!')
else:
    print(f'({x}, {y}) - On {"X" if x == 0 else "Y"}-axis')
