from TestareUnitara.calc import mini_calc
from TestareUnitara.calc.mini_calc import MiniCalc


class TestMiniCalc:

    def setup_method(self):
        self.calculator = MiniCalc()

    def tear_down(self):
        print("Am terminat de executat instructiunile")

    def test_adunare(self):
        assert self.calculator.adunare(5, 5) == 10, 'Adunarea nu functioneaza corect'

    def test_scadere(self):
        assert self.calculator.scadere(5, 5) == 0, 'Scaderea nu functioneaza corect'

    def test_inmultire(self):
        assert self.calculator.inmultire(5, 5) == 25, 'Inmultirea nu functioneaza corect'

    def test_impartire(self):
        assert self.calculator.impartire(5, 5) == 1, 'Impartirea nu functioneaza corect'
