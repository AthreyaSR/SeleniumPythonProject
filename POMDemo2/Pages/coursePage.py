from selenium.webdriver.common.by import By
from POMDemo2.Locators.locators import Locators

class CoursePage():

    def __int__(self,driver):
        self.driver = driver

        self.CloseChatbot_button_className = Locators.CloseChatbot_button_className
        self.logo_button_xPath = Locators.logo_button_xPath

    def click_CloseChatbot(self):
        self.driver.find_element(By.CLASS_NAME, self.CloseChatbot_button_className).click()

    def click_Logo(self):
        self.driver.find_element(By.XPATH, self.logo_button_xPath).click()
