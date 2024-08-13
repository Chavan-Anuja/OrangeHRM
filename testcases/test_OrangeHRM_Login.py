import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import LoginPage_Class
from Utilities.readConfigFile import ReadConfig_Class
from Utilities.LoggerFile import LogGenerator


class Test_OrangeHRM_Login:
    username = (ReadConfig_Class.getUsername())
    password = ReadConfig_Class.getPassword()
    log = LogGenerator.loggen()

    def test_OrangeHRM_url_001(self, setup):
        self.log.info("test_OrangeHRM_url_001 is started")
        self.driver = setup
        self.log.info("Opening browser")
        print("driver.title-->" + self.driver.title)
        self.log.info("Verifying the page title")
        if self.driver.title == "OrangeHRM":
            self.log.info("test_OrangeHRM_url_001 is passed,landed on correct url")
            time.sleep(3)
            self.log.info("Taking the Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_url_001_Pass.png")

            assert True
        else:
            self.log.info("test_OrangeHRM_url_001 is Failed")
            self.log.info("Taking the screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_url_001_fail.png")
            assert False
        self.log.info("Closing the broweser ")
        self.driver.quit()
        self.log.info("Test_OrabgeHrm_url_001 is completed")

    def test_OrangeHRM_Login_002(self, setup):
        self.log.info("test_OrangeHrm_002 is started")
        self.driver = setup
        self.log.info("Opening the browser")
        self.lp = LoginPage_Class(self.driver)
        # print("Username-->", self.username)
        # print("password-->", self.password)
        self.log.info("Entering Username-->" + self.username)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.lp.Enter_UserName(self.username)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.log.info("Entering password-->" + self.password)
        self.lp.Enter_Password(self.password)
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.log.info("Clicking on login button")
        self.lp.Click_LoginButton()
        self.log.info("Verifying the login status")
        if self.lp.Validate_Login_Stauts() == "LoginPass":
            self.log.info("Taking the screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_002_Pass.png")
            self.log.info("Clicking on Menu button")
            self.lp.Click_Menu_Button()
            self.log.info("clicking on logout button")
            self.lp.Click_Logout_Button()
            assert True
        else:
            self.log.info("test_orangeHrm_002 is failed")
            self.log.info("Taking the screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_002_Fail.png")
            assert False
        self.log.info("Closing the Browser")
        self.driver.quit()
        self.log.info("test_orangeHrm_002 is completed")
