import unittest
from helpers import get_next_datetime
import datetime


class NextDatetimeTest(unittest.TestCase):
    def test_12_07(self):
        self.assertEqual(get_next_datetime(datetime.time(hour=12, minute=7)), False)


if __name__ == '__main__':
    unittest.main()
