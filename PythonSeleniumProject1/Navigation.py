from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Users\\Athreya S R\\chromedriver.exe")

driver.get("https://practice.microdegree.work")
print(driver.find_element(By.LINK_TEXT, "Manual Testing").text)
driver.find_element(By.LINK_TEXT, "Manual Testing").click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)