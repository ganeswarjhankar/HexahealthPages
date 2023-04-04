################Condition as Piles any Entity for sanity ###########################################
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait



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
            self.driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Test GJ Patient Name")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000100")
            self.driver.implicitly_wait(2)

            BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcity2']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")

            YogaTreatment = self.driver.find_element(By.XPATH, "//select[@id='treamentcondition1']")
            drop2 = Select(YogaTreatment)
            drop2.select_by_visible_text("Yoga")

            self.driver.find_element(By.XPATH, "//textarea[@id='leadquery']").send_keys("Query test")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitNewHome']").click()
            # Lead1 in CRM
            Handles2 = self.driver.window_handles[0]

            ThankYou = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text
            print("Get a FREE Second Opinion from Top Surgeons! Book an Appointment » Successfully Passed")
            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()
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


    def NABHAccreditedHospitals(self):
        try:
            self.driver.get("https://www.hexahealth.com/condition/piles")
            self.driver.maximize_window()

            self.driver.implicitly_wait(2)

            one = self.driver.find_element(By.XPATH, "//*[@id='slick-slide-control21']")
            self.driver.execute_script("arguments[0].click();", one)
            self.driver.implicitly_wait(2)
            two = self.driver.find_element(By.XPATH, "//*[@id='slick-slide21']/div[1]/div/div[2]/a[2]/span")
            self.driver.execute_script("arguments[0].click();", two)
            self.driver.implicitly_wait(2)

            self.driver.find_element(By.XPATH, "//*[@id='leadnamehome1']").send_keys("Gj Test check")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='contactnumhome1']").send_keys("1000000100")
            #self.driver.implicitly_wait(2)

            BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcityhome1']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")


            #self.driver.find_element(By.XPATH, "//*[@id='leadcity2']").send_keys("Gurugram")
            #self.driver.implicitly_wait(2)
            #self.driver.find_element(By.XPATH, "//*[@id='treamentcondition1']").send_keys("Tips Procedure")
            #self.driver.implicitly_wait(2)
            #self.driver.find_element(By.XPATH, "//*[@id='leadquery']").send_keys("Query Test check")
            #self.driver.implicitly_wait(2)
            Button = self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitCondition1']")
            self.driver.execute_script("arguments[0].click();", Button)
            # Lead3 in CRM
            self.driver.implicitly_wait(2)
            print("The Expert Doctor form is passed")

            Handles2 = self.driver.window_handles[0]

            ThankYou = self.driver.find_element(By.XPATH, "/html/body/div/div/div/h1").text

            self.driver.back()
            self.driver.implicitly_wait(2)
            self.driver.refresh()




        except:
            print("The Condition Expert Doctors form is failed")


    def ConditionExpertDoctors(self):
        try:





            self.driver.get("https://www.hexahealth.com/condition/piles")
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            OneSlide = self.driver.find_element(By.XPATH, "//*[@id='slick-slide-control11']")
            self.driver.execute_script("arguments[0].click();", OneSlide)
            self.driver.implicitly_wait(2)
            BookApButton =self.driver.find_element(By.XPATH, "//*[@id='slick-slide11']/div[1]/div/div[2]/a[2]/span")
            self.driver.execute_script("arguments[0].click();", BookApButton)
            self.driver.implicitly_wait(2)

            self.driver.find_element(By.XPATH, "//*[@id='leadnamehome1']").send_keys("Test GJ XYZ")

            self.driver.find_element(By.XPATH, "//*[@id='contactnumhome1']").send_keys("1000000100")

            BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcityhome1']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")

            self.driver.implicitly_wait(2)
            BookAnAppointmentButton =self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitCondition1']")
            self.driver.execute_script("arguments[0].click();", BookAnAppointmentButton)
            # Lead4 in CRM
            self.driver.implicitly_wait(2)
            print("NABHAccreditedHospitals Form is Passed")

        except:
            print("NABHAccreditedHospitals Form is Failed")



    def BookAppointmentButtonMethod(self):
        try:





            self.driver.get("https://www.hexahealth.com/treatment/piles-stapler-surgery")
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

            self.driver.implicitly_wait(2)
            BookApButton =self.driver.find_element(By.XPATH, "//*[@id='slick-slide10']/div[1]/div/div[2]/a[2]")
            self.driver.execute_script("arguments[0].click();", BookApButton)
            self.driver.implicitly_wait(2)

            self.driver.find_element(By.XPATH, "//*[@id='leadnamehome1']").send_keys("Test GJ Treatment ")
            self.driver.implicitly_wait(2)
            self.driver.find_element(By.XPATH, "//*[@id='contactnumhome1']").send_keys("1000000100")
            self.driver.implicitly_wait(2)

            BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcityhome1']")
            drop1 = Select(BengaluruCity)
            drop1.select_by_visible_text("Bengaluru")

            BookAnAppointmentButton =self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitTreatement1']")
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

           self.driver.get("https://www.hexahealth.com/treatment/piles-stapler-surgery")
           self.driver.maximize_window()
           self.driver.implicitly_wait(5)

           self.driver.implicitly_wait(2)
           #BookApButton = self.driver.find_element(By.XPATH, "//*[@id='slick-slide10']/div[1]/div/div[2]/a[2]")
           #self.driver.execute_script("arguments[0].click();", BookApButton)
           #self.driver.implicitly_wait(2)

           self.driver.find_element(By.XPATH, "//*[@id='leadnamehome']").send_keys("Test GJ Treatment ")
           self.driver.implicitly_wait(2)
           self.driver.find_element(By.XPATH, "//*[@id='contactnumhome']").send_keys("1000000100")
           self.driver.implicitly_wait(2)

           BengaluruCity = self.driver.find_element(By.XPATH, "//select[@id='leadcityhome']")
           drop1 = Select(BengaluruCity)
           drop1.select_by_visible_text("Bengaluru")

           BookAnAppointmentButton = self.driver.find_element(By.XPATH, "//*[@id='LeadSubmitTreatement']")
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






Conditionmethod_obj1 = ConditionClass()
Conditionmethod_obj1.Conditionmethod() #Lead



Conditionmethod_obj2 = ConditionClass() #lead 2
Conditionmethod_obj2.BookAppointmentForm1()

Conditionmethod_obj3 = ConditionClass() #ok 200
Conditionmethod_obj3.ContactUsWhatsapp()

Conditionmethod_obj4 = ConditionClass() #lead 3
Conditionmethod_obj4.ConditionExpertDoctors()

Conditionmethod_obj5 = ConditionClass() #lead 4
Conditionmethod_obj5.NABHAccreditedHospitals()





Conditionmethod_obj6 = ConditionClass() #lead 5
Conditionmethod_obj6.BookAppointmentButtonMethod()


Conditionmethod_obj7 = ConditionClass() #lead 6
Conditionmethod_obj7.BookAppointmentMainForm()



