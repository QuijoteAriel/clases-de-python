# -*- coding: utf-8 -*- 

# -----------------------------------------------------------------------------
# NOTAS DE CLASE DE PYTHON
# 
# Este script contiene notas y ejemplos de código de conceptos básicos de Python.
# Ha sido refactorizado para mejorar la legibilidad y corregir errores.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# 1. Manejo de cadenas de caracteres (Strings)
# -----------------------------------------------------------------------------

# Las cadenas de caracteres se pueden manipular de muchas formas.
# Una de ellas es accediendo a caracteres específicos mediante su índice.

name = 'jose'

# Acceso a caracteres por índice. Python cuenta los índices desde 0.
print(name[0])  # Imprime el carácter en la posición 0, que es la 'j'.
print(name[1])  # Imprime el carácter en la posición 1, que es la 'o'.
print(name[2])  # Imprime el carácter en la posición 2, que es la 's'.
print(name[3])  # Imprime el carácter en la posición 3, que es la 'e'.

# Slicing para invertir una cadena.
print(name[::-1])  # Imprime la cadena en orden inverso: 'esoj'.

# Para incluir comillas dobles dentro de una cadena, se pueden escapar con \".
print("hola \"como\" estas?")

# Python ofrece varios métodos para transformar cadenas.
print(name.upper())    # Convierte toda la cadena a mayúsculas: 'JOSE'.
print(name.title())    # Pone en mayúscula la primera letra: 'Jose'.
print("  texto  ".strip()) # Elimina espacios en blanco al inicio y al final.
print(len(name))       # Devuelve la longitud de la cadena: 4.


# -----------------------------------------------------------------------------
# 2. Tipos de datos y la función print()
# -----------------------------------------------------------------------------

# La función type() devuelve el tipo de un dato.
x = 10
print(type(x))  # Imprime el tipo de la variable x: <class 'int'>.

# En Python, True se evalúa como 1 y False como 0 en contextos numéricos.
print(True == 1)   # Esto imprimirá True.
print(False == 0)  # Esto también imprimirá True.

# La función print() puede tomar múltiples argumentos.
# Por defecto, los separa con un espacio.
print("nunca", "pares", "de", "aprender")

# El operador '+' concatena las cadenas sin añadir espacios.
print("nunca" + "pares" + "de" + "aprender")

# Se puede especificar un separador personalizado con el argumento `sep`.
print("nunca", "pares", "de", "aprender", sep="; ")

# El argumento `end` define qué se imprime al final. Por defecto es un salto de línea ('\n').
print("Nunca", end=" ")
print("pares de aprender")  # Esta línea continuará en la misma línea que la anterior.

# El carácter '\n' en una cadena representa un salto de línea.
print("Hola\nmundo")
print("jose\nluis\nflores")

# Impresión con formato específico usando f-strings (método moderno).
valor = 3.14159
print(f"Valor: {valor:.2f}") # Formatea el número a dos decimales: "Valor: 3.14"

# Impresión con formato usando el método format().
print("Valor: {:.4f}".format(valor)) # Formatea a cuatro decimales: "Valor: 3.1416"

# Para imprimir rutas de archivos en Windows, es necesario escapar la barra invertida '\\'.
print("Ruta en Windows: C:\\Users\\Usuario\\Desktop\\archivo.txt")
# En sistemas tipo Unix (Linux, macOS), no es necesario.
print("Ruta en Unix/Linux: /home/user/documentos/archivo.txt")


# -----------------------------------------------------------------------------
# 3. Listas
# -----------------------------------------------------------------------------

# Las listas son colecciones ordenadas y mutables.
# Pueden contener diferentes tipos de datos.
to_do = ["Estudiar Python", 1, False, 5.7, ["A", "B"]]
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Imprimir una lista completa.
print(to_do)

# Métodos que modifican la lista in-place (no devuelven una nueva lista).
numbers.reverse()  # Invierte el orden de los elementos en la lista.
print(numbers)

# Slicing para invertir una lista (crea una copia invertida).
print(to_do[::-1])

# La lista original no se modifica con el slicing.
print(to_do)

# `del` puede eliminar elementos de una lista por su índice o por un slice.
del to_do[:2]  # Elimina los dos primeros elementos: "Estudiar Python" y 1.
print(to_do)


# --- Modificación de listas y referencias ---

a = [1, 2, 3, 4, 5]

# Asignación de referencia: 'b' apunta al mismo objeto en memoria que 'a'.
b = a
a.append(6)  # Cualquier cambio en 'a' se reflejará en 'b'.

print(f"ID de a: {id(a)}, Contenido de a: {a}")
print(f"ID de b: {id(b)}, Contenido de b: {b}") # Mismo ID y contenido que 'a'

# Creación de una copia superficial (shallow copy): 'c' es un nuevo objeto.
c = a[:] # El slicing [:] crea una copia de la lista.
c.append(7) # Los cambios en 'c' no afectan a 'a'.

print(f"ID de c: {id(c)}, Contenido de c: {c}") # ID diferente, contenido diferente.
print(f"Contenido de a no ha cambiado: {a}")
