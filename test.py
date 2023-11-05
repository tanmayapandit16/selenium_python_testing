from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import time 
#ALL LOGIN TESTS
BASEURL="http://localhost/Online-Food-Order"

def test1(driver):
    ''' 
    verify web page title
    '''
    driver.get(BASEURL)
    title=driver.title
    if title == "Home | Le Cafe'":
        print("\nTest 1 : Verify web page title | Status : PASSED")
        return True
    else:
        print("test failed")
        return False

def test2(driver):
    driver.get(BASEURL)
    '''
    verify that a web element (home) is present on a web page
    '''
    try:
        element = driver.find_element(By.XPATH, "//a[contains(text(),'Home')]")
        if element:
            print("\nTest 2 : Verify that a web element (home) is present on a web page | Status : PASSED")
            return True
        else:
            print("Test failed")
            return False
    except Exception as e:
        print(f"Test failed with exception: {e.msg}")
        return False

def test3(driver):
    driver.get(BASEURL)
    '''
    verify that a web element (order now) is present on a web page
    '''
    try:
        element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/center[1]/a[1]")
        if element:
            print("\nTest 3 : Verify that a web element (order now) is present on a web page | Status : PASSED")
            return True
        else:
            print("Test failed")
            return False
    except Exception as e:
        print(f"Test failed with exception: {e.msg}")
        return False


def test4(driver):
    '''
    verify functionality of "order now" button -> redirects to login page
    '''
    driver.get(f"{BASEURL}/")
    order_button = driver.find_element(By.NAME, "order")
    order_button.click()
    expected_url = f"{BASEURL}/customerlogin.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("\nTest 4 : Verify functionality of ORDER NOW button -> redirects to login page | Status : PASSED")
            return True
        else:
            print("Test failed")
            return False
    except Exception as e:
        print("Test failed because of unexpected result" )
        return False
    
def test5(driver):
    '''
    verify functionality of "create account" link
    '''
    driver.get(f"{BASEURL}/customerlogin.php")
    create_button = driver.find_element(By.NAME, "create")
    create_button.click()
    expected_url = f"{BASEURL}/customersignup.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("\nTest 5 : Verify functionality of CREATE ACCOUNT link | Status : PASSED")
            return True
        else:
            print("Test failed")
            return False
    except Exception as e:
        print("Test failed because of unexpected result" )
        return False

def test6(driver):
    '''
    verify that no login is possible with empty credentials
    '''
    driver.get(f"{BASEURL}/customersignup.php")
    fullname_field = driver.find_element(By.ID, "fullname")
    username_field = driver.find_element(By.ID, "username")
    email_field = driver.find_element(By.ID, "email")
    contact_field = driver.find_element(By.ID, "contact")
    address_field =driver.find_element(By.ID, "address")
    password = driver.find_element(By.ID, "password")
    fullname_field.send_keys("")
    username_field.send_keys("")
    email_field.send_keys("")
    contact_field.send_keys("")
    address_field.send_keys("")
    password.send_keys("")

    submit_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[7]/div[1]/button[1]")
    submit_button.click()
    expected_url = f"{BASEURL}/customer_registered_success.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("Test failed")
            return False
        else:
            print("\nTest 6 : Verify that no login is possible with empty credentials | Status : PASSED")
            return True
    except Exception as e:
        print("\nTest 6 : Verify that no login is possible with empty credentials | Status : PASSED")
        return True
    
def test7(driver):
    '''
    verify that no login is possible with empty username
    '''
    driver.get(f"{BASEURL}/customersignup.php")
 
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("")

    submit_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[7]/div[1]/button[1]")
    submit_button.click()
    expected_url = f"{BASEURL}/customer_registered_success.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("Test failed")
            return False
        else:
            print("\nTest 7 : Verify that no login is possible with empty username | Status : PASSED")
            return True
    except Exception as e:
        print("\nTest 7 : Verify that no login is possible with empty username | Status : PASSED")
        return True
    
def test8(driver):
    '''
    verify that no login is possible with empty email
    '''
    driver.get(f"{BASEURL}/customersignup.php")
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("")

    submit_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[7]/div[1]/button[1]")
    submit_button.click()
    expected_url = f"{BASEURL}/customer_registered_success.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("Test failed")
            return False
        else:
            print("\nTest 8 : Verify that no login is possible with empty email | Status : PASSED")
            return True
    except Exception as e:
        print("\nTest 8 : Verify that no login is possible with empty email | Status : PASSED")
        return True
    
def test9(driver):
    '''
    verify that no login is possible with empty password
    '''
    driver.get(f"{BASEURL}/customersignup.php")
    password = driver.find_element(By.ID, "password")
    password.send_keys("")

    submit_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[7]/div[1]/button[1]")
    submit_button.click()
    expected_url = f"{BASEURL}/customer_registered_success.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("Test failed")
            return False
        else:
            print("\nTest 9 : that no login is possible with empty password | Status : PASSED")
            return True
    except Exception as e:
        print("\nTest 9 : Verify that no login is possible with empty password | Status : PASSED")
        return True
    
def test10(driver):
    '''
    verify that registration is possible with correct inputs
    '''
    driver.get(f"{BASEURL}/customersignup.php")
    fullname_field = driver.find_element(By.ID, "fullname")
    username_field = driver.find_element(By.ID, "username")
    email_field = driver.find_element(By.ID, "email")
    contact_field = driver.find_element(By.ID, "contact")
    address_field =driver.find_element(By.ID, "address")
    password = driver.find_element(By.ID, "password")
    fullname_field.send_keys("abc4")
    username_field.send_keys("abc_4")
    email_field.send_keys("abc4@gmail.com")
    contact_field.send_keys("4567462345")
    address_field.send_keys("pune")
    password.send_keys("abc456")

    submit_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[7]/div[1]/button[1]")
    submit_button.click()
    expected_url = f"{BASEURL}/customer_registered_success.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("\nTest 10 : Verify that registrations is possible with correct inputs | Status : PASSED")
            return True
        else:
            print("Test failed")
            return False
    except Exception as e:
        print("Test failed because of unexpected result")
        return False


def test11(driver):
    '''
    verify functionality of login form and submit button
    '''
    driver.get(f"{BASEURL}/customerlogin.php")
    username_field = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    username_field.send_keys("abc_1")
    password.send_keys("abc123")

    submit_button1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/button[1]")
    submit_button1.click()
    expected_url = f"{BASEURL}/foodlist.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("\nTest 11 : Verify functionality of login form and Submit button | Status : PASSED")
            return True
        else:
            print("Test failed")
            return False
    except Exception as e:
        print("Test failed because of unexpected result")
        return False


if __name__ == "__main__":
    driver = webdriver.Chrome()
    test1(driver)
    test2(driver)
    test3(driver)
    test4(driver)
    test5(driver)
    test6(driver)
    test7(driver)
    test8(driver)
    test9(driver)
    test10(driver)
    test11(driver)
    driver.quit()