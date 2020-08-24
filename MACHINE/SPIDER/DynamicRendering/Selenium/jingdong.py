from selenium import webdriver
import io, sys, time
from bs4 import BeautifulSoup
import requests, random


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')  # 改变标准输出的默认编码
# browser = webdriver.Chrome()

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

# def test1():
#     browser.get('https://www.jd.com/')
#     i = browser.find_element_by_id('key')
#     i.send_keys('iPad')
#     button = browser.find_element_by_class_name('button')
#     button.click()
#     html = browser.page_source
#     print(html)
#     soup = BeautifulSoup(html, 'lxml')
#     lis = soup.find_all('li', class_='gl-item')
#     for li in lis:
#         img_url = li.find('div', class_='p-img').find('a').get('href')
#         price = li.find('div', class_='p-price').find('i').string
#         commit = li.find('div', class_='p-commit').find('a', id='J_comment_100008348554').string
#         print([img_url, price, commit])


def test2(url1, header):
    r = requests.get(url=url1, headers=header)
    r.encoding = r.apparent_encoding
    # r.raise_for_status()
    soup = BeautifulSoup(r.text, 'lxml')

    lis = soup.find_all('li', class_='gl-item')
    for li in lis:
        img_url = li.find('div', class_='p-img').find('a').get('href')
        price = li.find('div', class_='p-price').find('i').string
        # commit = li.find('div', class_='p-commit').find('a', id='J_comment_100008348554').string
        print([img_url, price])


if __name__ == "__main__":
    url = 'https://search.jd.com/Search?keyword=iPad&enc=utf-8&wq=iPad&pvid=44ad91b584914f62922496328d499bb7'
    test2(url, user_agent)