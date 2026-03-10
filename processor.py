def filtrar_por_precio_maximo(productos, maximo):
    """Filtra productos con precio menor o igual al máximo dado."""
    return [p for p in productos if p["precio"] <= maximo]


def filtrar_por_categoria(productos, categoria):
    """Filtra productos de una categoría específica (sin distinción de mayúsculas)."""
    return [p for p in productos if p["categoria"].lower() == categoria.lower()]


def filtrar_por_stock_minimo(productos, stock_minimo):
    """Filtra productos con stock mayor o igual al mínimo dado."""
    return [p for p in productos if p["stock"] >= stock_minimo]


def ordenar_por_nombre(productos):
    """Ordena los productos alfabéticamente por nombre."""
    return sorted(productos, key=lambda p: p["nombre"].lower())


def ordenar_por_precio(productos, ascendente=True):
    """Ordena los productos por precio. Por defecto, ascendente."""
    return sorted(productos, key=lambda p: p["precio"], reverse=not ascendente)


def ordenar_por_stock(productos, ascendente=False):
    """Ordena los productos por stock. Por defecto, descendente (más disponibles primero)."""
    return sorted(productos, key=lambda p: p["stock"], reverse=not ascendente)


def calcular_valor_total_inventario(productos):
    """Calcula el valor total del inventario (precio * stock por producto)."""
    if not productos:
        return 0.0
    return sum(p["precio"] * p["stock"] for p in productos)


def calcular_precio_promedio(productos):
    """Calcula el precio promedio de todos los productos."""
    if not productos:
        return 0.0
    return sum(p["precio"] for p in productos) / len(productos)


def calcular_estadisticas(productos):
    """
    Calcula estadísticas básicas del inventario:
    - Total de productos
    - Valor total del inventario
    - Precio promedio
    - Producto más caro y más barato
    - Conteo por categoría
    """
    if not productos:
        return {
            "total_productos":       0,
            "valor_total":           0.0,
            "precio_promedio":       0.0,
            "producto_mas_caro":     None,
            "producto_mas_barato":   None,
            "conteo_por_categoria":  {},
        }

    mas_caro   = max(productos, key=lambda p: p["precio"])
    mas_barato = min(productos, key=lambda p: p["precio"])

    conteo = {}
    for p in productos:
        cat = p["categoria"]
        conteo[cat] = conteo.get(cat, 0) + 1

    return {
        "total_productos":      len(productos),
        "valor_total":          round(calcular_valor_total_inventario(productos), 2),
        "precio_promedio":      round(calcular_precio_promedio(productos), 2),
        "producto_mas_caro":    mas_caro["nombre"],
        "producto_mas_barato":  mas_barato["nombre"],
        "conteo_por_categoria": conteo,
    }
