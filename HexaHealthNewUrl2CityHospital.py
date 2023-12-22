"""https://www.hexahealth.com/delhi/hospitals/cardiology"""
import time

import requests

"""Script for the City with Doctor as below"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class CityHospitalClass:

    def __init__(self):

        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service

        # open each URL with Selenium and run code for it
        S = Service("D:\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=S)


    def CityHospitalBookmethod1(self):
        try:

            self.driver.get("https://www.hexahealth.com/delhi/hospitals/cardiology")
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()



            BookAppointmentButton = self.driver.find_element(By.XPATH,"//a[@class='link-appointment']").click()
            self.driver.implicitly_wait(5)
            self.driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Test GJ Patient Name")
            self.driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000100")

            BengaluruCity = self.driver.find_element(By.XPATH,"//select[@id='leadcity2']")
            drop1 =Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")


            YogaTreatment= self.driver.find_element(By.XPATH,"//select[@id='treamentcondition1']")
            drop2= Select(YogaTreatment)
            drop2.select_by_visible_text("Yoga")

            self.driver.find_element(By.XPATH,"//*[@id='leadquery']").send_keys("Query Test For City Doctor")


            self.driver.find_element(By.XPATH,"//button[@id='LeadSubmitNewHome']").click()

            Handles2 = self.driver.window_handles[0]

            ThankYou = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text
            print("Book Appointment is Successfully done")
            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()


        except:
            print("Doctor Page Test Case got failed")

        finally:
            print("All are Doctor Pages")

    def CityHospitalListMethod2(self):
        try:

            self.driver.get("https://www.hexahealth.com/delhi/hospitals/cardiology")
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()



            BookAppointmentButton = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div[1]/div[1]/div[3]/a[2]/span").click()
            self.driver.implicitly_wait(5)
            self.driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Test GJ Patient Name")
            self.driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000100")

            BengaluruCity = self.driver.find_element(By.XPATH,"//select[@id='leadcity2']")
            drop1 =Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")


            YogaTreatment= self.driver.find_element(By.XPATH,"//select[@id='treamentcondition1']")
            drop2= Select(YogaTreatment)
            drop2.select_by_visible_text("Yoga")

            self.driver.find_element(By.XPATH,"//*[@id='leadquery']").send_keys("Query Test For City Doctor")


            self.driver.find_element(By.XPATH,"//button[@id='LeadSubmitNewHome']").click()

            Handles2 = self.driver.window_handles[0]

            ThankYou = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text
            print("Book Appointment is Successfully done")
            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()


        except:
            print("Doctor Page Test Case got failed")

        finally:
            print("All are Doctor Pages")

        self.driver.close()


    def CityHospitalFormMethod3(self):
        try:

            self.driver.get("https://www.hexahealth.com/delhi/hospitals/cardiology")
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()



            #BookAppointmentButton = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div[1]/div[1]/div[3]/a[2]/span").click()
            #self.driver.implicitly_wait(5)
            self.driver.find_element(By.XPATH, "//*[@id='leadnamehome']").send_keys("Test GJ Patient Name")
            self.driver.find_element(By.XPATH, "//*[@id='contactnumhome']").send_keys("1000000100")

            BengaluruCity = self.driver.find_element(By.XPATH,"//select[@id='leadcity1']")
            drop1 =Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")


            YogaTreatment= self.driver.find_element(By.XPATH,"//select[@id='treamentcondition']")
            drop2= Select(YogaTreatment)
            drop2.select_by_visible_text("Yoga")

            #self.driver.find_element(By.XPATH,"//*[@id='leadquery']").send_keys("Query Test For City Doctor")


            BookApButton = self.driver.find_element(By.XPATH,"//button[@id='LeadSubmitBlog']")
            self.driver.execute_script("arguments[0].click();", BookApButton)

            Handles2 = self.driver.window_handles[0]

            ThankYou = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text
            print("Book Appointment is Successfully done")
            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()


        except:
            print("Doctor Page Test Case got failed")

        finally:
            print("All are Doctor Pages")




    def ContactUsWhatsapp(self):

        try:
            self.driver.get("https://www.hexahealth.com/delhi/doctors/cardiologist")
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self.driver.find_element(By.XPATH, "//*[@id='whtsapHeaderBtn']").click()
            # self.driver.switch_to.window(self.driver.window_handles[2])
            msg = self.driver.find_element(By.XPATH, "//p[@class='_9vd5']")
            print(msg.text)

            # Get the current URL
            current_url = self.driver.current_url
            print(current_url)
            # Verify that the current URL contains the expected value
            response = requests.get(current_url)
            if 'api.' in current_url:
                if response.status_code == 200:
                    print("Status Code 200 Ok")
                else:
                    print("Failed API link")


            else:
                print('Verification failed as the URl Not containing "api"')

            # response = requests.get(current_url)

            time.sleep(5)
            self.driver.refresh()
            self.driver.back()

            print("Passed ")
        except:
            print("Failed")

            # finally:
            # print("This is Cost Variant Marketing Pages")

        self.driver.quit()







#####First Link#
CityHospitalmethod_obj = CityHospitalClass()
CityHospitalmethod_obj.CityHospitalBookmethod1()
######List Of doctors#
CityHospitalListMethod_obj = CityHospitalClass()
CityHospitalListMethod_obj.CityHospitalListMethod2()
######Object for the Main Form#
CityDoctorFormMethod_obj = CityHospitalClass()
CityDoctorFormMethod_obj.CityHospitalFormMethod3()

##To verify the WhatApp functionality
CityHospitalWhatApp_obj=CityHospitalClass()
CityHospitalWhatApp_obj.ContactUsWhatsapp()


















