import requests
from homework.lesson_27.app import config

class PeopleService:

    def __init__(self):
        self.__people_url = f"{config['host']}/people"


    def get_person(self, person_id):
        response = requests.get(f"{self.__people_url}/{person_id}")
        return response

