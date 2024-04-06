"""numero = input("Ingrese su numero:")

numero_introducido = int(numero)

if numero_introducido % 2 == 0 :
    print("su numero es par")
else:
    print("su numero es impar")
    """

numero = int(input("Introduzca su número:"))

cuenta = 1  # primer numero impar

while cuenta < numero:   
    if cuenta % 2 != 0:  
        print(cuenta)
    cuenta += 2  
