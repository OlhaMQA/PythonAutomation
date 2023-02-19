from math import pi

# Task 1
first_name = input("please, enter your first name:\n")
last_name = input("please, enter your last name:\n")
full_name = first_name + " " + last_name

print('You are: ' + full_name)
print('In Upper register: ' + full_name.upper())
print('In Lower register: ' + full_name.lower())
print('Each word capitalised: ' + full_name.title())
print('Five times in a row: '+(full_name + " ")*5)

first_name = "   \t\n   " + first_name + "   \t\n   "

print("Updated name with whitespaces: " + first_name)

first_name = first_name.strip()

print("Updated name stripped: " + first_name)

# Task 2

radius = float(input('Enter radius: '))

square = pi*radius**2
circuit = pi*radius*2

print(f'Square is: {round(square, 2)}\nCircuit is: {round(circuit, 2)}')

# Task 3

dollar_exchange_rate = 36.42
uah_amount = float(input('Enter amount: '))
usd_amount = round(uah_amount/dollar_exchange_rate, 2)

print(f'Поточний курс складає: {uah_amount} грн. = {usd_amount} доларів')
