import pytest
from Human import Human

class TestHuman:

    def setup_class(self):
        print('выворачивай карманы')

    def teardown_class(self):
        print('не суйся больше в наш район')

    @pytest.mark.parametrize("money", [()])
    def test_line(self, money):
        assert self.money() => 0