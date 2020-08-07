from bs4 import BeautifulSoup
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
"""

soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())  # 把要解析的字符串以标准的缩进格式输出。
# print(soup.title)
# print(soup.p)
# print(type(soup.title))
# print(soup.head)

# 获取名称（name）
# print(soup.title.name)

# 获取所有属性（attrs）
# print(soup.p.attrs)  # 以字典的形式输出
# print(soup.p.attrs['name'])

# contents属性得到的结果是直接子节点的列表。
# descendants: 获取所有的子孙节点

# for i, child in enumerate(soup.p.descendants):
#     print(i, child)

# print(soup.a.parent)
# print(soup.a.parents)

# 同级
# print(soup.a.next_sibling)
# print(soup.a.next_siblings)
# print(soup.a.previous_sibling)
# print(soup.a.previous_siblings)

# for ul in soup.find_all('ul'):
#     for li in soup.find_all('li'):
#         print(li.string)
# print('=======================================')

# uls = soup.find_all(atrs={'id': "list-1"})
# print(soup.find_all(id='list-1'))
# print(soup.find_all(class_='element'))

# print(soup.find_all(text=re.compile('link')))

# CSS选择器
# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))

for ul in soup.select('ul'):
    print(ul.select('li'))
    print(ul['id'])
    print(ul.attrs['id'])