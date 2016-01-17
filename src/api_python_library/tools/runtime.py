import signal

__trap_signals = (signal.SIGINT, signal.SIGTERM)
__funcs = []


# noinspection PyBroadException
def __shutdown_func(*args, **kwargs):
    print('trap signal')

    for func in __funcs:
        try:
            print('run func %s', str(func.__name__))
            func()
        except BaseException:
            pass


for sig in __trap_signals:
    signal.signal(sig, __shutdown_func)


def add_shutdown_hook(func):
    __funcs.append(func)
