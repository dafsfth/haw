# 同属一个进程的多个线程共享进程拥有的所有资源，CPU给进程分配空间， 而线程没有
# 线程之间的顺序是无序的

import threading, time, os


def sing(n, name):
    # print('唱歌的进程编号是：', os.getpid())
    # print('唱歌父亲的进程编号是：', os.getppid())
    for i in range(n):
        print(name + 'sing----------------')
        print(threading.current_thread())
        time.sleep(2)


def dance(n, name):
    # print('跳舞的进程编号是：', os.getpid())
    # print('跳舞父亲的进程编号是：', os.getppid())
    for i in range(n):
        print(name + ' ' + 'dance----------------')
        print(threading.current_thread())
        time.sleep(2)


if __name__ == '__main__':
    t1 = threading.Thread(target=sing, args=(3, 'wang'), daemon=True)
    t2 = threading.Thread(target=dance, args=(4, 'li'))

    t1.start()
    t2.start()

    print('主线程：', threading.current_thread())
    print('我执行完了')
