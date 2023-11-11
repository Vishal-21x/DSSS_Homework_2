import unittest
from math_quiz import Random_Integer_Generator, Operator, Arithmetic_Operation


class TestMathGame(unittest.TestCase):

    def test_Random_Integer_Generator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = Random_Integer_Generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_Operator(self):
        result = Operator()
        self.assertIn(result, ['+', '-', '*'])

    def test_Arithmetic_Operation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (7, 4, '-', '7 - 4', 3),
            (3, 4, '*', '3 * 4', 12)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            self.assertTrue(expected_answer,
                            Arithmetic_Operation(num1, num2, operator))


if __name__ == "__main__":
    unittest.main()
