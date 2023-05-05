import time
import os

archivo_a_eliminar = "comprimido.elmejorprofesor"

if os.path.exists(archivo_a_eliminar):
    os.remove(archivo_a_eliminar)

def lzw_compress(file_name):
    # Abrir el archivo de entrada
    with open(file_name, 'r', encoding='utf-8') as f:
        input_data = f.read()
    # Inicializar el diccionario con caracteres ASCII
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    output = []
    string = ""

    # Comprimir la entrada
    for char in input_data:
        
        if string + char in dictionary:
            string = string + char
        else:
            output.append(dictionary[string])
            dictionary[string + char] = next_code
            next_code += 1
            string = char
    
    # Agregar el último código a la salida
    if string in dictionary:
        output.append(dictionary[string])
    
    # Escribir la salida en un archivo comprimido
    with open('comprimido.elmejorprofesor', 'w',encoding='utf-8') as f:
        f.write(" ".join(str(code) for code in output))
        

archivo_comprimir='LaBiblia.txt'
start_time = time.time()
lzw_compress(archivo_comprimir)
end_time = time.time()

total_time = end_time - start_time
print(f"El tiempo total de ejecución fue de: {total_time:.2f} segundos")

sizea = os.path.getsize(archivo_comprimir)
sizeb = os.path.getsize(archivo_a_eliminar)
print(f"El porcentaje total de compresión fue: {(sizea-sizeb)/sizea*100:.2f}%")