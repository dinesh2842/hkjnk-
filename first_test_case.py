# from selenium import webdriver

# driver=webdriver.chrome("chromedriver.exe")
# driver.get("https://opensource-demo.orangehrmlive.com/")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the desired URL
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(10)
