import requests, asyncio


async def down(url):
    r = requests.get(url)
    print('下载 %s，长度为 %d' % (url, len(r.text)))


if __name__ == '__main__':
    urls = ['http://www.baidu.com', 'http://www.163.com', 'http://www.sina.cm.cn']
    tasks = [down(i) for i in urls]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()