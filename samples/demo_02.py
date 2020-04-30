import os,time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from common.base_page import Basepage

class demo_02(Basepage):
    def __init__(self, driver, ):  # 属性==》页面的控件
        super().__init__(driver)

    def handle(self, value):
        self.hand(value)

    def alert_all(self, type, selector, value=''):
        self.alert(Type=type, Selector=selector, Value =value)



if __name__=='__main__':
    current_path = os.path.dirname(__file__)
    chrome_driver_path = os.path.join(current_path, '../webdriver/chromedriver')
    page_path = os.path.join(current_path, '../pages/element_samples.html')
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    demo02 = demo_02(driver)
    driver.get('file://' + page_path)
    # windows句柄处理
    # demo02.handle(0)
    # e = driver.find_element(By.XPATH, '//select[@name="jumpMenu"]')
    # Select(e).select_by_visible_text('开封教育网')
    # demo02.handle(1)
    # driver.find_element(By.XPATH, '//a[text()="政务服务"]').click()
    # demo02.handle(0)
    # driver.find_element(By.XPATH, '//input[@name="edit"]').send_keys('cherry')

    # alert处理
    # driver.find_element(By.XPATH, '//input[@name="alterbutton"]').click()
    # time.sleep(1)
    # demo02.alert_all(type='no', selector='alert')
    # # confirm
    # driver.find_element(By.XPATH, '//input[@name="confirmbutton"]').click()
    # time.sleep(1)
    # demo02.alert_all(type='no', selector='confirm')
    # # prompt
    # driver.find_element(By.XPATH, '//input[@name="promptbutton"]').click()
    # time.sleep(1)
    # demo02.alert_all(type='yes', selector='prompt',value='cherry')
