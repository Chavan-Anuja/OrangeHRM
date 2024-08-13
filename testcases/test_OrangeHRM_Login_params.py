import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import LoginPage_Class
from Utilities.readConfigFile import ReadConfig_Class
from Utilities.LoggerFile import LogGenerator

class Test_OrangeHrm_Login_params:
    log = LogGenerator.loggen()

    def test_OrangeHrm_Login_params_003(self,setup,getDataForLogin):
        self.log.info("Test_OrangeHrm_login_params_003 is started")
        self.driver = setup
        self.log.info("Opening the Browser")
        self.lp = LoginPage_Class(self.driver)
        self.log.info("entering username-->" + getDataForLogin[0])
        self.lp.Enter_UserName(getDataForLogin[0])
        self.log.info("entering password-->" + getDataForLogin[1])
        self.lp.Enter_Password(getDataForLogin[1])
        self.log.info("Clicking on login button")
        self.lp.Click_LoginButton()
        self.log.info("Verifying the login status")
        if self.lp.Validate_Login_Stauts() == "LoginPass" and getDataForLogin[2] == "LoginPass":
            self.log.info("test_OrangeHrm_Login_Params_003 is passed")
            self.log.info("Taking the screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_pass.png")
            self.log.info("Clicking on Menu Button")
            self.lp.Click_Menu_Button()
            self.log.info("Clicking on logout button")
            self.lp.Click_Logout_Button()
            assert False
        elif self.lp.Validate_Login_Stauts() == "LoginPass" and getDataForLogin[2] == "LoginFail":
            self.log.info("test_OrangeHrm_Login_Params_003 is failed")
            self.log.info("Taking the screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_fail.png")
            self.log.info("Clicking on Menu Button")
            self.lp.Click_Menu_Button()
            self.log.info("Clicking on logout button")
            self.lp.Click_Logout_Button()
            assert False
        elif self.lp.Validate_Login_Stauts() == "LoginFail" and getDataForLogin[2] == "LoginPass":
            self.log.info("test_OrangeHrm_Login_Params_003 is failed")
            self.log.info("Taking a screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_003_fail.png")
            assert False
        elif self.lp.Validate_Login_Stauts() == "LoginFail" and getDataForLogin[2] == "LoginFail":
            self.log.info("test_OrangeHrm_Login_Params_003 is failed")
            self.log.info("Taking a screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_003_fail.png")
            assert True
        self.log.info("Closing the browser")
        self.driver.quit()
        self.log.info("test_OrangeHRM_Login_params_003 is completed")

