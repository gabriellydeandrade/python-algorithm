from greatest_common_divisor.validator import validate_args


@validate_args
def naive_gcd(a: int, b: int) -> int:
    """
    :param a: first number
    :param b: second number
    :return: greatest divisor between a and b
    """

    best_greatest_divisor = 1
    for divisor in range(1, max(a, b)):
        if a % divisor == 0 and b % divisor == 0:
            best_greatest_divisor = divisor

    return best_greatest_divisor
