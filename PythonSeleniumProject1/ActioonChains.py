from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\\Users\\Athreya S R\\chromedriver.exe")
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

driver.find_element(By.ID,"langSelect-EN").click()

BigCookie = driver.find_element(By.ID,"bigCookie")
Count_Cookies = driver.find_element(By.ID,"bigCookie")
items = [driver.find_element(By.ID,"productPrice0") ]

actions = ActionChains(driver)
for i in range(500):
    actions.click(BigCookie)
time.sleep(10)

for i in range(5000):
    actions.perform()

i= i+1

time.sleep(10)