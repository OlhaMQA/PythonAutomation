from random import choice, randint, sample
from string import ascii_lowercase


def create_email(domains_list, names_list):
    """Generates email in specified format. Names and Domains are lists of strings.
Returns an email string"""

    name = choice(names_list)
    number = randint(100, 999)
    random_string = ''.join(sample(ascii_lowercase, randint(5, 7)))
    domain = choice(domains_list)

    return f'{name}.{number}@{random_string}.{domain}'


names = ['Test', 'name', 'John', 'Mary', 'Anna', 'hillel']
domains = ['com', 'ua', 'ch', 'org', 'gov']

email = create_email(domains, names)
print(email)
