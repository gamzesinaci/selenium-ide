from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
import pytest

class Test:
  
    def setup_method(self): #her test başlangıcında çalışacak fonk
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() 

    def teardown_method(self): # her testinin bitiminde çalışacak fonk
        self.driver.quit()

    @pytest.mark.parametrize("username,password,errorMessage",[("","","Epic sadface: Username and password do not match any user in this service"),("standart_user","","Epic sadface: Password is required"),("locked_out_user","secret_sauce","Epic sadface: Sorry, this user has been locked out.")])
    def test_bir(self,username,password,errorMessage):
       usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
       usernameInput.send_keys(username)
       
       passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
       passwordInput.send_keys(password)
       
       loginButton = self.driver.find_element(By.ID,"login-button")
       loginButton.click()
       
       errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]")
       assert errorMessage.text == errorMessage
