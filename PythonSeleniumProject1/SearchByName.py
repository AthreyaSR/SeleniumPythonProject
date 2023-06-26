from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# driver = webdriver.Chrome(executable_path="C:\\Users\\Athreya S R\\chromedriver.exe")
driver = webdriver.Chrome("C:\\Users\\Athreya S R\\chromedriver.exe")
# to open the website
driver.get("https://www.youtube.com/")
# to print the title of website
print(driver.title)
# to search element by name
search = driver.find_element(By.NAME, "search_query")
# to clear any junk in input field
search.clear()
# to enter input in text field
search.send_keys("test", Keys.ARROW_DOWN)
# print(driver.page_source)
# to press enter button
search.send_keys(Keys.RETURN)

#explicit Wait
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    print(main.text)
except:
    driver.quit()

time.sleep(5)
