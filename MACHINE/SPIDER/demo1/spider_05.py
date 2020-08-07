# -*coding:gbk*-

import requests, random, re, time
import openpyxl
from bs4 import BeautifulSoup

page = 0
# url = 'http://www.ip3366.net/?stype=1&page={}'.format(page)
url = 'https://maoyan.com/board/4?offset={}'
wb = openpyxl.Workbook()
ws = wb.active

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


def get_ip():
    s = requests.session()
    r = s.get(url=url, headers=user_agent)
    r.raise_for_status()
    r.encoding = r.apparent_encoding

    soup = BeautifulSoup(r.text, 'lxml')
    tbody = soup.find('tbody')

    soup1 = BeautifulSoup(str(tbody), 'lxml')
    trs = soup1.find_all('tr')
    for i in trs:
        soup2 = BeautifulSoup(str(i), 'lxml')
        tds = soup2.find_all('td')
        ws.append([tds[0].string, tds[3].string])


def get_film(n):

    s = requests.session()
    r = s.get(url=url.format(n), headers=user_agent)
    r.raise_for_status()
    r.encoding = r.apparent_encoding

    soup = BeautifulSoup(r.text, 'lxml')
    div = soup.find('div', class_="content")

    soup1 = BeautifulSoup(str(div), 'lxml')
    dds = soup1.find_all('dd')
    for i in dds:
        # print(i)
        name = i.find('p', class_="name").find('a').string
        print(name)
        releasetime = i.find('p', class_="releasetime").string
        score_integer = i.find('p', class_='score').find('i', class_="integer").string
        score_fraction = i.find('p', class_="score").find('i', class_='fraction').string
        main_star = i.find('p', class_='star').string
        ws.append([name, main_star, releasetime, (score_integer+score_fraction)])


for i in range(4):
    # get_ip()
    get_film(i * 10)
    # page += 1
    time.sleep(1)
    print('-----------------------------')

wb.save('film.xlsx')

"""
https://maoyan.com/board/4?offset=10
https://maoyan.com/board/4?offset=20
"""