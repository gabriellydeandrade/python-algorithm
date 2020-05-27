import signal
from unittest import TestCase

from greatest_common_divisor.naive_gcd import naive_gcd
from utils import handler_signal, AlgorithmTooSlow


class TestNaiveGCD(TestCase):

    def test_if_returns_2_for_gcd_between_10_and_4(self):
        result = naive_gcd(a=10, b=4)
        self.assertEqual(result, 2)

    def test_if_returns_5_for_gcd_between_25_and_5(self):
        result = naive_gcd(a=25, b=5)
        self.assertEqual(result, 5)

    def test_if_takes_longer_than_2_seconds_for_big_numbers_of_gcd(self):
        signal.signal(signal.SIGALRM, handler_signal)
        seconds_wait = 2
        signal.alarm(seconds_wait)

        with self.assertRaises(AlgorithmTooSlow):
            naive_gcd(a=252478738783, b=5123122312312)

    def test_if_raises_exception_if_the_two_params_passed_are_not_integers(self):
        with self.assertRaises(TypeError):
            naive_gcd(a="bla", b="bli")
