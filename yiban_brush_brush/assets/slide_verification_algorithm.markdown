# 但失败了，从 selenium 转战 appuim 框架去了
# 模拟人滑动滑块
```
import random

# 通过加速减速模拟滑动轨迹
def moveTrack(xoffset):
    updistance = xoffset * 4 / 5
    # 速度
    t = 1
    v = 0
    steps_list = []
    current_offset = 0
    while current_offset < xoffset:
        if current_offset < updistance:
            a = 2 + random.random() * 2
        else:
            a = -random.uniform(12, 13)
            pass
        vo = v
        v = vo + a * t
        x = vo * t + 1 / 2 * a * (t * t)
        # 整数、小数
        x = round(x)
        current_offset += abs(x)
        steps_list.append(abs(x))
    pass

    # 上面的 sum(steps_list) 会比实际的大一点，所以再模拟一个往回拉的动作，补平多出来的距离
    disparty = sum(steps_list) - xoffset
    last1 = round(-random.random() - disparty, 2)
    last2 = round(-disparty - last1, 2)
    steps_list.append(last1)
    steps_list.append(last2)
    return steps_list


```
# 图片获取距离
```

    import time
    import cv2
    import requests


    download_image('https://castatic.fengkongcloud.cn/crb/set-000008-1.0.1-r1/v4/23d2fe0ed38fbb7d8e5c6805f41d3e44_bg.jpg', 'slider_background_image', '.jpg')
    download_image('https://castatic.fengkongcloud.cn/crb/set-000008-1.0.1-r1/v4/23d2fe0ed38fbb7d8e5c6805f41d3e44_fg.png', 'slider_image', '.png')
    time.sleep(2)
    img = cv2.imread("./image/slider_background_image.jpg", 0)  # 由于Canny只能处理灰度图，所以将读取的图像转成灰度图
    img = cv2.GaussianBlur(img, (3, 3), 0)  # 用高斯平滑处理原图像降噪。若效果不好可调节高斯核大小
    canny = cv2.Canny(img, 200, 600)  # 调用Canny函数，指定最大和最小阈值，其中apertureSize默认为3。
    img2 = cv2.imread("./image/slider_image.png", 0)  # 由于Canny只能处理灰度图，所以将读取的图像转成灰度图
    img2 = cv2.GaussianBlur(img2, (3, 3), 0)  # 用高斯平滑处理原图像降噪。若效果不好可调节高斯核大小
    canny2 = cv2.Canny(img2, 200, 600)  # 调用Canny函数，指定最大和最小阈值，其中apertureSize默认为3。
    # cv2.imshow('Canny', canny)
    # cv2.waitKey(1)
    # 匹配滑块在背景图的位置
    res = cv2.matchTemplate(img, img2, cv2.TM_CCOEFF_NORMED)
    # 获取位置
    location = cv2.minMaxLoc(res)
    # 那个2 是图片缩放比
    print(location[3][0]/2)
    print(location)
```