

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from OrangeHRM.Loginpage import OrangeHrm

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()






class Admin(OrangeHrm):






    def Admin(self):
        self.driver.OrangeHrm.ValidLogin()
        time.sleep(3)

        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
        time.sleep(3)

        #self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click()
        time.sleep(3)





        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()

        #new page

        userrole=Select(driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]"))
        userrole.select_by_index(2)

        EmployeeName=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("Test1")





