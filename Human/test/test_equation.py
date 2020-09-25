import pytest
from formulaEquation import Equation

class TestEquation:

    def setup_class(self):
        self.equal=Equation()
        print('инициализация для класса')

    def teardown_class(self):
        print('деинициализация для класса')

    @pytest.mark.parametrize("a, b, c, answer", [(4, 6, 2, (-0.5, -1.0)), (8, 12, 4, (-0.5, -1.0))])
    def test_line(self, a, b, c, answer):
        assert self.equal.square(a, b, c) == answer