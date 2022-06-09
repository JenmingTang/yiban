# 步骤
```python
1 # cmd 启动官网的下载的adb桥接服务
    -g 为global，下载到npm环境变量那，不是在本项目文件夹
    cmd：npm install -g appium --registry http://registry.npmmirror.com
    
    cmd：appium


2 # 下载夜神模拟器
    # 安装目录下 nox_adb.exe 替换为 sdk 的 adb.exe 
    https://support.yeshen.com/zh-CN/qt/ml
    
    # 安装 Xposed 框架
    https://support.yeshen.com/zh-CN/qt/xp

    # 推荐XPosed模块【可选】
    https://support.yeshen.com/zh-CN/often/xposed

    # 关闭Hyper-x服务
    https://support.yeshen.com/zh-CN/qt/Hyper

    # 摸 tomcat【可选】
    https://support.yeshen.com/zh-CN/qt/tomcat

3 # 启动夜神模拟器
    安装 被测 apk ，注意版本对应 

4 查看 sdk 的 adb 是否连接到模拟器
    cmd：adb devices
    cmd：adb connect 127.0.0.1:62001

5 查看 apk 的包名和可启动活动
    # aapt 在sdk 目录工具里
    cmd：aapt dump badging ApiDemos-debug.apk

6 编写客户端



```
# 6 编写客户端
```python

from appium import webdriver

desired_caps = dict(
    platformName='Android',
    platformVersion='7.1.2',
    appPackage='com.yiban.app',
    appActivity='com.yiban.app.activity.WelcomeActivity',
    # 留着数据，不会重置app
    noReset=True,
    automationName='uiautomator2',
    # 乱填的
    deviceName='Android Emulator',
    # 在 7 webview 处理介绍
    chromedriverExecutable=r'D:\workspace\projects\python\yiban_app\my\chromedriver_v92.0.4515.107.exe'
)

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)
driver.quit()
```

# 7 webview
```

    1 chrome browser 输入 chrome://inspect/#devices
    2 模拟器打开被测app，安装了的，打开有 webview 页
    3 查看 app chromedriver 版本号
    4 https://chromedriver.chromium.org/downloads 下载对应版本号驱动文件
    chromedriverExecutable=r'D:\workspace\projects\python\yiban_app\my\chromedriver_v92.0.4515.107.exe'




    
    web_view = driver.contexts[1]
    driver.switch_to.context(web_view)
    driver.switch_to.context('NATIVE_APP')



    
        # 每次开webview都新建句柄，0 号是最初的,0 号句柄一直不会变，这里 ok
        driver.switch_to.window(driver.window_handles[0])

```


# 找元素
```


from appium.webdriver.common.appiumby import AppiumBy
原生
    
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                        value='new UiSelector().resourceId("com.yiban.app:id/home_bottom_item_title")'
                              '.className("android.widget.TextView").text("互动")').click()




webview
    
    driver.find_element(by=AppiumBy.CSS_SELECTOR,
                        value='body > div.container.with-bg > section > div.posts-container.box > '
                              'div.post-nav > div > nav > li:nth-child(7)').click()
```
# 其他

```python

desktop
    # 启动官网的下载的adb桥接服务
    appium_application
    # 原生元素查看器，sdk的UIXX用不了
    appium_inspect_application
```


# 坑
```
appium inspector
    Error Failed to create session. Unexpected end of JSON input
        将host改为127.0.0.1，服务得为0.0.0.0或127.0.0.1


```

# 真机环境
```
开发者选项
developer option
    open
        USB debugging
        Install via USB
            回去通过USB安装以下三个app
                Appium Settings
                io.appium.uiautomator2.server
                io.appium.uiautomator2.server.test
        USB debugging（Security settings）

```