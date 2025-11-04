import csv
import os

ARCHIVO_PRODUCTOS = "data/productos.csv"


def leer_productos():
    if not os.path.exists(ARCHIVO_PRODUCTOS):
        return []
    with open(ARCHIVO_PRODUCTOS, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


def guardar_productos(productos):
    with open(ARCHIVO_PRODUCTOS, "w", newline="") as f:
        fieldnames = ["id", "nombre", "precio", "stock"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(productos)


def generar_id():
    productos = leer_productos()
    if not productos:
        return "1"
    ultimo_id = max(int(p["id"]) for p in productos)
    return str(ultimo_id + 1)


def agregar_producto():
    nombre = input("📝 Nombre del producto: ").strip()
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return

    productos = leer_productos()
    if any(p["nombre"].lower() == nombre.lower() for p in productos):
        print("⚠️ Ya existe un producto con ese nombre.")
        return

    try:
        precio = float(input("💰 Precio: "))
        stock = int(input("📦 Stock inicial: "))
    except ValueError:
        print("❌ Datos inválidos.")
        return

    nuevo = {
        "id": generar_id(),
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
    }
    productos.append(nuevo)
    guardar_productos(productos)
    print("✅ Producto agregado correctamente.")


def listar_productos():
    productos = leer_productos()
    if not productos:
        print("⚠️ No hay productos registrados.")
        return
    print("\n=== LISTA DE PRODUCTOS ===")
    for p in productos:
        print(f"ID: {p['id']} | {p['nombre']} - ${p['precio']} | Stock: {p['stock']}")


def editar_producto():
    productos = leer_productos()
    if not productos:
        print("⚠️ No hay productos para editar.")
        return

    listar_productos()
    id_buscar = input("🆔 Ingrese el ID del producto a editar: ")

    for p in productos:
        if p["id"] == id_buscar:
            print(f"Editando producto: {p['nombre']}")
            nuevo_nombre = input(f"Nuevo nombre ({p['nombre']}): ").strip() or p["nombre"]
            try:
                nuevo_precio = input(f"Nuevo precio ({p['precio']}): ").strip()
                nuevo_precio = float(nuevo_precio) if nuevo_precio else float(p["precio"])
                nuevo_stock = input(f"Nuevo stock ({p['stock']}): ").strip()
                nuevo_stock = int(nuevo_stock) if nuevo_stock else int(p["stock"])
            except ValueError:
                print("❌ Datos inválidos.")
                return

            p.update({"nombre": nuevo_nombre, "precio": nuevo_precio, "stock": nuevo_stock})
            guardar_productos(productos)
            print("✅ Producto actualizado.")
            return

    print("❌ No se encontró un producto con ese ID.")


def eliminar_producto():
    productos = leer_productos()
    if not productos:
        print("⚠️ No hay productos para eliminar.")
        return

    listar_productos()
    id_buscar = input("🆔 Ingrese el ID del producto a eliminar: ")

    for p in productos:
        if p["id"] == id_buscar:
            confirmar = input(f"¿Eliminar '{p['nombre']}'? (s/n): ").lower()
            if confirmar == "s":
                productos.remove(p)
                guardar_productos(productos)
                print("🗑️ Producto eliminado.")
            else:
                print("❎ Operación cancelada.")
            return

    print("❌ No se encontró un producto con ese ID.")
