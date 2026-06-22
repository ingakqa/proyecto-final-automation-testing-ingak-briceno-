from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # 📌 Selectores Centralizados
    USER_INPUT = (By.ID, "user-name")
    PASS_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.url = "https://saucedemo.com"

    def abrir(self):
        self.driver.get(self.url)

    def login(self, usuario, password):
        self.abrir()
        u_campo = self.wait.until(EC.visibility_of_element_located(self.USER_INPUT))
        u_campo.clear()
        u_campo.send_keys(usuario)
        
        p_campo = self.wait.until(EC.visibility_of_element_located(self.PASS_INPUT))
        p_campo.clear()
        p_campo.send_keys(password)
        
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def obtener_mensaje_error(self):
        elemento = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return elemento.text

