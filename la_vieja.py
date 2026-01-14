#import ramdon
matrix = [[None, None, None],
          [None, None, None],
          [None, None, None]]



for row in matrix:
    # Creamos una versión de la fila donde None es " "
    fila_limpia = [" " if x is None else str(x) for x in row]
    
    # Unimos los elementos de esa fila con un espacio o un separador visual
    print("| " + " | ".join(fila_limpia) + " |")
    




columna0 = [fila[0] for fila in matrix]
print(columna0)  # Resultado: [1, 4, 7]


columna1 = [fila[1] for fila in matrix]
print(columna1)

columna2 = [fila[2] for fila in matrix]
print(columna2)


for i in range(len(matrix)):
    print(matrix[i][i])






