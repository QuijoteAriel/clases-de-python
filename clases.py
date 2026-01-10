# Manejo de canena de caracteres
 
# Se puee manipular las cadenas de caracteres de mchas formas, una de ella es llamando a caracteres especificos como :

name = 'jose'
print(name[0])  # llama al caracter en la pocicion 1 que seria la 'o' ya que python cuenta desde el cero y no desde el 1
print(name[1])  
print(name[2]) 
print(name[3])

print(name[::-1]) # imprime de atras hasta a delante

print("hola  \"como \" , estas ? ") # imprime las comillas dobles como parte del print sin afectar a las comillas que rodean al mismo print

# tambien se puedes ordenar y dividir las cadenas de otras formas, cambiar el formato y reorganizar los caracteres

print(name.upper()) # escribe en mayusculas
print(name.title()) # escribe el modo titulo
print(name.strip()) # elimina los espacion de adelante a atras de la caneda
print(len(name)) # escibe el numero de largo  de la cadena


 
# TIPOS DE DATOS 

x = 10 
print(type(x))  # escribe el tipo de dato ya sea 'ini' , 'str', 'float', o 'bool' pero no el dato en si


print(True == 1) # por astrabcion True es igual a uno


print(False == 0) # por lo tanto False es igual a cero 


print("nunca","pares","de","aprender")  # separado por comas se hace un espacio 
print("nunca" + "pares" + "de" + "aprender") # no se hace espacio en blanco 


# Uso de sep, permite especificar como separar los elementos al imprimir


print("nunca","pares","de","aprender", sep="; ")  

# uso de end, los que este dentro de las  comillas del end afecta al print, si hay "\n" sera un salto de linea , si hay espacios en blanco esos espacios se imprimiran tambien  

print("Nunca", end=" ")
print("pares de aprender")
print("Hola\nmundo")
print("jose\nluis\nflores")

# Impresion con formato especifico 

# Puedes controlar el formato de los números al imprimir. En este ejemplo, :.2f indica que el número debe mostrarse con dos decimales. Así, imprimirá “Valor: 3.14”, redondeando el número a dos decimales. Esto es especialmente útil cuando trabajas con datos numéricos y necesitas un formato específico.

valor = 3.14159
print("Valor: {:.4f}".format(valor))

# Para imprimir rutas de windows se necesita tambien la ruta de escape 

print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")
print("La ruta de archivo es: /home/user/documentos/archivo.txt")


# Clases  y metodos

# listas

to_do = ["hola", 1, False, 5.7, [ 2,3,4,5 ]]  
numbers = [ 1,2,3,4,5,6,7,8 ]
# puede contener todos los tipos de datos a la vez incluso puede  contener listas, dicionarios, tuplas , listas de listas, listas de diccionarios

numbers.reverse() # hay que dar la instruccion de reverse(), pop(), sort() etc y luego imprimir
print(numbers)
print(to_do) # imprime la lista to_do
print(to_do[::-1]) # imprime la lista to_do desde el ultimo elemento de la lsta hasta el primero usando slices
to_do.reverse() # hace que la lista se imprima desde el ultimo elemento al primero
print(to_do)

del to_do[:2] # puedo borrar todo el elemento o parte de el usando slices [::] 
print(to_do)
print(numbers)

# modificar listas 

a = [1,2,3,4,5,]
b = a
a.append(6)
print(id(a))
print(a)
print(id(b))
print(b)
c = a[:]
print(id(c))
print(c)


