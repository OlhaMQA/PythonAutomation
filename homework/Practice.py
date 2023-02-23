num = input('Enter number: ')

user_nums = []

while num != 'sum':
    try:
        user_nums.append(float(num))
        num = input('Enter number: ')
    except ValueError:
        print('Enter valid number or "sum"')
        num = input('Enter number: ')
        continue

print(sum(user_nums))