import requests
import gevent
from gevent import monkey


monkey.patch_all()


def down(url):
    r = requests.get(url)
    print('下载｛0｝，长度为{1}'.format(url, len(r.text)))


if __name__ == '__main__':
    urls = ['http://www.baidu.com', 'http://www.163.com', 'http://www.sina.cm.cn']
    for i in urls:
        g = gevent.spawn(down, i)
        g.join()