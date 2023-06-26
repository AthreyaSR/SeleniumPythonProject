from selenium.webdriver.common.by import By
from POMDemo2.Locators.locators import Locators

class WelcomePage():

    def __int__(self,driver):
        self.driver =driver

        self.allCourses_button_linktext = Locators.allCourses_button_linktext
# The R.H.S value can be directly used in the below function next to By.Link_Text
    def click_AllCourses(self):
        self.driver.find_element(By.LINK_TEXT, self.allCourses_button_linktext).click()



