import pytest
from homework.lesson_27.entities.person_entity import People


@pytest.mark.parametrize('keyword, value', [('name', 'Luke Skywalker'), ('mass', '77'), ('height', '172')])
def test_person_1(people_service, keyword, value):
    response = people_service.get_person(1).json()
    assert response[keyword] == value


def test_check_person(people_service, fifth_person):
    response = people_service.get_person(5)
    actual_leia_organa = People(
        response.json()['name'],
        response.json()['height'],
        response.json()['mass'],
        response.json()['hair_color'],
        response.json()['skin_color']
    )
    assert actual_leia_organa == fifth_person
