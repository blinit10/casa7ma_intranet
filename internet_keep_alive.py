import os
from pathlib import Path

import requests
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
import pandas as pd


def nauta_keep_alive_firefox():
    try:
        result = requests.get("http://127.0.0.1:8000/control/internet_nauta").json()
        connected = result['connected']
        username = result['username']
        password = result['password']
        my_url = f'https://secure.etecsa.net:8443/'
        option = Options()
        option.add_argument('-headless')
        if os.system("ping google.com") != 0 and connected == True:
            print("if os.system(\"ping google.com\") != 0 and connected == True")
            driver = webdriver.Firefox(options=option)
            try:
                print("Entro en el try")
                driver.get(my_url)
                driver.maximize_window()
                wait = WebDriverWait(driver, 15)
                wait.until(EC.element_to_be_clickable((By.ID, "username"))).click()
                sleep(1)
                wait.until(EC.element_to_be_clickable((By.ID, "username"))).send_keys(username)
                sleep(1)
                wait.until(EC.element_to_be_clickable((By.ID, "password"))).click()
                sleep(1)
                wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(password)
                sleep(1)
                element = driver.find_element(By.CLASS_NAME, "btn")
                driver.execute_script("arguments[0].click();", element)
                sleep(1)
            except:
                driver.quit()
                return nauta_keep_alive_firefox()
            while connected == True:
                print("while connected == True")
                result = requests.get("http://127.0.0.1:8000/control/internet_nauta").json()
                connected = result['connected']
                print("Connected = " + str(connected))
                hostname = "google.com"
                response = os.system("ping " + hostname)
                if response == 0:
                    print("if response == 0")
                    pass
                else:
                    print("if response !=0")
                    driver.quit()
                    return nauta_keep_alive_firefox()
            print("element = driver.find_element(By.NAME, \"logout\")")
            element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/input[2]")
            element.click()
            sleep(5)
            alert = Alert(driver)
            alert.accept()
            sleep(10)
            driver.quit()
    finally:
        try:
            driver.quit()
        except:
            pass
        return nauta_keep_alive_firefox()

nauta_keep_alive_firefox()