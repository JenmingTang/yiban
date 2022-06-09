# 先进入 cmd
# 如果网络下载不了看看VPN（开或者关）

# selenium 4
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# option = webdriver.EdgeOptions()
# option.add_experimental_option("detach", True)


def run():
    global driver
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("https://www.yiban.cn/")
    elements = driver.find_elements(By.TAG_NAME, 'li')


if __name__ == '__main__':
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    el = WebDriverWait(driver, 10).until(lambda d: d.find_element_by_tag_name("p"))


    # run()
    # driver.get("https://www.yiban.cn/")
    # driver.implicitly_wait(2)
    # print(driver.title)
    # elements = driver.find_elements(By.CSS_SELECTOR, '#main-menu a')
    # for e in elements:
    #     print(e.text)
    #     if e.text == '优课YOOC':
    #         e.click()
    #         break
    # driver.implicitly_wait(2)
    # print(driver.title)
    # 这里！！！！实现不关闭的重点
    pass
    # option = webdriver.ChromeOptions()

    # ****************分割线**************

    # print(driver.title)
    # waiting page load
    # driver.implicitly_wait(0.5)
    # driver.implicitly_wait(0.5)
    # driver.implicitly_wait(3)
    # account-txt password-txt login-btn
    # lis = driver.find_element(By.CSS_SELECTOR, "#main-menu pull-left main-menu-item")
    # for e in elements:
    #     print(e.text)
    #     if e.text == '优课YOOC':
    #         e.click()
    #         break

    # print(lis.get_attribute('value'))
    # print(lis)
    # driver.find_element(By.ID, "account-txt").send_keys("17776424705")
    # driver.find_element(By.ID, "password-txt").send_keys("1.7776424705")
    # driver.find_element(By.ID, "login-btn").click()
    # driver.implicitly_wait(3)
    # print(driver.title)
    # driver.quit()
