from selenium.webdriver.common.by import By
import  HtmlTestRunner
import unittest
class HomePage():

    def __int__(self, driver):
        self.driver = driver

        self.profilePic_image_classname = "oxd-userdropdown-img"
        self.logout_button_linktext = "Logout"

    def click_profilePic(self):
        self.driver.find_element(By.CLASS_NAME, self.profilePic_image_classname).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_button_linktext).click()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Athreya S R/PycharmProjects/pythonProject2/POMDemo/report"))