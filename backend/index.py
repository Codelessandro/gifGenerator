from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://torahgenerator.s3.us-east-2.amazonaws.com/index.html")
driver.save_screenshot("screenshot.png")
driver.close()