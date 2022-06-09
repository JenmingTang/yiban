# selenium 4
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys

import sys
import threading
import time
# 显示等
from selenium.webdriver.support import expected_conditions as EC

WEB_DRIVER_WAIT_TIMEOUT = 10
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
wait = WebDriverWait(driver, WEB_DRIVER_WAIT_TIMEOUT)
el_likes = None
el_likes_num = 0


def back_previous_page():
    # 存储原始窗口的 ID
    original_window = driver.current_window_handle
    # 关闭当前
    driver.close()
    # 循环执行，直到找到一个新的窗口句柄
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    pass


def run():
    # 防止自动关闭 browser，方法持有它吧
    global driver
    # driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    # global wait
    # wait = WebDriverWait(driver, WEB_DRIVER_WAIT_TIMEOUT)
    # 执行

    driver.get("https://www.yiban.cn/login?go=http%3A%2F%2Fwww.yiban.cn%2Fschool%2Findex%2Fid%2F460")

    wait.until(lambda d: d.find_element(By.ID, "account-txt")).send_keys('17776424705')
    # 同一个页第一等完，应该所有加载出来了
    driver.find_element(By.ID, "password-txt").send_keys('1.7776424705')
    driver.find_element(By.ID, "login-btn").click()
    # 重定向问题，重定向不用等，从http变为https
    driver.get("https://www.yiban.cn/school/index/id/460")
    driver.get("https://www.yiban.cn/school/index/id/460")

    # 经常有网络问题，这里再refresh下
    # 最后做出的妥协，延时长短根据网速而定
    # time.sleep(2)
    driver.refresh()
    # 大概30次加载2次，
    # 0~30
    for i in range(0, 81):
        webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
    time.sleep(2)
    # 切换了页面，留了状态，这界面一直活着
    global el_likes
    el_likes = wait.until(
        lambda d: d.find_elements(By.CSS_SELECTOR, 'body > main > div > div > div > div.grid-box.grid-box'
                                                   '--3of4.content-left-container > div > div.posts > a'))
    global el_likes_num
    while True:
        url = el_likes[el_likes_num].get_attribute('href')
        el_likes_num += 1
        driver.switch_to.new_window('tab')
        driver.get(url)
        # 先点赞可以了，在这也不用睡觉 viewBox="" 0 0 24 20 0 0 22 18

        # wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
        #                                     'body > div.container.with-bg > section > '
        #                                     'section.submit > div > div:nth-child(2) > div > svg')).click()

        # view_box = wait.until(lambda d: d.find_element(By.CSS_SELECTOR, 'body > div.container.with-bg > section > '
        #                                                                 'section.submit > div > div:nth-child(2) > '
        #                                                                 'div > svg')).get_attribute(
        #     'viewBox')
        get_property = wait.until(lambda d: d.find_element(By.CSS_SELECTOR, 'body > div.container.with-bg > section > '
                                                                            'section.submit > div > div:nth-child(2) > '
                                                                            'div > svg')).get_property(
            'viewBox')
        get_dom_attribute = driver.find_element(By.CSS_SELECTOR, 'body > div.container.with-bg > section > '
                                                                 'section.submit > div > div:nth-child(2) > '
                                                                 'div > svg').get_dom_attribute('viewBox')
        # 'WebElement' object has no attribute 'viewBox'
        # getattribute = driver.find_element(By.CSS_SELECTOR, 'body > div.container.with-bg > section > '
        #                                                     'section.submit > div > div:nth-child(2) > '
        #                                                     'div > svg').__getattribute__('viewBox')


        # get_attribute
        # viewBox: None
        # viewBox type: <class 'NoneType'>
        print(f'get_property: {get_property}')
        print(f'get_property type: {type(get_property)}')
        # get_property: {'animVal': {'height': 20, 'width': 24, 'x': 0, 'y': 0}, 'baseVal': {'height': 20, 'width': 24, 'x': 0, 'y': 0}}
        # get_property type: <class 'dict'>
        print(f'get_dom_attribute: {get_dom_attribute}')
        print(f'get_dom_attribute type: {type(get_dom_attribute)}')
        # get_dom_attribute: 0 0 24 20
        # get_dom_attribute type: <class 'str'>
        # print(f'getattribute: {getattribute}')
        # print(f'getattribute type: {type(getattribute)}')

        back_previous_page()
        continue
        if str(view_box) == '0 0 22 18':
            back_previous_page()
            continue
        driver.find_element(By.CSS_SELECTOR,
                            'body > div.container.with-bg > section > '
                            'section.submit > div > div:nth-child(2) > div > svg').click()

        time.sleep(1)
        # 关闭当前页回到home页、前一页
        back_previous_page()
        time.sleep(4)
    pass


run()
