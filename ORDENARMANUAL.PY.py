# ORDENAR UNA FILA ESPECIFICA DE UN ARREGLO
matriz = []
n = int()
fila_seleccionada = int()
#INGRESANDO LOS DATOS A LA MATRIZ POR TECLADO
for i in range (0, 3):
    valor = []
    for j in range (0, 3):
        valor.append(int(input(f"ESCRIBA VALOR PARA LA MATRIZ EL FILA {i}, columna {j} ")))
    matriz.append(valor)


# IMPIENDO EN PANTALLA LA MATRIZ
for i in matriz:
    for j in i:
        print(j, end= "  ")
    print()

#ORDENANDO LA FILA SELECCIONADA
fila_seleccionada = int(input("ESCRIBA FILA A ORDENAR, PARA ESTO OBSERVE LA MATRIZ : "))


#fila_seleccionada = 1  # Índice de la fila que queremos ordenar (en este caso, la segunda fila)

# Accedemos a la fila que queremos ordenar
fila = matriz[fila_seleccionada]

n = len(fila)
for i in range(n):
    for j in range(0, n-i-1):
        if fila[j] > fila[j+1]:
            fila[j], fila[j+1] = fila[j+1], fila[j]

print("Matriz con la fila ordenada usando Bubble Sort:")
for fila in matriz:
    print(fila)

