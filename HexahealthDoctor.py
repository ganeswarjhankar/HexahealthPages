################Search any Entity for sanity ###########################################
"""Ok Tested Script with Doctor all automation Points"""
import time

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class DoctorClass:

    def __init__(self):

        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service

        # open each URL with Selenium and run code for it
        S = Service("D:\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=S)


    def Doctormethod(self):
        try:
            #self.driver =driver
            self.driver.get("https://www.hexahealth.com/")
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

            self.driver.find_element(By.XPATH, "//input[@id='txtArticls']").send_keys("Aman Priya Khanna")

            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Aman Priya Khanna")))
            self.driver.find_element(By.LINK_TEXT, "Aman Priya Khanna").click()
            print(" Search is Working successfully")



        except:
            print("Doctor Page Test Case got failed")

        finally:
            print("All are Doctor Pages")







    def BookAppointmentForm1(self):
        try:

            self.driver.get("https://www.hexahealth.com/delhi/doctor/dr-aman-priya-khanna-general-surgery")
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/a").click()
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("test GJ ")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000100")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='leadcity2']").send_keys("Gurugram")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='treamentcondition1']").send_keys("Tips Procedure")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='leadquery']").send_keys("Test Query check")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitNewHome']").click()
            # Lead2 in CRM
            print("BookAppointmentForm1 passed")
            self.driver.quit()
        except:
            print("BookAppointmentForm1 failed")


    def ContactUsWhatsapp(self):

        try:

            self.driver.get("https://www.hexahealth.com/delhi/doctor/dr-aman-priya-khanna-general-surgery")
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
                    print("Failed")


            else:
                print('Verification failed as the URl Not containing "api"')

            # response = requests.get(current_url)

            time.sleep(5)
            self.driver.refresh()
            self.driver.back()

            print("Passed")
        except:
            print("Failed")

            # finally:
            # print("This is Cost Variant Marketing Pages")

        self.driver.quit()

    def DoctorExpertDoctors(self):
        try:
            self.driver.get("https://www.hexahealth.com/delhi/doctor/dr-aman-priya-khanna-general-surgery")
            self.driver.maximize_window()

            self.driver.implicitly_wait(2)

            one = self.driver.find_element(By.XPATH, "//*[@id='slick-slide-control01']")
            self.driver.execute_script("arguments[0].click();", one)
            self.driver.implicitly_wait(2)
            two = self.driver.find_element(By.XPATH, "//*[@id='slick-slide01']/div[1]/div/div[2]/a[2]")
            self.driver.execute_script("arguments[0].click();", two)
            self.driver.implicitly_wait(2)

            self.driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Gj Test check")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000100")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='leadcity2']").send_keys("Gurugram")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='treamentcondition1']").send_keys("Tips Procedure")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='leadquery']").send_keys("Query Test check")
            self.driver.implicitly_wait(2)
            Button = self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitNewHome']")
            self.driver.execute_script("arguments[0].click();", Button)
            # Lead3 in CRM
            self.driver.implicitly_wait(2)
            print("The Expert Doctor form is passed")

        except:
            print("The Expert Doctors form is failed")

    def NABHAccreditedHospitals(self):
        try:

            self.driver.get("https://www.hexahealth.com/delhi/doctor/dr-aman-priya-khanna-general-surgery")
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            #OneSlide = self.driver.find_element(By.XPATH, "//*[@id='slick-slide-control01']")
            #self.driver.execute_script("arguments[0].click();", OneSlide)
            #self.driver.implicitly_wait(2)
            BookApButton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/div/div[1]/div/div[5]/div/div[1]/div[2]/div[2]/a/span")
            self.driver.execute_script("arguments[0].click();", BookApButton)
            self.driver.implicitly_wait(2)

            self.driver.find_element(By.XPATH, "//*[@id='leadnamedoctor2']").send_keys("Test GJ XYZ")

            self.driver.find_element(By.XPATH, "//*[@id='contactnumdoctor2']").send_keys("1000000100")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH,"//*[@id='treamentcondition2']").send_keys("Mastectomy")
            #YogaTreatment = self.driver.find_element(By.XPATH, "//select[@id='treamentcondition2']")
            #drop2 = Select(YogaTreatment)
            #drop2.select_by_visible_text("Yoga")

            BookAnAppointmentButton = self.driver.find_element(By.XPATH, "//*[@id='leadSubmitDoctor2']")
            self.driver.execute_script("arguments[0].click();", BookAnAppointmentButton)
            # Lead4 in CRM
            self.driver.implicitly_wait(2)
            print("NABHAccreditedHospitals Form is Passed")

        except:
            print("NABHAccreditedHospitals Form is Failed")


    def BookAppointmentButtonMethod(self):
        try:





            self.driver.get("https://www.hexahealth.com/delhi/doctor/dr-aman-priya-khanna-general-surgery")
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

            self.driver.implicitly_wait(2)
            BookApButton =self.driver.find_element(By.LINK_TEXT, "Book Appointment")
            self.driver.execute_script("arguments[0].click();", BookApButton)
            #Button = self.driver.find_element(By.LINK_TEXT," Book Appointment").click()



            self.driver.implicitly_wait(2)

            self.driver.find_element(By.XPATH, "//*[@id='leadnamedoctor2']").send_keys("Test GJ Treatment ")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='contactnumdoctor2']").send_keys("1000000100")
            self.driver.implicitly_wait(2)

            self.driver.find_element(By.XPATH, "//*[@id='treamentcondition2']").send_keys("Mastectomy")

            #BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcityhome1']")
            #drop1 = Select(BengaluruCity)
            #drop1.select_by_visible_text("Bengaluru")

            BookAnAppointmentButton =self.driver.find_element(By.XPATH, "//*[@id='leadSubmitDoctor2']")
            self.driver.execute_script("arguments[0].click();", BookAnAppointmentButton)
            # Lead4 in CRM
            self.driver.implicitly_wait(2)

            Handles2 = self.driver.window_handles[0]

            ThankYou = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text
            print("BookAppointmentButtonMethod is Successfully Passed")
            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()

        except:
            print("BookAppointmentButtonMethod Form is Failed")


    def BookAppointmentMainForm(self):
       try:

           self.driver.get("https://www.hexahealth.com/delhi/doctor/dr-aman-priya-khanna-general-surgery")
           self.driver.maximize_window()
           self.driver.implicitly_wait(5)

           #self.driver.implicitly_wait(2)
           #BookApButton = self.driver.find_element(By.XPATH, "//*[@id='slick-slide10']/div[1]/div/div[2]/a[2]")
           #self.driver.execute_script("arguments[0].click();", BookApButton)
           #self.driver.implicitly_wait(2)

           self.driver.find_element(By.XPATH, "//*[@id='leadnamehome']").send_keys("Test GJ Treatment ")
           #self.driver.implicitly_wait(2)
           #self.driver.find_element(By.XPATH, "//*[@id='leadSubmitDoctor']")
           #self.driver.execute_script("arguments[0].click();", NameTextBox)

           self.driver.find_element(By.XPATH, "//*[@id='contactnumhome']").send_keys("1000000100")
           self.driver.implicitly_wait(2)

           self.driver.find_element(By.XPATH, "//*[@id='treatmentcondition']").send_keys("Mastectomy")

           #BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcityhome']")
           #drop1 = Select(BengaluruCity)
           #drop1.select_by_visible_text("Bengaluru")

           BookAnAppointmentButton = self.driver.find_element(By.XPATH, "//*[@id='leadSubmitDoctor']")
           self.driver.execute_script("arguments[0].click();", BookAnAppointmentButton)
           # Lead4 in CRM
           self.driver.implicitly_wait(2)
           Handles2 = self.driver.window_handles[0]

           ThankYou = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text
           print("BookAppointmentMainForm is Successfully done")
           self.driver.back()
           self.driver.implicitly_wait(2)
           self.driver.refresh()


       except:
           print("BookAppointmentMainForm Form is Failed")










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















################Search any Entity for sanity ###########################################

