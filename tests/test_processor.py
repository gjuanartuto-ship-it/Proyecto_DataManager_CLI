import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from processor import (
    filtrar_por_precio_maximo,
    filtrar_por_categoria,
    filtrar_por_stock_minimo,
    ordenar_por_nombre,
    ordenar_por_precio,
    ordenar_por_stock,
    calcular_precio_promedio,
    calcular_valor_total_inventario,
    calcular_estadisticas,
)

# ── Datos de prueba ──────────────────────────────────────────

PRODUCTOS = [
    {"nombre": "Laptop Pro",       "categoria": "Electrónica",  "stock": 12, "precio": 1299.99},
    {"nombre": "Teclado Mecánico", "categoria": "Accesorios",   "stock": 45, "precio": 89.50},
    {"nombre": "Monitor 27",       "categoria": "Electrónica",  "stock":  8, "precio": 349.00},
    {"nombre": "Mouse Inalámbrico","categoria": "Accesorios",   "stock": 60, "precio": 34.99},
    {"nombre": "Silla Ergonómica", "categoria": "Muebles",      "stock": 15, "precio": 220.00},
]

# ── Tests: filtrar_por_precio_maximo ─────────────────────────

def test_filtrar_precio_maximo_normal():
    resultado = filtrar_por_precio_maximo(PRODUCTOS, 200.00)
    assert all(p["precio"] <= 200.00 for p in resultado)
    assert len(resultado) == 2

def test_filtrar_precio_maximo_todos():
    resultado = filtrar_por_precio_maximo(PRODUCTOS, 9999.00)
    assert len(resultado) == len(PRODUCTOS)

def test_filtrar_precio_maximo_ninguno():
    resultado = filtrar_por_precio_maximo(PRODUCTOS, 0.01)
    assert resultado == []

def test_filtrar_precio_maximo_lista_vacia():
    assert filtrar_por_precio_maximo([], 100.0) == []


# ── Tests: filtrar_por_categoria ─────────────────────────────

def test_filtrar_categoria_normal():
    resultado = filtrar_por_categoria(PRODUCTOS, "Electrónica")
    assert len(resultado) == 2
    assert all(p["categoria"] == "Electrónica" for p in resultado)

def test_filtrar_categoria_insensible_mayusculas():
    resultado = filtrar_por_categoria(PRODUCTOS, "accesorios")
    assert len(resultado) == 2

def test_filtrar_categoria_inexistente():
    assert filtrar_por_categoria(PRODUCTOS, "Ropa") == []

def test_filtrar_categoria_lista_vacia():
    assert filtrar_por_categoria([], "Electrónica") == []


# ── Tests: filtrar_por_stock_minimo ──────────────────────────

def test_filtrar_stock_minimo_normal():
    resultado = filtrar_por_stock_minimo(PRODUCTOS, 15)
    assert all(p["stock"] >= 15 for p in resultado)

def test_filtrar_stock_minimo_todos():
    resultado = filtrar_por_stock_minimo(PRODUCTOS, 0)
    assert len(resultado) == len(PRODUCTOS)

def test_filtrar_stock_minimo_ninguno():
    assert filtrar_por_stock_minimo(PRODUCTOS, 9999) == []


# ── Tests: ordenar_por_nombre ────────────────────────────────

def test_ordenar_por_nombre():
    resultado = ordenar_por_nombre(PRODUCTOS)
    nombres = [p["nombre"].lower() for p in resultado]
    assert nombres == sorted(nombres)

def test_ordenar_por_nombre_lista_vacia():
    assert ordenar_por_nombre([]) == []


# ── Tests: ordenar_por_precio ────────────────────────────────

def test_ordenar_precio_ascendente():
    resultado = ordenar_por_precio(PRODUCTOS, ascendente=True)
    precios = [p["precio"] for p in resultado]
    assert precios == sorted(precios)

def test_ordenar_precio_descendente():
    resultado = ordenar_por_precio(PRODUCTOS, ascendente=False)
    precios = [p["precio"] for p in resultado]
    assert precios == sorted(precios, reverse=True)


# ── Tests: ordenar_por_stock ─────────────────────────────────

def test_ordenar_stock_descendente():
    resultado = ordenar_por_stock(PRODUCTOS, ascendente=False)
    stocks = [p["stock"] for p in resultado]
    assert stocks == sorted(stocks, reverse=True)

def test_ordenar_stock_ascendente():
    resultado = ordenar_por_stock(PRODUCTOS, ascendente=True)
    stocks = [p["stock"] for p in resultado]
    assert stocks == sorted(stocks)


# ── Tests: calcular_precio_promedio ──────────────────────────

def test_precio_promedio_normal():
    promedio = calcular_precio_promedio(PRODUCTOS)
    esperado = sum(p["precio"] for p in PRODUCTOS) / len(PRODUCTOS)
    assert abs(promedio - esperado) < 0.001

def test_precio_promedio_lista_vacia():
    assert calcular_precio_promedio([]) == 0.0

def test_precio_promedio_un_elemento():
    uno = [{"nombre": "X", "categoria": "Y", "stock": 1, "precio": 50.0}]
    assert calcular_precio_promedio(uno) == 50.0


# ── Tests: calcular_valor_total_inventario ───────────────────

def test_valor_total_normal():
    total = calcular_valor_total_inventario(PRODUCTOS)
    esperado = sum(p["precio"] * p["stock"] for p in PRODUCTOS)
    assert abs(total - esperado) < 0.01

def test_valor_total_lista_vacia():
    assert calcular_valor_total_inventario([]) == 0.0

def test_valor_total_stock_cero():
    sin_stock = [{"nombre": "X", "categoria": "Y", "stock": 0, "precio": 100.0}]
    assert calcular_valor_total_inventario(sin_stock) == 0.0


# ── Tests: calcular_estadisticas ─────────────────────────────

def test_estadisticas_lista_vacia():
    stats = calcular_estadisticas([])
    assert stats["total_productos"] == 0
    assert stats["valor_total"] == 0.0
    assert stats["producto_mas_caro"] is None
    assert stats["producto_mas_barato"] is None

def test_estadisticas_normal():
    stats = calcular_estadisticas(PRODUCTOS)
    assert stats["total_productos"] == 5
    assert stats["producto_mas_caro"] == "Laptop Pro"
    assert stats["producto_mas_barato"] == "Mouse Inalámbrico"
    assert "Electrónica" in stats["conteo_por_categoria"]
    assert stats["conteo_por_categoria"]["Electrónica"] == 2

def test_estadisticas_tipo_retorno():
    stats = calcular_estadisticas(PRODUCTOS)
    assert isinstance(stats["valor_total"], float)
    assert isinstance(stats["conteo_por_categoria"], dict)
    assert isinstance(stats["precio_promedio"], float)
