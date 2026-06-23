import pytest
import pytest_check as check
import requests
from utils.logger import configurar_logger

log = configurar_logger("API_Requests")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Content-Type": "application/json"
}

def test_api_get_users():
    log.info("Ejecutando API: GET usuarios")
    respuesta = requests.get("https://jsonplaceholder.typicode.com/users/1", headers=HEADERS)
    check.equal(respuesta.status_code, 200)
    datos = respuesta.json()
    check.is_in("id", datos)
    check.equal(datos["id"], 1)
    log.info("✅ API GET verificado con exito")

def test_api_post_user():
    log.info("Ejecutando API: POST crear usuario")
    payload = {
        "name": "Ingak",
        "username": "ingak_qa"
    }
    respuesta = requests.post("https://jsonplaceholder.typicode.com/users", json=payload, headers=HEADERS)
    check.equal(respuesta.status_code, 201)
    datos = respuesta.json()
    check.equal(datos["name"], "Ingak")
    log.info("✅ API POST verificado con exito")

def test_api_delete_user():
    log.info("Ejecutando API: DELETE eliminar usuario")
    respuesta = requests.delete("https://jsonplaceholder.typicode.com/users/1", headers=HEADERS)
    assert respuesta.status_code == 200
    log.info("✅ API DELETE verificado con exito")
    
    
    
