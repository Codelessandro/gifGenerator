from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://localhost:4200/")
driver.save_screenshot("screenshot.png")
driver.close()