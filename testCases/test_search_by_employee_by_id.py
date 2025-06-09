import time

import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import logFileGen
from pageObjects.addEmployee import addEmployee
from pageObjects.searchEmployee import searchEmployee
from pageObjects.addEmployee import generateRandomNumber
from pageObjects.addEmployee import generateRandomname


class Test_004_Search_by_Employee:
    baseUrl = ReadConfig.getApplicationURL()
    logger = logFileGen.loggen()
    firstName = generateRandomname(length=8)
    middleName = generateRandomname(length=8)
    lastName = generateRandomname(length=8)
    emp_id = generateRandomNumber(length=6)


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_serach_by_employee_name(self,setup):
        self.logger.info("--------- Test_004_Search_By_Employee ---------")
        self.logger.info("************ Verifying Login search employee test **************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setUserName("Admin")
        self.lp.setPassowrd("admin123")
        self.lp.clickLogin()
        time.sleep(5)
        self.addEmp = addEmployee(self.driver)
        self.addEmp.clickPim()
        time.sleep(3)
        self.addEmp.clickaddEmployee()
        time.sleep(3)
        self.addEmp.setFirstname(self.firstName)
        self.addEmp.setMiddlename(self.middleName)
        self.addEmp.setLastName(self.lastName)
        self.addEmp.setEmpId(self.emp_id)
        self.addEmp.clickSaveBut()
        time.sleep(10)
        self.searchEmp = searchEmployee(self.driver)
        self.searchEmp.clickEmployeeList()
        time.sleep(5)

        self.searchEmp.setEmployeeId(self.emp_id)
        time.sleep(3)
        self.searchEmp.searchButton()
        time.sleep(5)
        flag = self.searchEmp.searchCustomerByemployeeId(self.emp_id)

        if flag:
            assert True
            self.logger.info("********* search employee through employee name Passed **************")
        else:
            self.logger.info("********* Search Employee through employee name is failed ***********")
            assert False
