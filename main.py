# Clase que representa un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor, categoria):
        self.titulo = titulo  # Título del libro
        self.autor = autor    # Autor del libro
        self.categoria = categoria  # Categoría del libro

# Clase que representa un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, codigo):
        self.nombre = nombre  # Nombre del usuario
        self.codigo = codigo  # Código del usuario

# Clase principal que gestiona la biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []  # Lista de libros registrados
        self.usuarios = []  # Lista de usuarios registrados
        self.categorias = ["Ciencia", "Literatura", "Tecnología"]  # Categorías disponibles

    def registrar_libro(self):
        print("\n--- Registro de Nuevo Libro📚 ---")
        titulo = input("Título del libro: ").strip()
        autor = input("Autor del libro: ").strip()
        print("Categorías disponibles:")
        # Muestra las categorías disponibles con ayuda de un bucle.
        for i, cat in enumerate(self.categorias):
            print(f"{i+1}. {cat}")
        cat_select = input("Elige la categoría (1-3): ").strip()
        # Valida la selección de categoría, que esté dentro del rango.
        if cat_select not in ['1','2','3']:
            print("Categoría no válida.")
            return
        # Categoria es igual al valor del número seleccionado menos 1 (índice de la lista).
        categoria = self.categorias[int(cat_select)-1]
        libro = Libro(titulo, autor, categoria)  # Crea un objeto Libro
        self.libros.append(libro)  # Agrega el libro a la lista
        print("Libro registrado exitosamente.")

    def registrar_usuario(self):
        print("\n--- Registro de Nuevo Usuario 👨 ---")
        nombre = input("Nombre del usuario: ").strip()
        codigo = input("Código del usuario: ").strip()
        usuario = Usuario(nombre, codigo)  # Crea un objeto Usuario
        self.usuarios.append(usuario)  # Agrega el usuario a la lista
        print("Usuario registrado exitosamente.")

    def mostrar_libros(self):
        print("\n--- Libros Registrados ---")
        if not self.libros:
            print("No hay libros registrados.")
            return
        # Muestra los datos de cada libro registrado
        for libro in self.libros:
            print(f"Título: {libro.titulo}, Autor: {libro.autor}, Categoría: {libro.categoria}")

    def mostrar_usuarios(self):
        print("\n--- Usuarios Registrados ---")
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return
        # Muestra los datos de cada usuario registrado
        for usuario in self.usuarios:
            print(f"Nombre: {usuario.nombre}, Código: {usuario.codigo}")

# Función principal que ejecuta el menú interactivo
def main():
    biblioteca = Biblioteca()  # Crea una instancia de Biblioteca
    print("Bienvenido al simulador de biblioteca universitaria.")
    while True:
        print("\n--- Menú Principal ---")
        print("\n1. Registrar nuevo libro 📚")
        print("2. Registrar nuevo usuario 👨")
        print("\n3. 👁️ Mostrar libros registrados")
        print("4. 👁️ Mostrar usuarios registrados")
        print("\n5.Salir ↩️")
        opcion = input("Elige una opción (1-5): ").strip()
        if opcion == '1':
            biblioteca.registrar_libro()
        elif opcion == '2':
            biblioteca.registrar_usuario()
        elif opcion == '3':
            biblioteca.mostrar_libros()
        elif opcion == '4':
            biblioteca.mostrar_usuarios()
        elif opcion == '5':
            print("Gracias por usar el simulador. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Punto de entrada del script
if __name__ == "__main__":
    main()