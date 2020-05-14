def get_maximum_pairwise_product(numbers: list) -> int:
    """
    Maximum Pairwise Product Problem
    Find the maximum product of two distinct numbers in a sequence of non-negative integers.
    Input: A sequence of non-negative integers.
    Output: The maximum value that can be obtained by multiplying two different elements from the sequence.
    """
    first_maximum_value = max(numbers)
    numbers.remove(first_maximum_value)
    second_maximum_value = max(numbers)

    return first_maximum_value * second_maximum_value


if __name__ == "__main__":
    user_input = [int(x) for x in input().split()]
    print(get_maximum_pairwise_product(numbers=user_input))
