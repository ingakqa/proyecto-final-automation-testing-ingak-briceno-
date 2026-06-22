from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    TITULO_PAGINA = (By.CLASS_NAME, "title")
    ITEMS = (By.CLASS_NAME, "inventory_item")
    BOTON_AGREGAR = (By.CSS_SELECTOR, ".inventory_item button")
    CONTADOR_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")
    LINK_CARRITO = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def obtener_titulo(self):
        return self.wait.until(EC.visibility_of_element_located(self.TITULO_PAGINA)).text

    def contar_productos(self):
        self.wait.until(EC.presence_of_all_elements_located(self.ITEMS))
        return len(self.driver.find_elements(*self.ITEMS))

    def agregar_primer_producto(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_AGREGAR)).click()

    def obtener_contador_carrito(self):
        return self.wait.until(EC.visibility_of_element_located(self.CONTADOR_CARRITO)).text

    def ir_al_carrito(self):
        self.wait.until(EC.element_to_be_clickable(self.LINK_CARRITO)).click()

