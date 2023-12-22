import tkinter as tk
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class SeleniumBotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Selenium Bot UI")

        self.driver = None
        self.running = False

        self.create_ui()

    def create_ui(self):
        self.start_button = tk.Button(self.root, text="Start Bot", command=self.start_bot)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop Bot", command=self.stop_bot)
        self.stop_button.pack()

        self.num_results_label = tk.Label(self.root, text="Number of Image Results:")
        self.num_results_label.pack()

        self.num_results_entry = tk.Entry(self.root)
        self.num_results_entry.pack()

    def start_bot(self):
        if self.running:
            return

        self.running = True
        num_results = int(self.num_results_entry.get()) if self.num_results_entry.get() else 10

        # Create a new instance of a web browser (replace 'chromedriver_path' with the actual path to ChromeDriver)



        S = Service("D:\\msedgedriver.exe")

        self.driver = webdriver.Edge(service=S)
        self.driver.get("https://www.thailandos.com/app/uploads/2023/07/sim-card-hero.webp")
        self.driver.maximize_window()
        time.sleep(5)

        # Locate the image you want to right-click
        image_element = self.driver.find_element(By.XPATH,"//img")  # Replace 'image_id' with the actual ID of the image

        # Create an ActionChains instance
        actions = ActionChains(self.driver)

        #Right click on the image

        actions.context_click(image_element).perform()

        # Locate and click on the "Search Google for image" option
        option_element = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Search image in bing')]")
        time.sleep(5)
        option_element.click()



        # Simulate search (replace 'your_search_query' with the actual search query)
        search_box = self.driver.find_element(By.XPATH,"//*[@id='APjFqb']")
        search_box.send_keys("india images")
        time.sleep(5)
        search_box.send_keys(Keys.RETURN)

        # You can add more automation steps here, e.g., interacting with search results and extracting images

        # For demonstration purposes, let's wait for a few seconds
        time.sleep(5)

        self.stop_bot()

    def stop_bot(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
        self.running = False


if __name__ == "__main__":
    root = tk.Tk()
    app = SeleniumBotUI(root)
    root.mainloop()
