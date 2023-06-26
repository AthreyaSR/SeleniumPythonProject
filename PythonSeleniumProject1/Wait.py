from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\\Users\\Athreya S R\\chromedriver.exe")

driver.get("https://www.amazon.in/")
try:
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Mobiles"))
)
    element.click()

    # element = WebDriverWait(driver, 20).until(
    #         EC.presence_of_element_located((By.ID, "sobe_d_b_1_3"))
    #     )
    # element.click()
# to Navigate back to previous page
    driver.back()
    driver.back()
 # if you donot want to quit before execution use except otherwise use finally
finally:
    driver.quit()