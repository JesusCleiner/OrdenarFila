#
matriz =[]
encontrado = bool()
encontrado = False
busqueda  = int()

# INGRESO DE VALORES POR TECLADO
for i in range(0, 3):
    valor = []
    for j in range(0, 3):
        valor.append(int(input(f"ESCRIBA VALOR PARA LA MATRIZ fila {i} columna {j} : ")))
    matriz.append(valor)

# IMPRESION DE LA MATRIZ
for i in matriz:
    for j in i:
        print(j, end = " ")
    print()

# BUSQUEDA DEL VALOR INGRESADO
busqueda = int(input("ESCRIBA VALOR A BUSCAR ===>"))
for i in range(0, 3):
    for j in range(0, 3):
        if matriz[i][j] == busqueda:
            print(f"el valor {busqueda} esta en la posicion, fila {i}, columna {j}")
            encontrado = True
            break
    if encontrado:
        break
if not encontrado:
    print("valor no existe")