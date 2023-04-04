################Search any Entity for sanity ###########################################
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support.select import Select
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



        except:
            print("Hospital Page Test Case got failed")

        finally:
            print("All are Hospital Pages")


#driver.switch_to.active_element.find_element(By.LINK_TEXT," Book Appointment ").click()





Doctormethod_obj1 = DoctorClass()
Doctormethod_obj1.Doctormethod()


Doctormethod_obj = DoctorClass()  # lead 1
Doctormethod_obj.BookAppointmentForm1()



Doctormethod_obj = DoctorClass()  # ok 200
Doctormethod_obj.ContactUsWhatsapp()

#Doctormethod_obj = DoctorClass()  # lead 3 this is not Applicable Here
#Doctormethod_obj.DoctorExpertDoctors() #lead 3 this is not Applicable Here

Doctormethod_obj = DoctorClass()  # lead 4
Doctormethod_obj.NABHAccreditedHospitals()




Doctormethod_obj6 = DoctorClass() #lead 5
Doctormethod_obj6.BookAppointmentButtonMethod()


Doctormethod_obj6 = DoctorClass() #lead 6
Doctormethod_obj6.BookAppointmentMainForm()


