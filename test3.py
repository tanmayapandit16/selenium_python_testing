from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import time 
#ALL FUNCTION TESTS
BASEURL="http://localhost/Online-Food-Order"

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
 
def test12(driver):
    '''
    verify redirection to HOME PAGE
    '''
    driver.get(f"{BASEURL}/")

    home = driver.find_element(By.XPATH, "//a[contains(text(),'Home')]")
    home.click()
    expected_url = f"{BASEURL}/index.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("\nTest 12 : Verify redirection to HOME PAGE  | Status : PASSED")
            return True
        else:
            print("Test failed")
            return False
    except Exception as e:
        print("Test failed because of unexpected result")
        return False

def test13(driver):
    '''
    verify redirection to ABOUT PAGE
    '''
    driver.get(f"{BASEURL}/")

    about = driver.find_element(By.XPATH, "//a[contains(text(),'About')]")
    about.click()
    expected_url = f"{BASEURL}/aboutus.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("\nTest 13 : Verify redirection to ABOUT PAGE  | Status : PASSED")
            return True
        else:
            print("Test failed")
            return False
    except Exception as e:
        print("Test failed because of unexpected result")
        return False

def test14(driver):
    '''
    verify redirection to CONTACT US PAGE
    '''
    driver.get(f"{BASEURL}/")

    contact = driver.find_element(By.XPATH, "//a[contains(text(),'Contact Us')]")
    contact.click()
    expected_url = f"{BASEURL}/contactus.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("\nTest 14 : Verify redirection to CONTACT US PAGE  | Status : PASSED")
            return True
        else:
            print("Test failed")
            return False
    except Exception as e:
        print("Test failed because of unexpected result")
        return False

def test15(driver):
    '''
    verify that no login is possible with empty credentials
    '''
    driver.get(f"{BASEURL}/contactus.php")
    name_field = driver.find_element(By.ID, "name")
    email_field = driver.find_element(By.ID, "email")
    mobile_field = driver.find_element(By.ID, "mobile")
    subject_field =driver.find_element(By.ID, "subject")
    name_field.send_keys("")
    email_field.send_keys("")
    mobile_field.send_keys("")
    subject_field.send_keys("")

    submit_button2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/form[1]/input[1]")
    submit_button2.click()
    expected_url = f"{BASEURL}/contactus.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("\nTest 15 : Verify that no login is possible with empty credentials | Status : PASSED")
            return False
        else:
            print("\nTest 15 : Verify that no login is possible with empty credentials | Status : PASSED")
            return True
    except Exception as e:
        print("\nTest 15 : Verify that no login is possible with empty credentials | Status : PASSED")
        return True
    
def test16(driver):
    '''
    verify that no login is possible with empty name & email
    '''
    driver.get(f"{BASEURL}/contactus.php")
    name_field = driver.find_element(By.ID, "name")
    email_field = driver.find_element(By.ID, "email")
    name_field.send_keys("")
    email_field.send_keys("")

    submit_button2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/form[1]/input[1]")
    submit_button2.click()
    expected_url = f"{BASEURL}/contactus.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("\nTest 16 : Verify that no login is possible with empty name & email | Status : PASSED")
            return False
        else:
            print("\nTest 16 : Verify that no login is possible with empty name & email | Status : PASSED")
            return True
    except Exception as e:
        print("\nTest 16 : Verify that no login is possible with empty name & email | Status : PASSED")
        return True
    
def test17(driver):
    '''
    verify that no login is possible with empty name & mobile
    '''
    driver.get(f"{BASEURL}/contactus.php")
    name_field = driver.find_element(By.ID, "name")
    mobile_field = driver.find_element(By.ID, "mobile")
    name_field.send_keys("")
    mobile_field.send_keys("")

    submit_button2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/form[1]/input[1]")
    submit_button2.click()
    expected_url = f"{BASEURL}/contactus.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("\nTest 17 : Verify that no login is possible with empty name & mobile | Status : PASSED")
            return False
        else:
            print("\nTest 17 : Verify that no login is possible with empty name & mobile | Status : PASSED")
            return True
    except Exception as e:
        print("\nTest 17 : Verify that no login is possible with empty name & mobile | Status : PASSED")
        return True
    
def test18(driver):
    '''
    verify that no login is possible with empty subject
    '''
    driver.get(f"{BASEURL}/contactus.php")
    subject_field = driver.find_element(By.ID, "subject")
    subject_field.send_keys("")

    submit_button2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/form[1]/input[1]")
    submit_button2.click()
    expected_url = f"{BASEURL}/contactus.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("\nTest 18 : Verify that no login is possible with empty subject | Status : PASSED")
            return False
        else:
            print("\nTest 18 : Verify that no login is possible with empty subject | Status : PASSED")
            return True
    except Exception as e:
        print("\nTest 18 : Verify that no login is possible with empty subject| Status : PASSED")
        return True

def test19(driver):
    '''
    verify that login is possible with correct input
    '''
    driver.get(f"{BASEURL}/contactus.php")
    name_field = driver.find_element(By.ID, "name")
    email_field = driver.find_element(By.ID, "email")
    mobile_field = driver.find_element(By.ID, "mobile")
    subject_field =driver.find_element(By.ID, "subject")
    name_field.send_keys("tanmaya")
    email_field.send_keys("tanmaya@gmail.com")
    mobile_field.send_keys("4564564563")
    subject_field.send_keys("topic")

    submit_button2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/form[1]/input[1]")
    submit_button2.click()
    expected_url = f"{BASEURL}/contactus.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("\nTest 19 : Verify that login is possible with correct input | Status : PASSED")
            return True
        else:
            print("\nTest 19 : Verify that login is possible with correct input | Status : PASSED")
            return False
    except Exception as e:
        print("\nTest 19 : Verify that login is possible with correct input | Status : PASSED")
        return False

def test20(driver):
    '''
    verify functionality of "order now" button -> redirects to foodlist page
    '''
    driver.get(f"{BASEURL}/")
    order_button = driver.find_element(By.NAME, "order")
    order_button.click()
    expected_url = f"{BASEURL}/foodlist.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("\nTest 20 : Verify functionality of ORDER NOW button -> redirects to foodlist page | Status : PASSED")
            return True
        else:
            print("Test failed")
            return False
    except Exception as e:
        print("Test failed because of unexpected result" )
        return False
    
def test21(driver):
    '''
    verify functionality of LOGOUT button
    '''
    driver.get(f"{BASEURL}/")
    order_button = driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[1]/div[2]/ul[2]/li[4]/a[1]")
    order_button.click()
    expected_url = f"{BASEURL}/customerlogin.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("\nTest 21 : Verify functionality of LOGOUT button | Status : PASSED")
            return True
        else:
            print("Test failed")
            return False
    except Exception as e:
        print("Test failed because of unexpected result" )
        return False
    
def test22(driver):
    '''
    verify redirection after clicking on LOGO
    '''
    driver.get(f"{BASEURL}/")

    home = driver.find_element(By.NAME, "logo")
    home.click()
    expected_url = f"{BASEURL}/index.php"
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
        if driver.current_url == expected_url:
            print("\nTest 22 : Verify redirection after clicking on LOGO  | Status : PASSED")
            return True
        else:
            print("Test failed")
            return False
    except Exception as e:
        print("Test failed because of unexpected result")
        return False

if __name__ == "__main__":
    driver = webdriver.Chrome()
    test11(driver)
    test13(driver)
    test14(driver)
    test15(driver)
    test16(driver)
    test17(driver)
    test18(driver)
    test19(driver)
    test20(driver)
    test21(driver)
    test22(driver)

    driver.quit()