import unittest
from Convert import Convert


class TestIntoRoman(unittest.TestCase):
    def test_roman(self):
        self.assertEqual(Convert(10), "X")


if __name__ == "__main__":
    unittest.main()
