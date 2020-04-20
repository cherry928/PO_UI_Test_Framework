import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from selenium.webdriver.support.wait import WebDriverWait

class Basepage(object):
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    # 浏览器操作封装  ——> 二次封装
    def open_url(self, url):
        self.driver.get(url)
        logger.info('打开url地址  %s' % url)

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('设置浏览器的最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info('设置浏览器的最小化')

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新操作')

    def get_title(self):
        value = self.driver.title
        logger.info('获取网页标题，标题是 %s ' % value)
        return value

    # 获取元素属性值
    def get_attribute_title(self, element_info):
        element = self.find_element(element_info)
        title = element.get_attribute('title')
        logger.info('[%s]元素获取title，为：%s' % (element_info['element_name'], title))
        return title

    # 获取元素text
    def get_text(self, element_info):
        element = self.find_element(element_info)
        text = element.text
        logger.info('[%s]元素获取成功，为：%s' % (element_info['element_name'], text))
        return text

    # 元素封装操作
    def find_element(self, element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        elif locator_type_name == 'link_text':
            locator_type = By.LINK_TEXT
        elif locator_type_name == 'css_selector':
            locator_type = By.CSS_SELECTOR
        elif locator_type_name == 'name':
            locator_type = By.NAME
        elif locator_type_name == 'partial_link_text':
            locator_type = By.PARTIAL_LINK_TEXT
        elif locator_type_name == 'tag_name':
            locator_type = By.TAG_NAME

        element = WebDriverWait(self.driver,locator_timeout)\
            .until(lambda x:x.find_element(locator_type, locator_value_info))
        logger.info('[%s]元素识别成功'%element_info['element_name'])
        return element

    # 点击
    def click(self, element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('[%s]元素进行点击操作'%element_info['element_name'])

    # 输入值
    def input(self, element_info, content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入内容:%s'% (element_info['element_name'], content))

    # 清除输入框内容
    def clear(self, element_info):
        element = self.find_element(element_info)
        element.clear()
        logger.info('[%s]元素内容清除成功'%element_info['element_name'])

    # 切换frame
    def switch_to_frame(self, element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)
        logger.info('已经切换到[%s]' % element_info['element_name'])

    # 切换到默认frame
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        logger.info('切换到default_frame')

    # 滑到指定元素
    def slide_specified_element(self, element_info):
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        logger.info('滑到指定元素：%s按钮成功'%element_info['element_name'])

