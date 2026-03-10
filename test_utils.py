import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import validar_producto, validar_lista

PRODUCTO_VALIDO = {
    "nombre": "Laptop Pro",
    "categoria": "Electrónica",
    "stock": 12,
    "precio": 1299.99,
}

# ── Tests: validar_producto ──────────────────────────────────

def test_validar_producto_valido():
    ok, msg = validar_producto(PRODUCTO_VALIDO)
    assert ok is True
    assert msg is None

def test_validar_nombre_vacio():
    prod = {**PRODUCTO_VALIDO, "nombre": ""}
    ok, msg = validar_producto(prod)
    assert ok is False

def test_validar_categoria_vacia():
    prod = {**PRODUCTO_VALIDO, "categoria": ""}
    ok, msg = validar_producto(prod)
    assert ok is False

def test_validar_stock_negativo():
    prod = {**PRODUCTO_VALIDO, "stock": -5}
    ok, msg = validar_producto(prod)
    assert ok is False

def test_validar_stock_cero_es_valido():
    # stock 0 es válido: producto agotado pero existente
    prod = {**PRODUCTO_VALIDO, "stock": 0}
    ok, msg = validar_producto(prod)
    assert ok is True

def test_validar_precio_negativo():
    prod = {**PRODUCTO_VALIDO, "precio": -10.0}
    ok, msg = validar_producto(prod)
    assert ok is False

def test_validar_precio_cero():
    prod = {**PRODUCTO_VALIDO, "precio": 0.0}
    ok, msg = validar_producto(prod)
    assert ok is False

def test_validar_precio_valido_bajo():
    prod = {**PRODUCTO_VALIDO, "precio": 0.01}
    ok, msg = validar_producto(prod)
    assert ok is True


# ── Tests: validar_lista ─────────────────────────────────────

def test_validar_lista_todos_validos():
    lista = [PRODUCTO_VALIDO, {**PRODUCTO_VALIDO, "nombre": "Teclado"}]
    resultado = validar_lista(lista)
    assert len(resultado) == 2

def test_validar_lista_filtra_invalidos():
    lista = [
        PRODUCTO_VALIDO,
        {**PRODUCTO_VALIDO, "nombre": "", "precio": -5.0},
    ]
    resultado = validar_lista(lista)
    assert len(resultado) == 1

def test_validar_lista_vacia():
    assert validar_lista([]) == []

def test_validar_lista_todos_invalidos():
    lista = [
        {**PRODUCTO_VALIDO, "precio": 0.0},
        {**PRODUCTO_VALIDO, "stock": -1},
    ]
    resultado = validar_lista(lista)
    assert resultado == []
