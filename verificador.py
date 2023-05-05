# Nombre del archivo original
archivo_original = "LaBiblia.txt"

# Nombre del archivo comprimido
archivo_descomprimido = "descomprimido-elmejorprofesor.txt"


with open(archivo_original, "rb") as f1, open(archivo_descomprimido, "rb") as f2:
    contenido_original = f1.read()
    contenido_descomprimido = f2.read()

print(contenido_original[0])
print(contenido_descomprimido[0])
print(contenido_original[1])
print(contenido_descomprimido[1])
# Comparar contenido de ambos archivos
if contenido_original == contenido_descomprimido:
    print("El archivo original y su archivo comprimido y descomprimido son iguales.")
else:
    print("El archivo original y su archivo comprimido y descomprimido son diferentes.")
    