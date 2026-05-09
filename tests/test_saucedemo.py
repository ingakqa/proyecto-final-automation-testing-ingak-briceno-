# tests/test_saucedemo.py
# Autor: ingak briceno
# Descripción: Casos de prueba automatizados para saucedemo.com

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import iniciar_navegador, hacer_login, obtener_wait

@pytest.fixture
def driver():
    """Inicia el navegador antes del test y lo cierra después"""
    driver = iniciar_navegador()
    yield driver
    driver.quit()

def test_login_exitoso(driver):
    hacer_login(driver)
    wait = obtener_wait(driver)
    wait.until(EC.url_contains("inventory.html"))
    assert "inventory.html" in driver.current_url
    assert "Swag Labs" in driver.title
    print("✅ Login exitoso")

def test_catalogo_productos(driver):
    hacer_login(driver)
    wait = obtener_wait(driver)
    titulo = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert titulo.text == "Products"
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0
    nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"✅ Primer producto: {nombre} - {precio}")

def test_agregar_al_carrito(driver):
    hacer_login(driver)
    wait = obtener_wait(driver)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    nombre_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    driver.find_element(By.CSS_SELECTOR, ".inventory_item button").click()
    contador = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert contador.text == "1"
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    items = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
    )
    assert len(items) == 1
    print(f"✅ Producto en carrito: {nombre_producto}")