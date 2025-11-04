from alumno import Alumno

#* Creo una lista para almacenar los alumnos.
alumnos = []

#* Función para agregar un alumno.
def agregar_alumno():
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    dni = input('DNI: ')
    email = input('Email: ')
    nuevo_alumno = Alumno(nombre, apellido, dni, email)
    alumnos.append(nuevo_alumno)
    print(f'Agregaste a {nuevo_alumno}.')

#* Función para mostrar todos los alumnos.
def modificar_alumno():
    dni = input("Ingrese DNI del alumno a modificar: ")
    for alumno in alumnos:
        if alumno.dni == dni:
            alumno.nombre = input('Nuevo nombre: ')
            alumno.apellido = input('Nuevo apellido: ')
            alumno.email = input('Nuevo email: ')
            print(f'Modificaste a {alumno}.')
            return
    print('Alumno no encontrado.')

#* Función para eliminar un alumno.
def eliminar_alumno():
    dni = input("Ingrese DNI del alumno a eliminar: ")
    for alumno in alumnos:
        if alumno.dni == dni:
            alumnos.remove(alumno)
            print(f'Eliminaste a {alumno}.')
            return
    print('Alumno no encontrado.')

#* Función para buscar un alumno por DNI.
def buscar_alumno():
    dni = input("Ingrese DNI a buscar: ")
    for alumno in alumnos:
        if alumno.dni == dni:
            print(alumno)
            return
    print('Alumno no encontrado.')

#* Función para mostrar todos los alumnos.
def mostrar_alumnos():
    if not alumnos:
        print('No hay alumnos registrados.')
    else:
        for alumno in alumnos:
            print(alumno)

#* Función para mostrar el menú de opciones.
def menu():
    while True:
        print('\n- - - Gestor de Alumnos - - -')
        print('1. Agregar Alumno')
        print('2. Modificar Alumno')
        print('3. Eliminar Alumno')
        print('4. Buscar Alumno')
        print('5. Mostrar Todos los Alumnos')
        print('6. Salir')

        opcion = input('\nSeleccione una opcion: ')

        if opcion == '1':
            agregar_alumno()
        elif opcion == '2':
            modificar_alumno()
        elif opcion == '3':
            eliminar_alumno()
        elif opcion == '4':
            buscar_alumno()
        elif opcion == '5':
            mostrar_alumnos()
        elif opcion == '6':
            print('Saliste del programa.')
            break
        else: 
            print('Opción no válida, intente nuevamente.')

menu()