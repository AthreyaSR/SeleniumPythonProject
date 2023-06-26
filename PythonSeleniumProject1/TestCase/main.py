import unittest
from selenium import webdriver
import page
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

class PythonOrgSearch(unittest.TestCase):
     # The flow is run set-up --> run set of test examples --> tear down
    def setUp(self) -> None:
        print("setup")
        # self.driver = webdriver.Chrome()
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://www.python.org")

    # This func calls the MainPage() in page.py and assert true or false by using mainPage.is_title_matches()
    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matches()

# To execute the TCs and get the count of passesd and failed testCases
#     def test_example1(self):
#         print("test")
#         assert True
#
#     def test_example2(self):
#         assert False


    def tearDown(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
