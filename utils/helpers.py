# utils/helpers.py
# Descripción: Funciones auxiliares para los tests de SauceDemo

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.saucedemo.com"
USUARIO = "standard_user"
CONTRASENA = "secret_sauce"
TIEMPO_ESPERA = 10

def iniciar_navegador():
    """Inicia y retorna una instancia de Chrome"""
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.maximize_window()
    return driver

def hacer_login(driver):
    """Realiza el login en saucedemo con credenciales válidas"""
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, TIEMPO_ESPERA)
    campo_usuario = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    campo_usuario.send_keys(USUARIO)
    driver.find_element(By.ID, "password").send_keys(CONTRASENA)
    driver.find_element(By.ID, "login-button").click()

def obtener_wait(driver):
    """Retorna una instancia de WebDriverWait"""
    return WebDriverWait(driver, TIEMPO_ESPERA)