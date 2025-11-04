import csv
import datetime
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

ARCHIVO_VENTAS = "data/ventas.csv"
CARPETA_REPORTES = "reportes"

# Asegurar que la carpeta exista
os.makedirs(CARPETA_REPORTES, exist_ok=True)


def leer_ventas():
    if not os.path.exists(ARCHIVO_VENTAS):
        print("⚠️ No hay registros de ventas.")
        return []
    ventas = []
    with open(ARCHIVO_VENTAS, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ventas.append(row)
    return ventas


# ==== REPORTES EN CONSOLA ====

def reporte_total_ventas():
    ventas = leer_ventas()
    if not ventas:
        return
    total = sum(float(v["total"]) for v in ventas)
    print(f"\n💵 Total de ventas registradas: ${total:.2f}")
    exportar = input("¿Desea exportar este reporte? (s/n): ").lower()
    if exportar == "s":
        exportar_pdf("total_ventas", [("Total de ventas", f"${total:.2f}")])
        exportar_csv("total_ventas", [["Total de ventas", total]])


def reporte_por_cliente():
    ventas = leer_ventas()
    if not ventas:
        return
    clientes = {}
    for v in ventas:
        nombre = v["cliente"]
        clientes[nombre] = clientes.get(nombre, 0) + float(v["total"])
    print("\n👥 Ventas por cliente:")
    datos = []
    for c, t in clientes.items():
        print(f"- {c}: ${t:.2f}")
        datos.append([c, t])

    exportar = input("¿Desea exportar este reporte? (s/n): ").lower()
    if exportar == "s":
        exportar_pdf("ventas_por_cliente", datos, titulo="Ventas por cliente")
        exportar_csv("ventas_por_cliente", [["Cliente", "Total"]] + datos)


def reporte_por_producto():
    ventas = leer_ventas()
    if not ventas:
        return
    productos = {}
    for v in ventas:
        nombre = v["producto"]
        productos[nombre] = productos.get(nombre, 0) + float(v["cantidad"])
    print("\n📦 Ventas por producto (cantidad vendida):")
    datos = []
    for p, c in productos.items():
        print(f"- {p}: {c} unidades")
        datos.append([p, c])

    exportar = input("¿Desea exportar este reporte? (s/n): ").lower()
    if exportar == "s":
        exportar_pdf("ventas_por_producto", datos, titulo="Ventas por producto")
        exportar_csv("ventas_por_producto", [["Producto", "Cantidad"]] + datos)


def reporte_por_fecha():
    ventas = leer_ventas()
    if not ventas:
        return
    fecha_inicio = input("📅 Ingrese fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("📅 Ingrese fecha de fin (YYYY-MM-DD): ")

    try:
        inicio = datetime.date.fromisoformat(fecha_inicio)
        fin = datetime.date.fromisoformat(fecha_fin)
    except ValueError:
        print("❌ Formato de fecha incorrecto.")
        return

    filtradas = [
        v for v in ventas
        if inicio <= datetime.date.fromisoformat(v["fecha"]) <= fin
    ]

    if not filtradas:
        print("⚠️ No hay ventas en ese rango de fechas.")
        return

    total = sum(float(v["total"]) for v in filtradas)
    print(f"\n🗓️ Ventas desde {inicio} hasta {fin}: ${total:.2f}")
    datos = [["Fecha", "Cliente", "Producto", "Cantidad", "Total"]]
    for v in filtradas:
        datos.append([v["fecha"], v["cliente"], v["producto"], v["cantidad"], v["total"]])

    exportar = input("¿Desea exportar este reporte? (s/n): ").lower()
    if exportar == "s":
        nombre = f"ventas_{inicio}_{fin}".replace("-", "")
        exportar_pdf(nombre, datos, titulo=f"Ventas desde {inicio} hasta {fin}")
        exportar_csv(nombre, datos)


# ==== FUNCIONES DE EXPORTACIÓN ====

def exportar_csv(nombre, datos):
    archivo = os.path.join(CARPETA_REPORTES, f"{nombre}.csv")
    with open(archivo, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(datos)
    print(f"✅ Reporte exportado a CSV: {archivo}")


def exportar_pdf(nombre, datos, titulo="Reporte"):
    archivo = os.path.join(CARPETA_REPORTES, f"{nombre}.pdf")
    c = canvas.Canvas(archivo, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, titulo)
    c.setFont("Helvetica", 12)

    y = 720
    for fila in datos:
        texto = " | ".join(str(v) for v in fila)
        c.drawString(50, y, texto)
        y -= 20
        if y < 50:
            c.showPage()
            y = 750

    c.save()
    print(f"✅ Reporte exportado a PDF: {archivo}")
