# 🧪 Pre-Entrega Automation Testing - Ingak Briceño

## Propósito del proyecto
Automatización de pruebas funcionales sobre saucedemo.com
utilizando Selenium WebDriver y Python.

## Tecnologías utilizadas
- Python 3.11
- Selenium WebDriver
- Pytest
- pytest-html
- webdriver-manager
- Git y GitHub

## Instalación de dependencias
pip install selenium pytest pytest-html webdriver-manager

## Cómo ejecutar las pruebas
py -3.11 -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html

## Estructura del proyecto
├── tests/
│   └── test_saucedemo.py
├── utils/
│   └── helpers.py
├── reports/
│   └── reporte.html
└── README.md

## Casos de prueba
1. test_login_exitoso
2. test_catalogo_productos
3. test_agregar_al_carrito

## Autor
Ingak Briceño
