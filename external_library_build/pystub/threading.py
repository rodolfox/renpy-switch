class Condition():
    def __enter__(self): pass

    def __exit__(self, _type, value, traceback): pass

    def notify(self): pass

    def acquire(self): pass

    def release(self): pass

    def notifyAll(self): pass

    def wait(self, duration=None): pass


class RLock(object):
    def __enter__(self): pass

    def __exit__(self, _type, value, traceback): pass


class Event(object):
    def set(self): pass

    def isSet(self): return True

    def clear(self): pass

    def wait(self, timeout=None): return True


class Thread(object):
    def __init__(self, *args, **kwargs): pass

    def start(self): pass

    def join(self): pass

    def setDaemon(self, value): pass

    def isAlive(self):
        return False


class _MainThread(Thread):

    def __init__(self): pass

    def _set_daemon(self):
        return False

    def _exitfunc(self): pass


_current_thread = Thread()

_shutdown = _MainThread()._exitfunc


def current_thread():
    return _current_thread