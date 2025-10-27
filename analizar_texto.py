def generar_contrasena(n):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*?"
    contrasena = ""
    for i in range(n):
        contrasena += choice(caracteres)
    return contrasena

# Programa principal
n = int(input("Longitud de la contraseña: "))
print("Contraseña generada:", generar_contrasena(n))