#Modulo de Productos

from productos import agregar_producto, listar_productos, editar_producto, eliminar_producto

def menu_productos():
    while True:
        print("\n=== 📦 GESTIÓN DE PRODUCTOS ===")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            editar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            break
        else:
            print("❌ Opción no válida.")

def menu_principal():
    while True:
        print("\n=== 🧾 GESTORPY – SISTEMA DE GESTIÓN ===")
        print("1. Gestión de productos")
        print("2. Gestión de clientes (próximamente)")
        print("3. Registro de ventas (próximamente)")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            print("\n👤 Módulo de clientes en desarrollo.")
        elif opcion == "3":
            print("\n💰 Módulo de ventas en desarrollo.")
        elif opcion == "4":
            print("\n👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")


if __name__ == "__main__":
    menu_principal()

#Modulo de Clientes

from productos import agregar_producto, listar_productos, eliminar_producto
from clientes import agregar_cliente, listar_clientes, eliminar_cliente


def menu_productos():
    while True:
        print("\n=== 📦 GESTIÓN DE PRODUCTOS ===")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Eliminar producto")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            break
        else:
            print("❌ Opción no válida.")


def menu_clientes():
    while True:
        print("\n=== 👤 GESTIÓN DE CLIENTES ===")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Eliminar cliente")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "4":
            break
        else:
            print("❌ Opción no válida.")


def menu_principal():
    while True:
        print("\n=== 🧾 GESTORPY – SISTEMA DE GESTIÓN ===")
        print("1. Gestión de productos")
        print("2. Gestión de clientes")
        print("3. Registro de ventas (próximamente)")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            print("\n💰 Módulo de ventas en desarrollo.")
        elif opcion == "4":
            print("\n👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")


if __name__ == "__main__":
    menu_principal()

#Modulo de Ventas

from productos import agregar_producto, listar_productos, eliminar_producto
from clientes import agregar_cliente, listar_clientes, eliminar_cliente
from ventas import registrar_venta, listar_ventas


def menu_productos():
    while True:
        print("\n=== 📦 GESTIÓN DE PRODUCTOS ===")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Eliminar producto")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            break
        else:
            print("❌ Opción no válida.")


def menu_clientes():
    while True:
        print("\n=== 👤 GESTIÓN DE CLIENTES ===")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Eliminar cliente")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "4":
            break
        else:
            print("❌ Opción no válida.")


def menu_ventas():
    while True:
        print("\n=== 💰 REGISTRO DE VENTAS ===")
        print("1. Registrar nueva venta")
        print("2. Listar ventas")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            listar_ventas()
        elif opcion == "3":
            break
        else:
            print("❌ Opción no válida.")


def menu_principal():
    while True:
        print("\n=== 🧾 GESTORPY – SISTEMA DE GESTIÓN ===")
        print("1. Gestión de productos")
        print("2. Gestión de clientes")
        print("3. Registro de ventas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            menu_ventas()
        elif opcion == "4":
            print("\n👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")


if __name__ == "__main__":
    menu_principal()

#Modulo de Reportes

from productos import agregar_producto, listar_productos, eliminar_producto
from clientes import agregar_cliente, listar_clientes, eliminar_cliente
from ventas import registrar_venta, listar_ventas
from reportes import reporte_total_ventas, reporte_por_cliente, reporte_por_producto, reporte_por_fecha


def menu_productos():
    while True:
        print("\n=== 📦 GESTIÓN DE PRODUCTOS ===")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Eliminar producto")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            break
        else:
            print("❌ Opción no válida.")


def menu_clientes():
    while True:
        print("\n=== 👤 GESTIÓN DE CLIENTES ===")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Eliminar cliente")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "4":
            break
        else:
            print("❌ Opción no válida.")


def menu_ventas():
    while True:
        print("\n=== 💰 REGISTRO DE VENTAS ===")
        print("1. Registrar nueva venta")
        print("2. Listar ventas")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            listar_ventas()
        elif opcion == "3":
            break
        else:
            print("❌ Opción no válida.")


def menu_reportes():
    while True:
        print("\n=== 📊 REPORTES ===")
        print("1. Total de ventas")
        print("2. Ventas por cliente")
        print("3. Ventas por producto")
        print("4. Ventas por fecha")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            reporte_total_ventas()
        elif opcion == "2":
            reporte_por_cliente()
        elif opcion == "3":
            reporte_por_producto()
        elif opcion == "4":
            reporte_por_fecha()
        elif opcion == "5":
            break
        else:
            print("❌ Opción no válida.")


def menu_principal():
    while True:
        print("\n=== 🧾 GESTORPY – SISTEMA DE GESTIÓN ===")
        print("1. Gestión de productos")
        print("2. Gestión de clientes")
        print("3. Registro de ventas")
        print("4. Reportes")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            menu_ventas()
        elif opcion == "4":
            menu_reportes()
        elif opcion == "5":
            print("\n👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")


if __name__ == "__main__":
    menu_principal()

#Modulo de Usuarios

from productos import agregar_producto, listar_productos, editar_producto, eliminar_producto
from clientes import agregar_cliente, listar_clientes, editar_cliente, eliminar_cliente
from ventas import registrar_venta, listar_ventas
from reportes import reporte_total_ventas, reporte_por_cliente, reporte_por_producto, reporte_por_fecha
from usuarios import registrar_usuario, login


def menu_productos(usuario):
    while True:
        print("\n=== 📦 GESTIÓN DE PRODUCTOS ===")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            if usuario["rol"] == "admin":
                editar_producto()
            else:
                print("🚫 No tienes permiso para editar productos.")
        elif opcion == "4":
            if usuario["rol"] == "admin":
                eliminar_producto()
            else:
                print("🚫 No tienes permiso para eliminar productos.")
        elif opcion == "5":
            break
        else:
            print("❌ Opción no válida.")


def menu_clientes(usuario):
    while True:
        print("\n=== 👤 GESTIÓN DE CLIENTES ===")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Editar cliente")
        print("4. Eliminar cliente")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            if usuario["rol"] == "admin":
                editar_cliente()
            else:
                print("🚫 No tienes permiso para editar clientes.")
        elif opcion == "4":
            if usuario["rol"] == "admin":
                eliminar_cliente()
            else:
                print("🚫 No tienes permiso para eliminar clientes.")
        elif opcion == "5":
            break
        else:
            print("❌ Opción no válida.")


def menu_principal(usuario):
    while True:
        print(f"\n=== 🧾 GESTORPY – Bienvenido, {usuario['nombre']} ({usuario['rol']}) ===")
        print("1. Gestión de productos")
        print("2. Gestión de clientes")
        print("3. Registro de ventas")
        print("4. Reportes")
        if usuario["rol"] == "admin":
            print("5. Registrar nuevo usuario")
            print("6. Cerrar sesión")
        else:
            print("5. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_productos(usuario)
        elif opcion == "2":
            menu_clientes(usuario)
        elif opcion == "3":
            registrar_venta()
        elif opcion == "4":
            submenu_reportes()
        elif opcion == "5" and usuario["rol"] == "admin":
            registrar_usuario()
        elif (opcion == "5" and usuario["rol"] != "admin") or (opcion == "6"):
            print("\n👋 Cerrando sesión...")
            break
        else:
            print("❌ Opción no válida.")


def submenu_reportes():
    while True:
        print("\n=== 📊 REPORTES ===")
        print("1. Total de ventas")
        print("2. Ventas por cliente")
        print("3. Ventas por producto")
        print("4. Ventas por fecha")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            reporte_total_ventas()
        elif opcion == "2":
            reporte_por_cliente()
        elif opcion == "3":
            reporte_por_producto()
        elif opcion == "4":
            reporte_por_fecha()
        elif opcion == "5":
            break
        else:
            print("❌ Opción no válida.")


def iniciar_sistema():
    print("=== 🧾 GESTORPY – SISTEMA DE GESTIÓN ===")
    while True:
        print("\n1. Iniciar sesión")
        print("2. Registrar nuevo usuario (solo si no hay ninguno)")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = login()
            if usuario:
                menu_principal(usuario)
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")


if __name__ == "__main__":
    iniciar_sistema()