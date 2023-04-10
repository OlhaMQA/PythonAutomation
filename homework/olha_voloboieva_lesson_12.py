import datetime


# Exception handling
def division_func(a, b):
    try:                                        # Try to divide the numbers, return the result
        return a/b
    except ZeroDivisionError:                   # if ZeroDivisionError is raised, return 'n/a' and print error text
        print('Division by 0 is Not allowed')
        return 'n/a'


# Console output of exception handling
division_func(20, 0)


# Date calculation
def calculate_date(date, days, boolean):
    delta = datetime.timedelta(days=days)                # Create delta from the days
    # Calculate new date: add delta if boolean = True, otherwise - subtract
    new_date = date + (delta if boolean else delta*(-1))
    return new_date                                     # Return new date


# Date calculation demonstration
date_today = datetime.datetime.now()

yesterday = calculate_date(date_today, 1, False)
tomorrow = calculate_date(date_today, 1, True)

print(f'Yesterday was {yesterday}')
print(f'Tomorrow will be {tomorrow}')


# Calculate exact age by birthdate
def calculate_age(birthdate):
    age_in_days = (datetime.datetime.today() - birthdate).days          # calculate age in days
    birth_timestamp = datetime.datetime.timestamp(birthdate)            # find the timestamp of birthday
    return age_in_days, birth_timestamp

# Demonstration of age calculation (return age and timestamp)
my_age, my_birth_timestamp = calculate_age(datetime.datetime(1991, 9, 18, 9, 16, 00, 000))

print(f'I\'m {my_age} days old')
print(f'Timestamp of my birthday is {my_birth_timestamp}')
