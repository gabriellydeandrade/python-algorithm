import signal
from unittest import TestCase

from fibonacci.naive_fibonacci import naive_fibonacci, calculate_number_of_steps_in_naive_algorithm
from fibonacci.test.utils import handler_signal, AlgorithmTooSlow


class TestNaiveFibonacci(TestCase):
    def test_if_a_number_less_or_equal_to_1_return_itself(self):
        self.assertEqual(naive_fibonacci(number=0), 0)
        self.assertEqual(naive_fibonacci(number=1), 1)

    def test_if_4_is_passed_it_returns_3(self):
        self.assertEqual(naive_fibonacci(number=4), 3)

    def test_if_3_is_passed_it_returns_2(self):
        self.assertEqual(naive_fibonacci(number=3), 2)

    def test_if_takes_longer_than_2_seconds_for_big_numbers_of_fibonacci(self):
        signal.signal(signal.SIGALRM, handler_signal)
        seconds_wait = 2
        signal.alarm(seconds_wait)

        with self.assertRaises(AlgorithmTooSlow):
            naive_fibonacci(number=100)


class TestNumberOfStepsInNaiveAlgorithm(TestCase):
    def test_if_tn_is_greater_or_equal_than_fn(self):
        tn = calculate_number_of_steps_in_naive_algorithm(number=6)
        fn = naive_fibonacci(number=6)

        self.assertGreaterEqual(tn, fn)
