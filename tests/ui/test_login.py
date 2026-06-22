import pytest
from pages.login_page import LoginPage
from utils.data_reader import cargar_datos_json
from utils.logger import configurar_logger

datos = cargar_datos_json("users.json")
log = configurar_logger("UI_Login")

def test_login_exitoso(driver, wait):
    log.info("Iniciando prueba: Login Exitoso")
    login_page = LoginPage(driver, wait)
    credenciales = datos["usuario_valido"]
    
    login_page.login(credenciales["user"], credenciales["pass"])
    assert "inventory.html" in driver.current_url
    log.info("✅ Login Exitoso verificado correctamente")

def test_login_fallido_negativo(driver, wait):
    log.info("Iniciando prueba: Escenario Negativo de Login")
    login_page = LoginPage(driver, wait)
    credenciales = datos["usuario_invalido"]
    
    login_page.login(credenciales["user"], credenciales["pass"])
    assert credenciales["error"] in login_page.obtener_mensaje_error()
    log.info("✅ Escenario Negativo validado correctamente")


