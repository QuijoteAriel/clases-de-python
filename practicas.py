
""" 
# ####################################################################
# Ejercicio 1: Almacenar y Mostrar Asignaturas
# ####################################################################

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

asignaturas = ['matematicas', 'lengua', 'fisica', 'historia ']

print(asignaturas)


# ####################################################################
# Ejercicio 2: Mostrar Asignaturas con un Mensaje Personalizado
# ####################################################################

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.


for i in asignaturas:
    print("Yo estudio ", i)


# ####################################################################
# Ejercicio 3: Mostrar Notas por Asignatura
# ####################################################################

# Escribir un programaque almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y 
# después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las 
# asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.


ns =[]
for i in asignaturas:
    n = int(input("cuanta nota sacaste en : "+ i + " " ))
    ns.append(n)
for j in range(len(asignaturas)):

    print('En '+ asignaturas[j] + ' sacaste ' + str(ns[j]))


# ####################################################################
# Ejercicio 4: Números Ganadores de la Lotería Primitiva
# ####################################################################

# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una 
# lista y los muestre por pantalla ordenados de menor a mayor.



ganador = []

for i in range(6):
    ganador.append(int(input('numero ganadores')))
ganador.sort()
#for i in range(len(ganador)):

print('los numeo gandores son : ' ,str(ganador))


# ####################################################################
# Ejercicio 5: Mostrar Números del 1 al 10 en Orden Inverso
# ####################################################################

#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.


n = [1,2,3,4,5,6,7,8,9,10]
m = [1,2,3,4,5,6,7,8,9,10]

print(n)
n.reverse()
print(n)

for i in range(1,11):
    print(m[-i],end=", ")

# ####################################################################
# Ejercicio 6: Asignaturas a Repetir
# ####################################################################

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

asignaturas = ['matematicas', 'lengua', 'fisica', 'historia ']

ns =[]
for i in asignaturas:
    n = int(input("cuanta nota sacaste en : "+ i + " " ))
    ns.append(n)
for j in range(len(asignaturas)):
    if ns[j] <= 5:
        print('Debes repetir '+ asignaturas[j] + ' sacaste ' + str(ns[j]))
    else:
        print("Aprovaste el año escolar")

# #####################################################################
# Ejercicio 7: 
# #####################################################################
import string

# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.


# abc = ["a", "b", "c", "d", "e", "f", "g", "h", "j", "i", "k", "l", "m", "n", "o","p" ,"q" , "r", "s", "t", "u", "v", "w", "x", "y", "z"]
abc = list(string.ascii_lowercase)
print(abc)
for i in range(len(abc),1 , -1):
    if i % 3 == 0:
        abc.pop(i-1)
print(abc, end='')



# #####################################################################
# Ejercicio 8: 
# #####################################################################

# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

palabra = input("Dime una palabra: ")
palabra = palabra.lower()
palabra = palabra.replace(" ","")
palabra = palabra.replace("á","a")
palabra = palabra.replace("é","e")
palabra = palabra.replace("í","i")
palabra = palabra.replace("ó","o")
palabra = palabra.replace("ú","u")
palabra = palabra.replace(",","")
print(palabra)
    
if palabra == palabra[::-1]:
    print("es palindromo")
else:
    print("no es palindromo")

"""


# #####################################################################
# Ejercicio 9:
# #####################################################################

# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

frase = input("Dime una frase: ")



