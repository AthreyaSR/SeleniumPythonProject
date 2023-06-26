from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver = webdriver.Chrome("C:\Users\Athreya S R\chromedriver.exe")

driver.get("https://www.amazon.in/")
print(driver.title)
# print(driver.find_element(By.LINK_TEXT, "Mobiles").text)
# driver.find_element(By.LINK_TEXT, "Mobiles").click()
try:
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"//select[@id =searchDropdownBox]"))
)
    element.click()
finally:
    driver.close()
    # driver.find_element(By.XPATH,"//select[@id =searchDropdownBox]").click()
    # driver.find_element(By.XPATH,"//*[@id="nav-hamburger-menu"]")
    # Items = driver.find_element(By.ID, "nav-xshop")
# print(Items.text)
# for Item in Items:
#     mobile = Item.find_element(By.XPATH, "/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[1]")
#     print(mobile.text)
time.sleep(10)
driver.quit()
