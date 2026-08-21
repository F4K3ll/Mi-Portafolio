# 🧾 GestorPy

> Sistema de gestión para pequeños negocios, desarrollado en **Python**.  
> Permite administrar productos, clientes, ventas, reportes y usuarios con roles y contraseñas seguras.

---

## 🚀 Características principales

✅ **Gestión de productos**
- Alta, baja, edición y listado de productos.  
- Control de stock automático.  

✅ **Gestión de clientes**
- Registro, edición y eliminación de clientes.  
- Evita duplicados y valida campos vacíos.  

✅ **Ventas**
- Registro de ventas con fecha, cliente, producto y total.  
- Actualización automática del stock.  

✅ **Reportes**
- Totales, por cliente, producto o rango de fechas.  
- Exportación a **CSV** y **PDF** (listos para imprimir o compartir).  

✅ **Usuarios y roles**
- Sistema de login seguro (hash SHA256).  
- Roles: `admin` y `vendedor`.  
- Control de permisos (solo admin puede editar o eliminar).  

---

## 🧩 Estructura del proyecto

```
GestorPy/
│
├── data/                  # Archivos CSV de datos
│   ├── productos.csv
│   ├── clientes.csv
│   ├── ventas.csv
│   └── usuarios.csv
│
├── reportes/               # Archivos exportados (PDF, CSV)
│
├── main.py                 # Menú principal
├── productos.py             # Módulo de gestión de productos
├── clientes.py              # Módulo de gestión de clientes
├── ventas.py                # Módulo de registro de ventas
├── reportes.py              # Módulo de reportes y exportación
└── usuarios.py              # Módulo de login y usuarios
```

---

## ⚙️ Instalación

1. Cloná el repositorio:
   ```bash
   git clone https://github.com/F4K3ll/Mi-Portafolio.git
   cd Mi-Portafolio/Gestor-Negocios
   ```

---

## 📊 Ejemplo Visual (interfaz de consola)

```
=== 🧾 GESTORPY – SISTEMA DE GESTIÓN ===
1. Iniciar sesión
2. Registrar nuevo usuario (solo si no hay ninguno)
3. Salir

🔐 Usuario: admin
Contraseña: *****

✅ Bienvenido, admin (admin)

=== 📦 GESTIÓN DE PRODUCTOS ===
1. Agregar producto
2. Listar productos
3. Editar producto
4. Eliminar producto
5. Volver al menú principal
```

## 🗂️ Reportes importados

Los reportes se guardan automáticamente en la carpeta `reportes/`, por ejemplo:

- ventas_por_cliente.csv
- ventas_por_producto.pdf
- ventas_20250101_20250131.pdf

## 🧠 Tecnologías utilizadas

- 🐍 Python 3.x
- 📄 CSV (almacenamiento de datos)
- 🧾 ReportLab (generación de PDF)
- 🔐 Hashlib (SHA256) (seguridad de contraseñas)

## 🏗️ Mejoras futuras (roadmap)

- Interfaz gráfica (Tkinter o PyQt).
- Migración a versión web (Flask o Django).
- Base de datos relacional (SQLite o PostgreSQL).
- Gráficos estadísticos de ventas.
- Envío automático de reportes por correo.

## 👨‍💻 Autor

**Julián Augusto Leguizamón**

📍 Caseros, Buenos Aires, Argentina

📧 [j.a.leguizamon13@gmail.com](mailto:j.a.leguizamon13@gmail.com)

🔗 [LinkedIn](https://www.linkedin.com/in/julian-augusto-leguizamon-8854282a6)

💻 [GitHub](https://github.com/F4K3ll)

## 🏁 Licencia

Este proyecto está bajo la licencia MIT.  
Podés usarlo, modificarlo y distribuirlo libremente, dando crédito al autor.

## 💬 Nota final

Este proyecto fue creado como práctica integral de Python, aplicando:

- Manipulación de archivos.
- Programación modular.
- Validaciones y roles.
- Exportación de reportes en PDF y CSV.

Ideal para presentar como proyecto en tu portfolio.
