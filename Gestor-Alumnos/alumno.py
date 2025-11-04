'''
Es una aplicación por consola que permite:

-   Agregar un alumno
-   Modificar sus datos
-   Eliminar un alumno
-   Buscar un alumno por DNI
-   Mostrar todos los alumnos
'''

#* Creo la clase Alumno que representa a un alumno con sus atributos básicos.
class Alumno:
    def __init__(self, nombre, apellido, dni, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
    def __str__(self):
        return f"\nAlumno: {self.nombre} {self.apellido}, DNI: {self.dni}, Email: {self.email}"