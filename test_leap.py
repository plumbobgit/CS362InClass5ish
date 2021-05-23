import unittest
import leap_year


class TestLeapYear(unittest.TestCase):

    def test_leap(self):
        value = leap_year.leap('2020')
        self.assertEqual(value, ' 2020 is a leap year')

    def test_notleap(self):
        value = leap_year.leap('2021')
        self.assertEqual(value, ' 2021 is not a leap year')


if __name__ == "__main__":
    unittest.main()
