# Gestor de Pedidos "Goloso" — Guía de uso

**Sistema**: Heladería de un amigo de Julián  
**Desarrollado por**: Julián (estudiante IT)  
**URL pública**: https://f4k3ll.pythonanywhere.com

---

## 1. Cómo entrar al sistema

Abrí el navegador e ís a:

**https://f4k3ll.pythonanywhere.com/pedidos/agenda/**

### Primera vez:
1. El sistema te pedirá **iniciar sesión**.
2. Usá los datos que te dimos:
   - **Usuario**: `Goloso.Gelato` *(o el que te indicamos)*
   - **Contraseña**: `Goloso.Gelato` *(o la que configuraste)*

### Si ya entraste antes:
El sistema recuerda la mientras no la cierres. Si cerraste el navegador, vuelve a pasos 1 y 2.

---

## 2. Ver la agenda de pedidos

Al entrar, verás una lista de pedidos filtrados por **hoy** (fecha actual).

- **Formulario superior**: seleccioná una fecha con el calendario para ver los pedidos de ese día.
- **Formato de fecha**: debajo del selector aparece explícitamente `dd/mm/aaaa`, para evitar confusiones.
- **Si no hay pedidos**: aparecerá un mensaje: *"No hay pedidos para este día"*.

---

## 3. Cargar un nuevo pedido

Hay dos formas:

### Opción A: Desde la agenda
1. En la parte inferior de la tabla, hacé clic en **+ Cargar nuevo pedido**.
2. Se abrirá el formulario de creación.
3. Completá los campos:
   - **Cliente**: elegí de la lista (ya cargados anteriormente).
   - **Producto**: seleccioná **sabor** y **tipo** (helado o postre).
   - **Cantidad**: **cuarto** (1/4 kg), **medio** (1/2 kg) o **kilo** (1 kg).
   - **Fecha de entrega**: elegí una fecha **futura** (no se aceptan fechas pasadas).
   - **Estado**: por defecto viene **Pendiente**.
4. Hacé clic en el botón **Guardar pedido**.

### Opción B: Desde el menú directo
Ingresá a: `https://f4k3ll.pythonanywhere.com/pedidos/nuevo/`

Los pasos son los mismos que en la Opción A.

---

## 4. Cambiar el estado de un pedido (agenda)

En la tabla de la agenda, cada pedido tiene una columna **Acción** con un botón:

- **Si el estado es "Pendiente"**: el botón dice **Marcar Listo**. Al hacer clic, el pedido pasa a estado **Listo**.
- **Si el estado es "Listo"**: el botón dice **Marcar Entregado**. Al hacer clic, el pedido pasa a estado **Entregado**.
- **Si el estado es "Entregado"**: no aparece botón (el pedido ya finalizó).

> **Importante**: Los cambios de estado solo se pueden hacer desde la agenda, usando ese botón. No uses el formulario de "Nuevo pedido" para esto.

---

## 5. Panel de administración (opcional)

El sistema incluye un panel de administración de Django para cargar clientes, productos y ver pedidos.

Ingresá a:

**https://f4k3ll.pythonanywhere.com/admin/**

Usuario y contraseña: los mismos que para entrar al sistema (Goloso.Gelato / Goloso.Gelato).

Desde ahí podés:
- Ver/listar todos los pedidos.
- Filtrar por fecha o estado.
- Agregar nuevos clientes o productos.
- Cambiar estados manualmente (útil para pruebas).

---

## 6. Backups automáticos

El sistema realiza **backups diarios automáticos** de la base de datos.

- **No es necesario hacer nada**: el sistema copia `db.sqlite3` cada día y lo guarda en la carpeta `backups/`.
- **Para descargar un backup manualmente** (opcional):
  1. Entrá a la consola de PythonAnywhere (o pedí al desarrollador).
  2. Vas a: `Mi-Portafolio/Gestor-Pedidos-Goloso/backups/`.
  3. Ahí verás archivos con nombre `db_YYYYMMDD_HHMMSS.sqlite3`.

---

## 7. Cerrar sesión (buena práctica)

Al terminar de usar el sistema, cerá la haciendo clic en el botón de **logout** que aparece en la esquina superior derecha (o cerrando la pestaña del navegador).

---

## 8. Preguntas frecuentes

**¿La fecha de entrega puede ser hoy?**
No. El sistema valida que la fecha sea **futura**. Si intentás guardar una fecha del día o anterior, el sistema devolverá un cartel en rojo indicando el error.

**¿Qué pasa si cometo un error al cargar un pedido?**
Los campos obligatorios son cliente, producto, cantidad y fecha de entrega. Si faltá alguno, el formulario mostrará un cartel en rojo debajo del campo correspondiente. Podés corregirlo y volver a guardar.

**¿Puedo ver pedidos de otros días?**
Sí. En la agenda, seleccioná otra fecha en el calendario de la parte superior.

**¿Puedo acceder desde el celular?**
Sí. La interfaz está diseñada para verse bien en computadoras y celulares, usando Bootstrap por CDN.

---

## 9. Contacto

Si encontrás algún error o tenés dudas, contactá a Julián (desarrollador del proyecto).

--- 
*Última actualización: 19/09/2026*