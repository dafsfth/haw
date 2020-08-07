import requests, re, time, sys
from bs4 import BeautifulSoup


class DownLoad():

    def __init__(self):
        self.start_url = 'https://www.biquge.com.cn/book/27699/'
        self.headers = {'User_Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1'}
        self.name = []
        self.page_url = []
        self.title = ""
        self.file_path = '龙血魔帝.txt'

    def get_url(self):
        r = requests.get(self.start_url, headers=self.headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        soup = BeautifulSoup(r.text, 'lxml')
        div = soup.find('div', id='list')
        soup1 = BeautifulSoup(str(div), 'lxml')
        dds = soup1.find_all('dd')
        self.title = soup1.find('dt').string
        for dd in dds:
            self.name.append(dd.find('a').string)
            url = dd.find('a').get('href').split('/')[3]
            self.page_url.append(url)

    def get_text(self, url):

        r = requests.get(url, headers=self.headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        soup = BeautifulSoup(r.text, 'lxml')
        div = soup.find('div', id='content').text
        text = div.replace('\xa0' * 8, '\n\n')
        return text

    def write_in(self, text, name):
        with open(self.file_path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == "__main__":

    dl = DownLoad()
    dl.get_url()
    with open(dl.file_path, 'a', encoding='utf-8') as fr:
        fr.write(dl.title + '\n')
    for i in range(len(dl.name)):
        dl.write_in(dl.get_text(dl.start_url + dl.page_url[i]), dl.name[i])
        sys.stdout.write('已下载{:.2%}'.format(float(i / len(dl.name))) + '\r')
        sys.stdout.flush()
    print('over')