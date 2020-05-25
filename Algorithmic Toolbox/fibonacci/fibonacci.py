def fibonacci(number: int) -> int:
    """

    :param number: the order of the fibonacci that we want to discover Fn
    :return: the fibonacci number
    """

    fib_numbers = list()
    fib_numbers.append(0)
    fib_numbers.append(1)

    for i in range(2, number+1):
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])
    return fib_numbers[number]


def calculate_number_of_steps_in_algorithm(number: int):
    if number == 0:
        return 4
    else:
        return 2 + 2*number
