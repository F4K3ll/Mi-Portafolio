import csv
import os
import hashlib

ARCHIVO_USUARIOS = "data/usuarios.csv"


def leer_usuarios():
    if not os.path.exists(ARCHIVO_USUARIOS):
        return []
    with open(ARCHIVO_USUARIOS, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


def guardar_usuarios(usuarios):
    with open(ARCHIVO_USUARIOS, "w", newline="") as f:
        fieldnames = ["id", "nombre", "rol", "password"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(usuarios)


def generar_id():
    usuarios = leer_usuarios()
    if not usuarios:
        return "1"
    ultimo_id = max(int(u["id"]) for u in usuarios)
    return str(ultimo_id + 1)


def hash_password(password):
    """Genera un hash SHA256 seguro para la contraseña"""
    return hashlib.sha256(password.encode()).hexdigest()


def registrar_usuario():
    print("\n=== 👤 REGISTRO DE USUARIO ===")
    nombre = input("Nombre de usuario: ").strip()
    rol = input("Rol (admin / vendedor): ").strip().lower()
    password = input("Contraseña: ").strip()

    if rol not in ["admin", "vendedor"]:
        print("❌ Rol inválido. Use 'admin' o 'vendedor'.")
        return

    usuarios = leer_usuarios()
    if any(u["nombre"].lower() == nombre.lower() for u in usuarios):
        print("⚠️ Ese nombre de usuario ya existe.")
        return

    nuevo = {
        "id": generar_id(),
        "nombre": nombre,
        "rol": rol,
        "password": hash_password(password)
    }

    usuarios.append(nuevo)
    guardar_usuarios(usuarios)
    print("✅ Usuario registrado correctamente.")


def login():
    print("\n=== 🔐 INICIO DE SESIÓN ===")
    nombre = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()
    usuarios = leer_usuarios()

    for u in usuarios:
        if u["nombre"].lower() == nombre.lower() and u["password"] == hash_password(password):
            print(f"✅ Bienvenido, {u['nombre']} ({u['rol']})")
            return u  # Devuelve el usuario autenticado
    print("❌ Usuario o contraseña incorrectos.")
    return None
