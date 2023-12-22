##"""This Script is regarding the Contact Us and About US page from the Hexahealth page"""###
import time

import requests
from selenium.webdriver.common.by import By
#import HexaFomatRandomUrlDisplay



class HexaHomePageClass():

    def __init__(self):

        from selenium.webdriver.chrome.service import Service
        from selenium import webdriver
        import time
        from selenium.webdriver.common.by import By



        # open each URL with Selenium and run code for it
        S = Service("D:\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=S)

    def HexaHomepage(self):
            try:
                self.driver.get("https://hexahealth.com")
                self.driver.maximize_window()
                self.driver.find_element(By.LINK_TEXT,("Get a FREE Second Opinion from Top Surgeons! Book an Appointment »")).click()
                time.sleep(5)
                self.driver.find_element(By.XPATH, "//input[@id='leadname2']").send_keys("Patient test Auto Name check")

                self.driver.find_element(By.XPATH, "//input[@id='contactnum2']").send_keys("1000000100")
                self.driver.find_element(By.XPATH, "//input[@name='leadcity2']").send_keys("Delhi")
                self.driver.find_element(By.XPATH, "//input[@name='treamentcondition1']").send_keys("ACL Reconstruction Surgery ")
                self.driver.find_element(By.XPATH, "//textarea[@id='leadquery']").send_keys("test Auto check")

                self.driver.find_element(By.XPATH, "//button[@id='LeadSubmitNewHome']").click()

                self.driver.find_element(By.XPATH, "//button[@id='closemodal']").click()
                time.sleep(3)
                self.driver.back()

                print("HexaHomepage Form has  Passed")
            except:
                print("HexaHomepage has Failed")

            finally:
                print("All are HexaHomePages")

            self.driver.quit()


    def HomePageWhatsapp(self):

        try:
            self.driver.get("https://www.hexahealth.com")
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





HexaHomePage_Obj = HexaHomePageClass()
HexaHomePage_Obj.HexaHomepage()

#ContactUsWhatsApp_Obj = HexaFomatRandomUrlDisplay.MarketingPage()
#ContactUsWhatsApp_Obj.DisplayVariant()


HomePageWhatsapp_obj =HexaHomePageClass()
print(HomePageWhatsapp_obj.HomePageWhatsapp())


