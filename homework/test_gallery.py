import pytest
from olha_voloboieva_lesson_17 import Painting, Sculpture


@pytest.fixture
def painting():
    return Painting()


@pytest.fixture
def sculpture():
    return Sculpture()


@pytest.mark.parametrize('obj', ['painting', 'sculpture'])
def test_show(obj, request):
    obj = request.getfixturevalue(obj)
    seen_before = obj.seen
    obj.show(1)
    seen_after = obj.seen
    assert seen_after - seen_before == 1


@pytest.mark.painting
def test_sell(painting, buyer='test buyer'):
    painting.price = 10
    assert round(painting.sell(buyer), 1) == 16


@pytest.mark.sculpture
def test_broke_part_naming(sculpture):
    part = sculpture.broke()
    assert part.name == 'Part of unknown'


@pytest.mark.sculpture
def test_broke_sculpture_naming(sculpture):
    sculpture.broke()
    assert sculpture.name == 'unknown Broken'


@pytest.mark.sculpture
def test_broke_sculpture_price(sculpture):
    sculpture.price = 100
    sculpture.broke()
    assert sculpture.price == 200
