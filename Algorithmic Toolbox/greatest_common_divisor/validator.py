def validate_args(func):
    def param_is_integer(a, b):
        if isinstance(a, int) and isinstance(b, int):
            param_is_positive(a, b)
        else:
            raise TypeError("Arguments passed should be integers to calculate")

    def param_is_positive(a, b):
        if a >= 0 and b >= 0:
            return func(a, b)
        else:
            raise AttributeError("Arguments passed shout be positive integers")

    return param_is_integer
