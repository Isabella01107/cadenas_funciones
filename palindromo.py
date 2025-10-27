def palindromo(palabra):
    """
    Verifica si una palabra es palíndromo.
    
    Argumentos:
        palabra (str): Palabra a verificar
        
    Returns:
        str: Mensaje indicando si es palíndromo o no
    """
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        return "Tu palabra es un palíndromo"
    else:
        return "No es un Palíndromo"

# Entrada principal
palabra = input("Escribe una palabra: ")
resultado = palindromo(palabra)
print(resultado)