# InventarioCLI — Sistema de Gestión de Inventario de Productos

Aplicación de línea de comandos para cargar, validar, filtrar, ordenar y exportar registros de productos desde archivos CSV.

## Estructura del Proyecto

```
inventario_cli/
├── main.py           # Menú CLI principal
├── data_loader.py    # Carga de datos desde CSV
├── processor.py      # Filtros, ordenamiento y estadísticas
├── exporter.py       # Exportación a JSON
├── utils.py          # Validación de datos
├── tests/
│   ├── __init__.py
│   ├── test_processor.py
│   └── test_utils.py
└── data/
    ├── productos.csv
    └── resultados.json   # se genera al exportar
```

## Requisitos

- Python 3.8+
- pytest (`pip install pytest`)

## Cómo correr el proyecto

Desde la carpeta `inventario_cli/`:

```bash
python main.py
```

Al iniciar, el programa carga automáticamente 5 productos de ejemplo para que se pueda usar de inmediato sin necesidad de subir un CSV:

- Laptop Pro 15 — Electrónica
- Teclado Mecánico — Accesorios
- Monitor 27 — Electrónica
- Mouse Inalámbrico — Accesorios
- Silla Ergonómica — Muebles

## Menú

```
1 - Cargar datos desde CSV
2 - Filtrar
3 - Ordenar
4 - Mostrar estadísticas
5 - Exportar resultados
6 - Salir
```

## Cómo cargar un CSV propio

Al elegir la opción 1, el programa pide la ruta del archivo. Dependiendo de dónde se esté corriendo:

En Google Colab, primero subir el archivo y luego escribir:
```
/content/productos.csv
```

En computadora local, escribir la ruta completa del archivo, por ejemplo:
```
C:\Users\TuNombre\Downloads\productos.csv
```

Si no se escribe nada y se presiona Enter, busca el archivo en `data/productos.csv` por defecto.
Si el archivo no se encuentra o tiene errores, el programa mantiene los datos que ya estaban cargados.

El CSV debe tener este formato:
```
nombre,categoria,stock,precio
Laptop Pro 15,Electronica,12,1299.99
Teclado Mecanico,Accesorios,45,89.50
```

El programa detecta automáticamente el encoding del archivo (utf-8, cp1252, latin-1) así que no hay que preocuparse por problemas de caracteres especiales.

## Tests

```bash
pytest tests
pytest tests -v   # con detalle
```

- `test_processor.py` prueba filtros, ordenamiento, precios, valor total y estadísticas
- `test_utils.py` prueba la validación de productos individuales y listas


