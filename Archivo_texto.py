# Escritura de Archivo de Texto
# Crear un nuevo archivo llamado my_notes.txt
with open("my_notes.txt", "w") as Archivo_definicion:
    # Escribir al menos tres líneas de notas personales en el archivo
    Archivo_definicion.write("DEFINCION DE ARCHIVOS EN PYTHON:\n")
    Archivo_definicion.write("Un archivo de texto es un tipo de archivo de computadora que contiene texto sin formato, .\n")
    Archivo_definicion.write("es decir, caracteres legibles por humanos. Los usuarios de computadoras crean, \n")
    Archivo_definicion.write("editan y leen archivos de texto en editores de texto, \n")
    Archivo_definicion.write("que es un software diseñado para la manipulación de texto.  \n")

# Lectura de Archivo de Texto
# Abrir el archivo my_notes.txt
with open("my_notes.txt", "r") as Archivo_definicion:
    # Leer el contenido del archivo línea por línea
    print("============================================================")
    print("Contenido del archivo my_notes.txt:")
    print("============================================================")
    for line in Archivo_definicion:
        # Mostrar en la consola cada línea leída
        print(line.strip())  # Eliminar cualquier espacio en blanco adicional

# Cierre de Archivos
# Asegurarse de cerrar el archivo my_notes.txt después de realizar las operaciones necesarias
# El archivo se cerrará automáticamente gracias al uso del contexto "with"
