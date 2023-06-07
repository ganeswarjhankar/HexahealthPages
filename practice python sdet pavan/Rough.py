import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)

driver.get("https://www.hexahealth.com/")

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

for link in links:
    href = link.get_attribute("href")
    if href and not href.startswith(("tel:", "mailto:", "javascript:")):
        try:
            response = requests.head(href)
            if response.status_code == 200:
                print(f"Link '{href}' is accessible.")
            else:
                print(f"Link '{href}' is broken (status code: {response.status_code}).")
        except requests.ConnectionError:
            print(f"Error connecting to link '{href}'.")
    else:
        print(f"Link '{href}' does not have a valid URL.")
