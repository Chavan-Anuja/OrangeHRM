import pytest

from pageObjects.Add_Emp_Page import AddEmp_Class
from pageObjects.Login_Page import LoginPage_Class
from Utilities.LoggerFile import LogGenerator
from Utilities.readConfigFile import ReadConfig_Class


class Test_AddEmp:
    username = ReadConfig_Class.getUsername()
    password = ReadConfig_Class.getPassword()
    log = LogGenerator.loggen()

    Photo_File_Path = r"C:\Users\omkar\OneDrive\Pictures\Screenshots\Screenshot (15).png"

    def test_AddEmp_005(self, setup):
        self.log.info("test_AddEmp_005 testcase is started")
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
        self.log.info("Click on AddEmp  Button")
        self.ae.Click_AddEmp_Button()
        self.log.info("Enter FirstName")
        self.ae.Enter_FirstName("Credence")
        self.log.info("Enter MiddleName")
        self.ae.Enter_MiddleName("IT")
        self.log.info("Enter LastName")
        self.ae.Enter_LastName("Pune")
        self.log.info("Uploading Image")
        self.ae.Upload_Photo_File(self.Photo_File_Path)
        self.log.info("Click On Save Button")
        self.ae.Click_Save_Button()
        self.log.info("Validating the success message for add emp ")
        if self.ae.Validate_AddEmp_SuccessMessage() == "Successfully Saved":
            self.log.info("test_AddEmp_005 testcase is passed")
            assert True
        else:
            self.log.info("test_AddEmp_005 testcase is failed")
            self.driver.save_screenshot(".\\Screenshots\\test_AddEmp_005_fail.png")
            assert False
        self.log.info("test_AddEmp_005 testcase is completed")


# pytest -v -s --browser firefox "testCases/test_OrangeHRM_AddEmp.py"