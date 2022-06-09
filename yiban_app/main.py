# Android environment
import datetime
import sys
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from my.assets import title_and_content as tc


class Counter:

    def __str__(self) -> str:
        return f'count: {self.count} publish_count: {self.publish_count} comment_count: {self.comment_count} ' \
               f'experience :{self.experience} datetime: {datetime.datetime.now().__str__()[:-7]}'

    def __init__(self) -> None:
        self.count = 0
        self.publish_count = 0
        self.comment_count = 0
        self.experience = 0


counter = Counter()

desired_caps = dict(
    platformName='Android',
    platformVersion='7.1.2',
    appPackage='com.yiban.app',
    appActivity='com.yiban.app.activity.WelcomeActivity',
    noReset=True,
    automationName='uiautomator2',
    deviceName='Android Emulator',
    chromedriverExecutable=r'D:\workspace\projects\python\yiban_app\my\chromedriver_v92.0.4515.107.exe'
)

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)


def swipe_scroll():
    swipe_count = 0
    while swipe_count < 15:
        swipe_count += 1
        driver.swipe(300, 700, 300, 200)
        time.sleep(0.5)
    pass


def touch_tap(x, y, duration=50):  # 点击坐标  ,x1,x2,y1,y2,duration
    """

    method explain:点击坐标
    parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
    Usage:
        device.touch_coordinate(277,431)      #277.431为点击某个元素的x与y值
    :param x:
    :param y:
    :param duration:
    :return:
    """
    screen_width = driver.get_window_size()['width']  # 获取当前屏幕的宽
    screen_height = driver.get_window_size()['height']  # 获取当前屏幕的高
    a = (float(x) / screen_width) * screen_width
    x1 = int(a)
    b = (float(y) / screen_height) * screen_height
    y1 = int(b)
    driver.tap([(x1, y1), (x1, y1)], duration)
    pass


old_window_handle = []
new_window_handle = []

every_handle = []


def micro_community_comments():
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                        value='new UiSelector().resourceId("com.yiban.app:id/home_bottom_item_title")'
                              '.className("android.widget.TextView").text("互动")').click()
    time.sleep(3)
    # 点击杂谈
    web_view = driver.contexts[1]
    driver.switch_to.context(web_view)

    driver.find_element(by=AppiumBy.CSS_SELECTOR,
                        value='body > div.container.with-bg > section > div.posts-container.box > '
                              'div.post-nav > div > nav > li:nth-child(7)').click()
    time.sleep(2)
    # driver.switch_to.context('NATIVE_APP')
    try:
        # 滑动屏幕，在webview无法滑动
        # 可能会报错
        swipe_scroll()
    except:
        swipe_scroll()
        pass
    # 这里也可能报错，现sleep下
    time.sleep(3)
    # web_view = driver.contexts[1]
    # driver.switch_to.context(web_view)
    # like_items = driver.find_elements(by=AppiumBy.CSS_SELECTOR,
    #                                   value='body > div.container.with-bg > section > div.posts-container.box '
    #                                         '> div.posts > div')

    like_items_count = 5
    # webview 句柄
    webview_handle = 1
    webview_handle_length = 0
    while counter.comment_count < 33:
        # while counter.comment_count < 1:
        """
        莓开一个webview产生一个新的句柄，close() back() 方法也都不能用，那安卓的返回并没有杀死webview句柄
        莓开一个webview产生一个新的句柄，close() back() 方法也都不能用，那安卓的返回并没有杀死webview句柄
        莓开一个webview产生一个新的句柄，close() back() 方法也都不能用，那安卓的返回并没有杀死webview句柄
            
每次进都走driver.window_handles: ['CDwindow-1E87477C238AB6A00AE39AEA542D6D2F']
driver.window_handles: ['CDwindow-1E87477C238AB6A00AE39AEA542D6D2F', 'CDwindow-6FA505A28F3EB8B511E575180FE2B905']
view_box: 0 0 24 20
count: 1 publish_count: 0 comment_count: 1 experience :2 datetime: 2022-05-02 23:52:02
每次进都走driver.window_handles: ['CDwindow-1E87477C238AB6A00AE39AEA542D6D2F', 'CDwindow-6FA505A28F3EB8B511E575180FE2B905']
driver.window_handles: ['CDwindow-1E87477C238AB6A00AE39AEA542D6D2F', 'CDwindow-6FA505A28F3EB8B511E575180FE2B905',
 'CDwindow-7FC43BB81C21DB198E91830100916366']
        """
        #
        web_view = driver.contexts[1]
        driver.switch_to.context(web_view)
        # print(f'每次进都走driver.window_handles: {driver.window_handles}')
        # 每次开webview都新建句柄，0 号是最初的,0 号句柄一直不会变，这里 ok
        # driver.switch_to.window(driver.window_handles[0])
        # 点击跳转，会产生第二个webview，一个chromedriver管两个webview
        # 切换回webview句柄和webview context 还是能摸到它
        # 切换回webview句柄和webview context 还是能摸到它
        # 切换回webview句柄和webview context 还是能摸到它
        # 存状态
        # 说什么该元素不能交互？？，前面的又得
        # try:

        like_items = driver.find_elements(by=AppiumBy.CSS_SELECTOR,
                                          value='body > div.container.with-bg > section > div.posts-container.box '
                                                '> div.posts > div')
        like_items[like_items_count].click()
        like_items_count += 1
        # except:
        #     continue
        #     pass
        time.sleep(3)
        # ！！！在webview context 才能调，记得看下有多少个webview
        # print(f'driver.window_handles: {driver.window_handles}')
        # 每次都新建句柄，所以这里递增数组（列表）
        # driver.switch_to.window(driver.window_handles[1])
        # =======================================
        """
            报了个下标越界，可能是打开了打开过的页面 set 装不重复的
            判断driver.window_handles长度有没有自增，有就改句柄，没就关闭页面，开下个循环
            
            它是把前一个句柄杀了，不是不会杀的吗
                        
driver.window_handles: ['CDwindow-E01AB5E1C8553D582B207E51FFC55DE4', 'CDwindow-72B25E278F09EADA641261642D61890D', 'CDwindow-57CAF6422681CB1766027F8C235B8B6F']
count: 2 publish_count: 0 comment_count: 2 experience :4 datetime: 2022-05-03 00:40:51
driver.window_handles: ['CDwindow-E01AB5E1C8553D582B207E51FFC55DE4', 'CDwindow-72B25E278F09EADA641261642D61890D', 'CDwindow-AB20EA1F4EB5EC1F9092D5233976804C']

        """
        last_handle = driver.window_handles[-1:].__str__()[2:-2]

        # 如果该句柄已走过，开下个循环
        if every_handle.count(last_handle) != 0:
            time.sleep(2)
            comment_back_to_home()
            time.sleep(2)
            continue
            pass

        # 存下每次的句柄
        every_handle.append(last_handle)
        driver.switch_to.window(last_handle)
        # ++++++++++++++++++++++++++++++++++++
        """
        ok ok ok 了
driver.window_handles: ['CDwindow-A5ADBEFCF3CC45661BCB59123F2604A3', 'CDwindow-9978AD1407F5F058EAD3B69D54E2A102', 'CDwindow-B3571875719D08F1EBC24EA2602348D1', 'CDwindow-DA9E5DB2054B9C0A9ED09E7CECE2521F', 'CDwindow-DCF998EF4687266CA4B3C5585DCE4556', 'CDwindow-AA1A1C0B4A26C7798329CD35277B4B2D', 'CDwindow-AD7CD50265BD4ECA5CC4A16DDB460C42']
count: 8 publish_count: 0 comment_count: 8 experience :16 datetime: 2022-05-03 12:03:05
driver.window_handles: ['CDwindow-A5ADBEFCF3CC45661BCB59123F2604A3', 'CDwindow-AD7CD50265BD4ECA5CC4A16DDB460C42', 'CDwindow-FBA3CAEA65E6154C53A425F9FEB22AFE']
        """
        # ++++++++++++++++++++++++++++++++++++
        # print(f'comment driver.window_handles: {driver.window_handles}')

        # 总之，上面新开有webview的界面就要加一，当然，这不会越界
        # webview_handle += 1
        # =======================================
        view_box = driver.find_element(by=AppiumBy.CSS_SELECTOR,
                                       value='body > div.container.with-bg > section > section.submit '
                                             '> div > div:nth-child(2) > div > svg').get_dom_attribute(
            'viewBox')
        # print(f'view_box: {view_box}')
        if view_box == '0 0 22 18':
            time.sleep(2)
            comment_back_to_home()
            time.sleep(2)
            continue
        # 这里也报过错 element click intercepted
        # 这里也报过错 element click intercepted
        # 这里也报过错 element click intercepted
        time.sleep(2)
        driver.find_element(by=AppiumBy.CSS_SELECTOR,
                            value='body > div.container.with-bg > section > section.submit > div > '
                                  'div:nth-child(2) > div > svg').click()
        time.sleep(2)
        # 先取消评论，搞点赞，测试用
        driver.find_element(by=AppiumBy.CSS_SELECTOR,
                            value='body > div.container.with-bg > section > section.submit > div > div.input-trigger') \
            .click()
        time.sleep(2)
        driver.find_element(by=AppiumBy.CSS_SELECTOR,
                            value='body > div.container.with-bg > section > section.submit > div > div.inner > '
                                  'div.input-wrapper > input[type=text]').send_keys('为你点赞，加油加油加加油！')
        time.sleep(2)
        driver.find_element(by=AppiumBy.CSS_SELECTOR,
                            value='body > div.container.with-bg > section > section.submit > div > div.inner > '
                                  'div.submit-btn.btn > svg').click()
        time.sleep(3)
        counter.comment_count += 1
        counter.count += 1
        counter.experience += 2
        print(counter)
        comment_back_to_home()

        # =========================
        # time.sleep(2)
        # web_view = driver.contexts[1]
        # driver.switch_to.context(web_view)
        # 还有两个webview
        # print(f'driver.window_handles: {driver.window_handles}')
        # print(f'driver.window_handles: {driver.window_handles}')
        # print(f'driver.window_handles: {driver.window_handles}')

        # =========================
        # 上面共 9 秒
        time.sleep(49)
        # time.sleep(3)
        pass
    pass


def comment_back_to_home():
    driver.switch_to.context('NATIVE_APP')
    # 点击返回home页面
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                        value='new UiSelector().resourceId("com.yiban.app:id/'
                              'widget_custom_titlebar_back_btn")'
                              '.className("android.widget.ImageButton")').click()


# 点了不生效，可能没进入webview
# touch_tap(280, 500)
# touch_tap(280, 500)

flag_publish = True


# 微社区发布
def micro_community_publish():
    publish_handle_flag = True
    # time.sleep(2)
    # webview = driver.contexts[1]
    # driver.switch_to.context(webview)
    # handles = driver.window_handles
    # time.sleep(2)
    # driver.switch_to.context('NATIVE_APP')

    while counter.publish_count < 20:
        # while counter.publish_count < 2:
        time.sleep(3)
        # 下面报过元素为加载到页面
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                            value='new UiSelector().text("发布").className("android.widget.TextView")').click()
        time.sleep(0.5)
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                            value='new UiSelector().text("微社区").className("android.widget.TextView")').click()
        time.sleep(0.5)
        # 弹出是否重新编辑，选是
        try:
            driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                value='new UiSelector().resourceId("com.yiban.app:id/tv_positive")'
                                      '.text("是").className("android.widget.TextView")').click()
        except:
            pass

        time.sleep(3)
        webview = driver.contexts[1]
        driver.switch_to.context(webview)
        # global flag_publish
        # if flag_publish:
        #     flag_publish = False
        #     for x in driver.window_handles:
        #         if handles.count(x) != 0:
        #             driver.switch_to.window(x)
        #             pass
        #
        #         pass
        # ==================================================
        """
            前面评论哪里处理了webview句柄
            我切过来就找不到元素了？？article_title
        """
        # ==================================================
        # 只走一次，取回发布的句柄
        # print(f'driver.window_handles: {driver.window_handles}')
        # driver.switch_to.window(driver.window_handles[-1:].__str__()[2:-2])

        # 因为有时 在0位有时在最后位
        # +++++++++++++++++++++++
        # print(f'啊啊啊every_handle:{every_handle}')
        # print(f'啊啊啊driver.window_handles:{driver.window_handles}')
        # for i in driver.window_handles:
        #     if every_handle.count(i) == 0:
        #         print(i)
        #         print(i)
        #         driver.switch_to.window(i)
        #         break
        #         pass
        #     pass

        # +++++++++++++++++++++++

        # last_handle = driver.window_handles[-1:].__str__()[2:-2]
        # # 如果该句柄已走过，开下个循环
        # if every_handle.count(last_handle) != 0:
        #     comment_back_to_home()
        #     time.sleep(1)
        #     continue
        #     pass
        # if publish_handle_flag:
        #     publish_handle_flag = False
        #     driver.switch_to.window(driver.window_handles[0])
        #     pass

        # article_title
        # article_content
        driver.find_element(by=AppiumBy.CSS_SELECTOR, value='#article_title').clear()
        driver.find_element(by=AppiumBy.CSS_SELECTOR, value='#article_content').clear()
        time.sleep(0.5)
        driver.find_element(by=AppiumBy.CSS_SELECTOR, value='#article_title').send_keys(
            tc[counter.publish_count]['title'])
        driver.find_element(by=AppiumBy.CSS_SELECTOR, value='#article_content') \
            .send_keys(tc[counter.publish_count]['content'])
        driver.switch_to.context('NATIVE_APP')
        time.sleep(0.5)
        # 点下一步
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                            value='new UiSelector().text("下一步").resourceId("com.yiban.app:id/tv_more")'
                                  '.className("android.widget.TextView")').click()
        time.sleep(0.5)
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                            value='new UiSelector().resourceId("com.yiban.app:id/iv_more")'
                                  '.className("android.widget.ImageView")').click()
        counter.count += 1
        counter.publish_count += 1
        counter.experience += 5
        print(counter)
        time.sleep(55)
        pass  # while end
    pass


# 先搞评论
# micro_community_comments()
"""
    到发布时，句柄直接替换了 0 号位？？
    到发布时，句柄直接替换了 0 号位？？
    到发布时，句柄直接替换了 0 号位？？在首次打开输入title时
    comment driver.window_handles: ['CDwindow-EC0B72E1E071A236269C372AEC792E51', 'CDwindow-A2346D4BA74ABCC3E659C4E922807A34', 'CDwindow-409B9FF76DBCA4BF4A6C385FE0D77171']
count: 2 publish_count: 0 comment_count: 2 experience :4 datetime: 2022-05-03 12:55:41
driver.window_handles: ['CDwindow-A6C1052F0736AFA1CBDCE52F2853CA82', 'CDwindow-EC0B72E1E071A236269C372AEC792E51', 'CDwindow-A2346D4BA74ABCC3E659C4E922807A34']
Traceback (most recent call last):
"""
# 决定终止会话，新建一个，不想搞webview句柄了，一开始就是直接搞发布的
# driver.quit()
# time.sleep(10)
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# time.sleep(10)
micro_community_publish()

# 微社区点赞操作
# Android recycler view 会回收view
# view_box = ''
"""
    Android recycler view 会回收view
    无法实现
    无法实现
    无法实现
"""
print('exit')
driver.quit()
sys.exit()
