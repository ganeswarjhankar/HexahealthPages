##"""This Script is regarding the Contact Us and About US page from the Hexahealth page"""###
import time

import requests
from selenium.webdriver.common.by import By
#import HexaFomatRandomUrlDisplay



class ContactUsPage():

    def __init__(self):

        from selenium.webdriver.chrome.service import Service
        from selenium import webdriver
        import time
        from selenium.webdriver.common.by import By



        # open each URL with Selenium and run code for it
        S = Service("D:\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=S)

    def ContactUs(self):
            try:
                self.driver.get("https://www.hexahealth.com/contact-us")
                self.driver.maximize_window()
                self.driver.implicitly_wait(5)
                self.driver.find_element(By.XPATH, "//input[@id='leadnamehome']").send_keys("Test GJ Contact Us Text Box")
                self.driver.find_element(By.XPATH, "//input[@id='contactnumhome']").send_keys("1000000100")

                self.driver.find_element(By.XPATH, "//input[@id='conactEmail']").send_keys("test@gmail.com")
                self.driver.find_element(By.XPATH,"//textarea[@id='leadqueryhome']").send_keys("Enter the Test Query")
                self.driver.find_element(By.XPATH,"//button[@id='leadSubmitContact']").click()
                print("ContactUs page Form is Passed")
            except:
                print("ContactUs page Form is Failed")

            #finally:
                #print("Contact Us Pages")

            self.driver.quit()


    def ContactUsWhatsapp(self):

        try:
            self.driver.get("https://www.hexahealth.com/contact-us")
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





ContactUs_Obj = ContactUsPage()
ContactUs_Obj.ContactUs()

#ContactUsWhatsApp_Obj = HexaFomatRandomUrlDisplay.MarketingPage()
#ContactUsWhatsApp_Obj.DisplayVariant()


ContactUsWhatsApp_obj =ContactUsPage()
ContactUsWhatsApp_obj.ContactUsWhatsapp()