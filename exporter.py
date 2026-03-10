import json


def exportar_json(datos, ruta_salida):
    """
    Guarda un diccionario o lista en un archivo JSON.
    Retorna True si tuvo éxito, False en caso contrario.
    """
    try:
        with open(ruta_salida, "w", encoding="utf-8") as file:
            json.dump(datos, file, ensure_ascii=False, indent=2)
        print(f"  [OK] Resultados exportados a: {ruta_salida}")
        return True
    except Exception as e:
        print(f"  [Error] No se pudo exportar: {e}")
        return False
