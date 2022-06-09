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
# el_likes = None
el_likes_num = 0


def loop():
    global el_likes_num
    el_likes = wait.until(
        lambda d: d.find_elements(By.CSS_SELECTOR, 'body > main > div > div > div > div.grid-box.grid-box'
                                                   '--3of4.content-left-container > div > div.posts > a'))

    # 无法点击，但属性有超链接
    url = el_likes[el_likes_num].get_attribute('href')
    # 直接点会重定向，要新打开页
    # 打开新标签页并切换到新标签页
    driver.switch_to.new_window('tab')
    driver.get(url)

    # el_likes[el_likes_num].click()
    el_likes_num += 1
    # original_window = driver.current_window_handle
    # 等待新窗口或标签页
    # wait.until(EC.number_of_windows_to_be(2))
    # 循环执行，直到找到一个新的窗口句柄
    # for window_handle in driver.window_handles:
    #     # print(f'asdasd: {window_handle}')
    #     # 一共两个，ok
    #     if window_handle != original_window:
    #         driver.switch_to.window(window_handle)
    #         break

    # 先点赞可以了，在这也不用睡觉
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        'body > div.container.with-bg > section > '
                                        'section.submit > div > div:nth-child(2) > div > svg')).click()

    # 已到点赞页，进行评论
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        'body > div.container.with-bg > section > '
                                        'section.submit > div > div.input-trigger')).click()
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        'body > div.container.with-bg > section > section.submit'
                                        ' > div > div.inner > div.input-wrapper > input[type=text]')).send_keys(
        '为你点赞，加油加油加加油！')
    # 点击发送
    driver.find_element(By.CSS_SELECTOR, 'body > div.container.with-bg > section > section.submit'
                                         ' > div > div.inner > div.submit-btn.btn').click()

    # 不知为啥，先点点赞
    # 点击点赞 p not
    # svg ok
    # Message: stale element reference: element is not attached to the page document

    # 过时的元素引用：元素未附加到页面文档
    # 错误原因：代码执行了click（），但是没有完成翻页，又爬了一次当前页，再执行翻页时页面已刷新，无法找到前面的翻页执行click()
    # 解决方法：click()后设置time.sleep()
    # 强制睡一会儿
    # 睡一会在执行下面得翻页
    # time.sleep(2)

    # 主要思路就在于，看报错信息是哪一行，就在那一行前面重新定位一下元素即可（不是再点一次吗），如果有循环存在，适当sleep一下，保证每个循环都能完美执行。
    # 或者先点赞先，搬到上面
    # 不得，我搬到上面了
    # wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
    #                                     'body > div.container.with-bg > section > '
    #                                     'section.submit > div > div:nth-child(2) > div > svg')).click()
    # wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
    #                                     'body > div.container.with-bg > section > '
    #                                     'section.submit > div > div:nth-child(2) > div > svg')).click()

    # ==========================
    # 关的很快，我再次点进去，也实现了，
    # ==========================
    # 关闭当前页回到home页、前一页
    time.sleep(2)
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
    global driver
    # driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    # wait = WebDriverWait(driver, WEB_DRIVER_WAIT_TIMEOUT)

    driver.get("https://www.yiban.cn/login?go=http%3A%2F%2Fwww.yiban.cn%2Fschool%2Findex%2Fid%2F460")

    wait.until(lambda d: d.find_element(By.ID, "account-txt")).send_keys('17776424705')
    # 同一个页第一等完，应该所有加载出来了
    driver.find_element(By.ID, "password-txt").send_keys('1.7776424705')
    driver.find_element(By.ID, "login-btn").click()
    # 重定向问题，重定向不用等，从http变为https
    driver.get("https://www.yiban.cn/school/index/id/460")
    driver.get("https://www.yiban.cn/school/index/id/460")

    for i in range(0, 51):
        webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()

    # 经常有网络问题，这里在refresh下
    # 最后做出的妥协，延时长短根据网速而定
    # time.sleep(2)
    driver.refresh()

    loop()
    loop()
    pass


run()
