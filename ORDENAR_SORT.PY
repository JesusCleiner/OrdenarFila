# OEDENAR UNA FILA DE UNA MATRIZ UTILIZANDO LA FUNCION SORT
encontrado = bool()
encontrado = False

# CREANDO MATRIZ DE 3 X 3
matriz =[[70, 80, 90],
         [60 ,10, 40],
         [30, 20, 50]] 
fila_ordenar = int()

# MOSTRANDO LA  MATRIZ ORIGINAL DE 3 X 3
for fila in matriz:
    for columna in fila:
        print(columna, end= " ")
    print()

# ORDENANDO LA FILA SELECCIONADA
fila_ordenar= int(input("ESCRIBA LA FILA A ORDENAR : "))
if (fila_ordenar >= 0) and (fila_ordenar <= len(matriz)):
    matriz[fila_ordenar] = sorted(matriz[fila_ordenar])
    for fila in matriz:
        for columna in fila:
            print(columna, end= " ")
        print()
