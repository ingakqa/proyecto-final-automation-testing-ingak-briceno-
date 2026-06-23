🧪 Pruebas de Automatización Pre-Entrega - Ingak Briceño
📌 Propósito del proyecto

Framework de automatización de pruebas funcionales desarrollado para validar los principales flujos de usuario de SauceDemo, utilizando Selenium WebDriver y Python.

El proyecto implementa pruebas de interfaz de usuario (UI) y pruebas de servicios API, aplicando buenas prácticas como el patrón Page Object Model (POM), parametrización de datos, generación de reportes y registro de evidencias.

🚀 Tecnologías utilizadas
Lenguaje: Python 3.11+
Framework de pruebas: Pytest
Automatización UI: Selenium WebDriver
Pruebas API: Requests
Reportes: Pytest-HTML
Gestión de datos: Archivos JSON parametrizados
Control de versiones: Git / GitHub
📁 Estructura del proyecto
proyecto-final-automation-testing/

├── pages/                  # Page Object Model (POM)
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py

├── tests/                  # Casos de prueba automatizados
│   ├── ui/                 # Pruebas funcionales de interfaz (SauceDemo)
│   └── api/                # Pruebas de servicios REST (ReqRes)

├── utils/                  # Módulos auxiliares
│   ├── data_reader.py      # Lectura de datos JSON
│   ├── helpers.py          # Funciones reutilizables
│   └── logger.py           # Gestión de logs

├── test_data/              # Datos externos de prueba
│   └── users.json

├── screenshots/            # Evidencias automáticas de fallos

├── reports/                # Reportes HTML generados

├── logs/                   # Registro de ejecución

├── pytest.ini              # Configuración principal de Pytest

├── conftest.py             # Fixtures, WebDriver y hooks

└── README.md
🛠️ Instalación de dependencias

Instalar las librerías necesarias ejecutando:

pip install selenium pytest pytest-html webdriver-manager requests
🚦 Ejecución de pruebas

Para ejecutar la suite completa de pruebas UI y API:

python -m pytest

El framework ejecutará los escenarios automatizados configurados mediante Pytest.

📊 Resultados y evidencias
Reportes HTML

Luego de la ejecución se genera un reporte visual:

reports/reporte_final.html

El reporte permite analizar:

Estado de cada prueba.
Tiempo de ejecución.
Resultados obtenidos.
Información del entorno.
Capturas de pantalla

En caso de fallo durante una prueba UI, el framework captura automáticamente evidencia visual y la almacena en:

screenshots/

Estas evidencias permiten facilitar el análisis y seguimiento de errores.

Logs de ejecución

Los eventos relevantes quedan registrados en:

logs/automatizacion.log

permitiendo mantener trazabilidad sobre la ejecución del framework.

