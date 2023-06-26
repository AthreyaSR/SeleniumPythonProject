from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome("C:\\Users\\Athreya S R\\chromedriver.exe")
# driver.get("https://practice.microdegree.work")
# print(driver.title)
# element = driver.find_element(By.ID, "selenium-tutorials-button")
# print(element.text)
# element.click()
# # to get url of resultant page postclick
# currentUrl = driver.current_url
#
# # to compare current url with expected
# if currentUrl == "https://practice.microdegree.work/selenium.html":
#     print("test success")
# else:
#     print("test failed")
#
# time.sleep(10)

                                 #  OPTIMIZING THE CODE

driver = webdriver.Chrome("C:\\Users\\Athreya S R\\chromedriver.exe")
driver.get("https://practice.microdegree.work")
print(driver.title)
element = driver.find_element(By.ID, "selenium-tutorials-button")
print(element.text)
element.click()

if driver.current_url == "https://practice.microdegree.work/selenium.html":
    print("test Success")
else:
    print("test failed")

time.sleep(5)
driver.quit()





