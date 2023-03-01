import random

# Task 1
numbers_1 = random.choices(range(11), k=10)               # 1st List of numbers generated
numbers_2 = random.choices(range(11), k=10)               # 2nd List of numbers generated
print(f'List 1: {numbers_1}\nList 2: {numbers_2}')        # Given lists printed for visibility

common_numbers = list(set(numbers_1).intersection(set(numbers_2)))      # List of common numbers of two lists

print('Common numbers: ')
for number in sorted(common_numbers):
    print(number)                                      # Output: common numbers of both lists, sorted by asc

# Task 2
students_score = {                                                      # Dictionary with students' names and scores
    'Petro': 10,
    'Anna': 15,
    'Ivan': 2,
    'Max': 6.5
}

average = sum(students_score.values())/len(students_score)      # Calculation of an average score of the class

print(f'Average score is {average}\nStudents exceeding the average score:')   # Description printed for visibility
for student in students_score:
    if students_score[student] > average:
        print(student)                            # Output: Names of the students, whose score is greater than average

# Task 3
numbers_list = random.choices(range(11), k=10)    # List of 10 elements, containing randomly generated numbers 0-10

print(numbers_list)                               # Output: Numbers List printed for visibility
print(f'Кількість унікальних значень: {len(set(numbers_list))}')       # Output: Quantity of unique values

# Task 4
# 2 lists of 10 elements, containing randomly generated numbers 0-10
user_numbers_1 = random.choices(range(11), k=10)
user_numbers_2 = random.choices(range(11), k=10)

# List of common numbers of 2 sets, sorted by asc
common_list = sorted(list(set(user_numbers_1).intersection(set(user_numbers_2))))

print(f'List 1: {user_numbers_1}\nList 2: {user_numbers_2}\nCommon numbers:')      # Given lists printed for visibility
for element in common_list:
    print(int(element), end=' ')                      # Common numbers printed in the same line
print()                                               # Empty string printed to separate the next task

# Task 5
text = 'one two three one four five seven ten seven one'            # String of text given
words_count = {}                                                    # Dictionary to keep the words and their count

for word in text.split():
    words_count[word] = text.split().count(word)                    # Fill the dictionary with pairs (word: count)

for item in words_count.items():
    print(item, end=' ')                                            # Print the (word: count) pairs in the same line
