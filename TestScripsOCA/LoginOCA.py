import pytest
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
import os 
import takeCapture
"""
# Script directory
script_dir = os.path.dirname(__file__)
# Chrome driver path
chrome_driver_path = f"{script_dir}/../ChromeDriver/chromedriver.exe" 
print(chrome_driver_path)


def chrome_options_selected():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    #chrome_options.add_argument("headless")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("window-size=1920x1080")
    chrome_options.add_argument("--disable-popup-blocking")
    return chrome_options

#Chrome
service_obj = Service(chrome_driver_path)
options = chrome_options_selected()
driver = webdriver.Chrome(service=service_obj, options=options)

# Variables
url = "https://vs-as-oca-front-qa-core.azurewebsites.net/"
usuario = "162690167"
password = "vida2023"
"""
# Elementos
txtUsuario = '//*[@id="ext-element-79"]'
txtPassword = '//*[@id="ext-element-86"]'
btnIngresar = '//*[@id="ext-element-100"]'

# Hacer login
def login(driver, url, usuario, password, test, capt):
    # Go to OCA
    driver.get(url)
    # Ingresar usuario
    driver.find_element(By.XPATH, txtUsuario).send_keys(usuario)
    # Ingresar contraseña
    driver.find_element(By.XPATH, txtPassword).send_keys(password)
    # Take capture
    sst = "Login_" + test
    takeCapture.takeCapture(sst, capt)
    # Click en el botón de Iniciar Sesión
    driver.find_element(By.XPATH, btnIngresar).click()
    # Esperar 5 segundos
    time.sleep(5)








