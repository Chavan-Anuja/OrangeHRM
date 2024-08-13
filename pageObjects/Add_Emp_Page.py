import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AddEmp_Class:
    Click_PIM_XPATH = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a"
    Click_Add_Emp_Button_XPATH = "//i[@class='oxd-icon bi-plus oxd-button-icon']"
    Text_FirstName_XPATH = "//input[@placeholder='First Name']"
    Text_MiddleName_XPATH = "//input[@placeholder='Middle Name']"
    Text_LastName_XPATH = "//input[@placeholder='Last Name']"
    File_Upload_XPATH = "//input[@type='file']"
    Click_Save_Button_XPATH = "//button[@type='submit']"
    success_msg_XPATH = "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def Click_PIM(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.Click_PIM_XPATH)))
        self.driver.find_element(By.XPATH, self.Click_PIM_XPATH).click()

    def Click_AddEmp_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.Click_Add_Emp_Button_XPATH)))
        self.driver.find_element(By.XPATH, self.Click_Add_Emp_Button_XPATH).click()

    def Enter_FirstName(self, firstname):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.Text_FirstName_XPATH)))
        self.driver.find_element(By.XPATH, self.Text_FirstName_XPATH).send_keys(firstname)

    def Enter_MiddleName(self, middlename):
        self.driver.find_element(By.XPATH, self.Text_MiddleName_XPATH).send_keys(middlename)

    def Enter_LastName(self, lastname):
        self.driver.find_element(By.XPATH, self.Text_LastName_XPATH).send_keys(lastname)

    def Upload_Photo_File(self, path):
        self.driver.find_element(By.XPATH, self.File_Upload_XPATH).send_keys(path)

    def Click_Save_Button(self):
        self.driver.find_element(By.XPATH, self.Click_Save_Button_XPATH).click()

    def Validate_AddEmp_SuccessMessage(self):
        try:
            self.wait.until(
                expected_conditions.visibility_of_element_located((By.XPATH, self.success_msg_XPATH)))
            self.driver.find_element(By.XPATH, self.success_msg_XPATH)
            success_msg = self.driver.find_element(By.XPATH, self.success_msg_XPATH).text
            return success_msg
        except:
            pass

    
