import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_reader import cargar_datos_json
from utils.logger import configurar_logger

datos = cargar_datos_json("users.json")
log = configurar_logger("UI_Productos")

def test_verificacion_catalogo(driver, wait):
    log.info("Iniciando prueba: Validacion de catalogo")
    login_page = LoginPage(driver, wait)
    inventory_page = InventoryPage(driver, wait)
    
    login_page.login(datos["usuario_valido"]["user"], datos["usuario_valido"]["pass"])
    assert inventory_page.obtener_titulo() == "Products"
    assert inventory_page.contar_productos() > 0
    log.info("✅ Catalogo verificado con productos listados")

def test_agregar_producto_al_carrito(driver, wait):
    log.info("Iniciando prueba: Anadir producto al carrito")
    login_page = LoginPage(driver, wait)
    inventory_page = InventoryPage(driver, wait)
    
    login_page.login(datos["usuario_valido"]["user"], datos["usuario_valido"]["pass"])
    inventory_page.agregar_primer_producto()
    assert inventory_page.obtener_contador_carrito() == "1"
    log.info("✅ Producto anadido al carrito de compras exitosamente")


