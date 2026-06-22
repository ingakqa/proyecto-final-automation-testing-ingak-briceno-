# Framework de Automatización de Pruebas Profesional (UI & API)

Este proyecto consiste en un framework de pruebas automatizadas avanzado y mantenible desarrollado en **Python**, utilizando **Pytest** como motor de pruebas, **Selenium WebDriver** para la automatización de la interfaz gráfica (UI) y la biblioteca **Requests** para la validación de servicios de API REST.

Se aplican estándares de la industria como el patrón de diseño **Page Object Model (POM)**, inyección de datos parametrizados desde archivos externos, reportes visuales dinámicos en HTML y registros de trazabilidad mediante logging corporativo.

## 🚀 Tecnologías Utilizadas
* **Lenguaje:** Python 3.11+
* **Test Runner:** Pytest
* **UI Automation:** Selenium WebDriver
* **API Testing:** Requests Library
* **Reportes:** Pytest-HTML
* **Control de Versiones:** Git / GitHub

## 📁 Estructura del Proyecto
```text
proyecto-final-automation-testing/
├── pages/                # Clases bajo el patrón Page Object Model (POM)
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/                # Casos de prueba modulares y ordenados
│   ├── ui/               # Escenarios funcionales de la plataforma web (SauceDemo)
│   └── api/              # Escenarios de integración de servicios REST (ReqRes)
├── utils/                # Utilidades de soporte del framework
│   ├── data_reader.py    # Lector centralizado de archivos de datos JSON
│   └── logger.py         # Registrador log de eventos en tiempo real
├── test_data/            # Archivos JSON externos de parametrización
│   └── users.json
├── screenshots/          # Almacenamiento automático de capturas en fallos
├── reports/              # Almacenamiento de Reportes HTML autogenerados
├── logs/                 # Archivos físicos persistentes de trazabilidad .log
├── pytest.ini            # Archivo central de configuración de Pytest
├── conftest.py           # Inicialización distribuidas de WebDriver y Hooks
└── README.md             # Documentación técnica del proyecto
```

## 🛠️ Instalación de Dependencias
Para desplegar el entorno local de ejecución, instale las librerías requeridas ejecutando:
```bash
pip install selenium pytest pytest-html webdriver-manager requests
```

## 🚦 Ejecución de las Pruebas
Gracias a la centralización lógica en el archivo `pytest.ini`, puede lanzar el framework completo (las 8 pruebas de UI y API coordinadas de forma nativa) ejecutando simplemente:
```bash
python -m pytest
```

## 📊 Interpretación de Resultados y Evidencia
* **Reportes Visuales:** Al finalizar la ejecución, se autogenera un reporte interactivo detallado en `reports/reporte_final.html`. Puede abrirlo en cualquier navegador web para analizar duraciones, estados y metadatos.
* **Captura de Evidencia (Screenshots):** Si una prueba de UI falla, el hook embebido en `conftest.py` tomará un screenshot de la pantalla de forma automática, guardándolo en la carpeta `screenshots/` e incrustándolo directamente dentro del Reporte HTML.
* **Trazabilidad (Logs):** Cada paso relevante queda registrado cronológicamente en la consola y de forma persistente dentro del archivo log en `logs/automatizacion.log`.
