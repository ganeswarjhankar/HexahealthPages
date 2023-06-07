import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Launch the website and navigate to the payment page
driver = webdriver.Chrome()
driver.get("https://www.example.com/payment")

# Enter valid payment details
card_number = driver.find_element(By.ID, "cardNumber")
card_number.send_keys("1234567890123456")

expiry_date = driver.find_element(By.ID, "expiryDate")
expiry_date.send_keys("12/24")

cvv = driver.find_element(By.ID, "cvv")
cvv.send_keys("123")

# Click on the "Submit" button
submit_button = driver.find_element(By.ID, "submitButton")
submit_button.click()

# Verify that the payment gateway API is called and returns a successful response
payment_api_url = "https://api.example.com/payment"
payment_data = {
    "cardNumber": "1234567890123456",
    "expiryDate": "12/24",
    "cvv": "123"
}
response = requests.post(payment_api_url, json=payment_data)

if response.status_code == 200:
    print("Payment API call successful")
else:
    print("Payment API call failed")

# Validate that the user is redirected to a confirmation page after successful payment
confirmation_page = driver.find_element(By.ID, "confirmationPage")

if confirmation_page.is_displayed():
    print("Payment successful, redirected to confirmation page")
else:
    print("Payment failed")

# Verify that the payment details are stored correctly in the database
database_query = "SELECT * FROM payment_details WHERE card_number = '1234567890123456'"
# Execute the database query and validate the results

# Close the browser
driver.quit()
