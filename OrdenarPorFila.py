# OEDENAR  FILAS DE UNA MATRIZ UTILIZANDO LA FUNCION SORT
columna = 3
fila = 3

# CREANDO MATRIZ DE 3 X 3
matriz =[[90, 80, 70],
         [60 ,10, 40],
         [30, 20, 50]] 
fila_ordenar = int()

# mMOSTRANDO LA  MATRIZ ORIGINAL DE 3 X 3
print("MATRIZ ORIGINAL")
for fila in matriz:
    for columna in fila:
        print(columna, end = " ")
    print()

print("=================================================")
# ORDENANDO LA  MATRIZ ORIGINAL DE 3 X 3
for fila in matriz:
    fila.sort()
print ("ORDENANDO FILAS")
for fila in matriz:
    for columna in fila:
        print(columna, end=" ")
    print()