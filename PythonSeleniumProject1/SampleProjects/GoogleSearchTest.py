from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automation(self):
          self.driver.get("https://www.google.com/")
          self.driver.find_element(By.ID,"APjFqb").send_keys("Automation")
          time.sleep(5)
          print(self.driver.find_element(By.NAME, "btnK").text)
          self.driver.find_element(By.NAME, "btnK").click()
          print(self.driver.title)

     # Intentionally making testcase to fail
    def test_search_Athreya(self):
          self.driver.get("https://www.google.com/")
          self.driver.find_element(By.ID,"APjFqb").send_keys("Athreya")
          time.sleep(5)
          print(self.driver.find_element(By.NAME, "btnK1").text)
          self.driver.find_element(By.NAME, "btnK").click()
          print(self.driver.title)

    @classmethod
    def tearDownClass(cls) -> None:
        print("test completed")
        cls.driver.minimize_window()
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output='C:/Users/Athreya S R/PycharmProjects/PythonSeleniumProject1/SampleProjects/Reports'))