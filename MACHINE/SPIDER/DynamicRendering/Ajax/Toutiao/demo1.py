import random, requests, time, os
from hashlib import md5

headers = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36 OPR/63.0.3368.43',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/534.54.16 (KHTML, like Gecko) Version/5.1.4 Safari/534.54.16',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3739.400',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 QIHU 360EE',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
]
user_agent = {'User-Agent': random.choice(headers)}
base_url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=20&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1598238167572&_signature=6V5-gAAgEBCBRA1ZOk.XvOlfP5AALYox4Scy1tyV5rcFWmIQw0K.bVL7k0kHCGrTP1C1BWyvkidg047cfbpu6eRmYNxWzcYky.bhTWlHGpwACC8ot6aUMeIHdAx8WRW0v9y'


def get_json():
    r = requests.get(url=base_url, headers=user_agent)
    r.encoding = r.apparent_encoding
    json1 = r.json()
    if json1.get('data'):
        for item in json1.get('data'):
            title = item.get('title')
            imgs = item.get('image_list')
            for img in imgs:
                yield {
                    'image': img.get('url'),
                    'title': title
                }


def save_img(item):
    # base_path = 'E:\LEARN\PYTHON\Picture\\' + item.get('title')
    if not os.path.exists(item.get('title')):
        os.makedirs(item.get('title'))
    try:
        r = requests.get(url=item.get('image'))
        if r.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(r.content).hexdigest(), 'jpg')
            # path = base_path + file_path
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(r.content)
    except requests.ConnectionError:
        print('failed to save images')


def main():
    # 通过把秒转换毫秒的方法获得13位的时间戳
    # millis = int(round(time.time() * 1000))
    for item in get_json():
        save_img(item)
    # time.sleep(1)


if __name__ == '__main__':
    main()
