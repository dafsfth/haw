def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[Consumer] consuming %s....' % n)
        r = '200 ok'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[Consumer] Producing  %s' % n)
        r = c.send(n)
        print('[consumer] Consumer return %s ' % r)
    c.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)
