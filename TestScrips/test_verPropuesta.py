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
test = "Ver Propuesta"

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
    sim = 131
    element = f"ext-element-{sim}"
    driver.find_element(By.ID, element).click()
    # driver wait
    driver.implicitly_wait(5)

    # Menu Izquierdo: Opciones
    try: 
      # Seleccionar opcion "Propuesta"
      driver.find_element(By.ID, "ext-element-49").click()
      # driver wait
      driver.implicitly_wait(5)
    except:
      driver.find_element(By.ID, "ext-element-1202").click()
      # driver wait
      driver.implicitly_wait(5)
      pass  

    try:
      # Seleccionar la Propuesta
      driver.find_element(By.ID, "ext-element-400").click()
      # driver wait
      driver.implicitly_wait(5)
    except:
      driver.find_element(By.ID, "ext-element-1202").click()
      # driver wait
      driver.implicitly_wait(5)
      pass  

    # Pantalla de Propuesta
    try:
      # Seleccionar la cotización
      driver.find_element(By.ID, "ext-element-515").click()
      # driver wait
      driver.implicitly_wait(5)
    except:
      driver.find_element(By.ID, "ext-element-468").click() 
      # driver wait
      driver.implicitly_wait(5)
      pass
    
    # Pantalla Informacion 1 Asegurado
    try:
      # Boton Siguiente:
      driver.find_element(By.ID, "ext-element-782").click()
      # driver wait
      driver.implicitly_wait(5)
    except:
      driver.find_element(By.ID, "ext-element-1202").click()
      # driver wait
      driver.implicitly_wait(5)
      pass

    # Pantalla Informacion 2 Otros Roles
    try:
      # Boton Siguiente:
      driver.find_element(By.ID, "ext-element-958").click()
      # driver wait
      driver.implicitly_wait(5)
    except:
      driver.find_element(By.ID, "ext-element-1202").click()
      # driver wait
      driver.implicitly_wait(5)
      pass  
    
    # Pantalla Informacion 3 Pago
    try:
      # Boton Siguiente:
      driver.find_element(By.ID, "ext-element-2030").click()
      # driver wait
      driver.implicitly_wait(5)
    except:
      driver.find_element(By.ID, "ext-element-2032").click()
      # driver wait
      driver.implicitly_wait(5)
      pass

    # Pantalla Informacion 4 FATCA
    try:
      # Boton Siguiente:
      driver.find_element(By.ID, "ext-element-2203").click()
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
          mensaje = driver.find_element(By.ID, "ext-button-111")
          mensaje.click()
      except:
          mensaje = driver.find_element(By.ID, "ext-button-76")
          mensaje.click()
    except:
      pass

    # Patalla DPS
    try:
      driver.find_element(By.ID, "ext-element-2249").click()
      # driver wait
      driver.implicitly_wait(5)
    except:
      pass

    # Frame emergente de Documentos
    try:
      # boton Propuesta
      time.sleep(3)
      driver.find_element(By.ID, "ext-element-2321").click()
      # driver wait
      driver.implicitly_wait(5)
    except:
      pass  

    # Vizualizar Reporte de Cotizacion en PDF
    time.sleep(5)

    # Seleccionar la primera pestaña del navegador
    handles = driver.window_handles
    # Contar el número de pestañas abiertas
    num_pestañas = len(handles)-len(handles)
    # Cambiar a la primera pestaña
    driver.switch_to.window(driver.window_handles[num_pestañas])

    # Cerrar frame emergente de Documentos
    try:
      driver.find_element(By.ID, "ext-element-2307").click()
      # driver wait
      driver.implicitly_wait(5)
    except:
      pass

    # Volver a la pantalla de Propuestas:
    try:
      driver.find_element(By.ID, "ext-element-2224").click() # Boton Home
      # driver wait
      driver.implicitly_wait(5)
    except:
      driver.find_element(By.ID, "ext-element-2226").click() # Boton Home
      # driver wait
      driver.implicitly_wait(5)
      pass   

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


