import unittest
from Calculator.StatisticsCalculator import StatsCalculator
from Random.Elements import Elements
from Random.Lists import Lists
from Random.Numbers import Numbers


class MyTestCase(unittest.TestCase):

    def __init__(self):
        self.calculator = StatsCalculator()
        self.seed = 1
        self.IntegerList = Lists.prandINTL(1, 100, 100, self.seed)
        self.FloatList = Lists.prandFLTL(1, 100, 100, self.seed)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, StatsCalculator)


if __name__ == '__main__':
    unittest.main()
