import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="function")
def driver(request):
    """Inicializa el WebDriver de Chrome con configuraciones robustas."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # Compartimos el driver con el sistema de reportes para las capturas en fallas
    if request.node:
        request.node.funcargs['selenium_driver'] = driver
        
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def wait(driver):
    """Provee un objeto WebDriverWait de 10 segundos por defecto."""
    return WebDriverWait(driver, 10)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Captura screenshots automáticamente si un test de UI falla."""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("selenium_driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name
            screenshot_path = f"screenshots/FALLO_{test_name}_{timestamp}.png"
            
            driver.save_screenshot(screenshot_path)
            
            html = item.config.pluginmanager.get_plugin("html")
            if html:
                extra = getattr(rep, "extra", [])
                extra.append(html.extras.image(screenshot_path))
                rep.extra = extra

