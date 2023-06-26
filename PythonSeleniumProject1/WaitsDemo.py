from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path= "C:/Users/Athreya S R/chromedriver.exe")
driver.get("https://www.microdegree.work/")
driver.implicitly_wait(10)

wait = WebDriverWait(driver,10)
try:
    element = wait.until(EC.element_to_be_clickable(By.LINK_TEXT,"All Course"))
    print("Element is clickable")
except:
    print("Element is not clickable")
    exit(2)
element.click()

driver.find_element(By.LINK_TEXT,"All Courses").click()
# driver.find_element(By.NAME,"btn").click()

print("test completed")
driver.close()
driver.quit()

