from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
# The below 3 lines need to be written before import of page class to avoid ModuleNotFoundError
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import unittest
from POMDemo.Pages.loginPage import LoginPage
from POMDemo.Pages.homePage import HomePage
import HtmlTestRunner


class LoginTests(unittest.TestCase):

     @classmethod
     def setUpClass(cls) -> None:
          cls.driver = webdriver.Chrome(ChromeDriverManager().install())
          cls.driver.implicitly_wait(10)

     def test_Login_valid(self):
           driver = self.driver
           driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

           login = LoginPage()
           login.__int__(driver)
           login.enter_username("Admin")
           login.enter_password("admin123")
           login.click_Login()



           homepage = HomePage()
           homepage.__int__(driver)
           homepage.click_profilePic()
           homepage.click_logout()


           # time.sleep(5)
           # self.driver.find_element(By.NAME, "username").send_keys("Admin")
           # self.driver.find_element(By.NAME, "password").send_keys("admin123")
           # time.sleep(20)
           # self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
           # time.sleep(5)
           # self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-img").click()
           # self.driver.implicitly_wait(3)
           # self.driver.find_element(By.LINK_TEXT, "Logout").click()
           time.sleep(2)

     @classmethod
     def tearDownClass(cls) -> None:
         cls.driver.close()
         cls.driver.quit()
         print("test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Athreya S R/PycharmProjects/pythonProject2/POMDemo/report"))