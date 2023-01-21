import unittest
from Tasks.string_reductor.Task_from_teacher import stringreduction

class TestStringReduction(unittest.TestCase):

    def test_1(self):
        self.assertEqual(stringreduction('c'), 1)

    def test_2(self):
        self.assertEqual(stringreduction('ccc'), 3)

    def test_3(self):
        self.assertEqual(stringreduction('abc'), 2)

    def test_4(self):
        self.assertEqual(stringreduction('bcab'), 1)

    def test_5(self):
        self.assertEqual(stringreduction('aabc'), 1)

    def test_6(self):
        self.assertEqual(stringreduction('abcabc'), 2)

    def test_7(self):
        self.assertEqual(stringreduction('abb'), 1)

    def test_8(self):
        self.assertEqual(stringreduction('aa'), 2)

    def test_9(self):
        self.assertEqual(stringreduction('ccaa'), 2)

    def test_10(self):
        self.assertEqual(stringreduction('abbcb'), 2)


if __name__ == '__main__':
    unittest.main()
