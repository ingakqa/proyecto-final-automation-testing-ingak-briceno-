from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    BOTON_CONTINUE = (By.ID, "continue")
    BOTON_FINISH = (By.ID, "finish")
    MENSAJE_EXITO = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def completar_formulario(self, nombre, apellido, cp):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(nombre)
        self.driver.find_element(*self.LAST_NAME).send_keys(apellido)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(cp)
        self.driver.find_element(*self.BOTON_CONTINUE).click()

    def finalizar_compra(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_FINISH)).click()

    def obtener_confirmacion(self):
        return self.wait.until(EC.visibility_of_element_located(self.MENSAJE_EXITO)).text
