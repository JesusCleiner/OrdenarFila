# factura punto de venta

# FUNCION PARA LA GENERACION DE FACTURA DE VENTA
Valor_imponible = 0
def ventas():
    subtotal = float()
    bandera = bool
    cantidad = 0
    precio = 0
    subtotal = 0
    imponible = 0
    bandera = True
    while bandera:
        print("===========================================")
        print("<1>  BOTELLAS PET 300ML")
        print("<2>  BOTELLAS PET 400ML")
        print("<3>  BOTELLAS PET 500ML")
        print("<4>  BOTELLAS PET 1000ML")
        print("<5>  TAPAS 28MM")
        print("===========================================")
        opcion = int(input("Escoja opción : "))
        match opcion:
            case 1:
                cantidad = int(input("indique cantidad a vender de botellas de 300ml : "))
                precio = float(input("indique el precio de la unidad : "))
                subtotal = cantidad * precio
                imponible += subtotal 
                
            case 2:
                cantidad = int(input("indique cantidad a vender de botellas de 400ml : "))
                precio = float(input("indique el precio de la unidad : "))
                subtotal = cantidad * precio
                imponible += subtotal
                
            case 3:
                cantidad = int(input("indique cantidad a vender de botellas de 500ml : "))
                precio = float(input("indique el precio de la unidad : "))
                subtotal = cantidad * precio
                imponible += subtotal 
                
            case 4:
                cantidad = int(input("indique cantidad a vender de botellas de 1000ml : "))
                precio = float(input("indique el precio de la unidad : "))
                subtotal = cantidad * precio
                imponible += subtotal 
                
            case 5:
                cantidad = int(input("indique cantidad a vender de tapas 28mm : "))
                precio = float(input("indique el precio de la unidad : "))
                subtotal = cantidad * precio
                imponible += subtotal 
                
        continuar = str(input("continua vendiendo s/n : "))
        if (continuar == "N") or (continuar == "n"):
            return(imponible)
            break 

def Descuento_venta(imponible):
    subtotal_factura = 0
    Subtotal = 0
    Subtotal = imponible
    monto_descontar = 0
    print("================================================")
    Descuento = float(input("Escriba porcentaje de Descuento : "))
    monto_descontar = ((Subtotal * Descuento) / 100) 
    subtotal_factura = Subtotal - monto_descontar
    total_final = subtotal_factura * 1.12
    print("================================================")
    print("EL SUBTOTAL A PAGAR ES : ",    Subtotal)
    print(f"EL {Descuento},% DE DESCUENTO ES  :  {monto_descontar}")
    print("EL SUBTOTAL ANTE DE IVA ES  :",   subtotal_factura)
    print("EL VALOR REAL A PAGAR ES  :",     total_final)
    print("================================================")


Valor_imponible = ventas()

Descuento_venta(Valor_imponible)




