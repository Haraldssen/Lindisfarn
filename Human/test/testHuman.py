import pytest
from Human.Human import Human
from Human.Woman import Woman

human = Human()
woman = Woman(Human)


@pytest.fixture()
def sex():
    return human.sex

def test_sex(sex):
    assert sex == 'male'

@pytest.fixture()
def sex2():
    return woman.sex

def test_sex2(sex2):
    assert sex2 == 'female'


@pytest.fixture()
def money():
    return human.money

def test_money(money):
    assert money == 0


'''
class TestHuman:

    def setup_class(self):
        print('выворачивай карманы')

    def teardown_class(self):
        print('не суйся больше в наш район')

@pytest.mark.parametrize()
    def money(Human):
        assert money > 0
'''