################Search any Entity for sanity ###########################################
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
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
            handles = self.driver.window_handles

            self.driver.switch_to.window(handles[0])

            self.driver.execute_script("window.scrollBy(0,500)", "")
            self.driver.implicitly_wait(5)

            Button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/div[4]/div/a[1]").click()


            self.driver.implicitly_wait(5)
            self.driver.find_element(By.XPATH, "//*[@id='leadname2']").send_keys("Test GJ Patient Name")
            self.driver.find_element(By.XPATH, "//*[@id='contactnum2']").send_keys("1000000100")
            self.driver.find_element(By.XPATH, "//*[@id='treamentcondition1']").send_keys("Laparoscopy")
            self.driver.find_element(By.XPATH, "//button[@id='leadSubmitDoctor2']").click()

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




Hospitalmethod_obj = DoctorClass()
Hospitalmethod_obj.Doctormethod()


















################Search any Entity for sanity ###########################################

