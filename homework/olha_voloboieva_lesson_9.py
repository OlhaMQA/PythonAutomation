import re


# Task 1
def check_string(string):           # Checks if string matches the pattern A-Za-z0-9_
    return bool(re.fullmatch(r'\w*', string))


# Task 2
def remove_text_in_parentheses(strings):        # Removes any text in parentheses together with them
    result = []

    for el in strings:      # Replace text matching the pattern '(any text)' by '' and add it to list
        result.append(re.sub(r'\(.*\)', '', el))

    return result           # returns a list of updated strings


# Task 3
def add_space(text_string):     # Adds a space before each uppercase letter and returns an updated string
    return re.sub(r'([A-Z])', r' \1', text_string)
