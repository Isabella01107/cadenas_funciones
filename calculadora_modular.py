def suma(num1, num2):
    """
    Realiza la suma de dos números.

    Parámetros:
    - num1 (int o float): Primer número.
    - num2 (int o float): Segundo número.

    Retorno:
    - int o float: Resultado de la suma.
    """
    return num1 + num2

def resta(num1, num2):
    """
    Realiza la resta entre dos números.

    Parámetros:
    - num1 (int o float): Minuendo.
    - num2 (int o float): Sustraendo.

    Retorno:
    - int o float: Resultado de la resta.
    """
    return num1 - num2

def multiplicacion(num1, num2):
    """
    Realiza la multiplicación de dos números.

    Parámetros:
    - num1 (int o float): Primer número.
    - num2 (int o float): Segundo número.

    Retorno:
    - int o float: Producto de los dos números.
    """
    return num1 * num2

def division(num1, num2):
    """
    Realiza la división entre dos números, validando que el divisor no sea cero.

    Parámetros:
    - num1 (int o float): Dividendo.
    - num2 (int o float): Divisor.

    Retorno:
    - float: Resultado de la división si el divisor es distinto de cero.
    - str: Mensaje de error si el divisor es cero.
    """
    if num2 == 0:
        return "Error: no se puede dividir entre cero"
    else:
        return num1 / num2

# Menú de selección
opcion = int(input("Ingrese la operación que desea realizar:\n"
                   "1. Suma\n"
                   "2. Resta\n"
                   "3. Multiplicación\n"
                   "4. División\n"))

# Entrada de números
num1 = int(input("Ingrese el primer número:\n"))
num2 = int(input("Ingrese el segundo número:\n"))

# Ejecución según la opción
if opcion == 1:
    print("El resultado de la suma es:", suma(num1, num2))
elif opcion == 2:
    print("El resultado de la resta es:", resta(num1, num2))
elif opcion == 3:
    print("El resultado de la multiplicación es:", multiplicacion(num1, num2))
elif opcion == 4:
    print("El resultado de la división es:", division(num1, num2))
else:
    print("Opción inválida")
