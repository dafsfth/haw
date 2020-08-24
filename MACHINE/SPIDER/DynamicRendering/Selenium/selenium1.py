from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import io, sys, time


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')  # 改变标准输出的默认编码
browser = webdriver.Chrome()


def test1():
    try:
        browser.get('https:www.baidu.com')
        i = browser.find_element_by_id('kw')
        i.send_keys('python')
        i.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser, 10)
        wait.until(ec.presence_of_element_located((By.ID, 'content_left')))
        print(browser.current_url)
        print(browser.get_cookies())
        print(browser.page_source)  # 打印出源代码
    finally:
        browser.close()


def test2():
    browser.get('https://www.taobao.com')
    first_input = browser.find_element_by_id('q')
    second_input = browser.find_element_by_css_selector('#q')
    third_input = browser.find_element_by_xpath('//*[@id="q"]')
    print(first_input, second_input, third_input)
    # browser.find_elements()  # 查找所有满足条件的节点
    browser.close()


# 节点交互
def test3():
    browser.get('https://www.taobao.com')
    i = browser.find_element_by_id('q')
    i.send_keys('iphone')
    time.sleep(10)
    i.clear()
    i.send_keys('华为')
    button = browser.find_element_by_class_name('btn-search')
    button.click()


# 动作链
def test4():
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#droppable')
    actions = ActionChains(browser)     # 声明ActionChains对象并将其赋值为actions变量
    actions.drag_and_drop(source, target)
    actions.perform()       # 执行动作


# 执行javascrip
def test5():
    browser.get('https://www.zhihu.com/explore')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 将进度条下拉到最底部
    browser.execute_script('alert("To Bottom")')  # 弹出alert提示框



"""
    网页中有一种节点叫作iframe，也就是子Frame，相当于页面的子页面，它的结构和外部网页的结构完全一致。
    Selenium打开页面后，它默认是在父级Frame里面操作，而此时如果页面中还有子Frame，它是不能获取到子Frame里面的节点的 
"""


# 切换frame
def test7():
    from selenium.common.exceptions import NoSuchElementException
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    try:
        logo = browser.find_element_by_class_name('logo')
    except NoSuchElementException:
        print('no logo')
    browser.switch_to.parent_frame()
    logo = browser.find_element_by_class_name('logo')
    print(logo)
    print(logo.text)


# 前进和后退
def test8():
    browser.get('https://www.baidu.com')
    browser.get('https://www.taobao.com')
    browser.get('https://www.python.org')
    browser.back()
    time.sleep(10)
    browser.forward()
    time.sleep(10)
    browser.close()


# cookies
def test9():
    browser.get('https://www.zhihu.com/explore')
    print(browser.get_cookies())
    browser.add_cookie({'name': 'name', 'domain': 'zhihui.com', 'value': 'germey'})
    print(browser.get_cookies())
    browser.delete_all_cookies()
    print(browser.get_cookies())


# 选项卡
def test10():
    browser.get('https://www.baidu.com')
    browser.execute_script('window.open()')
    print(browser.window_handles)
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://www.taobao.com')
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[0])
    browser.get('https://www.python.org')


test10()