import time, asyncio


@asyncio.coroutine
def task1():
    print('task1 start work-----')
    yield from asyncio.sleep(2)
    print('task1 finish the task')
    return task1.__name__


@ asyncio.coroutine
def task2():
    print('task2 start work-----')
    yield from asyncio.sleep(5)
    print('task1 finish the task')
    return task2.__name__


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [task1(), task2()]
    loop.run_until_complete(asyncio.wait(tasks))   # 任务2没完成时， 进行任务1
    loop.close()