import time

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)









driver.get("https://www.hexahealth.com/treatment/piles-laser-treatment")
driver.maximize_window()
driver.implicitly_wait(5)
#driver.execute_script("window.scrollBy(0,14690)", "")
driver.implicitly_wait(5)
#results = driver.find_elements(By.XPATH,"//*[@id='slick-slide10']/div[1]/div")
#count = len(results)
#print(count)

one = driver.find_element(By.XPATH,"//*[@id='slick-slide-control01']")
driver.execute_script("arguments[0].click();", one)
time.sleep(5)
two = driver.find_element(By.XPATH,"//*[@id='slick-slide01']/div[1]/div/div[2]/a[2]")
driver.execute_script("arguments[0].click();", two)
time.sleep(5)

driver.find_element(By.XPATH,"//*[@id='leadname2']").send_keys("Gj Test check")
driver.find_element(By.XPATH,"//*[@id='contactnum2']").send_keys("1000000100")
driver.find_element(By.XPATH,"//*[@id='leadcity2']").send_keys("Gurugram")
driver.find_element(By.XPATH,"//*[@id='treamentcondition1']").send_keys("Tips Procedure")
driver.find_element(By.XPATH,"//*[@id='leadquery']").send_keys("Query Test check")
Button = driver.find_element(By.XPATH,"//*[@id='LeadSubmitNewHome']")
driver.execute_script("arguments[0].click();", Button)
driver.implicitly_wait(2)




#for result in results:
 #   result.find_element(By.XPATH,"div[2]/a[2]/span").click()
    #driver.execute_script("arguments[0].click();", one)
  #  time.sleep(5)



