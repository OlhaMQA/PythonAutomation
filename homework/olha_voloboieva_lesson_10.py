import datetime


# Exception
def division_func(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Division by 0 is Not allowed')
        return 'n/a'


# Console output of exception
division_func(20, 0)


# Date
def calculate_date(date, days, boolean):
    delta = datetime.timedelta(days=days)
    new_date = date + (delta if boolean else delta*(-1))
    return new_date


date_today = datetime.datetime.now()

yesterday = calculate_date(date_today, 1, False)
tomorrow = calculate_date(date_today, 1, True)

print(f'Yesterday was {yesterday}')
print(f'Tomorrow will be {tomorrow}')


# Birthday
def calculate_age(birthdate):
    age_in_days = (datetime.datetime.today() - birthdate).days
    birth_timestamp = datetime.datetime.timestamp(birthdate)
    return age_in_days, birth_timestamp


my_age, my_birth_timestamp = calculate_age(datetime.datetime(1991, 9, 18, 9, 16, 00, 000))

print(f'I\'m {my_age} days old')
print(f'Timestamp of my birthday is {my_birth_timestamp}')







