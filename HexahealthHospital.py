################Search any Entity for sanity ###########################################
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
# import time
#class HexaHealthHospital:

class Hospitalclass:

    def Hospitalmethod(self):
        try:
            self.driver = driver
            self.driver.get("https://www.hexahealth.com/")
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

            # SearchBox = driver.find_element(By.XPATH,"//input[@id='txtArticls']").send_keys("Anu")

            self.driver.find_element(By.XPATH, "//input[@id='txtArticls']").send_keys("Apollo Hospital, Noida")

            wait = WebDriverWait(driver, 10)
            wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Apollo Hospital, Noida")))
            self.driver.find_element(By.LINK_TEXT, "Apollo Hospital, Noida").click()
            print("Hospital Apollo is been Searched successfully")
            # BannerMessage = driver.find_element(By.XPATH,"//h1[@class='banner-title mb-3']") .text

            # assert "Apollo Hospital, Noida" in BannerMessage
            handles = driver.window_handles
            #print(handles)

            self.driver.switch_to.window(handles[0])

            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/div[4]/div/a[1]/i").click()

            self.driver.find_element(By.XPATH, "//*[@id='leadnamehome2']").send_keys("Test GJ Patient Name")
            self.driver.find_element(By.XPATH, "//*[@id='contactnumhome2']").send_keys("1000000100")
            self.driver.find_element(By.XPATH, "//*[@id='treatmentcondition2']").send_keys("Laparoscopy")
            self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitHospital2']").click()
            Handles2 = driver.window_handles[0]
            #print(Handles2)
            ThankYou = driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text
            print("Book Appointment is Successfully done")
            self.driver.back()
            time.sleep(2)
            self.driver.refresh()


        except:
            print("Hospital Page Test Case got failed")

        finally:
            print("All are Hospital Pages")


#driver.switch_to.active_element.find_element(By.LINK_TEXT," Book Appointment ").click()

Hospitalmethod_obj = Hospitalclass()
Hospitalmethod_obj.Hospitalmethod()
"""Get free Form is not done"""
""""""