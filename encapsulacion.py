
def verificar_encampus(nombre):
    # Lista de nombres de personas en el campus
    nombres_encampus = ["Juan", "María", "Pedro", "Ana"]  # Puedes agregar más nombres según sea necesario

    # Verificar si el nombre está en la lista de nombres en el campus
    if nombre in nombres_encampus:
        return True
    else:
        return False

def main():
    # Solicitar al usuario que ingrese su nombre
    nombre_usuario = input("Por favor, ingresa tu nombre: ")

    # Verificar si el usuario está en el campus
    if verificar_encampus(nombre_usuario):
        print("¡Bienvenido al campus, {}!".format(nombre_usuario))
    else:
        print("Lo siento, {} no está en el campus en este momento.".format(nombre_usuario))

if __name__ == "__main__":
    main()
