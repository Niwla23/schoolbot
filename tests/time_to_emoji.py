import unittest
from schoolbot.helpers import time_to_emoji


class TimeToEmojiTest(unittest.TestCase):
    def test_normal(self):
        converted = time_to_emoji("11:00")
        self.assertEqual(converted, ":clock11:")

    def test_normal_30(self):
        converted = time_to_emoji("11:30")
        self.assertEqual(converted, ":clock1130:")

    def test_11_59(self):
        converted = time_to_emoji("11:59")
        self.assertEqual(converted, ":clock12:")

    def test_15_50(self):
        converted = time_to_emoji("15:50")
        self.assertEqual(converted, ":clock4:")

    def test_12_50(self):
        converted = time_to_emoji("12:50")
        self.assertEqual(converted, ":clock1:")

    def test_bigger_twelve(self):
        converted = time_to_emoji("14:30")
        self.assertEqual(converted, ":clock230:")


if __name__ == '__main__':
    unittest.main()
