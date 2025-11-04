import csv
import os
from utils.validaciones import pedir_float, pedir_int, pedir_texto

ARCHIVO_CLIENTES = "data/clientes.csv"


def leer_clientes():
    if not os.path.exists(ARCHIVO_CLIENTES):
        return []
    with open(ARCHIVO_CLIENTES, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


def guardar_clientes(clientes):
    with open(ARCHIVO_CLIENTES, "w", newline="") as f:
        fieldnames = ["id", "nombre", "email"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(clientes)


def generar_id():
    clientes = leer_clientes()
    if not clientes:
        return "1"
    ultimo_id = max(int(c["id"]) for c in clientes)
    return str(ultimo_id + 1)


def agregar_cliente():
    nombre = input("👤 Nombre del cliente: ").strip()
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return
    email = input("📧 Email: ").strip()

    clientes = leer_clientes()
    if any(c["nombre"].lower() == nombre.lower() for c in clientes):
        print("⚠️ Ya existe un cliente con ese nombre.")
        return

    nuevo = {"id": generar_id(), "nombre": nombre, "email": email}
    clientes.append(nuevo)
    guardar_clientes(clientes)
    print("✅ Cliente registrado correctamente.")


def listar_clientes():
    clientes = leer_clientes()
    if not clientes:
        print("⚠️ No hay clientes registrados.")
        return
    print("\n=== LISTA DE CLIENTES ===")
    for c in clientes:
        print(f"ID: {c['id']} | {c['nombre']} - {c['email']}")


def editar_cliente():
    clientes = leer_clientes()
    if not clientes:
        print("⚠️ No hay clientes para editar.")
        return

    listar_clientes()
    id_buscar = input("🆔 Ingrese el ID del cliente a editar: ")

    for c in clientes:
        if c["id"] == id_buscar:
            print(f"Editando cliente: {c['nombre']}")
            nuevo_nombre = input(f"Nuevo nombre ({c['nombre']}): ").strip() or c["nombre"]
            nuevo_email = input(f"Nuevo email ({c['email']}): ").strip() or c["email"]

            c.update({"nombre": nuevo_nombre, "email": nuevo_email})
            guardar_clientes(clientes)
            print("✅ Cliente actualizado.")
            return

    print("❌ No se encontró un cliente con ese ID.")


def eliminar_cliente():
    clientes = leer_clientes()
    if not clientes:
        print("⚠️ No hay clientes para eliminar.")
        return

    listar_clientes()
    id_buscar = input("🆔 Ingrese el ID del cliente a eliminar: ")

    for c in clientes:
        if c["id"] == id_buscar:
            confirmar = input(f"¿Eliminar '{c['nombre']}'? (s/n): ").lower()
            if confirmar == "s":
                clientes.remove(c)
                guardar_clientes(clientes)
                print("🗑️ Cliente eliminado.")
            else:
                print("❎ Operación cancelada.")
            return

    print("❌ No se encontró un cliente con ese ID.")
