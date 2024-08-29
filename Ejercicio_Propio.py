"""
Descripción del problema: 

Una biblioteca necesita un sistema para gestionar sus libros. Cada libro tiene
un título, un autor, un año de publicación y un estado (disponible o prestado).
El sistema debe permitir las siguientes funcionalidades:
1. Agregar nuevos libros a la biblioteca.
2. Marcar libros como prestados o devueltos.
3. Mostrar la lista de libros disponibles.

El objetivo es crear un sistema que permita llevar un control eficiente
de los libros en la biblioteca y su estado.
"""

# Clase Libro: Representa un libro en la biblioteca con atributos como título, 
# autor, año de publicación y estado.

class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.estado = 'Disponible'

        # se utiliza en marcar_prestado y marcar_devuelto para mostrar 
        # la información actualizada del libro.
    
    def marcar_prestado(self):
        if self.estado == 'Disponible':
            self.estado = 'Prestado'
            print(f"\nEl libro '{self.titulo}' ha sido marcado como prestado.")
        else:
            print(f"\nEl libro '{self.titulo}' ya está prestado.")
        self.mostrar_info()
    
    def marcar_devuelto(self):
        if self.estado == 'Prestado':
            self.estado = 'Disponible'
            print(f"\nEl libro '{self.titulo}' ha sido marcado como devuelto.")
        else:
            print(f"\nEl libro '{self.titulo}' ya está disponible.")
        self.mostrar_info()

       
    
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.año_publicacion}, Estado: {self.estado}"
    
    def mostrar_info(self):
        """
        Muestra los detalles del libro en un formato claro.
        """
        print("\nDetalles del libro:")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicación: {self.año_publicacion}")
        print(f"Estado: {self.estado}")

        #Clase Biblioteca: Gestiona una colección de libros. Permite agregar nuevos 
        # libros, mostrar los libros disponibles y buscar un libro por título.


class Biblioteca:
    def __init__(self):
        self.libros = []

        #  se imprime la información ingresada por el usuario (titulo, autor, año_publicacion) 
        # para confirmar los datos que se han introducido
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"\nEl libro '{libro.titulo}' ha sido agregado a la biblioteca.")
        libro.mostrar_info()
    
    def mostrar_libros_disponibles(self):
        print("\nLibros Disponibles:")
        for libro in self.libros:
            if libro.estado == 'Disponible':
                libro.mostrar_info()
    
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        print(f"No se encontró el libro con el título '{titulo}'.")
        return None


# Función principal para interactuar con el usuario
def main():
    biblioteca = Biblioteca()
    # Agregué un método mostrar_info para imprimir los detalles del libro en un formato legible.

    while True:
        print("\nSistema de Gestión de Biblioteca")
        print("1. Agregar libro")
        print("2. Marcar libro como prestado")
        print("3. Marcar libro como devuelto")
        print("4. Mostrar libros disponibles")
        print("5. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            año_publicacion = input("Ingrese el año de publicación del libro: ")
            libro = Libro(titulo, autor, año_publicacion)
            biblioteca.agregar_libro(libro)
            print("\nDatos del libro ingresado:")
            libro.mostrar_info()
        
        elif opcion == '2':
            titulo = input("Ingrese el título del libro a marcar como prestado: ")
            libro = biblioteca.buscar_libro(titulo)
            if libro:
                libro.marcar_prestado()
        
        elif opcion == '3':
            titulo = input("Ingrese el título del libro a marcar como devuelto: ")
            libro = biblioteca.buscar_libro(titulo)
            if libro:
                libro.marcar_devuelto()
        
        elif opcion == '4':
            biblioteca.mostrar_libros_disponibles()
        
        elif opcion == '5':
            print("Saliendo del sistema...")
            # Mostrar todos los libros disponibles antes de salir
            print("\nLibros disponibles en la biblioteca al salir:")
            biblioteca.mostrar_libros_disponibles()
            break
        
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()


