def es_par(numero):
    if es_par(numero % 2) ==0:
        return True
    else:
        return False
    
try:
    numero = int(input("Ingrese un numero")) 

    if es_par(numero):
        print(f"{numero} Es par")
    else:
        print(f"{numero} Es impar")
except:
    print("Ingrese un numero")