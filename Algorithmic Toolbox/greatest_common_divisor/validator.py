def validate_args(func):
    def param_is_integer(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return func(a, b)
        else:
            raise TypeError("Arguments passed should be integers to calculate")
    return param_is_integer
