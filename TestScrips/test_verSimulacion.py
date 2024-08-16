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
import LoginOCA

# nombre del test
test = "Ver Simulacion"

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

# Elementos

# Variables
url = "https://vs-as-oca-front-qa-core.azurewebsites.net/"
usuario = "162690167"
password = "vida2023"

def test_verSimulacion():
    sim = 263
    element = f"ext-element-{sim}"
    driver.find_element(By.ID, element).click()
    # driver wait
    driver.implicitly_wait(5)

    # Pantalla de Simulación
    try: 
      # Seleccionar la simulación
      driver.find_element(By.ID, "ext-element-335").click()
      # driver wait
      driver.implicitly_wait(5)
    except:
      driver.find_element(By.ID, "ext-element-1202").click()
      # driver wait
      driver.implicitly_wait(5)
      pass  

    # Cerrar Mensaje si aparece
    try:
      try:
          mensaje = driver.find_element(By.ID, "ext-button-35")
          mensaje.click()
      except:
          mensaje = driver.find_element(By.ID, "ext-button-76")
          mensaje.click()
    except:
      pass

    # Pantalla de Coberturas
    try:
      driver.find_element(By.ID, "ext-element-401").click()
      # driver wait
      driver.implicitly_wait(5)
    except:
      pass

    # Pantalla de Aportes
    try:
      driver.find_element(By.ID, "ext-element-623").click()
      driver.find_element(By.ID, "ext-button-40").click()
      # driver wait
      driver.implicitly_wait(5)
    except:
      pass

    # Pantalla de Rentabilidad
    try:
      driver.find_element(By.ID, "ext-element-753").click()
      driver.find_element(By.ID, "ext-button-48").click()
      # driver wait
      driver.implicitly_wait(5)
    except:
      pass
       
    # Pantalla de Resultado
    try:
      driver.find_element(By.ID, "ext-element-1000").click()
      #driver.switch_to.window( vars["win6081"])
      # driver wait
      driver.implicitly_wait(5)
    except:
      driver.find_element(By.ID, "ext-element-1003").click()
      # driver wait
      driver.implicitly_wait(5)
      pass
    
    # Vizualizar Reporte de Cotizacion en PDF
    time.sleep(5)

    # Seleccionar la primera pestaña del navegador
    handles = driver.window_handles
    # Contar el número de pestañas abiertas
    num_pestañas = len(handles)-len(handles)
    # Cambiar a la primera pestaña
    driver.switch_to.window(driver.window_handles[num_pestañas])

    # Volver a la pantalla de Simulación:
    try:
      driver.find_element(By.ID, "ext-element-879").click() # Boton Home
      # driver wait
      driver.implicitly_wait(5)
    except:
      driver.find_element(By.ID, "ext-element-882").click() # Boton Home
      # driver wait
      driver.implicitly_wait(5)   
    
    time.sleep(3)  

# Main
if __name__ == "__main__":
    # llama a la funcion login de LoginOCA
    LoginOCA.login(driver, url, usuario, password)
    # llama a la funcion test_verSimulacion 
    for sim in range(0, 1):
      test_verSimulacion()

    # cierra el navegador
    driver.quit()
    print(f"Test: {test} finalizado!")


