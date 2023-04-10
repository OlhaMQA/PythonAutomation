import csv


def open_csv(name):                         # Reads csv file, returns the list of rows
    with open(name, 'r') as file:           # Вона приймає назву файлу(str), повертає список рядків(list).
        reader = csv.reader(file)
        result = [el for el in reader]
        return result


def populate_csv(name, rows):               # Populate csv file with the rows provided
    with open(name, 'w') as file:           # Вона приймає назву файлу(str), список рядків(list),
        writer = csv.writer(file)           # які треба записать в файл. Нічого не повертає.
        for row in rows:
            writer.writerow(row)


'''
# Demonstration
initial_content = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
additional_content = [[10, 11, 12], [13, 14, 15]]

populate_csv('1.csv', initial_content)      # за допомогою створених функцій спочатку створюємо файл(3 рядків достатньо)
opened_content = open_csv('1.csv')          # потім читаємо той-же файл, записавши рядки в змінну

for el in additional_content:
    opened_content.append(el)               # потім додаємо два рядки в змінну

populate_csv('2.csv', opened_content)       # і після цього записуємо наші зміни в інший файл.
'''

# Genarates squares of all numbers from 0 to 100000
def squares_gen():
    for i in range(100001):
        yield i ** 2


''' 
# Demonstration

squares = squares_gen()             # generator

while True:
    try:
        print(next(squares))        # print all the squares one by one
    except StopIteration:
        print('Done!')              # as aoon as 100000 iteration is reached, break the cycle with a message
        break
'''









