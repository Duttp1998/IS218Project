import unittest
from Random.Elements import Elements
from Random.Lists import Lists
from Random.Numbers import Numbers

class MyTestCase(unittest.TestCase):
    def test_Random_Integer_Seed(self):
        self.assertEqual(9, Numbers.prandINT(1, 10, 30))

    def test_Random_Float_Seed(self):
        self.assertEqual(5.851734081452295, Numbers.prandFLT(1, 10, 30))

    def test_Random_IntegerList_Seed(self):
        self.assertEqual([9, 5, 1, 4, 5], Lists.prandINTL(1, 10, 5, 30))

    def test_Random_FloatList_Seed(self):
        self.assertEqual(
            [5.851734081452295, 3.6027679927574847, 1.2703321769601437, 6.882721785034857, 2.89007825994758]
            , Lists.prandFLTL(1, 10, 5, 30))

    def test_Random_Selection_Seed(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(5, Elements.prandElem(arr, 30))

    def test_Random_Multiple_Selection_Seed(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual([5, 3, 5, 1, 5], Elements.prandElems(arr, 5, 30))


if __name__ == '__main__':
    unittest.main()
