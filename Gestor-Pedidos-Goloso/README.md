# Gestor de Pedidos "Goloso"

Sistema de gestión de pedidos para una heladería. Permite agendar pedidos (sabor, tipo de helado, cantidad y fecha de entrega) sin depender de cuadernos o mensajes sueltos.

**URL pública en producción**: https://f4k3ll.pythonanywhere.com

---

## Características principales

- **Interfaz web amigable** para usuarios sin conocimientos de programación.
- **Validación de fechas**: no se aceptan fechas de entrega pasadas.
- **Control de estados**: cada pedido avanza por un flujo: Pendiente → Listo → Entregado.
- **Agenda diaria**: lista de pedidos filtrada por fecha, con selector de calendario.
- **Formulario de carga** con Bootstrap vía CDN (sin build tools).
- **Backups automáticos diarios** de la base de datos.
- **Panel de administración de Django** incluido para gestionar clientes, productos y pedidos.

---

## Stack tecnológico

- **Python 3.10** + **Django 5.2 LTS**
- **SQLite** (en desarrollo y producción)
- **Bootstrap 5** vía CDN para el frontend
- **Whitenoise** para servir archivos estáticos en producción
- **PythonAnywhere** como hosting (cuenta gratuita)

---

## Estructura del proyecto

Gestor-Pedidos-Goloso/
├── config/                          # Configuración del proyecto Django
│   ├── __init__.py                  # Vacío (shim de paquete)
│   ├── asgi.py                      # Configuración ASGI (para servidores asincrónicos)
│   ├── settings.py                  # Configuración principal: base de datos, seguridad, estáticos, etc.
│   ├── urls.py                      # URLs raíz del proyecto (incluye admin y pedidos)
│   └── wsgi.py                      # Configuración WSGI (para servidores síncronos como gunicorn)
│
├── pedidos/                         # Aplicación principal del proyecto
│   ├── __init__.py                  # Vacío (shim de paquete)
│   ├── admin.py                     # Configuración del panel de administración de Django
│   ├── apps.py                      # Configuración de la aplicación (AppConfig)
│   ├── forms.py                     # Formulario ModelForm para crear/editar pedidos
│   ├── models.py                    # Modelos: Cliente, Producto, Pedidos
│   ├── tests.py                     # Tests automatizados (8 pruebas)
│   ├── urls.py                      # Rutas de la aplicación: nuevo, agenda, avanzar, backup
│   ├── views.py                     # Vistas: nuevo_pedidos, agenda, avanzar_estado, backup_db_view
│   └── templates/pedidos/           # Plantillas HTML (Bootstrap 5 vía CDN)
│       ├── base.html                # Plantilla base (header, CSS, footer)
│       ├── nuevo_pedidos.html       # Formulario de creación de pedidos
│       └── agenda.html              # Lista de pedidos por día con botones de estado
│
├── staticfiles/                     # Archivos estáticos generados por Django (NO subir a Git)
│   └── admin/                       # CSS/JS del panel de Django (autogenerado)
│
├── backups/                         # Copias de seguridad de la base de datos (NO subir a Git)
│   └── db_YYYYMMDD_HHMMSS.sqlite3   # Archivos de backup generados automáticamente
│
├── backup_db.py                     # Script de backup: copia db.sqlite3 con marca de tiempo
│
├── requirements.txt                 # Dependencias con versiones exactas (Django, gunicorn, whitenoise, etc.)
│
├── manage.py                        # Script de gestión de Django (creado automáticamente)
│
├── db.sqlite3                       # Base de datos SQLite (NO subir a Git, está en .gitignore)
│
├── venv/                            # Entorno virtual (NO subir a Git, está en .gitignore)
│
├── .gitignore                       # Lista de archivos y carpetas que NO se suben a Git
│
├── GUIA_USO.md                      # Guía de uso para el cliente (cómo usar el sistema)
│
└── README.md                        # Documentación del proyecto (para GitHub)

- config/: Es el "cerebro" del proyecto Django. Contiene la configuración general (base de datos, seguridad, URLs, etc.).
- pedidos/: Es la aplicación en sí. Tiene los modelos (Cliente, Producto, Pedidos), las vistas (páginas web), las URLs (rutas), los formularios, las plantillas HTML y los tests.
- staticfiles/: Se genera automáticamente cuando corremos collectstatic. Contiene todos los archivos CSS, JS e imágenes que usa el sitio (incluidos los del panel de Django). No se sube a Git.
- backups/: Aquí se guardan las copias de seguridad de la base de datos. No se sube a Git.
- backup_db.py: Script que se ejecuta para crear un backup de la base de datos.
- requirements.txt: Lista las dependencias del proyecto con las versiones exactas que se deben instalar.
- db.sqlite3: La base de datos real donde se guardan los pedidos. No se sube a Git.
- venv/: El entorno virtual donde se instalan las dependencias. No se sube a Git.
- .gitignore: Archivo que le dice a Git qué archivos NO debe seguir (como la base de datos, el entorno virtual, los estáticos generados, etc.).
- GUIA_USO.md: Documento que explica cómo usar el sistema el cliente final.
- README.md: Documentación técnica del proyecto para GitHub.