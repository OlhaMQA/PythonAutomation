import csv
import json


class JSONtoCSVAdapter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename: str):
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            self.__lines = data

    def write_file(self, filename: str):
        with open(filename, 'w', newline='') as csv_file:
            fieldnames = self.__lines[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(self.__lines)

    def cleanup(self):
        self.__lines = []


# Використання адаптера для конвертації JSON в CSV
adapter = JSONtoCSVAdapter()
adapter.read_file('example.json')
adapter.write_file('example.csv')