import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service (r"C:\Users\BHAGYASHRI\Downloads\chromedriver_win32 (1)\chromedriver")
driver =webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "blinkingText").click()
parentwindow = driver.window_handles
driver.switch_to.window(parentwindow[1])
message = driver.find_element(By.XPATH, "//div//div[2]//p[2]").text
print(message)
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email = re.findall(pattern, message)
print(email)
driver.close()