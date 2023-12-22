
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

S = Service("D:\\chromedriver.exe")

driver = webdriver.Chrome(service=S)
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.XPATH,"//*[@id='username']").send_keys("student")
driver.find_element(By.XPATH,"//*[@id='password']").send_keys("Password123")
driver.find_element(By.XPATH,"//*[@id='submit']").click()

success_login=driver.find_element(By.XPATH,"//*[@id='loop-container']/div/article/div[1]/h1")
if success_login.text=="Logged In Successfully":
    print("Passed Login")
else:
    print("Failed Login")











