import csv
from homework.lesson_21.CSV_add_remove import csv_add_remove


def test_add_row_to_csv():
    csv_add_remove.add_row_to_csv('example.csv', ['John', 'Doe', '50', 'Male', '5000'])
    with open('example.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert rows[-1] == ['John', 'Doe', '50', 'Male', '5000']


def test_remove_row_from_csv():
    with open('example.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    csv_add_remove.remove_last_row_from_csv('example.csv')

    with open('example.csv', 'r') as file:
        reader = csv.reader(file)
        rows_upd = list(reader)

    assert rows_upd == rows[:-1]