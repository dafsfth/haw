from lxml import etree


"""
*   选取此节点的所有子节点
/   从当前节点选取直接子节点
//  从当前节点选取子孙节点
.   选取当前节点
..  选取当前节点的父节点
@   选取属性

|           计算两个节点集         //book | //cd           返回所有拥有book和cd元素的节点集
"""

text = """
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
         </li>
         <li class="li li-first"><a href="link.html">sixth item</a></li>
         <li class="li li-first" name="item"><a href="link.html">seventh item</a></li>
         <li class="li li-first" name="item"><p><a href="link.html">seventh item</a></p></li>
     </ul>
 </div>
"""
html = etree.HTML(text)
# html = etree.parse('test.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))

result = html.xpath('//li/a')  # * 代表匹配所有节点，
result1 = html.xpath('//ul//a')  # // 获取所有子孙节点
result2 = html.xpath('//a[@href="link4.html"]/../@class')  # 获取其父节点，然后再获取其class属性
result3 = html.xpath('//a[@href="link4.html"]/parent::*/@class')
result4 = html.xpath('//li[@class="item-0"]//text()')
result5 = html.xpath('//li[@class="item-0"]/a/text()')  # 获取内容
result6 = html.xpath('//li/a/@href')   # 获取属性
result7 = html.xpath('//li[contains(@class, "li")]/a/text()')  # 属性多值匹配
result8 = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')  # 多属性匹配

# 按序选择
result9 = html.xpath('//li[1]/a/text()')  # 1
result10 = html.xpath('//li[last()]/a/text()')  # -1
result11 = html.xpath('//li[last()-2]/a/text()')  # -3
result12 = html.xpath('//li[position()<3]/a/text()')  # 1, 2

# 节点轴
result13 = html.xpath('//li[1]/ancestor::*')  # 获取所有祖先节点
result14 = html.xpath('//li[1]/ancestor::div')
result15 = html.xpath('//li[1]/attribute::*')  # 获取所有属性值
result16 = html.xpath('//li[1]/child::a[@href="link1-html"]')
result17 = html.xpath('//li[8]/descendant::*')  # 获取所有子孙节点
result18 = html.xpath('//li[1]/following::*[2]')  # 获取当前节点之后的所有节点, 获取了第二个后续节点。
result19 = html.xpath('//li[1]/following-sibling::*')  # 获取当前节点之后的所有同级节点

# print(result4)
# print('-------------------------')
print(result17)
