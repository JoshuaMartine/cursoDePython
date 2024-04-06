
nombre = input("Escriba su nombre, por favor: ")
edad = input("Escriba su edad: ")

edad = int(edad)


if edad >= 18:
    print("Su nombre es " + nombre + " y su edad es: " + str(edad) + ", así que es mayor")
else:
    print("Su nombre es " + nombre + " y su edad es: " + str(edad) + ", así que es menor")
