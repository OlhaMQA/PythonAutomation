# Task 1. Used: lists, 'while' loops, 'for' loops, list slicing, list append, sorted().
notes = []     # List to keep the future notes

while True:
    command = input('Введіть команду:').lower()  # A user enters a command. Transform the command to lowercase
    if command == 'add':
        notes.append(input('Введіть нотатку:'))  # Add new note to the notes list
    elif command == 'earliest':
        print('Від найстарішої до найновішої:')
        for note in notes:
            print(note)                    # Output: list of notes sorted by time added (the earliest first)
    elif command == 'latest':
        print('Від найновішої до найстарішої')
        for note in notes[::-1]:
            print(note)                    # Output: list of notes sorted by time added (the latest first)
    elif command == 'longest':
        print('Від найдовшої до найкоротшоЇ:')
        for note in sorted(notes, key=len, reverse=True):
            print(note)                    # Output: list of notes sorted by length (the longest first)
    elif command == 'shortest':
        print('Від найкоротшої до найдовшої:')
        for note in sorted(notes, key=len):
            print(note)                    # Output: list of notes sorted by length (the shortest first)
    elif command == 'exit':
        break                              # Exit the program
    else:
        print('Введіть одну з існуючих команд: '
              'add, earliest, latest, shortest, longest, exit')  # Validation if Command is not in the list

