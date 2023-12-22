#######Test script is oK tested


import pytest
from PageObjects.HexaHomepage import HexaHomePage
from TestData.testdata import HomePageData
from utilities.BaseClass import Baseclass
import time
class TestHomepage(Baseclass):


    def test_formSubmission(self,getData):



        log = self.getLogger()

        homepage = HexaHomePage(self.driver)
        time.sleep(3)
        log.info("first name is " + getData["firstname"])

        #homepage.getleadname().send_keys(getData[0])
        #homepage.getcontactnum().send_keys(getData[1])
        #homepage.getTreatmentCondtion().send_keys(getData[2])
        #homepage.getLeadCity().send_keys(getData[3])
        #homepage.getLeadQuery().send_keys(getData[4])
        #homepage.LeadSubmitNewHome().click()
        #homepage.getAppointment().click()
        homepage.getleadname().send_keys(getData["firstname"])
        homepage.getcontactnum().send_keys(getData["contactNo"])
        homepage.getTreatmentCondtion().send_keys(getData ["treatment"])
        homepage.getLeadCity().send_keys(getData["city"])

        homepage.getLeadQuery().send_keys(getData["query"])
        homepage.getLeadSubmitNewHome().click()
        #homepage.CloseModal().click()

        #assert ("Thank you" in alertText)
        #self.driver.refresh()
    #@pytest.fixture(params=HomePageData.getTestData("Testcase2"))

    @pytest.fixture(params= HomePageData.getTestData("Testcase2"))


    def getData(self, request):
        return request.param





