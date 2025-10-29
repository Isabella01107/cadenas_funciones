 # Cadenas_Funciones
 
 Este repositorio contiene cinco programas básicos en Python que realizan diferentes operaciones con funciones, desde el análisis de texto y validación de palíndromos hasta la generación de contraseñas seguras y operaciones aritméticas básicas.Cada programa puede ejecutarse desde la terminal y permite la interacción directa con el usuario.

 Contenido
 1.contador_vocales.py
 2.palindromo.py
 3.calculadora_funciones.py
 4.analizador_texto.py
 5.generador_contrasena.py
 
 1. contador_vocales.py
 Descripción:
 Cuenta la cantidad de vocales, espacios y consonantes en una cadena de texto ingresada por el usuario. 
 Ejemplo de ejecución:
 Por favor ingrese una o varias palabras: Hola mundo
 Vocales: 4 | Espacios: 1 | Consonantes: 5
 Posibles errores:
 -Entrada vacía: el programa devolverá conteos en cero.
 -Caracteres especiales o números también se cuentan como consonantes.
 2. palindromo.py
 Descripción:
 Verifica si una palabra es un palíndromo, es decir, si se lee igual de izquierda a derecha que de derecha a izquierda.
 Ejemplo de ejecución:
 Escribe una palabra: radar
 Tu palabra es un palíndromo
 Escribe una palabra: casa
 No es un Palíndromo
 Posibles errores:
 -Ingresar espacios o frases → no se consideran correctamente.
 -Palabras con mayúsculas → se convierten a minúsculas automáticamente.
 3. calculadora_funciones.py
 Descripción:
 Permite realizar las operaciones básicas de suma, resta, multiplicación y división, utilizando funciones definidas por el usuario.
 Ejemplo de ejecución:
 Ingrese la operación que desea realizar:
 1. Suma
 2. Resta
 3. Multiplicación
 4. División
 3
 Ingrese el primer número:
 6
 Ingrese el segundo número:
 7
 El resultado de la multiplicación es: 42
 Posibles errores:
 -Dividir entre cero → “Error: no se puede dividir entre cero”.
 -Ingresar letras en lugar de números → ValueError.
 -Opción inválida → mensaje “Opción inválida”.
 4. analizador_texto.py
 Descripción:
 Analiza un texto e identifica la cantidad de palabras, frases y párrafos que contiene
 Ejemplo de ejecución:
 Ingresa el texto:
 Hola. ¿Cómo estás?
 Todo bien por aquí.
 Palabras: 5
 Frases: 2
 Párrafos: 2
 Posibles errores:
 -Texto vacío → todos los conteos serán 0.
 -Falta de signos de puntuación → el número de frases puede no reflejar el texto real.
 5. generador_contrasena.py
 Descripción:
 Genera una contraseña aleatoria con letras mayúsculas, minúsculas, números y caracteres especiales según la longitud indicada por el usuario.
 Ejemplo de ejecución:
 Longitud de la contraseña: 10
 Contraseña generada: A9b@Q2r!Xp
 Posibles errores:
 -Longitud no numérica → ValueError.
 -Longitud negativa o cero → genera una contraseña vacía.
 -No importar choice del módulo random → error NameError.