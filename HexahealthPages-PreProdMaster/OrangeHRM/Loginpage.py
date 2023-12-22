
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)

url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()


class OrangeHrm():
    def ValidLogin(self):
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        assert "Dashboard" in driver.page_source


    def Invalid_login(self):
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("INVALID_Admin")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("INVALID_admin123")
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        assert "Dashboard" in driver.page_source


    def ForgetPassword(self):
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p").click()
        UserName_forget=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/div/form/div[1]/div/div[2]/input")
        UserName_forget.send_keys("reset_username")
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/div/form/div[2]/button[2]").click()

    def cancelForgetPassword(self):
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p").click()
        UserName_forget = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/div/form/div[1]/div/div[2]/input")
        UserName_forget.send_keys("reset_username")
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/div/form/div[2]/button[1]").click()
        assert "OrangeHRM" in driver.page_source

    



validLoginObject=OrangeHrm()
validLoginObject.ValidLogin()

invalidloginObject=OrangeHrm()
invalidloginObject.Invalid_login()


cancelForgetPasswordObject=OrangeHrm()
cancelForgetPasswordObject.cancelForgetPassword()

