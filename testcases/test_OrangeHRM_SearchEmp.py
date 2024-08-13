import time

import pytest

from pageObjects.Add_Emp_Page import AddEmp_Class
from pageObjects.Login_Page import LoginPage_Class
from pageObjects.Search_Emp_Page import SearchEmp_Class
from Utilities.LoggerFile import LogGenerator
from Utilities.readConfigFile import ReadConfig_Class


class Test_SearchEmp:
    username = ReadConfig_Class.getUsername()
    password = ReadConfig_Class.getPassword()
    log = LogGenerator.loggen()

    @pytest.mark.regression
    @pytest.mark.group2
    def test_SearchEmp_006(self, setup):
        self.driver = setup
        self.log.info("Opening browser")
        self.lp = LoginPage_Class(self.driver)
        self.log.info("Enter Username")
        self.lp.Enter_UserName(self.username)
        self.log.info("Enter Password")
        self.lp.Enter_Password(self.password)
        self.log.info("Click on login Button")
        self.lp.Click_LoginButton()
        self.ae = AddEmp_Class(self.driver)
        self.log.info("Click on PIM Button")
        self.ae.Click_PIM()
        self.se = SearchEmp_Class(self.driver)
        Emp_ID = "09557"
        self.log.info("Entering Employee ID")
        self.se.Enter_EmpID(Emp_ID)

        self.log.info("Clicking Search Button")
        self.se.Click_Search_Emp()

        self.log.info("Verifying Search Result")
        if self.se.Search_Result() == Emp_ID:
            self.log.info("Test Passed: Employee found.")
            assert True
        else:
            self.log.error("Test Failed: Employee not found.")
            assert False

# logs are pending for above testcase


# Add emp  --> params and excel
# search emp --> params and excel