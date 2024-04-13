usuarios = {
    'usuario1': {'nombre': 'Juan', 'apellido': 'Pérez', 'edad': 30, 'pin': '1234', 'saldo': 1000},
    'usuario2': {'nombre': 'María', 'apellido': 'Gómez', 'edad': 25, 'pin': '5678', 'saldo': 1500}
}

def verificar_pin(usuario, pin):
    if usuario in usuarios and usuarios[usuario]['pin'] == pin:
        return True
    else:
        return False

def mostrar_informacion(usuario):
    info = usuarios[usuario]
    print("Nombre:", info['nombre'])
    print("Apellido:", info['apellido'])
    print("Edad:", info['edad'])
    print("Saldo:", info['saldo'])

def retirar_dinero(usuario, cantidad):
    if usuarios[usuario]['saldo'] >= cantidad:
        usuarios[usuario]['saldo'] -= cantidad
        print("Retiro exitoso. Nuevo saldo:", usuarios[usuario]['saldo'])
    else:
        print("Saldo insuficiente")

def depositar_dinero(usuario, cantidad):
    usuarios[usuario]['saldo'] += cantidad
    print("Depósito exitoso. Nuevo saldo:", usuarios[usuario]['saldo'])

print("Usuarios disponibles:", list(usuarios.keys()))  # Agregamos esta línea

usuario_actual = input("Ingrese su usuario: ")
pin_actual = input("Ingrese su PIN: ")

if verificar_pin(usuario_actual, pin_actual):
    print("Bienvenido,", usuarios[usuario_actual]['nombre'])
    opcion = input("¿Qué desea hacer? (1 para ver información, 2 para retirar dinero, 3 para depositar dinero): ")

    if opcion == '1':
        mostrar_informacion(usuario_actual)
    elif opcion == '2':
        cantidad = float(input("Ingrese la cantidad que desea retirar: "))
        retirar_dinero(usuario_actual, cantidad)
    elif opcion == '3':
        cantidad = float(input("Ingrese la cantidad que desea depositar: "))
        depositar_dinero(usuario_actual, cantidad)
    else:
        print("Opción no válida")
else:
    print("PIN incorrecto. Acceso denegado.") 

