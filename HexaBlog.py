################Search any Entity for sanity ###########################################
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

# import time

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)

driver.get("https://www.hexahealth.com/blog")


cards = driver.find_elements(By.XPATH,"//li[@class='item blog-article blogShadow']")
cards.count(len())




