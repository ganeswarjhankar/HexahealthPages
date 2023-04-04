

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pytest_html import extras




@pytest.fixture(scope="class")
def driver():

    S = Service("D:\\chromedriver.exe")
    driver = webdriver.Chrome(service=S)



    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs["driver"]
        except KeyError:
            return
        screenshot_path = f"screenshot_{item.name}.png"
        driver.save_screenshot(screenshot_path)
        with open(screenshot_path, "rb") as f:
            screenshot = f.read()
        html = (
            f'<div><img src="data:image/png;base64,{screenshot.decode()}" alt="screenshot"/></div>'
        )
        extra = getattr(rep, "extra", [])
        extra.append(extras.html(html))
        rep.extra = extra
