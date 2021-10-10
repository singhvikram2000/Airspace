########################################################
############# Test Cases to perform regression test suite on Login page ######
### Author : Vikram Singh
### Test Case 1: This test case will validate webpage response while logging with correct credentials.
### Test Case 2: This test case will validate webpage response while logging with Incorrect credentials.
### Test Case 3: This test case will validate webpage response when logged out after successful login.
### Pre-requite to run regression test suite: Install python 3.10 package. Install selenium library.
### To run the test suite: Open command prompt from python folder, and run "python AppLoginTest.py"

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager


def login_test_with_valid_credentials():
    print("Starting login test case with valid credentials")
    welcome = "Welcome to the Secure Area"
    user = "tomsmith"
    pasw = "SuperSecretPassword!"

    driver = webdriver.Chrome(ChromeDriverManager().install())
    time.sleep(2)
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    username.send_keys(user)
    time.sleep(1)
    password.send_keys(pasw)
    time.sleep(1)
    driver.find_element_by_css_selector(".radius").click()
    time.sleep(5)
    WELCOME = driver.find_element_by_class_name("subheader").text

    if welcome in WELCOME:
        print("Login test case passed with valid credentials")
    else:
        print("Login test case Failed with valid credentials")
    driver.quit()
	
def login_test_with_Invalid_credentials():
    print("Starting login test case with Invalid credentials")
    unwelcome = "Your username is invalid"
    user = "tom"
    pasw = "SuperSecret"

    driver = webdriver.Chrome(ChromeDriverManager().install())
    time.sleep(2)
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    username.send_keys(user)
    time.sleep(1)
    password.send_keys(pasw)
    time.sleep(1)
    driver.find_element_by_css_selector(".radius").click()
    time.sleep(5)
    UNWELCOME = driver.find_element_by_xpath("//div[@class='flash error']").text

    if unwelcome in UNWELCOME:
        print("Login test case with invalid credentials passed")
    else:
        print("Login test case with invalid credentials Failed")
    driver.quit()
	
def logout_test():
    print("Starting logged out test case after successful login")
    logout = "You logged out of the secure area"
    user = "tomsmith"
    pasw = "SuperSecretPassword!"

    driver = webdriver.Chrome(ChromeDriverManager().install())
    time.sleep(2)
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    username.send_keys(user)
    time.sleep(1)
    password.send_keys(pasw)
    time.sleep(1)
    driver.find_element_by_css_selector(".radius").click()
    time.sleep(5)
#    driver.find_element_by_css_selector(".button secondary radius").click()
    driver.find_element_by_partial_link_text("Logout").click()
    time.sleep(5)
    LOGOUT = driver.find_element_by_xpath("//div[@class='flash success']").text    

    if logout in LOGOUT:
        print("Logout test case passed")
    else:
        print("Logout test case Failed")
    driver.quit()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    login_test_with_valid_credentials()
    login_test_with_Invalid_credentials()
    logout_test()
