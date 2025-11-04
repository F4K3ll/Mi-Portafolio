import csv
import os
import json
import uuid
from utils.validaciones import pedir_float, pedir_int, pedir_texto

# Crear carpeta data si no existe
if not os.path.exists("data"):
    os.makedirs("data")

# Crear archivo productos.json si no existe
if not os.path.exists("data/productos.json"):
    with open("data/productos.json", "w", encoding="utf-8") as archivo:
        json.dump([], archivo, indent=4)

def guardar_productos(productos):
    with open("data/productos.json", "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, indent=4, ensure_ascii=False)

def generar_id():
    return str(uuid.uuid4())[:8]

def agregar_producto():
    print("\n🟩 AGREGAR NUEVO PRODUCTO 🟩")
    
    # 1️⃣ Pedir datos al usuario (con validaciones)
    nombre = pedir_texto("Ingrese el nombre del producto: ")
    precio = pedir_float("Ingrese el precio del producto: ")
    stock = pedir_int("Ingrese la cantidad en stock: ")

    # 2️⃣ Crear el nuevo producto
    nuevo = {
        "id": generar_id(),
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
    }
    # 3️⃣ Cargar lista actual de productos
    productos = guardar_productos()
    # 4️⃣ Agregar y guardar
    productos.append(nuevo)
    guardar_productos(productos)

    print(f"✅ Producto '{nombre}' agregado correctamente.\n")

def listar_productos():
    productos = guardar_productos()
    if not productos:
        print("⚠️ No hay productos registrados.")
        return
    
    print("\n=== LISTA DE PRODUCTOS ===")
    for p in productos:
        print(f"ID: {p['id']} | {p['nombre']} - ${p['precio']} | Stock: {p['stock']}")

def editar_producto():
    productos = guardar_productos()
    if not productos:
        print("⚠️ No hay productos para editar.")
        return

    listar_productos()
    id_buscar = input("🆔 Ingrese el ID del producto a editar: ")

    for p in productos:
        if p["id"] == id_buscar:
            print(f"\n✏️ Editando producto: {p['nombre']}")
            p["nombre"] = pedir_texto("Nuevo nombre: ")
            p["precio"] = pedir_float("Nuevo precio: ")
            p["stock"] = pedir_int("Nuevo stock: ")
            guardar_productos(productos)
            print("✅ Producto actualizado correctamente.\n")
            return

    print("❌ No se encontró un producto con ese ID.\n")

def eliminar_producto():
    """Elimina un producto por ID."""
    productos = guardar_productos()
    if not productos:
        print("⚠️ No hay productos para eliminar.\n")
        return

    listar_productos()
    id_eliminar = pedir_texto("Ingrese el ID del producto a eliminar: ")

    productos_actualizados = [p for p in productos if p["id"] != id_eliminar]

    if len(productos_actualizados) == len(productos):
        print("❌ No se encontró un producto con ese ID.\n")
    else:
        guardar_productos(productos_actualizados)
        print("🗑️ Producto eliminado correctamente.\n")