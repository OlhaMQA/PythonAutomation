# Task 1
import random

min = random.randrange(60)
quater = 0

if min in range(15):
    quater = 1
elif min in range(15, 30):
    quater = 2
elif min in range(30, 45):
    quater = 3
else:
    quater = 4

print(f'{min} is in {quater} quater')


# Task 2
try:
    birth_month = int(input('В якому місяці ти народився (1-12): '))

    if birth_month > 0 and birth_month <= 2 or birth_month == 12:
        print('За вікном падав сніг.')
    elif birth_month >=3 and birth_month <= 5:
        print('Все довкола розцвітало.')
    elif birth_month >=6 and birth_month <= 8:
        print('Діти насолоджувались літніми канікулами.')
    elif birth_month >=9 and birth_month <= 11:
        print('Все довкола загоралось яскравими фарбами.')
    else:
        print('Введи число від 1 до 12')

except ValueError:
    print('Тільки цілі числа від 1 до 12')


# Task 3
number = random.randint(0, 999)

hundreds = number // 100
tens = (number % 100) // 10
ones = number % 10

sum = hundreds + tens + ones

if not sum % 3 and not number % 2:
    print(f'Число {number} ділиться на 6')
else:
    print(f'Число {number} не ділиться на 6')


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










