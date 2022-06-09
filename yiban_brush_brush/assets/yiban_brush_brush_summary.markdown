# yiban brush brush by selenium implement
>基于 python 实现  
>一定要保证网络顺，不然会脱离你预料的结果  
一定要保证网络顺，不然会脱离你预料的结果  
一定要保证网络顺，不然会脱离你预料的结果  
.  
.  
搜爬虫框架、模拟浏览器框架、模拟网页框架  
.  
selenium是模拟浏览器  
scrap 废料、碎片  
url 编码用 scrapy 框架 requests模块

---
```
直走一次的方法
def execute(username, password):
    # 防止自动关闭 browser，方法持有它吧
    global driver
```
---
# except
```
认真看报错信息

    网络
        把VPN关了

    该元素不能交互
        请换xxx元素，测试没过的话，就得换元素了

        测试过了，就要time.sleep()了
        
        元素未附加到页面
            Message: stale element reference: element is not attached to the page document
    
    无法点击
        测试也没过，就要想换种实现
            a 不得，看 href 属性有无超链接，选到元素用
             get_attribute('href')、get_dom_attribute()交互、
             后，driver.get(url)，要打开新标签的话，记得切换标签页句柄（引用）

```

# wait page load
```

import time
# 推荐
# 使用
#       1、页面动态JS改变页面
#       2、等待页面元素显示
        3、报错
            1、有的报该元素不能点击，但该元素测试时，一遍过
            ，没问题，这是需强制睡眠久点

time.sleep(seconds)



official的显、隐式等待不好
    会报元素不能交互问题，但我已经测试过了，能用
```
# select element

```

from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

id class tagName selector



driver = webdriver.Edge(service
    =Service(EdgeChromiumDriverManager().install()))


driver.find_element(By.CSS_SELECTOR,
                        'body > div.container.with-bg > section > '
                        'section.submit > div > div:nth-child(2) > div >
                         svg').click()


driver.find_element(By.CSS_SELECTOR,
                        'body > div.container.with-bg > section > '
                        'section.submit > div > div:nth-child(2) > div >
                         svg').send_keys("谢谢您，易班员")


返回 元素list，需存在页面中的
driver.find_elements(By.XXX)
```
# element interact 元素交互
```
选到元素后
    .click()
    .send_keys("谢谢您，易班员")

每次交互完一次都要重新选到元素
```
# element attribute obtain
```

        # svg 元素
        
        # get_attribute
        # viewBox: None
        # viewBox type: <class 'NoneType'>


        print(f'get_property: {get_property}')
        print(f'get_property type: {type(get_property)}')
        # get_property: {'animVal': {'height': 20, 'width': 24, 'x': 0,
         'y': 0}, 'baseVal': {'height': 20, 'width': 24, 'x': 0, 'y': 0}}
        # get_property type: <class 'dict'>


        print(f'get_dom_attribute: {get_dom_attribute}')
        print(f'get_dom_attribute type: {type(get_dom_attribute)}')
        # get_dom_attribute: 0 0 24 20
        # get_dom_attribute type: <class 'str'>

        
        # print(f'getattribute: {getattribute}')
        # print(f'getattribute type: {type(getattribute)}')
```

# page tab
```

from selenium.webdriver.support import expected_conditions as e_c

切换标签页引用（就2页状态下）

    original_window = driver.current_window_handle
    # 可用time.sleep()替代，
    wait.until(e_c.number_of_windows_to_be(2))
    # 
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break


close
    driver.close()


退出浏览器
    driver.quit()



python system quit
import sys
    sys.exit()


打开新空的页
    driver.switch_to.new_window('tab')
    # 后加载自己的页
    driver.get(url)


refresh
    driver.refresh()

```
# event interact 事件交互
```

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

按下下箭头键，模拟鼠标滚轮在页面向下滚
    for i in range(0, 99):
        webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
        time.sleep(0.2)
```
# http and https
```
当前页为 http://www.baidu.com
执行，两次 带https 的同url，https://www.baidu.com
    driver.get("https://www.yiban.cn/school/index/id/460")
    driver.get("https://www.yiban.cn/school/index/id/460")
```