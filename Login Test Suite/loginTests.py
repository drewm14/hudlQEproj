from selenium import webdriver
import unittest
import time
from Methods.functions import *
from settings import username, password

#
# The following loginTests class holds the definitions for the test cases highlighted in the Introduction.txt file
#

class loginTests(unittest.TestCase):

    def setUp(self):
        # Assume test will fail
        self.test_failed = True

        # Open Google Chrome using stored Web Driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # navigate to Hudl
        self.driver.get("https://hudl.com")

    def tearDown(self):
        if self.test_failed:
            functions.logScreenshot(self, 'testFailure')
            print("Test Failed, please run manually to verify bug")

    def test1_successful_login_with_valid_username_and_pass(self):

        # calling in methods from functions to run tests
        # going to login page
        functions.navigate_to_login_page(self)
        # entering in email
        functions.enter_in_email(self, username)
        # entering in password
        functions.enter_in_password(self,password)
        # clicking login button
        functions.click_login_button(self)
        # Upon successful test completion, set test_failed to False
        self.test_failed = False


    def test2_verify_cannot_login_with_blank_credentials(self):
        # calling in methods from functions to run tests
        # going to login page
        functions.navigate_to_login_page(self)
        # entering nothing for email
        functions.enter_in_email(self, "")
        # entering nothing for password
        functions.enter_in_password(self, "")
        # expecting failure when trying to login
        functions.click_login_expecting_failure(self)
        # Upon successful test completion, set test_failed to False
        self.test_failed = False

    def test3_verify_cannot_login_with_blank_password(self):
        # calling in methods from functions to run tests
        functions.navigate_to_login_page(self)
        # entering in email
        functions.enter_in_email(self, username)
        # entering nothing for password
        functions.enter_in_password(self, "")
        # expecting failure when trying to login
        functions.click_login_expecting_failure(self)
        # Upon successful test completion, set test_failed to False
        self.test_failed = False

    def test4_verify_cannot_login_with_blank_email(self):
        # calling in methods from functions to run tests
        functions.navigate_to_login_page(self)
        # entering nothing for email
        functions.enter_in_email(self, "")
        # entering in password
        functions.enter_in_password(self, password)
        # expecting failure when trying to login
        functions.click_login_expecting_failure(self)
        # Upon successful test completion, set test_failed to False
        self.test_failed = False

    def test5_verify_cannot_login_with_incorrect_password(self):
        # calling in methods from functions to run tests
        functions.navigate_to_login_page(self)
        # entering nothing for email
        functions.enter_in_email(self, username)
        # entering in password
        functions.enter_in_password(self, "fake123")
        # expecting failure when trying to login
        functions.click_login_expecting_failure(self)
        # Upon successful test completion, set test_failed to False
        self.test_failed = False

    def test6_verify_cannot_login_with_invalid_credentials(self):
        # calling in methods from functions to run tests
        functions.navigate_to_login_page(self)
        # invalid email
        functions.enter_in_email(self, "fake.email123@gmail.com")
        # invalid password
        functions.enter_in_password(self, "fake123")
        # expecting failure when trying to login
        functions.click_login_expecting_failure(self)
        # Upon successful test completion, set test_failed to False
        self.test_failed = False

    def test7_security_verify_logged_out_user_cannot_be_logged_in_with_return_to_last_page(self):
        # calling in methods from functions to run tests
        # going to login page
        functions.navigate_to_login_page(self)
        # entering in email
        functions.enter_in_email(self, username)
        # entering in password
        functions.enter_in_password(self, password)
        # clicking login button
        functions.click_login_button(self)
        # select dropdown and log out
        functions.logout_of_account(self)
        # hit return to last page on browser
        self.driver.back()
        # verify user is not logged in by searching for log in button
        self.assertTrue(self.driver.find_element(by=By.ID, value="logIn").is_displayed())
        # Upon successful test completion, set test_failed to False
        self.test_failed = False


