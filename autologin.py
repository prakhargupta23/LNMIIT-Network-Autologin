import threading
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time


def autologin():
    token_path = "C:\\Users\\Prakhar\\OneDrive\\Desktop\\cred.txt"
    key_secret = open(token_path, 'r').read().split()

    # Set the path to the ChromeDriver executable
    chromedriver_path = "C:\\Users\\Prakhar\\Downloads\\chromedriver_win32\\chromedriver.exe"

    service = webdriver.chrome.service.Service(chromedriver_path)
    service.start()

    options = webdriver.ChromeOptions()
    #     options.add_argument("headless")
    options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
    # Pass the options and service to create the WebDriver
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(key_secret[0])
    time.sleep(2)
    connect_element = driver.find_elements(by=By.XPATH, value='//*[@id="primary-button"]')
    # Check if the element is present
    if len(connect_element) > 0:
        print(connect_element)
        driver.find_element(by=By.XPATH, value='//*[@id="primary-button"]').click()
        original_window = driver.current_window_handle
        for window_handle in driver.window_handles:
            if original_window != window_handle:
                driver.switch_to.window(window_handle)
                break
    else:
        print("Element is not present on the page")

    print("bcwn")
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="details-button"]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="proceed-link"]').click()
    time.sleep(2)
    username = driver.find_element(by=By.XPATH, value='//*[@id="LoginUserPassword_auth_username"]')
    username.send_keys(key_secret[1])
    print(type(key_secret[1]))
    password = driver.find_element(by=By.XPATH, value='//*[@id="LoginUserPassword_auth_password"]')
    password.send_keys(key_secret[2])
    time.sleep(0.5)
    driver.find_element(by=By.XPATH, value='//*[@id="UserCheck_Login_Button_span"]').click()
    time.sleep(2)
    time.sleep(50)


autologin()
