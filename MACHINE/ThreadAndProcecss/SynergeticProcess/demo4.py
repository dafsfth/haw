import time
from gevent import monkey
import gevent

monkey.patch_all()  # ºï×Ó²¹¶¡£¬ sleep


def taska():
    for i in range(3):
        print('A' + str(i))

        time.sleep(1)


def taskb():
    for i in range(3):
        print('B' + str(i))

        time.sleep(1)


def taskc():
    for i in range(3):
        print('C' + str(i))

        time.sleep(1)


if __name__ == '__main__':
    g1 = gevent.spawn(taska)
    g2 = gevent.spawn(taskb)
    g3 = gevent.spawn(taskc)

    g1.join()
    g2.join()
    g3.join()
