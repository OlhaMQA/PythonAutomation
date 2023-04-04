import re

def get_domains_list(filename):                 # reads the file with domain names
    with open(filename, 'r') as file:              # removes the dots from each line and adds the rest to the list
        domains = [line.strip().replace('.', '') for line in file]
    return domains                          # Returns the list of domains


def get_surnames_list(filename):            # reads the file, splits each line in two parts: Name and Surname
    with open(filename, 'r') as file:
        surnames = [line.split()[1] for line in file]       # adds all the Surnames to the list
    return surnames                             # returns the list of surnames


def get_dates_list(filename):           # Finds all the valid dates in the file and returns them in dictionaries
    with open(filename, 'r') as file:      # reads a file provided
        dates = []
        for line in file:
            date = re.search(r'\b\d+(st|nd|rd|th)\s+\w+\s+\d{4}\b', line)   # Checks if there are matches to regexp
            if date:                      # creates a new dictionary with 1 key 'date' and value = found regexp match
                dates.append({"date": date.group()})                        # and value = found regexp match
    return dates                                                  # returns the list of dictionaries

# Test
print(get_domains_list('domains.txt'))
print(get_surnames_list('names.txt'))
print(get_dates_list('authors.txt'))