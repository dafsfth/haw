"""
多任务： 并发：  按顺序执行
        并行： 一起执行

        进程是分配资源的最小单位
        线程是程序执行的最小单元
"""
import time, multiprocessing, os


def sing(n, name):
    print('唱歌的进程编号是：', os.getpid())
    print('唱歌父亲的进程编号是：', os.getppid())
    for i in range(n):
        print(name + 'sing----------------')
        time.sleep(1)


def dance(n, name):
    print('跳舞的进程编号是：', os.getpid())
    print('跳舞父亲的进程编号是：', os.getppid())
    for i in range(n):
        print(name + 'dance----------------')
        time.sleep(1)


if __name__ == '__main__':
    print('主进程的进程编号是：', os.getpid())
    sing_process = multiprocessing.Process(target=sing, args=(4, 'xiao ming'))
    sing_process.daemon = True  # 设置主进程守护， 当主进程结束时， 不再执行子进程， 由子进程自己开启
    # 字典传参时， 要保持参数名一致
    dance_process = multiprocessing.Process(target=dance, kwargs={'n': 4, 'name': 'xiao hua'})

    sing_process.start()
    dance_process.start()
    time.sleep(3)
    print('我执行完了')