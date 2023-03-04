import unittest
from Tasks.les20_tasks import MyContext


class TestMyContext(unittest.TestCase):

    def setUp(self) -> None:
        self.context = MyContext('myfile.txt')

    def test_get_count(self):
        with self.context as fo:
            fo.read()
        enter = self.context.get_count()
        self.assertEqual(enter, 1)

    def test_get_count2(self):
        with self.context as fo:
            fo.read()
        enter = self.context.get_count()
        self.assertEqual(enter, 2)


