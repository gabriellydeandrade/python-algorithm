def validate_args(func):
    def args_should_be_integer(a, b):
        if isinstance(a, int) and isinstance(b, int):
            args_should_be_positive(a, b)
        else:
            raise TypeError("Arguments passed should be integers")

    def args_should_be_positive(a, b):
        if a >= 0 and b >= 0:
            return func(a, b)
        else:
            raise AttributeError("Arguments passed should be positive integers")

    return args_should_be_integer
