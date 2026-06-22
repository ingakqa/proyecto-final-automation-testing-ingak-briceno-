import logging
import os


def configurar_logger(nombre_test):
    """Crea un registro detallado para depuración en la carpeta logs."""
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger(nombre_test)
    
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        # Formato profesional de logs con estampa de tiempo
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        # Log a archivo físico
        file_handler = logging.FileHandler("logs/automatizacion.log", encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        # Log a consola de VS Code
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        
    return logger
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.data_reader import cargar_datos_json
from utils.logger import configurar_logger

datos = cargar_datos_json("users.json")
log = configurar_logger("UI_Checkout")

def test_flujo_checkout_completo(driver, wait):
    log.info("Iniciando prueba: End-to-End Checkout completo")
    login_page = LoginPage(driver, wait)
    inventory_page = InventoryPage(driver, wait)
    cart_page = CartPage(driver, wait)
    checkout_page = CheckoutPage(driver, wait)
    
    login_page.login(datos["usuario_valido"]["user"], datos["usuario_valido"]["pass"])
    inventory_page.agregar_primer_producto()
    inventory_page.ir_al_carrito()
    
    assert cart_page.obtener_cantidad_items() == 1
    cart_page.ir_a_checkout()
    
    checkout_page.completar_formulario("Ingak", "Briceno", "1000")
    checkout_page.finalizar_compra()
    assert checkout_page.obtener_confirmacion() == "Thank you for your order!"
    log.info("✅ Flujo integral de checkout finalizado en verde")
