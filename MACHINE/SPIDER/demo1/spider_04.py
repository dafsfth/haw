# -*coding:gbk*-
import requests, urllib3, logging


proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}
"""
# ֤����֤�����ҳ��ʱ����verify��������ΪFalse����
urllib3.disable_warnings()  # ͨ�����ú��Ծ���ķ�ʽ�������������
logging.captureWarnings(True)  # ͨ�����񾯸浽��־�ķ�ʽ���Ծ���
r = requests.get('https://www.12306.cn', verify=False, proxies=proxies)
print(r.status_code)   
"""

"""
# �����֤��
from requests.auth import HTTPBasicAuth
req = requests.get(url='url', auth=({'username': 'password'}))
print(req.status_code)
"""




# ������ʽ   https://tool.oschina.net/regex/
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
result5 = re.match(r5, content1, re.S)   # \.ƥ����ǳ����з�֮��������ַ�
# print(result5.group(1))

"""
���η���
I: ʹƥ��Դ�Сд������
L: �����ػ�ʶ��locale-aware��ƥ��
M: ����ƥ�䣬Ӱ��^��$
S: ʹ.ƥ������������ڵ������ַ�
U: ����Unicode�ַ��������ַ��������־Ӱ��\w��\W�� \b��\B
X: �ñ�־ͨ������������ĸ�ʽ�Ա��㽫������ʽд�ø��������
"""
# search ɨ�������ַ�����Ȼ�󷵻ص�һ���ɹ�ƥ��Ľ��
html = '''<div id="songs-list">
    <h2 class="title">�����ϸ�</h2>
    <p class="introduction">
        �����ϸ��б�
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">һ·������</li>
        <li data-view="7">
            <a href="/2.mp3" singer="������">�׺�һ��Ц</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="����">�������</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">�������</a></li>
        <li data-view="5"><a href="/5.mp3" singer="�»���">���±�</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="������"><i class="fa fa-user"></i>��Ը�˳���</a>
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
p = re.compile('\d{2}:\d{2}')  # ��������ʽ�����һ��������ʽ�����Ա㸴�á�
result8 = re.sub(p, '', content4)
result9 = re.sub(p, '123', content5)
result10 = re.sub(p, 'fgdf', content6)
print(result10)