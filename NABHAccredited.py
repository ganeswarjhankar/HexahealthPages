
from selenium.webdriver.common.by import By

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
driver.get("https://www.hexahealth.com/treatment/piles-stapler-surgery")

driver.maximize_window()
driver.implicitly_wait(5)
one = driver.find_element(By.XPATH,"//*[@id='slick-slide-control01']")
driver.execute_script("arguments[0].click();", one)
driver.implicitly_wait(2)
two = driver.find_element(By.XPATH,"//*[@id='slick-slide10']/div[1]/div/div[2]/a[2]")
driver.execute_script("arguments[0].click();", two)
driver.implicitly_wait(2)

driver.find_element(By.XPATH,"//*[@id='leadnamehome1']").send_keys("Test GJ XYZ")

driver.find_element(By.XPATH,"//*[@id='contactnumhome1']").send_keys("1000000100")
BookAnAppointmentButton = driver.find_element(By.XPATH,"//*[@id='LeadSubmitTreatement1']")
driver.execute_script("arguments[0].click();", BookAnAppointmentButton)
driver.implicitly_wait(2)







