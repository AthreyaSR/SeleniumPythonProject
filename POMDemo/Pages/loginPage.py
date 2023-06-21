from selenium.webdriver.common.by import By
import HtmlTestRunner
import unittest

class LoginPage():

    def __int__(self,driver):
        self.driver = driver

        self.username_textbox_name = "username"
        self.password_textbox_name = "password"
        self.login_button_xpath = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"

    def enter_username(self,username):
        self.driver.find_element(By.NAME, self.username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).send_keys(password)

    def click_Login(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Athreya S R/PycharmProjects/pythonProject2/POMDemo/report"))