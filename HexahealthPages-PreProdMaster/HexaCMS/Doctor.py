from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)

# navigate to the form page
driver.get("http://stagingcms.hexahealth.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='UserName']").send_keys("ganeswar.jhankar@hexahealth.com")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//*[@id='Password']").send_keys("12345678")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//*[@id='btnLogin']").click()
driver.implicitly_wait(10)

#if driver.title=="Dashboard":
#    print("pass")
#else:
#    print("fail")



Drop=driver.find_element(By.XPATH, "//*[@id='drpAllForms']")
createDoctor=Select(Drop)
createDoctor.select_by_index(1)




testdata_string="Ganeshtestdata"
testdata_int=1234567890
testdata_email="ganeswarjhankar@gmail.com"


driver.find_element(By.XPATH,"//*[@id='BasicInfo_Name']").send_keys(testdata_string)
genderdrop=driver.find_element(By.XPATH,"//*[@id='BasicInfo_Gender']")
gender=Select(genderdrop)
gender.select_by_index(1)
driver.find_element(By.XPATH,"//*[@id='BasicInfo_AddressLine1']").send_keys(testdata_string)
driver.find_element(By.XPATH, "//*[@id='BasicInfo_AddressLine2']").send_keys(testdata_string)
driver.find_element(By.XPATH, "//*[@id='BasicInfo_AddressLine3']").send_keys(testdata_string)
driver.find_element(By.XPATH, "//*[@id='BasicInfo_DoctorEmail']").send_keys(testdata_email)
driver.find_element(By.XPATH, "//*[@id='BasicInfo_DoctorPhoneNo']").send_keys(testdata_int)
driver.find_element(By.XPATH, "//*[@id='BasicInfo_DoctorPhoneNo']").send_keys(testdata_int)





