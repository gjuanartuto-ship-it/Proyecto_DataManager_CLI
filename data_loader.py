import csv

# Encodings a intentar en orden (cubre UTF-8, UTF-8 con BOM, Windows, Latin)
ENCODINGS = ["utf-8-sig", "utf-8", "cp1252", "latin-1"]


def _detectar_encoding(ruta_archivo):
    """Prueba encodings comunes y retorna el primero que funcione."""
    for enc in ENCODINGS:
        try:
            with open(ruta_archivo, "r", encoding=enc) as f:
                f.read()
            return enc
        except (UnicodeDecodeError, LookupError):
            continue
    return "latin-1"  # fallback final: latin-1 acepta cualquier byte


def cargar_datos(ruta_archivo):
    """
    Carga productos desde un archivo CSV.
    Detecta automaticamente el encoding (utf-8, cp1252, latin-1, etc.).
    Retorna una lista de diccionarios con los datos de cada producto.
    """
    productos = []

    try:
        encoding = _detectar_encoding(ruta_archivo)
        with open(ruta_archivo, "r", encoding=encoding) as file:
            reader = csv.DictReader(file)
            for fila in reader:
                try:
                    producto = {
                        "nombre":    fila["nombre"].strip(),
                        "categoria": fila["categoria"].strip(),
                        "stock":     int(fila["stock"].strip()),
                        "precio":    float(fila["precio"].strip()),
                    }
                    productos.append(producto)
                except ValueError as e:
                    print(f"  [Advertencia] Fila invalida omitida: {dict(fila)} - {e}")
    except FileNotFoundError:
        print(f"  [Error] Archivo no encontrado: {ruta_archivo}")
    except Exception as e:
        print(f"  [Error inesperado al leer archivo]: {e}")

    return productos