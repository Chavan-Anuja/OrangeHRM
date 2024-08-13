import time  # Import the time module to introduce delays in the test

from pageObjects.Login_Page import LoginPage_Class  # Import the LoginPage class from pageObjects module
from Utilities import Excel_utils
from Utilities.LoggerFile import LogGenerator  # Import the LogGenerator class for logging


class Test_OrangeHRM_Login_DDT:  # Define the test class for parameterized OrangeHRM login tests
    log = LogGenerator.loggen()  # Initialize the logger
    File_Path = ".\\testcases\\Test_Data\\Test_Data_1.xlsx"

    def test_OrangeHRM_Login_DDT_004(self, setup):
        self.log.info("test_OrangeHRM_Login_DDT_004 is started")  # Log the start of the test
        self.driver = setup  # Initialize the WebDriver using the setup fixture
        self.log.info("Opening the browser")  # Log the action of opening the browser
        self.lp = LoginPage_Class(self.driver)  # Create an instance of the LoginPage class
        self.rows = Excel_utils.get_rowCount(self.File_Path, "Login_Data")
        print("Number of rows in Excel Test data-->" + str(self.rows))
        List_Status = []
        Test_Result_columnno = 5
        for r in range(2, self.rows + 1):
            self.username = Excel_utils.readData(self.File_Path, "Login_Data", r, 2)
            self.password = Excel_utils.readData(self.File_Path, "Login_Data", r, 3)
            self.Excel_Result = Excel_utils.readData(self.File_Path, "Login_Data", r, 4)
            # print("username-->" + "loop-->" + str(r) +"--"+  str(self.username))
            # print("password-->" + "loop-->" + str(r) +"--"+ str(self.password))
            # print("Excel_Result-->" + "loop-->" + str(r) +"--"+ str(self.Excel_Result))
            # print("---------------------")
            self.log.info("Entering Username-->" + self.username)  # Log the action of entering the username from the test data
            self.lp.Enter_UserName(self.username)  # Enter the username using the page object method
            self.log.info("Entering Password-->" + self.password)  # Log the action of entering the password from the test data
            self.lp.Enter_Password(self.password)  # Enter the password using the page object method
            self.log.info("Clicking on login button")  # Log the action of clicking the login button
            time.sleep(3)
            self.lp.Click_LoginButton()  # Click the login button using the page object method
            self.log.info("Verifying the login status")  # Log the verification of the login status

            if self.lp.Validate_Login_Stauts() == "LoginPass" and self.Excel_Result == "Login_Pass":  # Check if login passed and expected result is "Login_Pass"
                List_Status.append("Pass")
                Excel_utils.writeData(self.File_Path, "Login_Data", r, Test_Result_columnno, "Pass")
                self.log.info("Taking the screenshot")  # Log the action of taking a screenshot
                self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_DDT_004_pass.png")  # Save a screenshot
                self.log.info("Clicking on Menu button")  # Log the action of clicking the menu button
                self.lp.Click_Menu_Button()  # Click the menu button using the page object method
                self.log.info("Clicking on logout button")  # Log the action of clicking the logout button
                self.lp.Click_Logout_Button()  # Click the logout button using the page object method

            elif self.lp.Validate_Login_Stauts() == "LoginPass" and self.Excel_Result == "Login_Fail":  # Check if login passed and expected result is "Login_Fail"
                List_Status.append("Fail")
                Excel_utils.writeData(self.File_Path, "Login_Data", r, 5, "Fail")
                self.log.info("Taking a screenshot")  # Log the action of taking a screenshot
                self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_DDT_004_fail.png")  # Save a screenshot
                self.log.info("Clicking on Menu button")  # Log the action of clicking the menu button
                self.lp.Click_Menu_Button()  # Click the menu button using the page object method
                self.log.info("Clicking on logout button")  # Log the action of clicking the logout button
                self.lp.Click_Logout_Button()  # Click the logout button using the page object method
            elif self.lp.Validate_Login_Stauts() == "LoginFail" and self.Excel_Result == "Login_Pass":  # Check if login failed and expected result is "Login_Pass"
                List_Status.append("Fail")
                Excel_utils.writeData(self.File_Path, "Login_Data", r, 5, "Fail")
                self.log.info("Taking a screenshot")  # Log the action of taking a screenshot
                self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_DDT_004_fail.png")  # Save a screenshot
            elif self.lp.Validate_Login_Stauts() == "LoginFail" and self.Excel_Result == "Login_Fail":  # Check if login failed and expected result is "Login_Fail"
                List_Status.append("Pass")
                Excel_utils.writeData(self.File_Path, "Login_Data", r, 5, "Pass")
                self.log.info("Taking a screenshot")  # Log the action of taking a screenshot
                self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_DDT_004_pass.png")  # Save a screenshot

        print(List_Status)
        if "Fail" not in List_Status:
            self.log.info("test_OrangeHRM_Login_DDT_004 is passed")
            assert True
        else:
            self.log.info("test_OrangeHRM_Login_DDT_004 is failed")
            assert False

        self.driver.quit()  # Close the browser
        self.log.info("Closing the browser")  # Log the action of closing the browser
        self.log.info("test_OrangeHRM_Login_DDT_004 is completed")
