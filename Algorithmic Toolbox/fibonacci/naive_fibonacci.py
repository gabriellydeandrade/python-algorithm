def naive_fibonacci(number: int) -> int:
    """

    :param number: the order of the fibonacci that we want to discover Fn
    :return: the fibonacci number
    """

    # FIXME this is a naive algorithm and it takes so long to return the result for long numbers

    if number <= 1:
        return number
    else:
        return naive_fibonacci(number=number - 1) + naive_fibonacci(number=number - 2)


def calculate_number_of_steps_in_naive_algorithm(number: int):
    if number <= 1:
        return 2
    else:
        return (
            3
            + calculate_number_of_steps_in_naive_algorithm(number - 1)
            + calculate_number_of_steps_in_naive_algorithm(number - 2)
        )
