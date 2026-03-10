import sys
from data_loader import cargar_datos
from utils import validar_lista
from processor import (
    filtrar_por_precio_maximo,
    filtrar_por_categoria,
    filtrar_por_stock_minimo,
    ordenar_por_nombre,
    ordenar_por_precio,
    ordenar_por_stock,
    calcular_estadisticas,
)
from exporter import exportar_json

RUTA_CSV_DEFAULT  = "data/productos.csv"
RUTA_JSON_DEFAULT = "data/resultados.json"

PRODUCTOS_INICIALES = [
    {"nombre": "Laptop Pro 15",     "categoria": "Electronica", "stock": 12, "precio": 1299.99},
    {"nombre": "Teclado Mecanico",  "categoria": "Accesorios",  "stock": 45, "precio":   89.50},
    {"nombre": "Monitor 27",        "categoria": "Electronica", "stock":  8, "precio":  349.00},
    {"nombre": "Mouse Inalambrico", "categoria": "Accesorios",  "stock": 60, "precio":   34.99},
    {"nombre": "Silla Ergonomica",  "categoria": "Muebles",     "stock": 15, "precio":  220.00},
]


def mostrar_productos(productos):
    if not productos:
        print("  (No hay productos para mostrar)")
        return
    print(f"\n  {'Nombre':<25} {'Categoria':<14} {'Stock':>5} {'Precio':>10}")
    print("  " + "-" * 58)
    for p in productos:
        print(f"  {p['nombre']:<25} {p['categoria']:<14} {p['stock']:>5} ${p['precio']:>9.2f}")
    print(f"\n  Total: {len(productos)} producto(s)\n")


def menu_filtrar(productos):
    print("\n  -- Filtrar --")
    print("  1 - Por precio maximo")
    print("  2 - Por categoria")
    print("  3 - Por stock minimo")
    opcion = input("  Opcion: ").strip()

    if opcion == "1":
        try:
            maximo = float(input("  Precio maximo: $"))
            resultado = filtrar_por_precio_maximo(productos, maximo)
            print(f"\n  Productos con precio <= ${maximo:.2f}:")
            mostrar_productos(resultado)
            return resultado
        except ValueError:
            print("  [Error] Ingresa un numero valido.")

    elif opcion == "2":
        categoria = input("  Categoria: ").strip()
        resultado = filtrar_por_categoria(productos, categoria)
        print(f"\n  Productos de '{categoria}':")
        mostrar_productos(resultado)
        return resultado

    elif opcion == "3":
        try:
            minimo = int(input("  Stock minimo: "))
            resultado = filtrar_por_stock_minimo(productos, minimo)
            print(f"\n  Productos con stock >= {minimo}:")
            mostrar_productos(resultado)
            return resultado
        except ValueError:
            print("  [Error] Ingresa un numero entero valido.")

    else:
        print("  Opcion no valida.")

    return productos


def menu_ordenar(productos):
    print("\n  -- Ordenar --")
    print("  1 - Por nombre (A-Z)")
    print("  2 - Por precio (menor a mayor)")
    print("  3 - Por stock (mayor disponibilidad primero)")
    opcion = input("  Opcion: ").strip()

    if opcion == "1":
        resultado = ordenar_por_nombre(productos)
    elif opcion == "2":
        resultado = ordenar_por_precio(productos, ascendente=True)
    elif opcion == "3":
        resultado = ordenar_por_stock(productos, ascendente=False)
    else:
        print("  Opcion no valida.")
        return productos

    print("\n  Lista ordenada:")
    mostrar_productos(resultado)
    return resultado


def menu_estadisticas(productos):
    stats = calcular_estadisticas(productos)
    print("\n  -- Estadisticas del Inventario --")
    print(f"  Total de productos    : {stats['total_productos']}")
    print(f"  Valor total inventario: ${stats['valor_total']:,.2f}")
    print(f"  Precio promedio       : ${stats['precio_promedio']:.2f}")
    print(f"  Producto mas caro     : {stats['producto_mas_caro']}")
    print(f"  Producto mas barato   : {stats['producto_mas_barato']}")
    print("  Productos por categoria:")
    for cat, cantidad in stats["conteo_por_categoria"].items():
        print(f"    - {cat}: {cantidad}")
    print()
    return stats


def menu_exportar(productos, stats):
    ruta = input(f"  Ruta de salida [{RUTA_JSON_DEFAULT}]: ").strip()
    if not ruta:
        ruta = RUTA_JSON_DEFAULT

    datos_exportar = {
        "estadisticas": stats,
        "productos":    productos,
    }
    exportar_json(datos_exportar, ruta)


def main():
    print("=" * 55)
    print("   InventarioCLI - Gestion de Inventario de Productos")
    print("=" * 55)

    # Carga los 5 productos iniciales automaticamente
    productos = list(PRODUCTOS_INICIALES)
    stats     = {}

    print(f"\n  [OK] {len(productos)} productos cargados por defecto.")
    mostrar_productos(productos)

    while True:
        print("\n  -- Menu Principal --")
        print("  1 - Cargar datos desde CSV")
        print("  2 - Filtrar")
        print("  3 - Ordenar")
        print("  4 - Mostrar estadisticas")
        print("  5 - Exportar resultados")
        print("  6 - Salir")

        opcion = input("\n  Selecciona una opcion: ").strip()

        if opcion == "1":
            ruta = input(f"  Ruta del CSV [{RUTA_CSV_DEFAULT}]: ").strip()
            if not ruta:
                ruta = RUTA_CSV_DEFAULT
            cargados  = cargar_datos(ruta)
            if cargados:
                productos = validar_lista(cargados)
                print(f"\n  {len(productos)} producto(s) cargado(s) correctamente.")
                mostrar_productos(productos)
            else:
                print("  [Aviso] No se cargaron datos. Se mantienen los productos actuales.")

        elif opcion == "2":
            productos = menu_filtrar(productos)

        elif opcion == "3":
            productos = menu_ordenar(productos)

        elif opcion == "4":
            stats = menu_estadisticas(productos)

        elif opcion == "5":
            if not stats:
                stats = calcular_estadisticas(productos)
            menu_exportar(productos, stats)

        elif opcion == "6":
            print("\n  Hasta luego!\n")
            sys.exit(0)

        else:
            print("  [Error] Opcion no valida. Ingresa un numero del 1 al 6.")


if __name__ == "__main__":
    main()