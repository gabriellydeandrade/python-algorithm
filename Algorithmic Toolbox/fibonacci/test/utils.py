class AlgorithmTooSlow(Exception):
    pass


def handler_signal(signum, frame):
    raise AlgorithmTooSlow("It takes so long this algorithm")





