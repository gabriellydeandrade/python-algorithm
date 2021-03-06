from unittest import TestCase

from fibonacci.fibonacci import fibonacci, calculate_number_of_steps_in_algorithm


class TestFibonacci(TestCase):
    def test_if_a_number_less_or_equal_to_1_return_itself(self):
        self.assertEqual(fibonacci(number=0), 0)
        self.assertEqual(fibonacci(number=1), 1)

    def test_if_4_is_passed_it_returns_3(self):
        self.assertEqual(fibonacci(number=4), 3)

    def test_if_3_is_passed_it_returns_2(self):
        self.assertEqual(fibonacci(number=3), 2)


class TestNumberOfStepsInAlgorithm(TestCase):
    def test_if_tn_is_less_or_equal_than_fn_for_huge_numbers(self):
        tn = calculate_number_of_steps_in_algorithm(number=100)
        fn = fibonacci(number=100)

        self.assertLessEqual(tn, fn)


