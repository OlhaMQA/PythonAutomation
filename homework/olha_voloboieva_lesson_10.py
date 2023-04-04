a = [1, "1", 0, [1], print, {'t'}, (1, 2)]
b = [1, 2, 3, 4, 5, 6, 7, 8]
def all_errors (a):
    d = 0
    for i in range(9):
        try:
            c = b/a[i]
            print(f'success{c}')
        except TypeError:
            print('TypeError')
            continue
        except ValueError:
            print('ValueError')
            continue
        except IndexError:
            print('IndexError')
            continue
        except ZeroDivisionError:
            print('ZeroDivisionError')
            continue

all_errors(a)

import datetime, random

number = random.randint(1, 10)
today = datetime.date.today()
for i in range(1, number):
    delta = datetime.timedelta(days=i)
    print(f'{i} {"day" if i == 1 else "days"} ago it was {today-delta}')



