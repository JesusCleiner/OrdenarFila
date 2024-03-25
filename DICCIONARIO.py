# Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "MANTA",
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "PORTOVIEJO"

# Agregar una nueva clave-valor representando la profesión
informacion_personal["profesion"] = "Ingeniero"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-7890"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario resultante
print("Diccionario final:")
print(informacion_personal)