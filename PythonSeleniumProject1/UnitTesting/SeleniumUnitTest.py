import HtmlTestRunner
import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # def setUp(self) -> None:
    #     # self.driver.implicitly_wait(10)
    #     # self.driver.maximize_window()

    def test_search_2(self):
        self.driver.get("https://www.youtube.com/")
        time.sleep(10)

        self.driver.find_element(By.ID,"guide-icon").click()
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, "Library").click()
        time.sleep(5)
        # self.driver.find_element(By.CLASS_NAME, "BHzsHc").click()
        # self.driver.find_element(By.ID,"search-icon-legacy").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x,"Library - YouTube")

    def test_search_1(self):
        self.driver.get("https://www.youtube.com/")
        time.sleep(10)
        x = self.driver.title
        print(x)

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """


    @classmethod
    def tearDownClass(Class) -> None:
        Class.driver.close()
        Class.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Athreya S R/PycharmProjects/PythonSeleniumProject1/reports'))


