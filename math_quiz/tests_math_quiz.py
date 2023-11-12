import unittest
from math_quiz import Random_Integer, Random_Operator, Calculation


class TestMathGame(unittest.TestCase):

    def test_Random_Integer(self):
        # Test if random numbers generated are within the specified range
        min_value = 1
        max_value = 10
        for _ in range(500):  # Test a large number of random values
            random_number = Random_Integer(min_value, max_value)
            self.assertTrue(min_value <= random_number <= max_value)

    def test_Random_Operator(self):
        result = Random_Operator()
        self.assertIn(result, ['+', '-', '*'])

    def test_Calculation(self):
        test_cases = [
            (5, 5, '+', '5 + 5', 10),
            (6, 4, '-', '6 - 4', 2),
            (8, 9, '*', '8 * 9', 72)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            self.assertTrue(expected_answer,
                            Calculation(num1, num2, operator))


if __name__ == "__main__":
    unittest.main()
