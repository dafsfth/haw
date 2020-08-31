import time
from greenlet import greenlet




def taska():
    for i in range(3):
        print('A' + str(i))
        gb.switch()
        time.sleep(1)


def taskb():
    for i in range(3):
        print('B' + str(i))
        gc.switch()
        time.sleep(1)


def taskc():
    for i in range(3):
        print('C' + str(i))
        ga.switch()
        time.sleep(1)


if __name__ == '__main__':
    ga = greenlet(taska)
    gb = greenlet(taskb)
    gc = greenlet(taskc)

    ga.switch()