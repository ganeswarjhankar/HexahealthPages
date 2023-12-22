#######This script is used in the PythonSeleniumFramework-master#########
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":

        S = Service("D:\\chromedriver.exe")
        driver = webdriver.Chrome(service=S)


    elif browser_name == "chrome":
        S = Service("D:\\chromedriver.exe")
        driver = webdriver.Chrome(service=S)
        #driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "chrome":
        print("chrome driver")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.hexahealth.com")


    request.cls.driver = driver
    yield
    driver.close()









