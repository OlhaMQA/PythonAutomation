import random

# Task 1
numbers_1 = [1, 2, 3, 4, 5, 5, 8, 9, 6.11, 6]               # 1st List of numbers given
numbers_2 = [1, 6.11, 6, 8, 6, 0, -6, 4.6, 3, 4, 7]         # 2nd List of numbers given

common_numbers = list(set(numbers_1).intersection(set(numbers_2)))      # List of common numbers of two given lists

for number in sorted(common_numbers):
    print(number)                                                       # Output: numbers common for both lists

# Task 2
students_score = {                                                      # Dictionary with students' names and scores
    'Petro': 10,
    'Anna': 15,
    'Ivan': 2,
    'Max': 6.5
}

average = sum(students_score.values())/len(students_score)      # Calculation of an average score of the class

for student in students_score:
    if students_score[student] > average:
        print(student)                            # Output: Names of the students, whose score is greater than average

# Task 3
numbers_list = random.choices(range(11), k=10)    # List of 10 elements, containing randomly generated numbers 0-10

print(numbers_list)                               # Output: Numbers List printed for visibility
print(f'Кількість різних значень: {len(set(numbers_list))}')       # Output: Quantity of unique values

# Task 4
# User enters 2 lists of numbers separated by whitespaces, which are split and transformed to sets
user_numbers_1 = set(input('Enter a first list of numbers, separated by whitespace: ').split())
user_numbers_2 = set(input('Enter a second list of numbers, separated by whitespace: ').split())

# List of common numbers of 2 sets, sorted by ascending
common_list = sorted(list(user_numbers_1.intersection(user_numbers_2)))

print('Common numbers of your lists are: ', end='')   # Description of output printed
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