import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# from PageObjects.CheckoutPage import CheckOutPage
# from PageObjects.HexaHomepage import HexaHomePage

class HexaHomePage:
    def __init__(self, driver):
        self.driver = driver
    time.sleep(3)
    appointment = (By.LINK_TEXT, "Get a free second opinion from top surgeons! Book an appointment »")
    leadname = (By.XPATH, "//input[@id='leadname2']")
    contactnum = (By.XPATH, "//input[@id='contactnum2']")

################### #####LeadCity = (By.XPATH, "//input[@name='leadcity2']")############
#********************###############*************************************##############
    leadCity = (By.XPATH, "//*[@id='leadcity2']/option[13]")

######################################################new code can be removed##########################
    treatmentCondtion = (By.XPATH, "//input[@name='treamentcondition1']")

    leadQuery = (By.XPATH, "//textarea[@id='leadquery']")

    leadSubmitNewHome = (By.XPATH, "//button[@id='LeadSubmitNewHome']")

    closeModal = (By.XPATH, "//button[@id='closemodal']")


    #def getAppointment(self):
        #return self.driver.find_element(*HexaHomePage.appointment)

    def getleadname(self):
        return self.driver.find_element(*HexaHomePage.leadname)

    def getcontactnum(self):
        return self.driver.find_element(*HexaHomePage.contactnum)

    def getLeadCity(self):
        return self.driver.find_element(*HexaHomePage.leadCity)

    def getTreatmentCondtion(self):
        return self.driver.find_element(*HexaHomePage.treatmentCondtion)

    def getLeadQuery(self):
        return self.driver.find_element(*HexaHomePage.leadQuery)

    def getLeadSubmitNewHome(self):
        return self.driver.find_element(*HexaHomePage.leadSubmitNewHome)

    def getCloseModal(self):
        return self.driver.find_element(*HexaHomePage.closeModal)
