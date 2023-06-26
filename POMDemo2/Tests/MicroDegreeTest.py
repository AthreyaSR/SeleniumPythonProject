from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# The below 3 lines need to be written before import of page class to avoid ModuleNotFoundError
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import time
import unittest
from POMDemo2.Pages.welcomePage import WelcomePage
from POMDemo2.Pages.coursePage import CoursePage
import HtmlTestRunner


class microDegreeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver =webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)

    def test_MicroDegree(self):
        driver = self.driver
        driver.get("https://www.microdegree.work/")
        time.sleep(10)
        welcomePage = WelcomePage()
        welcomePage.__int__(driver)
        welcomePage.click_AllCourses()


        coursePage = CoursePage()
        coursePage.__int__(driver)
        time.sleep(10)
        coursePage.click_CloseChatbot()
        time.sleep(10)
        coursePage.click_Logo()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Athreya S R/PycharmProjects/pythonProject2/POMDemo2/reports"))