# utils/validaciones.py
# ────────────────────────────────
# Funciones reutilizables para validar entradas del usuario
# en todo el sistema de gestión de negocios.

def pedir_float(mensaje):
    """Pide un número decimal al usuario, validando el formato y que no sea negativo."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("❌ El valor no puede ser negativo. Intente nuevamente.")
            else:
                return valor
        except ValueError:
            print("❌ Ingrese un número válido (por ejemplo, 12.5).")

def pedir_int(mensaje):
    """Pide un número entero al usuario, validando el formato y que no sea negativo."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("❌ El número no puede ser negativo. Intente nuevamente.")
            else:
                return valor
        except ValueError:
            print("❌ Ingrese un número entero válido.")

def pedir_texto(mensaje):
    """Pide texto no vacío al usuario."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        else:
            print("❌ Este campo no puede estar vacío.")
