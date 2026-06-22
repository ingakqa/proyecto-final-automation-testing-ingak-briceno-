from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    ITEMS_CARRITO = (By.CLASS_NAME, "cart_item")
    BOTON_CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def obtener_cantidad_items(self):
        self.wait.until(EC.presence_of_all_elements_located(self.ITEMS_CARRITO))
        return len(self.driver.find_elements(*self.ITEMS_CARRITO))

    def ir_a_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_CHECKOUT)).click()


