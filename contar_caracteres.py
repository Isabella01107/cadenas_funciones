def contador(palabras: str) -> str:
    """
    Cuenta la cantidad de vocales, espacios y consonantes en una cadena de texto.

    Parámetros:
    - palabras (str): Cadena de texto ingresada por el usuario.

    Retorno:
    - str: Mensaje con el número de vocales, espacios y consonantes encontrados.
    
    Nota:
    - Se consideran vocales las letras 'a', 'e', 'i', 'o', 'u' en minúscula.
    - Todo carácter que no sea vocal ni espacio se cuenta como consonante, incluyendo signos y números.
    """
    vocales = 0
    espacios = 0
    consonantes = 0

    for i in range(len(palabras)):
        letra = palabras[i].lower()  # Convertimos a minúscula para comparar

        if letra in ["a", "e", "i", "o", "u"]:
            vocales += 1
        elif letra == " ":
            espacios += 1
        else:
            consonantes += 1  # Todo lo demás se cuenta como consonante

    mensaje = "Vocales: " + str(vocales) + " | Espacios: " + str(espacios) + " | Consonantes: " + str(consonantes)
    return mensaje

# Solicita al usuario una frase
palabras = input("Por favor ingrese una o varias palabras: ")

# Ejecuta la función y muestra el resultado
resultado = contador(palabras)
print(resultado)