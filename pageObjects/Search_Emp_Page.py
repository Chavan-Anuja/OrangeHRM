from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchEmp_Class:
    Text_Emp_name_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[" \
                          "1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"

    Text_EmpID_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]"

    Click_SearchEmp_Xpath = "//button[@type='submit']"

    Search_Result_CSS = "div[class='oxd-table-card'] div:nth-child(2) div:nth-child(1)"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Enter_EmpName(self, empname):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.Text_Emp_name_XPATH)))
        self.driver.find_element(By.XPATH, self.Text_Emp_name_XPATH).send_keys(empname)


    def Enter_EmpID(self, empId):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.Text_EmpID_XPATH)))
        self.driver.find_element(By.XPATH, self.Text_EmpID_XPATH).send_keys(empId)

    def Click_Search_Emp(self):
        self.driver.find_element(By.XPATH, self.Click_SearchEmp_Xpath).click()

    def Search_Result(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.Search_Result_CSS)))
            result = self.driver.find_element(By.CSS_SELECTOR, self.Search_Result_CSS).text
            print(result)
            return result
        except TimeoutException:
            pass



