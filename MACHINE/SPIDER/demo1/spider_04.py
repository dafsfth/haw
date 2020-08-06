# -*coding:gbk*-
import requests, urllib3, logging


proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}
"""
# 证书验证错误的页面时，把verify参数设置为False即可
urllib3.disable_warnings()  # 通过设置忽略警告的方式来屏蔽这个警告
logging.captureWarnings(True)  # 通过捕获警告到日志的方式忽略警告
r = requests.get('https://www.12306.cn', verify=False, proxies=proxies)
print(r.status_code)   
"""

"""
# 身份认证：
from requests.auth import HTTPBasicAuth
req = requests.get(url='url', auth=({'username': 'password'}))
print(req.status_code)
"""




# 正则表达式   https://tool.oschina.net/regex/
import re

r1 = '^Hello\s(\d+)\sWorld'
r2 = '^Hello.*Demo$'
r3 = '^Hello.*(\d+).*Demo$'
r4 = '^Hello.*?(\d+).*Demo$'
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match(r1, content)
result1 = re.match(r2, content)
result2 = re.match(r3, content)
result3 = re.match(r4, content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())
# print(result1.group())
# print(result2.group(1))
# print(result3.group(1))
content1 = """Hello 1234567 World
This is a Regex Demo
"""
r5 = '^He.*?(\d+).*Demo$'
result5 = re.match(r5, content1, re.S)   # \.匹配的是除换行符之外的任意字符
# print(result5.group(1))

"""
修饰符：
I: 使匹配对大小写不敏感
L: 做本地化识别（locale-aware）匹配
M: 多行匹配，影响^和$
S: 使.匹配包括换行在内的所有字符
U: 根据Unicode字符集解析字符。这个标志影响\w、\W、 \b和\B
X: 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解
"""
# search 扫描整个字符串，然后返回第一个成功匹配的结果
html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''
r6 = '<li.*?active.*?singer="(.*?)">(.*?)</a>'
result6 = re.search(r6, html, re.S)
# print(result6.group(1), result6.group(2))
r7 = '<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>?'
result7 = re.findall(r7, html, re.S)
# for i in result7:
    # print(i)

content2 = '54aK54yr5oiR54ix5L2g'
content3 = re.sub('\\d+', '', content2)
# print(content3)
content4 = '2016-12-15 12:00'
content5 = '2016-12-17 12:55'
content6 = '2016-12-22 13:21'
p = re.compile('\d{2}:\d{2}')  # 将正则表达式编译成一个正则表达式对象，以便复用。
result8 = re.sub(p, '', content4)
result9 = re.sub(p, '123', content5)
result10 = re.sub(p, 'fgdf', content6)
print(result10)