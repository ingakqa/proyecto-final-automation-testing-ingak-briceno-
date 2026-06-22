import pytest
from pages.login_page import LoginPage
from utils.data_reader import cargar_datos_json
from utils.logger import configurar_logger

datos = cargar_datos_json("users.json")
log = configurar_logger("UI_Login")

@pytest.mark.parametrize("caso", ["usuario_valido", "usuario_invalido"])
def test_login(driver, wait, caso):
    log.info(f"Iniciando prueba: Login con caso '{caso}'")
    login_page = LoginPage(driver, wait)
    credenciales = datos[caso]

    login_page.login(credenciales["user"], credenciales["pass"])

    if caso == "usuario_valido":
        assert "inventory.html" in driver.current_url
        log.info("✅ Login Exitoso verificado correctamente")
    else:
        assert credenciales["error"] in login_page.obtener_mensaje_error()
        log.info("✅ Escenario Negativo validado correctamente")
        
