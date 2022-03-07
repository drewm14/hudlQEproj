from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from settings import username, password
from selenium.webdriver.common.action_chains import ActionChains

#
#   This is the functions page which stores reusable functions for the login process.
#

class functions(unittest.TestCase):

    # Function to log screenshot and save to screenshots folder
    def logScreenshot(self, title):
        screenshot = str(time.localtime().tm_mon) + '_' + str(time.localtime().tm_mday) + "_" + str(time.localtime().tm_hour) + "_" + str(time.localtime().tm_min)+ "_" + str(time.localtime().tm_sec) + str(title)
        filepath = '..\Screenshots\\' + screenshot + '.png'
        self.driver.save_screenshot(filepath)
        print('Screenshot ' + screenshot + ' saved in folder!')

    # Function to verify web page appears on screen and go to login screen
    def navigate_to_login_page(self):

        # Get the log in button textbox and take screenshot
        self.loginButton = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/header/div/a[2]")
        functions.logScreenshot(self, 'findLoginBtn')
        print("Login Button has been found on Hudl homepage!")


        # Assert that the navigate to login button is able to be clicked and click the button
        self.loginButton
        self.assertTrue(self.loginButton.is_enabled())
        self.loginButton.click()
        print("Login Button has been clicked successfully")

        # Assert that the webpage is on the login screen and take screenshot
        self.assertTrue(self.driver.current_url == "https://www.hudl.com/login")
        print("Successfully navigated to Login page!")
        functions.logScreenshot(self, 'loginScreen')


    # Function to get email input box and input username
    def enter_in_email(self,user):
        time.sleep(1.5)
        # Verify that the email text box is on screen and retrieve it
        self.assertTrue(self.driver.find_element(by=By.ID, value="email").is_displayed())
        self.emailTextbox = self.driver.find_element(by=By.ID, value="email")
        print("Found the email input text box!")

        # Enter in email to email text box
        self.emailTextbox.send_keys(user)
        functions.logScreenshot(self, 'enteredInEmailForLogin')
        print("Successfully entered in email address!")

    # Function to get password input box and input password
    def enter_in_password(self, password):
        time.sleep(1.5)
        # Verify that the password text box is on screen and retrieve it
        self.assertTrue(self.driver.find_element(by=By.ID, value="password").is_displayed())
        self.passwordTextbox = self.driver.find_element(by=By.ID, value="password")
        print("Found the password input text box!")

        # Enter in password to password text box
        self.passwordTextbox.send_keys(password)
        functions.logScreenshot(self, 'enteredInPasswordForLogin')
        print("Successfully entered in password!")

        # Function to get password input box and input password

    def click_login_button(self):
        time.sleep(1.5)
        # Verify that the login button is on screen and retrieve it
        self.assertTrue(self.driver.find_element(by=By.ID, value="logIn").is_displayed())
        self.loginPageLoginButton = self.driver.find_element(by=By.ID, value="logIn")
        print("Found the log in button!")

        # Click Log In Button
        self.loginPageLoginButton.click()
        time.sleep(2.0)
        self.assertTrue(self.driver.current_url == "https://www.hudl.com/home")
        functions.logScreenshot(self, "loggedIn")
        print("Successfully logged in!")


    def click_login_expecting_failure(self):
        # Verify that the login button is on screen and click
        self.assertTrue(self.driver.find_element(by=By.ID, value="logIn").is_displayed())
        print("Log in button found!")
        self.loginPageLoginButton = self.driver.find_element(by=By.ID, value="logIn")
        self.loginPageLoginButton.click()
        print("Clicked log in button!")

        # Verify expected error appears
        time.sleep(2.0)
        self.assertTrue(self.driver.find_element(by=By.CLASS_NAME, value="login-error-container").is_displayed())
        functions.logScreenshot(self, "unableToLogin_Expected")

    #hui-globaluseritem
    def logout_of_account(self):
        # Assert logout button is available
        self.assertTrue(self.driver.find_element(by=By.XPATH, value="//*[@id='ssr-webnav']/div/div[1]/nav[1]/div[4]/div[2]/div[2]/div[3]/a").is_enabled())
        print("Log out button found!")
        self.logOutBtn = self.driver.find_element(by=By.XPATH, value="//*[@id='ssr-webnav']/div/div[1]/nav[1]/div[4]/div[2]/div[2]/div[3]/a")

        # get dropdown menu where log out button is located and hover over
        ActionChains(self.driver).move_to_element(self.driver.find_element(by=By.CLASS_NAME, value="hui-globalusermenu")).perform()

        # select log out button from dropdown
        self.logOutBtn.click()
        functions.logScreenshot(self, "loggedOut")

        #verify that user is logged out
        self.assertTrue(self.driver.current_url == "https://www.hudl.com/")