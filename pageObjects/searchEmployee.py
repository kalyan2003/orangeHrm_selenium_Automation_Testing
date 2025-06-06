from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class searchEmployee:
    employee_name_input_textbox_xpath = "//input[@placeholder='Type for hints...']"
    employee_id_input_textbox_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div[2]/input[1]"
    search_button_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
    reset_button_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--ghost']"
    search_employee_first_name_xpath = "//div[@class='oxd-table-cell oxd-padding-cell'][3]"
    search_employee_Id_xpath = "//div[@class='oxd-table-cell oxd-padding-cell'][2]"
    employee_list_button = "//a[text()='Employee List']"
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def setEmployeeName(self,emplName):
        employeeName = self.wait.until(EC.presence_of_element_located((By.XPATH,self.employee_name_input_textbox_xpath)))
        employeeName.send_keys(emplName)

    def setEmployeeId(self,emp_id):
        employeeId = self.wait.until(EC.presence_of_element_located((By.XPATH,self.employee_id_input_textbox_xpath)))
        employeeId.send_keys(emp_id)

    def searchButton(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()

    def resetButton(self):
        self.driver.find_element(By.XPATH,self.reset_button_xpath).click()

    def clickEmployeeList(self):
        self.driver.find_element(By.XPATH,self.employee_list_button).click()



    def searchCustomerByemployeeName(self,employeename):
        flag = False
        employee_first_name = self.wait.until(EC.presence_of_element_located((By.XPATH,self.search_employee_first_name_xpath)))
        if employeename in employee_first_name.text:
            flag = True

        return flag


    def searchCustomerByemployeeId(self,emp_id):
        flag = False
        employee_id = self.wait.until(EC.presence_of_element_located((By.XPATH,self.search_employee_Id_xpath)))
        if emp_id == employee_id.text:
            flag = True

        return flag



