import pytest
from homework.lesson_27.infrastructure.people import PeopleService
from homework.lesson_27.entities.person_entity import People


@pytest.fixture(scope='session')
def people_service():
    yield PeopleService()


@pytest.fixture
def fifth_person():
    yield People(
        name='Leia Organa',
        height='150',
        mass='49',
        hair_color='brown',
        skin_color='light'
    )
