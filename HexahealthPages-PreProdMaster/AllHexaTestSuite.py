import HexaHomePage
from HexaContactUs import ContactUsPage


obj_1 = HexaHomePage.HexaHomePageClass()
obj_1.HexaHomepage()

obj_2 = ContactUsPage()
obj_2.ContactUs()


listobj = [obj_1,obj_2]
print(listobj)

