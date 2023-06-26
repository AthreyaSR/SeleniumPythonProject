# Name of the file should be in test_filename.py format
# Each function name should start with test_functionName

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pytest

class Testsample():
    @pytest.fixture()
    def test_setup(self):
        # To make driver global and accessible to all functions
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("test completed")

    def test_login(self,test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME,"username").send_keys("Admin")
        driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(10)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(5)
        x = driver.title
        assert x == "OrangeHRM"

    # def test_tearDown():
    #     driver.close()
    #     driver.quit()
    #     print("test completed")

# In terminal type :pytest file_name to run