from pyquery import PyQuery as pq


html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
 <div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

doc = pq(html)
# doc = pq(url='https://www.baidu.com')
# print(doc('#container .list li'))

# 查找节点
# print(doc('.list').find('li'))

# 如果只想查找子节点，那么可以用children()
item = doc('.list')
# lis = item.children('.active')
# print(lis)

# 父亲节点
# print(item.parent())

# 兄弟节点
# li = doc('.list .item-0.active')
# print(li.siblings())

# 遍历
# lis = doc('li').items()
# for li in lis:
#     print(li)

# 获取属性  attr
a = doc('.item-0.active a')
# print(a.attr('href'))  # 第一个节点的属性。
# print(a.attr.href)

# 获取文本 text
# print(a.text())  # 所有的li节点内部的纯文本，
# print(doc('li').html())   # 第一个li节点的内部HTML文本

# 节点操作
li = doc('.item-0.active')
li.remove_class('active')
li.add_class('hi')
print(li)

