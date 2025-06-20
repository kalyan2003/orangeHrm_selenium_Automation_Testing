import time
import pytest
from pageObjects.LoginPage import Login
from pageObjects.addEmployee import addEmployee
from pageObjects.addEmployee import generateRandomname
from utilities.readProperties import ReadConfig
from utilities.customLogger import logFileGen
from pageObjects.addEmployee import generateRandomNumber
from utilities.csvReportGeneration import write_result_to_csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_003_Add_Employee:
    baseUrl = ReadConfig.getApplicationURL()
    logger = logFileGen.loggen()

    @pytest.mark.regression
    def test_add_employee(self,setup):
        self.logger.info("------- Test_003_Add_Employee--------")
        self.logger.info("****** Started Add Employee Test *******")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.firstName = generateRandomname(length=8)
        self.middleName = generateRandomname(length=8)
        self.lastName = generateRandomname(length=8)
        self.empId = generateRandomNumber(length=6)
        self.lp = Login(self.driver)
        self.lp.setUserName("Admin")
        self.lp.setPassowrd("admin123")
        self.lp.clickLogin()
        time.sleep(10)
        self.addEmp = addEmployee(self.driver)
        self.addEmp.clickPim()
        time.sleep(10)
        self.addEmp.clickaddEmployee()
        time.sleep(10)
        self.addEmp.setFirstname(self.firstName)
        self.addEmp.setMiddlename(self.middleName)
        self.addEmp.setLastName(self.lastName)
        self.addEmp.setEmpId(self.empId)
        self.addEmp.clickSaveBut()
        time.sleep(10)
        self.logger.info("**** Employee details are submitted ********")
        self.logger.info("------- Checking whether employee details are saved ----------")

        self.employee_name = self.addEmp.find_profile_name()

        if self.firstName in self.employee_name:
            self.logger.info("********** Add Employee test Passed **********")
            write_result_to_csv("Test_003", self.__class__.__name__,"PASSED")
            assert True
        else:
            self.logger.info("********** Add Employee test Failed ***********")
            write_result_to_csv("Test_003", self.__class__.__name__, "FAILED")
            assert False


        self.driver.close()
        self.logger.info("********* Ending Add Employee test ************")


