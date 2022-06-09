# author tang
# datetime 2022-04-22 13:25
from optparse import Option

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import sys
import time
from selenium.webdriver.support import expected_conditions as e_c
import datetime

WEB_DRIVER_WAIT_TIMEOUT = 10
from selenium.webdriver.edge.options import Options

options = Options()
# 需将msedgedriver_v100添加到环境变量，环境变量只能添加文件夹
# ================================================
# selenium.common.exceptions.WebDriverException: Message: unknown error: MSEdge failed to start: was killed
# 将 driver = webdriver.Edge(options=options)
# 换为 driver = webdriver.Edge(r"D:\workspace\projects\python\yiban\yiban_brush_brush\assets\msedgedriver.exe")
# ================================================
options.binary_location = r"D:\workspace\projects\python\yiban\yiban_brush_brush\assets\msedgedriver.exe"
# driver = webdriver.Edge(options=options)
driver = webdriver.Edge(r"D:\workspace\projects\python\yiban\yiban_brush_brush\assets\msedgedriver.exe")
# driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
wait = WebDriverWait(driver, WEB_DRIVER_WAIT_TIMEOUT)
el_likes = []
el_likes_num = 0


class Counter:

    def __str__(self) -> str:
        return f'count: {self.count} experience: {self.experience}  publish_count: {self.publish_count} like_' \
               f'and_comment_count: {self.like_and_comment_count} datetime: {datetime.datetime.now().__str__()[:-7]}'

    def __init__(self) -> None:
        # 有滑动验证了

        self.count = 19
        self.experience = 0
        self.publish_count = 0
        self.like_and_comment_count = 0


counter = Counter()


def loop_send_draft():
    time.sleep(2)
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        "body > div > section > div.page-title > div.right > button > div")).click()
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        "body > div.container > section > div.mdc-form.mdc-form--horizontal > "
                                        "div:nth-child(2) > div > input")).send_keys(
        "谢谢您，易班员")
    driver.find_element(By.ID, "draftContentType2").click()
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        "body > div.container > section > div.mdc-form.mdc-form--horizontal > "
                                        "div:nth-child(4) > div > input")).send_keys(
        "https://s.yiban.cn/articles/detail")
    driver.find_element(By.CSS_SELECTOR, "body > div.container > section > div.actions > div > "
                                         "button:nth-child(2) > div").click()
    time.sleep(3)
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        "body > div.container > section > div.mdc-alert.mdc-alert--success > "
                                        "div > p > a:nth-child(1) > div.mdc-button__ripple")).click()

    time.sleep(1)
    btn_delete = 'body > div.container > section > div.mdc-data-table.mdc-data-table--full' \
                 'width > div.mdc-data-table__table-container > table > t' \
                 'body > tr > td:nth-child(5) > a:nth-child(3) > div.mdc-button__ripple'
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        btn_delete)).click()
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        "body > div.mdc-confirm-dialog.mdc-dialog.mdc-dialog--open > div.mdc-dialog"
                                        "__container > div > footer > button.mdc-button.mdc-button--"
                                        "raised.mdc-confirm-dialog__primary-button")).click()


def micro_community_likes_and_comments():
    # 进了
    # print("++++++++++++++++++++++++++++++++")
    # print("++++++++++++++++++++++++++++++++")
    # print("++++++++++++++++++++++++++++++++")
    for i in range(0, 149):
        # print(f'i: {i}', end=' ')
        time.sleep(0.3)
        webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
    time.sleep(2)
    global el_likes
    el_likes = wait.until(
        lambda d: d.find_elements(By.CSS_SELECTOR, 'body > main > div > div > div > div.grid-box.grid-box'
                                                   '--3of4.content-left-container > div > div.posts > a'))


def back_previous_page():
    original_window = driver.current_window_handle
    driver.close()
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break


def loop_micro_community_like():
    global el_likes_num
    try:
        url = el_likes[el_likes_num].get_attribute('href')
    except IndexError:
        print('except IndexError: list index out of range')
        print('exit')
        driver.quit()
        sys.exit()
    el_likes_num += 1
    driver.switch_to.new_window('tab')
    driver.get(url)
    time.sleep(2)
    view_box = wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                                   'body > div.container.with-bg > section > '
                                                   'section.submit > div > div:nth-'
                                                   'child(2) > div > svg')).get_dom_attribute(
        'viewBox')
    if view_box == '0 0 22 18':
        back_previous_page()
        return
    counter.count += 1
    counter.experience += 2
    counter.like_and_comment_count += 1
    driver.find_element(By.CSS_SELECTOR,
                        'body > div.container.with-bg > section > '
                        'section.submit > div > div:nth-child(2) > div > svg').click()
    time.sleep(3)
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        'body > div.container.with-bg > section > '
                                        'section.submit > div > div.input-trigger')).click()
    time.sleep(1)
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        'body > div.container.with-bg > section > section.submit'
                                        ' > div > div.inner > div.input-wrapper > input[type=text]')).send_keys(
        '为你点赞，加油加油加加油！')
    driver.find_element(By.CSS_SELECTOR, 'body > div.container.with-bg > section > section.submit'
                                         ' > div > div.inner > div.submit-btn.btn').click()
    time.sleep(2)
    back_previous_page()


def switch_to_a_new_label():
    original_window = driver.current_window_handle
    wait.until(e_c.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break


def loop():
    while True:
        if counter.count <= 19:
            # 有滑动验证了
            # 进了
            # print('有滑动验证了')
            # print('有滑动验证了')
            # print('有滑动验证了')
            # loop_send_draft()
            # counter.experience += 5
            # counter.publish_count += 1
            counter.count += 1
            if counter.count == 20:
                # back_previous_page()
                micro_community_likes_and_comments()
        elif 20 <= counter.count <= 52:
            loop_micro_community_like()
        else:
            print('exit')
            driver.quit()
            sys.exit()
        print(counter)
        time.sleep(59)


def execute(username, password):
    global driver
    driver.get("https://www.yiban.cn/login?go=http%3A%2F%2Fwww.yiban.cn%2Fschool%2Findex%2Fid%2F460")
    wait.until(lambda d: d.find_element(By.ID, "account-txt")).send_keys(username)
    driver.find_element(By.ID, "password-txt").send_keys(password)
    driver.find_element(By.ID, "login-btn").click()
    driver.get("https://www.yiban.cn/school/index/id/460")
    driver.get("https://www.yiban.cn/school/index/id/460")
    # wait.until(lambda d: d.find_element(By.ID, "y-publish")).click()
    # wait.until(lambda d: d.find_element(By.CSS_SELECTOR, "#i-publish > li:nth-child(2) > a > b")).click()
    # switch_to_a_new_label()
    loop()


def entrance():
    if len(sys.argv) >= 3:
        execute(sys.argv[1], sys.argv[2])
    else:
        print('无参数输入或少了参数，输入账号密码')


# entrance()
execute('17776424705', '1.7776424705')
