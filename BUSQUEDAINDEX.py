# BUSQUEDA D EUN VALOR UTILIZANDO LA FUNCION INDEX
encontrado = bool()
encontrado = False
columna = int()

# CREANDO MATRIZ DE 3 X 3
matriz =[[1,2,3],
         [4,5,6],
         [7,8,9]]

# IMPRESIOND E MATRIZ ORIGINAL
for fila in matriz:
    for columna in fila:
        print(columna, end="  ")
    print()


# INGRESANDO VALOR A BUSCAR
buscar = int(input("escriba valor a buscar : "))

# PROCESO DE BUSQUEDA
for fila in range(len(matriz)):
    if buscar in matriz[fila]:
        columna = matriz[fila].index(buscar)
        encontrado = True
        break
# IMPRIMIENDO LOS RESULTADOS
if encontrado:
    print(f"el valor  buscado {buscar}, esta en la posicion: {fila}, {columna}")
else:
    print("valor no existe")
