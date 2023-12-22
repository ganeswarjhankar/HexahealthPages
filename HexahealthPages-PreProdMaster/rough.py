"""ALL OK Treatment detailed testcases Script"""
import time




from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from selenium.webdriver.common.by import By

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

button = driver.find_elements(By.XPATH,"//*[@id='content']/div/button")


count = 50
for button in range(count):
    driver.find_element(By.XPATH,"//*[@id='content']/div/button").click()
    time.sleep(0.1)



if count == count:
    delete_buttons = driver.find_elements(By.XPATH, "//*[@id='elements']/button")
    for delete_button in delete_buttons:
        delete_button.click()




driver.quit()






















