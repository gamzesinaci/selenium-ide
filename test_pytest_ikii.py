from typing import Literal
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driver bekleten yapı
from selenium.webdriver.support import expected_conditions  as ec #beklenen koşullar (webDriver verilen koşullar)
from selenium.webdriver.common.action_chains import ActionChains #elementlerı birden fazla işlem yapmak istiyordak kullanırız
import pytest


class Test_Pytest:

    def setup_method(self): #her test başlangıcında çalışacak fonksiyon
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() #ekranı büyütür
      
    def teardown_method(self): #her seferinde testin bitinminde çalışacak fonksiyon
        self.driver.quit()

    @pytest.mark.parametrize("username,password",[("1","secret_sauce"),("problem_user","1"),("error_user","1")])
    def test_invalid_login(self,username,password):
        
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)

        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert  errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
    
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_valid_remove(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)

        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)

        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()

        self.driver.execute_script("window.scrollTo(0,500)") 
        addToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-sauce-labs-fleece-jacket']")))
        addToCart.click()

        cartControl = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='shopping_cart_container']/a")))
        cartControl.click()

        remove = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='remove-sauce-labs-fleece-jacket']")))
        assert remove.text == "Remove"
        sleep(5)

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_filter(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)

        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)

        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()

        self.driver.execute_script("window.scrollTo(0,500)") 
        filterProduct = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='header_container']/div[2]/div/span/select")))
        filterProduct.click()

        PriceLowToHigh = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='header_container']/div[2]/div/span/select/option[3]")))
        PriceLowToHigh.click()
        sleep(5)

