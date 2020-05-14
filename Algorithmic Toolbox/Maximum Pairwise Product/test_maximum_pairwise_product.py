import random
import time
from unittest import TestCase
from .maximum_pairwise_product import get_maximum_pairwise_product


class TestMaximumPairwiseProduct(TestCase):
    def test_it_returns_the_two_maximum_products(self):
        maximum_pairwise_product = get_maximum_pairwise_product(
            elements=7, numbers=[7, 8, 1, 3, 2, 9, 10]
        )
        self.assertEqual(maximum_pairwise_product, 90)

    def test_it_returns_the_two_maximum_products_even_if_the_two_maximum_numbers_are_equal(
        self,
    ):
        maximum_pairwise_product = get_maximum_pairwise_product(
            elements=8, numbers=[7, 8, 1, 3, 2, 9, 10, 10]
        )
        self.assertEqual(maximum_pairwise_product, 100)

    def test_it_runs_in_at_least_one_second_even_with_large_numbers(self):
        numbers = [random.randint(2, 200000) for _ in range(0, 100001)]

        time_start = time.clock()
        get_maximum_pairwise_product(elements=100000, numbers=numbers)
        time_finish = time.clock() - time_start

        self.assertLess(time_finish, 1)
