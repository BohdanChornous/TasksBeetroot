import unittest
from Tasks.les15_tasks import TVController, CHANNELS


class TestTVController(unittest.TestCase):

    def setUp(self) -> None:
        self.controller = TVController(CHANNELS)

    def test_first_channel(self):
        first_channel = self.controller.first_channel()
        self.assertEqual(first_channel, "BBC")

    def test_last_channel(self):
        last_channel = self.controller.last_channel()
        self.assertEqual(last_channel, "TV1000")

    def test_next_channel(self):
        current_channel = self.controller.current_channel()
        self.assertEqual(current_channel, "BBC")
        self.controller.next_channel()
        current_channel = self.controller.current_channel()
        self.assertEqual(current_channel, "Discovery")
        self.controller.next_channel()
        current_channel = self.controller.current_channel()
        self.assertEqual(current_channel, "TV1000")
        self.controller.next_channel()
        current_channel = self.controller.current_channel()
        self.assertEqual(current_channel, "BBC")

    def test_turn_channel(self):
        turn_channel = self.controller.turn_channel(3)
        self.assertEqual(turn_channel, "TV1000")

    def test_previous_channel(self):
        current_channel = self.controller.current_channel()
        self.assertEqual(current_channel, "BBC")
        self.controller.previous_channel()
        current_channel = self.controller.current_channel()
        self.assertEqual(current_channel, "TV1000")
        self.controller.previous_channel()
        current_channel = self.controller.current_channel()
        self.assertEqual(current_channel, "Discovery")
        self.controller.previous_channel()
        current_channel = self.controller.current_channel()
        self.assertEqual(current_channel, "BBC")

    def test_is_exist(self):
        is_exist = self.controller.is_exist(4)
        self.assertEqual(is_exist, "NO")
        is_exist = self.controller.is_exist("BBC")
        self.assertEqual(is_exist, "YES")


if __name__ == '__main__':
    unittest.main()
