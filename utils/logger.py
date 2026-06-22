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
