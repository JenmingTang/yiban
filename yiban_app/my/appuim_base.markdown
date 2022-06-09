# js（单线程） 等待那，很麻烦，去搞 python 了

# miscellaneous 杂项
```
??
0.0.0.0 == 127.0.0.1 == localhost


```
# 模拟器
```

覆盖下 用Android SDK 的adb.exe 覆盖夜神模拟器目录的nox_adb.exe
覆盖下 用Android SDK 的adb.exe 覆盖夜神模拟器目录的nox_adb.exe
覆盖下 用Android SDK 的adb.exe 覆盖夜神模拟器目录的nox_adb.exe


36 为夜神模拟器的adb.exe 41为Android SDK
adb server version (36) doesn't match this client (41); killing...
adb.exe 不能同时两个
用Android SDK的adb服务连接模拟器
用Android SDK的adb服务连接模拟器
用Android SDK的adb服务连接模拟器



1 打开夜神模拟器
2 到它安装目录
3 用它的adb 查看夜神模拟器设备 adb devices
4 开Android sdk的adb，先执行一次 adb devices
4 开Android sdk的adb，先执行一次 adb devices



这是Android SDK的adb
C:\Users\tang>adb connect 127.0.0.1:62001
connected to 127.0.0.1:62001
```
# 环境
```
ANDROID_HOME
    C:\Users\tang\AppData\Local\Android\Sdk

JAVA_HOME
    C:\Program Files\Java\jdk-16.0.2

path
    node.js
        自带npm
        D:\software\node-v16.14.2-win-x64

    adb
    C:\Users\tang\AppData\Local\Android\Sdk\platform-tools

    aapt
    C:\Users\tang\AppData\Local\Android\Sdk\build-tools\31.0.0
```
# 命令
```
aapt dump badging ApiDemos-debug.apk
    能拿到 包名、启动activity

adb connect 127.0.0.1:5000
    将adb连接到模拟器（安卓原生模拟器自动会连接）

adb devices
    查看adb连接的设备
    能拿到 设备名
```
# 其他语言客户端
```
https://appium.io/docs/en/about-appium/appium-clients/index.html


https://github.com/appium/python-client
https://github.com/appium/java-client
```

# 操作流程
```
1 下载 appuim 服务端
    npm
        -g 为global，下载到npm环境变量那，不是在本项目文件夹
        npm install -g appium --registry http://registry.npmmirror.com

    desktop


2 启动服务端
    他在node.js的根文件夹下，前面配了node.js环境变量
    ，所以可以直接cmd appuim 启动


3 项目客户端
    1 新建个文件夹
    2 在它肚子里 npm init -y
    3 npm install webdriverio
    4 在文件夹肚子里新建 xx.js
    5 在下个markdown代码块
    5 在下个markdown代码块
    5 在下个markdown代码块
    6 node xx.js

```
>xx.js

```javascript
// 下面选项是必要的
// 下面选项是必要的
        // 都得
        // deviceName: "cannon",//cmd adb devices -l看
        // deviceName: "127.0.0.1:62001",//cmd adb devices看
// javascript

const wdio = require("webdriverio");
const assert = require("assert");

const opts = {
  path: '/wd/hub',
  port: 4723,
  capabilities: {
    platformName: "Android",
    platformVersion: "8",//改我，在模拟器设置看
    deviceName: "Android Emulator",//cmd adb devices 看
    // app 可无，具体看文档
    // app: "/path/to/the/downloaded/ApiDemos-debug.apk",
    // cmd aapt dump badging ApiDemos-debug.apk
    // ApiDemos-debug.apk 在模拟器已安装，建议处理好首次启动配置
    appPackage: "io.appium.android.apis",
    // cmd aapt dump badging ApiDemos-debug.apk
    appActivity: ".view.TextFields",
    automationName: "UiAutomator2"，
    noReset:true
  }
};

async function main () {
  const client = await wdio.remote(opts);

  const field = await client.$("android.widget.EditText");
  await field.setValue("Hello World!");
  const value = await field.getText();
  assert.strictEqual(value,"Hello World!");

  await client.deleteSession();
}

main();
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



确保手机安装有被测app
确保手机安装有被测app
确保手机安装有被测app

可以配置 onReset=true，会保留数据，不重置
每次启动都跟重新安装一样，把我易班清完数据（用模拟器有性能问题）
每次启动都跟重新安装一样

```


# 坑
```
appium inspector
    Error Failed to create session. Unexpected end of JSON input
        将host改为127.0.0.1，服务得为0.0.0.0或127.0.0.1


```
# 找元素
```java
UiAutomator2 只有UiSelector类和那个content descriptionID用


现用xPath（有性能问题）
```