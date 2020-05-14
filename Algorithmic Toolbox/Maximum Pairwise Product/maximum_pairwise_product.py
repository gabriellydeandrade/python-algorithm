def get_maximum_pairwise_product(elements: int, numbers: list) -> int:
    """
    Maximum Pairwise Product Problem
    Find the maximum product of two distinct numbers in a sequence of non-negative integers.
    Input: A sequence of non-negative integers.
    Output: The maximum value that can be obtained by multiplying two different elements from the sequence.
    """

    # Second Version of Solution: using order 2n (removing max builtin from Python)
    # TODO as a challenge, reduce the comparision for 1.5n and n + log(n) − 2

    first_maximum_value = 0
    for i in range(elements):
        if numbers[i] > first_maximum_value:
            first_maximum_value = numbers[i]

    numbers.remove(first_maximum_value)

    second_maximum_value = 0
    for i in range(elements-1):
        if numbers[i] > second_maximum_value:
            second_maximum_value = numbers[i]

    return first_maximum_value * second_maximum_value


if __name__ == "__main__":
    user_number_of_elements = int(input())
    user_numbers = [int(x) for x in input().split()]
    print(get_maximum_pairwise_product(elements=user_number_of_elements, numbers=user_numbers))
