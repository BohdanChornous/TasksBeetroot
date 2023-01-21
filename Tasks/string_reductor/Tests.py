import unittest
from Tasks.string_reductor.Task_from_teacher import stringreduction

class TestStringReduction(unittest.TestCase):

    def test_1(self):
        self.assertEqual(stringreduction('abc'), 2)

    def test_2(self):
        self.assertEqual(stringreduction('ccc'), 3)

    def test_3(self):
        self.assertEqual(stringreduction('bcab'), 1)

    def test_4(self):
        self.assertEqual(stringreduction('cab'), 2)


if __name__ == '__main__':
    unittest.main()