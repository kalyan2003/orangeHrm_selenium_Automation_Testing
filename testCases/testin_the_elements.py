from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait = WebDriverWait(driver,50)
username = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Username']"))).send_keys("Admin")
password = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Password']"))).send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

logout_but = wait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='oxd-userdropdown-tab']")))
logout_but.click()
logout = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='/web/index.php/auth/logout']")))
logout.click()
time.sleep(5)