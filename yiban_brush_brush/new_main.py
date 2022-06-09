# author tang
# datetime 2022-04-22 13:25

# selenium 4
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys

import sys
import time
# 显示等
from selenium.webdriver.support import expected_conditions as e_c

import datetime

# print('2019-08-14 12:52:55.817273'[:-7])


WEB_DRIVER_WAIT_TIMEOUT = 10
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
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
        # integral 积分 experience 经验
        self.experience = 0
        # release 释放、发布 publish 发布
        self.publish_count = 0
        self.like_and_comment_count = 0


counter = Counter()


# 都是前面走得快，报错</div> is not clickable at point
# 明明测试时走一步过
#     time.sleep(1)

def loop_send_draft():
    time.sleep(2)
    # span 不能点击
    # 现在投稿页，它是一个新的标签页
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        "body > div > section > div.page-title > div.right > button > div")).click()

    # 投稿标题输入
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        "body > div.container > section > div.mdc-form.mdc-form--horizontal > "
                                        "div:nth-child(2) > div > input")).send_keys(
        "谢谢您，易班员")

    # 点击投稿页的选择链接
    driver.find_element(By.ID, "draftContentType2").click()
    # 等JS替换输入框
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        "body > div.container > section > div.mdc-form.mdc-form--horizontal > "
                                        "div:nth-child(4) > div > input")).send_keys(
        "https://s.yiban.cn/articles/detail")

    # 点击投稿
    driver.find_element(By.CSS_SELECTOR, "body > div.container > section > div.actions > div > "
                                         "button:nth-child(2) > div").click()

    # 如果在规定时间内网页加载完成,则执行下一步（隐式等）
    # 建议强制等，我用隐式还会报，可能设置时间不够大
    # driver.implicitly_wait(1)
    # sleep 1 seconds 到第三次报错
    # time.sleep(2) 这也报，后给一个不存在的selector div
    # 等页面刷新并点击返回列表
    time.sleep(3)
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        "body > div.container > section > div.mdc-alert.mdc-alert--success > "
                                        "div > p > a:nth-child(1) > div.mdc-button__ripple")).click()
    # 不得
    # time.sleep(1)
    # wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
    #                                     "body > div.container > section > div.mdc-alert.mdc-alert--success > "
    #                                     "div > p > a:nth-child(1) > div.mdc-button__ripple")).send_keys(Keys.ENTER)
    # 'body > div.container > section > div.mdc-alert.mdc-alert-
    # -success > div > p > a:nth-child(1) > div.mdc-button__ripple'
    # 等页面刷新并点击删除记录
    time.sleep(1)
    btn_delete = 'body > div.container > section > div.mdc-data-table.mdc-data-table--full' \
                 'width > div.mdc-data-table__table-container > table > t' \
                 'body > tr > td:nth-child(5) > a:nth-child(3) > div.mdc-button__ripple'
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        btn_delete)).click()
    # span 不能点击 div、button 能
    # 等页面刷新并点击确认删除
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        "body > div.mdc-confirm-dialog.mdc-dialog.mdc-dialog--open > div.mdc-dialog"
                                        "__container > div > footer > button.mdc-button.mdc-button--"
                                        "raised.mdc-confirm-dialog__primary-button")).click()
    pass


def micro_community_likes_and_comments():
    # 经常有网络问题，这里再refresh下
    # 最后做出的妥协，延时长短根据网速而定
    # 该页本来就存在（home、第一页）
    # time.sleep(1)
    # driver.refresh()
    # 0~80
    # 大概 19个()没加sleep前
    for i in range(0, 99):
        webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
        time.sleep(0.2)
    #     给两秒加载图片
    time.sleep(2)
    # 切换了页面，留了状态，这界面一直活着
    global el_likes
    el_likes = wait.until(
        lambda d: d.find_elements(By.CSS_SELECTOR, 'body > main > div > div > div > div.grid-box.grid-box'
                                                   '--3of4.content-left-container > div > div.posts > a'))

    pass


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


def loop_micro_community_like():
    global el_likes_num
    #  list index out of range（去按下箭头键多点，加载多点）
    # 无法点击，但属性有超链接
    try:
        url = el_likes[el_likes_num].get_attribute('href')
    except IndexError:
        print('except IndexError: list index out of range')
        print('exit')
        driver.quit()
        sys.exit()
    finally:
        # 无论try是否，这都走
        pass
    el_likes_num += 1
    # 直接点会重定向，要新打开页
    # 打开新标签页并切换到新标签页
    driver.switch_to.new_window('tab')
    driver.get(url)
    # el_likes[el_likes_num].click()
    # original_window = driver.current_window_handle
    # 等待新窗口或标签页
    # wait.until(EC.number_of_windows_to_be(2))
    # 循环执行，直到找到一个新的窗口句柄
    # for window_handle in driver.window_handles:
    #     # print(f't: {window_handle}')
    #     # 一共两个，ok
    #     if window_handle != original_window:
    #         driver.switch_to.window(window_handle)
    #         break

    # 先点赞可以了，在这也不用睡觉 viewBox="" 0 0 24 20 0 0 22 18
    # get_dom_attribute
    # get_dom_attribute: 0 0 24 20
    # get_dom_attribute type: <class 'str'>
    view_box = wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                                   'body > div.container.with-bg > section > '
                                                   'section.submit > div > div:nth-'
                                                   'child(2) > div > svg')).get_dom_attribute(
        'viewBox')
    if view_box == '0 0 22 18':
        # 关闭当前页回到home页、前一页
        back_previous_page()
        return

    counter.count += 1
    counter.experience += 2
    counter.like_and_comment_count += 1

    driver.find_element(By.CSS_SELECTOR,
                        'body > div.container.with-bg > section > '
                        'section.submit > div > div:nth-child(2) > div > svg').click()
    time.sleep(1)

    # 已到点赞页，进行评论
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR,
                                        'body > div.container.with-bg > section > '
                                        'section.submit > div > div.input-trigger')).click()
    time.sleep(1)
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
    time.sleep(2)
    # 关闭当前页回到home页、前一页
    back_previous_page()
    pass


def switch_to_a_new_label():
    # 存储原始窗口的 ID
    original_window = driver.current_window_handle
    # 等待新窗口或标签页
    wait.until(e_c.number_of_windows_to_be(2))
    # 循环执行，直到找到一个新的窗口句柄
    for window_handle in driver.window_handles:
        # print(f't: {window_handle}')
        # 一共两个，ok
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    pass


# 20 次投稿 32次点赞、评论
def loop():
    while True:
        if counter.count <= 19:
            # 有滑动验证了

            # loop_send_draft()
            # counter.experience += 5
            # counter.publish_count += 1
            counter.count += 1
            if counter.count == 20:
                # 关闭当前页回到home页、前一页
                back_previous_page()
                # print('初始化，去做微社区点赞事,这只走一次')
                # print(counter)
                micro_community_likes_and_comments()
        elif 20 <= counter.count <= 52:
            # elif 1 <= counter.count < 30:
            # elif 1 <= counter.count < 2:

            # else:
            # print('循环微社区点赞')
            # print(counter)
            loop_micro_community_like()
            # 在真的走了的地方加 experience
            pass
        else:
            print('exit')
            driver.quit()
            sys.exit()
        print(counter)
        time.sleep(59)
    pass


def execute(username, password):
    # 防止自动关闭 browser，方法持有它吧
    global driver
    # driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    # global wait
    # wait = WebDriverWait(driver, WEB_DRIVER_WAIT_TIMEOUT)
    # 执行

    driver.get("https://www.yiban.cn/login?go=http%3A%2F%2Fwww.yiban.cn%2Fschool%2Findex%2Fid%2F460")

    wait.until(lambda d: d.find_element(By.ID, "account-txt")).send_keys(username)
    # 同一个页第一等完，应该所有加载出来了
    driver.find_element(By.ID, "password-txt").send_keys(password)
    driver.find_element(By.ID, "login-btn").click()
    # 重定向问题，重定向不用等，从http变为https
    driver.get("https://www.yiban.cn/school/index/id/460")
    driver.get("https://www.yiban.cn/school/index/id/460")
    # 点击发布
    wait.until(lambda d: d.find_element(By.ID, "y-publish")).click()
    # 点击投稿
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR, "#i-publish > li:nth-child(2) > a > b")).click()
    # 却换到新标签
    switch_to_a_new_label()
    # 循环投稿
    # MyThread(1, "thread_of_threadID=1", 59).start()
    loop()
    pass


def entrance():
    if len(sys.argv) >= 3:
        execute(sys.argv[1], sys.argv[2])
    else:
        print('无参数输入或少了参数，输入账号密码')


entrance()
