import random
import time
def emit_gel(step):
    value = 50
    while True:
        sign = yield value
        value += random.randint(0, step) * sign
        if value > 100:
            raise ValueError('invalid value (value > 100)')


def valve():
    func = emit_gel(30)
    res = next(func)
    sign = 1
    while True:
        print(res)
        time.sleep(0.06)
        if res > 90 or res < 10:
            func.close()
            exit(0)
        if res > 80 or res < 20:
            sign *= -1
            while res > 80 or res < 20:
                res = func.send(sign)
        res = func.send(sign)
valve()