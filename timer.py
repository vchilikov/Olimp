import time


def timer(f):
    def wrapper(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print(time.time() - t)
        return res

    return wrapper
