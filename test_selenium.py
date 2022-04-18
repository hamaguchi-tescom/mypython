import importlib
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("http://www.google.com")

search_box = driver.find_element(By.NAME, "q").send_keys("Selenium" + Keys.ENTER)
# search_button = driver.find_element(By.NAME, "btnK")  
# search_box.send_keys("Selenium")
# search_box.submit()

value = driver.find_element(By.NAME, "q").get_attribute("value") # => "Selenium"
print(value)
# driver.quit()