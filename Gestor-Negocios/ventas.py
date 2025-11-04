import csv
import os
import datetime
from productos import leer_productos, guardar_productos
from clientes import leer_clientes
from utils.validaciones import pedir_float, pedir_int, pedir_texto

ARCHIVO_VENTAS = "data/ventas.csv"

# Crear carpeta y archivo si no existen
if not os.path.exists("data"):
    os.mkdir("data")

if not os.path.exists(ARCHIVO_VENTAS):
    with open(ARCHIVO_VENTAS, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "cliente", "producto", "cantidad", "total", "fecha"])


def leer_ventas():
    ventas = []
    with open(ARCHIVO_VENTAS, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ventas.append(row)
    return ventas


def guardar_ventas(ventas):
    with open(ARCHIVO_VENTAS, "w", newline="") as f:
        fieldnames = ["id", "cliente", "producto", "cantidad", "total", "fecha"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(ventas)


def registrar_venta():
    print("\n=== 💰 REGISTRO DE VENTA ===")

    clientes = leer_clientes()
    productos = leer_productos()

    if not clientes:
        print("⚠️ No hay clientes registrados.")
        return
    if not productos:
        print("⚠️ No hay productos registrados.")
        return

    # Mostrar clientes
    print("\nClientes disponibles:")
    for c in clientes:
        print(f"{c['id']}. {c['nombre']} (DNI: {c['dni']})")

    id_cliente = input("Seleccione el ID del cliente: ")
    cliente = next((c for c in clientes if c["id"] == id_cliente), None)
    if not cliente:
        print("❌ Cliente no encontrado.")
        return

    # Mostrar productos
    print("\nProductos disponibles:")
    for p in productos:
        print(f"{p['id']}. {p['nombre']} - ${p['precio']} | Stock: {p['stock']}")

    id_producto = input("Seleccione el ID del producto: ")
    producto = next((p for p in productos if p["id"] == id_producto), None)
    if not producto:
        print("❌ Producto no encontrado.")
        return

    cantidad = int(input("Cantidad: "))

    if int(producto["stock"]) < cantidad:
        print("⚠️ No hay suficiente stock disponible.")
        return

    total = float(producto["precio"]) * cantidad

    # Actualizar stock
    producto["stock"] = str(int(producto["stock"]) - cantidad)
    guardar_productos(productos)

    # Registrar venta
    ventas = leer_ventas()
    nueva_venta = {
        "id": str(len(ventas) + 1),
        "cliente": cliente["nombre"],
        "producto": producto["nombre"],
        "cantidad": str(cantidad),
        "total": str(total),
        "fecha": datetime.date.today().isoformat()
    }
    ventas.append(nueva_venta)
    guardar_ventas(ventas)

    print(f"✅ Venta registrada correctamente. Total: ${total:.2f}\n")


def listar_ventas():
    ventas = leer_ventas()
    if not ventas:
        print("⚠️ No hay ventas registradas.")
        return

    print("\n📜 Historial de ventas:")
    for v in ventas:
        print(f"ID: {v['id']} | Cliente: {v['cliente']} | Producto: {v['producto']} | Cantidad: {v['cantidad']} | Total: ${v['total']} | Fecha: {v['fecha']}")
    print()
