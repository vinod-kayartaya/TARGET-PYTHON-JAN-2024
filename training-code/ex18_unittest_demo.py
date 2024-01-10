import unittest
from my_utils import factorial


class FactorialTests(unittest.TestCase):
    def test_for_positive_number(self):  # method name must have a prefix of test
        actual = factorial(5)
        expected = 120
        self.assertEqual(expected, actual)

    def test_for_0(self):
        actual = factorial(0)
        expected = 1
        self.assertEqual(expected, actual)

    def test_for_negative_number(self):
        try:
            factorial(-5)
            # test case failed, as this should have raised an error
            self.fail('was expecting a ValueError to be raised, but did not get one')
        except ValueError:
            # test case is assumed to have passed
            pass

    def test_for_non_int(self):
        def handler():
            factorial('asdf')

        self.assertRaises(TypeError, handler)


# required for executing this script from CLI
if __name__ == '__main__':
    unittest.main()

