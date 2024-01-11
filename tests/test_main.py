import unittest

from main import main_function


class TestMain(unittest.TestCase):
    def test_main_function(self):
        # Test case 1: Test with valid input
        result = main_function(10)
        self.assertEqual(result, 100)

        # Test case 2: Test with zero input
        result = main_function(0)
        self.assertEqual(result, 0)

        # Test case 3: Test with negative input
        result = main_function(-5)
        self.assertEqual(result, 25)

        # Test case 4: Test with large input
        result = main_function(1000)
        self.assertEqual(result, 1000000)

        # Test case 5: Test with decimal input
        result = main_function(2.5)
        self.assertEqual(result, 6.25)

        # Test case 6: Test with string input
        result = main_function("abc")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
