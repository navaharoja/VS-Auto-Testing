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

import listarElementos

# Script directory
script_dir = os.path.dirname(__file__)
# Chrome driver path
chrome_driver_path = "C:/Users/001089655/Desktop/VidaSecurity/VSProyect/ChromeDriver/chromedriver.exe"
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

# Go to OCA
driver.get("https://vs-as-oca-front-qa-core.azurewebsites.net/")

# Extraer todo el HTML de la pagina
html = driver.page_source

# Guardar el HTML en un archivo en la ruta del script
with open(script_dir + '/LoginOCA.html', 'w', encoding='utf-8') as f:
    f.write(html)

# listar elementos
elements = listarElementos.parse_html_file(script_dir + '/LoginOCA.html')

# Guardar los elementos en un archivo en la ruta del script
listarElementos.write_to_file(elements, script_dir + '/elementosLoginOCA.txt')


# Ingresar usuario
#driver.find_element(By.ID, "userName").send_keys("userName")

# Ingresar contraseña
#driver.find_element(By.ID, "password").send_keys("password")

# Click en el botón de Iniciar Sesión
#driver.find_element(By.CSS_SELECTOR, ".btn").click()



