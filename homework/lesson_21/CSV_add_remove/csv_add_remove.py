import csv


def add_row_to_csv(csv_file, row_data):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row_data)


def remove_last_row_from_csv(csv_file):
    rows = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows[:-1])

