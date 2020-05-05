import time
from common.chrome_driver import chromedriver
from selenium.webdriver.common.by import By
from element_infos.login.login_page import LoginPage


driver = chromedriver.get_driver
loginPage = LoginPage(driver)
loginPage.open_url('http://106.53.50.202:8999/zentao2/www/user-login-L3plbnRhbzYvd3d3Lw==.html')
loginPage.input_username('chenjuan')
loginPage.input_password('1q2w3e4r,')
loginPage.click_login()
time.sleep(1)
driver.find_element(By.XPATH, '//li[@data-id="project"]').click()
driver.find_element(By.XPATH, '//li[@data-id="team"]').click()
driver.find_element(By.XPATH, '//button[@id="currentItem"]').click()
driver.find_element(By.XPATH, '//a[@title="公共研发组sprint1"]').click()





# driver.find_element(By.XPATH, '//div[@class="btn-toolbar pull-right"]').click()
# driver.find_element(By.XPATH, '//tr[2]/td/div[@id="accounts_chosen"]').click()
# driver.find_element(By.XPATH, '//tr[2]/td/div/div/ul/li[@title="D:开发人员02"]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//tr[3]/td/div[@id="accounts_chosen"]').click()
# driver.find_element(By.XPATH, '//tr[3]/td/div/div/ul/li[@title="T:测试人员02"]').click()