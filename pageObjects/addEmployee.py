import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class addEmployee:
    pimButton_xpath = "//div[@class='oxd-sidepanel-body']//ul/li[2]/a"
    addEmplyee_buttton_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    textbox_input_firstName = "//input[@name='firstName']"
    textbox_input_middlename = "//input[@name='middleName']"
    textbox_input_lastname = "//input[@name='lastName']"
    textbox_input_empId = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    save_button_xpath = "//button[@type='submit']"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,30)

    def clickPim(self):
        pim_button = self.driver.find_element(By.XPATH,self.pimButton_xpath)
        pim_button.click()

    def clickaddEmployee(self):
        addButton = self.driver.find_element(By.XPATH,self.addEmplyee_buttton_xpath)
        addButton.click()

    def setFirstname(self,firstname):
        inputFirstname = self.driver.find_element(By.XPATH,self.textbox_input_firstName)
        inputFirstname.send_keys(firstname)

    def setMiddlename(self,middlename):
        inputMiddlename = self.driver.find_element(By.XPATH,self.textbox_input_middlename)
        inputMiddlename.send_keys(middlename)

    def setLastName(self,lastname):
        inputLastname = self.driver.find_element(By.XPATH,self.textbox_input_lastname)
        inputLastname.send_keys(lastname)

    def setEmpId(self,empId):
        inputEmpid = self.wait.until(EC.presence_of_element_located((By.XPATH,self.textbox_input_empId)))
        inputEmpid.send_keys(Keys.CONTROL + "a")
        inputEmpid.send_keys(Keys.DELETE)
        inputEmpid.send_keys(empId)


    def clickSaveBut(self):
        self.driver.find_element(By.XPATH,self.save_button_xpath).click()



def generateRandomname(length=8):
    prefix = "user_"
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return prefix + random_part



