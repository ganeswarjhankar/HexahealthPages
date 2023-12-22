import pymysql
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from ChainingOfElements import driver

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.XPATH,"//*[@id='username']")
driver.find_element(By.XPATH,"//*[@id='password']")
driver.find_element(By.XPATH,"//*[@id='submit']")
Logged_In_Successfully= driver.find_element(By.XPATH,"//*[@id='loop-container']/div/article/div[1]/h1").text


connection=pymysql.connect(host="localhost", user="", password="",database="")


