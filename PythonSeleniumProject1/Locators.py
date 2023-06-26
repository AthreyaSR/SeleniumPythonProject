from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
import time
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome("C:\\Users\\Athreya S R\\chromedriver.exe")

driver.get("https://practice.microdegree.work")

# # id
# driver.find_element(By.ID, "selenium-tutorials-button").click()

# # class
# driver.find_element(By.CLASS_NAME, "selectorsPractice").click()

# # name
# # driver.find_element(By.NAME, "yourname").send_keys("Ganesh")
# # driver.find_element(By.ID,"your_email").send_keys("ganesh@gmail.com")

# # tag( only first element with tag gets identified)
# print(driver.find_element(By.TAG_NAME, "a").text)
# driver.find_element(By.TAG_NAME, "a").click()

# Xpath
# print(driver.find_element(By.XPATH,"/html/body/a[1]").text)
# driver.find_element(By.XPATH,"/html/body/a[1]").click()

# Link_test
# print(driver.find_element(By.LINK_TEXT, "Manual Testing").text)
# driver.find_element(By.LINK_TEXT, "Manual Testing").click()

# CSS_Selectors
# print(driver.find_element(By.CSS_SELECTOR, "a.active").text)
# driver.find_element(By.CSS_SELECTOR, "a.active").click()
print(driver.find_element(By.CSS_SELECTOR,"a#selenium-tutorials-button").text)


time.sleep(5)