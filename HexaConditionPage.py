################Condition as Piles any Entity for sanity ###########################################
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time



from selenium.webdriver.support.wait import WebDriverWait



class ConditionClass:

    def __init__(self):



        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service




        # open each URL with Selenium and run code for it
        S = Service("D:\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=S)


    def Conditionmethod(self):
        try:

            self.driver.get("https://www.hexahealth.com/")
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

            self.driver.find_element(By.XPATH, "//input[@id='txtArticls']").send_keys("Gallstones")

            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Gallstones")))
            self.driver.find_element(By.LINK_TEXT, "Gallstones").click()
            print("Condition as GallStones  is been Searched successfully")
            handles = self.driver.window_handles

            self.driver.switch_to.window(handles[0])

            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[3]/div[2]/a[1]").click()

            self.driver.find_element(By.XPATH, "//*[@id='leadnamehome1']").send_keys("Test GJ Patient Name")
            self.driver.find_element(By.XPATH, "//*[@id='contactnumhome1']").send_keys("1000000100")
            self.driver.find_element(By.XPATH, "//input[@id='leadcityhome1']").send_keys("Gurugram")
            self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitCondition1']").click()
            Handles2 = self.driver.window_handles[0]

            ThankYou = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text
            print("Book Appointment is Successfully done")
            self.driver.back()
            time.sleep(2)
            self.driver.refresh()


        except:
            print("Condition Page Test Case got failed")

        finally:
            print("All are Condition Pages")



    def BookAppointmentForm1(self):
        try:
            self.driver.get("https://www.hexahealth.com/condition/piles")
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
            self.driver.get("https://www.hexahealth.com/condition/piles")
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
                    print("Status Code 200 Ok is Passed")
                else:
                    print("Failed")


            else:
                print('Verification failed as the URl Not containing "api"')

            # response = requests.get(current_url)

            time.sleep(5)
            self.driver.refresh()
            self.driver.back()


        except:
            print("Status Code 200 Ok is Failed")

            # finally:
            # print("This is Cost Variant Marketing Pages")

        self.driver.quit()


    def ConditionExpertDoctors(self):
        try:
            self.driver.get("https://www.hexahealth.com/condition/piles")
            self.driver.maximize_window()


            self.driver.implicitly_wait(2)

            one = self.driver.find_element(By.XPATH, "//*[@id='slick-slide-control01']")
            self.driver.execute_script("arguments[0].click();", one)
            self.driver.implicitly_wait(2)
            two =self.driver.find_element(By.XPATH, "//*[@id='slick-slide01']/div[1]/div/div[2]/a[2]")
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
            Button =self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitNewHome']")
            self.driver.execute_script("arguments[0].click();", Button)
            # Lead3 in CRM
            self.driver.implicitly_wait(2)
            print("The Condition Expert Doctor form is passed")

        except:
            print("The Condition Expert Doctors form is failed")


    def NABHAccreditedHospitals(self):
        try:





            self.driver.get("https://www.hexahealth.com/condition/piles")
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            OneSlide = self.driver.find_element(By.XPATH, "//*[@id='slick-slide-control01']")
            self.driver.execute_script("arguments[0].click();", OneSlide)
            self.driver.implicitly_wait(2)
            BookApButton =self.driver.find_element(By.XPATH, "//*[@id='slick-slide10']/div[1]/div/div[2]/a[2]")
            self.driver.execute_script("arguments[0].click();", BookApButton)
            self.driver.implicitly_wait(2)

            self.driver.find_element(By.XPATH, "//*[@id='leadnamehome1']").send_keys("Test GJ XYZ")

            self.driver.find_element(By.XPATH, "//*[@id='contactnumhome1']").send_keys("1000000100")
            self.driver.implicitly_wait(2)
            BookAnAppointmentButton =self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitTreatement1']")
            self.driver.execute_script("arguments[0].click();", BookAnAppointmentButton)
            # Lead4 in CRM
            self.driver.implicitly_wait(2)
            print("NABHAccreditedHospitals Form is Passed")

        except:
            print("NABHAccreditedHospitals Form is Failed")










Conditionmethod_obj = ConditionClass()
Conditionmethod_obj.Conditionmethod()



Conditionmethod_obj = ConditionClass() #lead 2
Conditionmethod_obj.BookAppointmentForm1()

Conditionmethod_obj = ConditionClass() #ok 200
Conditionmethod_obj.ContactUsWhatsapp()

Conditionmethod_obj = ConditionClass() #lead 3
Conditionmethod_obj.ConditionExpertDoctors()

Treatmentmethod_obj = ConditionClass() #lead 4
Treatmentmethod_obj.NABHAccreditedHospitals()








