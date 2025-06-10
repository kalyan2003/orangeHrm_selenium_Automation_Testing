import pytest
from selenium import webdriver
import time
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import logFileGen
from utilities import XLUtilities as xlu
from utilities.csvReportGeneration import write_result_to_csv


class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationURL()
    data_path = r"C:\Users\pavan\Documents\Selenium_Projects\nopCommerce_Project\TestData\LoginData.xlsx"
    logger =  logFileGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("------- Test_002_DDT_Login------")
        self.logger.info("********* Verifying Login DDT test *******")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.rows = xlu.getRowCount(self.data_path,'Sheet1')
        print("Number of rows:",self.rows)
        list_status = []
        for r in range(2,self.rows+1):
            self.username = xlu.readData(self.data_path,'Sheet1',r,1)
            self.password = xlu.readData(self.data_path,'Sheet1',r,2)
            self.expecResult = xlu.readData(self.data_path,'Sheet1',r,3)

            self.lp.setUserName(self.username)
            self.lp.setPassowrd(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            try:
                DashName = self.lp.geteleName()
            except Exception as e:
                DashName = "Pavan"
                self.logger.warning(f"Dashboard element not found for username: {self.username}. Exception: {e}")

            if DashName == "Dashboard":
                if self.expecResult == "Pass":
                    self.logger.info("****Passed*****")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("***failed****")
                    self.lp.clickLogout()
                    list_status.append("Fail")
            elif DashName != "Dashboard":
                if self.expecResult == 'Pass':
                    self.logger.info("****Failed****")
                    list_status.append("Fail")
                elif self.expecResult == 'Fail':
                    self.logger.info("***** Passed *******")
                    list_status.append("Pass")


        if "Fail" not in list_status:
            self.logger.info("***** Login DDT test passed *****")
            write_result_to_csv("Test_002", self.__class__.__name__, "PASSED")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT test failed ******")
            write_result_to_csv("Test_002", self.__class__.__name__, "FAILED")
            self.driver.close()
            assert False
        self.logger.info("***** End of Login DDT Test *******")
        self.logger.info("***** Completed TC_LoginDDT_002 ******")












