import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage_Class:
    Text_Username_Xpath = (By.XPATH, "//input[@placeholder='Username']")
    Text_Password_Xpath = (By.XPATH, "//input[@placeholder='Password']")
    Click_LoginButton_Xpath = (By.XPATH, "//button[normalize-space()='Login']")
    Menu_XPath = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    Click_Logout_Xpath = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def Enter_UserName(self, username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Username_Xpath))
        self.driver.find_element(*LoginPage_Class.Text_Username_Xpath).send_keys(username)

    def Enter_Password(self, password):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Password_Xpath))
        self.driver.find_element(*LoginPage_Class.Text_Password_Xpath).send_keys(password)

    def Click_LoginButton(self):
        self.driver.find_element(*LoginPage_Class.Click_LoginButton_Xpath).click()

    def Click_Menu_Button(self):
        self.driver.find_element(*LoginPage_Class.Menu_XPath).click()

    def Click_Logout_Button(self):
        self.driver.find_element(*LoginPage_Class.Click_Logout_Xpath).click()

    def Validate_Login_Stauts(self):
        try:
            time.sleep(2)
            self.driver.find_element(*LoginPage_Class.Menu_XPath)
            time.sleep(3)
            print("User login test case is passed")
            return "LoginPass"
        except:
            print("User login test case is failed")
            return "LoginFail"


