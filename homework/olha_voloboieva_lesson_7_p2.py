from random import choice, randint, sample
from string import ascii_lowercase


def create_email(domains_list, names_list) -> str:
    """Generates email in specified format. Names and Domains are lists of strings.
Returns an email string"""

    name = choice(names_list).lower()                                   # Selects random name from the list
    number = randint(100, 999)                                          # Selects a random number
    random_string = ''.join(sample(ascii_lowercase, randint(5, 7)))     # Selects 5-7 random letters from a to z
    domain = choice(domains_list)                                       # Selects random domain name from the list

    return f'{name}.{number}@{random_string}.{domain}'                  # Returns an email composed of the choices


names = ['Test', 'name', 'John', 'Mary', 'Anna', 'hillel']
domains = ['com', 'ua', 'ch', 'org', 'gov']

email = create_email(domains, names)
print(email)
