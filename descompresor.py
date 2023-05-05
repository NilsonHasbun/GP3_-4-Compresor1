import time
import os

archivo_a_eliminar = "descomprimido-elmejorprofesor.txt"

if os.path.exists(archivo_a_eliminar):
    os.remove(archivo_a_eliminar)


def lzw_decompress(file_name):
    # Abrir el archivo comprimido
    with open(file_name, 'r',encoding='utf-8') as f:
        input_data = f.read()
    input_data = input_data.split()
    # Inicializar el diccionario con caracteres ASCII
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    output = []
    string = chr(int(input_data.pop(0)))
    
    # Descomprimir la entrada
    for code in input_data:
        if int(code) in dictionary:
            entry = dictionary[int(code)]
        elif int(code) == next_code:
            entry = string + string[0]
        else:
            raise ValueError("Error de compresión")
        
        output.append(entry)
        dictionary[next_code] = string + entry[0]
        next_code += 1
        string = entry
    
    
    # Escribir la salida en un archivo de texto
    with open('descomprimido-elmejorprofesor.txt', 'w',encoding='utf-8') as f:
        f.write("".join(output))


start_time = time.time()
lzw_decompress('comprimido.elmejorprofesor')
end_time = time.time()

total_time = end_time - start_time
print(f"El tiempo total de ejecución fue de: {total_time:.2f} segundos")