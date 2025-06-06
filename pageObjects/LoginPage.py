from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class Login:
    textbox_username_xpath = "//input[@placeholder='Username']"
    textbox_password_xpath = "//input[@placeholder='Password']"
    button_login_xpath = "//button[@type='submit']"
    button_logout_dropdown_xpath = "//span[@class='oxd-userdropdown-tab']"
    button_logout = "//a[@href='/web/index.php/auth/logout']"
    eleRequired = "//h6[normalize-space()='Dashboard']"



    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,50)

    def setUserName(self,username):
        username_in = self.wait.until(EC.presence_of_element_located((By.XPATH,self.textbox_username_xpath)))
        username_in.clear()
        username_in.send_keys(username)

    def setPassowrd(self,password):
        password_in = self.wait.until(EC.presence_of_element_located((By.XPATH,self.textbox_password_xpath)))
        password_in.clear()
        password_in.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()


    def geteleName(self):
        eleName = self.driver.find_element(By.XPATH,self.eleRequired).text
        return eleName

    def clickLogout(self):
        logout_drop_but = self.wait.until(EC.presence_of_element_located((By.XPATH,self.button_logout_dropdown_xpath)))
        logout_drop_but.click()
        logout = self.wait.until(EC.presence_of_element_located((By.XPATH,self.button_logout)))
        logout.click()


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
#
# class Login:
#     textbox_username_xpath = "//input[@placeholder='Username']"
#     textbox_password_xpath = "//input[@placeholder='Password']"
#     button_login_xpath = "//button[@type='submit']"

#
#     def __init__(self,driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver,50)
#
#     def setUserName(self,username):
#         username_in = self.wait.until(EC.presence_of_element_located((By.XPATH,self.textbox_username_xpath)))
#         username_in.clear()
#         username_in.send_keys(username)
#
#     def setPassowrd(self,password):
#         password_in = self.wait.until(EC.presence_of_element_located((By.XPATH,self.textbox_password_xpath)))
#         password_in.clear()
#         password_in.send_keys(password)
#
#     def clickLogin(self):
#         self.driver.find_element(By.XPATH,self.button_login_xpath).click()
#
#
#
#
#
#
#
#
