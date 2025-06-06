import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
import time
class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_homePagetitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "OrangeHRM":
            assert True
        else:
            assert  False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassowrd(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        time.sleep(10)

        if act_title == "OrangeHRM":
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\pavan\\Documents\\Selenium_Projects\\OrqngeHrm_POM_project\\Screenshots\\test_login.png")
            time.sleep(5)
            self.driver.close()
            assert False


