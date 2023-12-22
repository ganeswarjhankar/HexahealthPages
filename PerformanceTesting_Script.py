from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class PerformanceTester:
    def __init__(self):
        # Set up Chrome options with performance logging enabled
        chrome_options = Options()
        chrome_options.add_argument("--enable-logging")
        chrome_options.add_argument("--headless")  # Optional: Run in headless mode for faster execution

        # Initialize the WebDriver with the Chrome options
        self.driver = webdriver.Chrome(options=chrome_options)

        # Enable performance logging
        self.driver.execute_cdp_cmd("Performance.enable", {})

    def measure_performance(self, url):
        # Navigate to the webpage you want to measure performance for
        self.driver.get(url)

        # Wait for the page to load completely (adjust the time as needed)
        self.driver.implicitly_wait(5)  # Waits for 5 seconds

        # Get the performance logs from the WebDriver
        performance_logs = self.driver.execute_cdp_cmd("Performance.getMetrics", {})['metrics']

        # Print the performance metrics
        for entry in performance_logs:
            print(entry['name'], ":", entry['value'])

        # Calculate and print the page load time
        navigation_start = self.driver.execute_script("return window.performance.timing.navigationStart")
        response_start = self.driver.execute_script("return window.performance.timing.responseStart")
        page_load_time = response_start - navigation_start
        print("Page load time:", page_load_time, "milliseconds")

    def quit(self):
        # Quit the WebDriver
        self.driver.quit()


# Example usage
tester = PerformanceTester()
tester.measure_performance('https://www.indiatimes.com/')
tester.quit()
