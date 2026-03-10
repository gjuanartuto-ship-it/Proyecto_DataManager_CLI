def validar_producto(producto):
    """
    Valida los campos de un producto.
    Retorna (True, None) si es válido, o (False, mensaje) si no.
    """
    if not producto.get("nombre", "").strip():
        return False, "El nombre no puede estar vacío."

    if not producto.get("categoria", "").strip():
        return False, "La categoría no puede estar vacía."

    try:
        stock = int(producto["stock"])
        if stock < 0:
            return False, f"El stock no puede ser negativo. Valor recibido: {stock}"
    except (ValueError, KeyError):
        return False, "El stock debe ser un número entero válido."

    try:
        precio = float(producto["precio"])
        if precio <= 0:
            return False, f"El precio debe ser mayor a 0. Valor recibido: {precio}"
    except (ValueError, KeyError):
        return False, "El precio debe ser un número válido."

    return True, None


def validar_lista(productos):
    """
    Filtra una lista de productos eliminando los inválidos.
    Retorna la lista limpia.
    """
    validos = []
    for prod in productos:
        ok, mensaje = validar_producto(prod)
        if ok:
            validos.append(prod)
        else:
            print(f"  [Validación] Producto '{prod.get('nombre', '?')}' descartado: {mensaje}")
    return validos
