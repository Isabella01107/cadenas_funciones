def analizar(texto):
    palabras = len(texto.split())
    frases = texto.count('.') + texto.count('!') + texto.count('?')
    parrafos = len([p for p in texto.split('\n') if p.strip()])
    print(f"Palabras: {palabras}\nFrases: {frases}\nPárrafos: {parrafos}")

texto = input("Ingresa el texto:\n")
analizar(texto)