class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def esta_en_campus(self):
        # Método para determinar si la persona está en el campus
        raise NotImplementedError("Subclase debe implementar el método 'esta_en_campus'.")


class PersonaEnCampus(Persona):
    def esta_en_campus(self):
        return True


class PersonaFueraDeCampus(Persona):
    def esta_en_campus(self):
        return False


def main():
    nombre = input("Por favor, ingresa tu nombre: ")

    # Crear una instancia de PersonaEnCampus o PersonaFueraDeCampus basada en el nombre ingresado
    if nombre.lower() == "juan":
        persona = PersonaEnCampus(nombre)
    else:
        persona = PersonaFueraDeCampus(nombre)

    # Verificar si la persona está en el campus
    if persona.esta_en_campus():
        print("¡Bienvenido al campus, {}!".format(persona.nombre))
    else:
        print("Lo siento, {} no está en el campus en este momento.".format(persona.nombre))


if __name__ == "__main__":
    main()
