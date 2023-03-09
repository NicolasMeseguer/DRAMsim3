# Definir la dirección física inicial y el valor inicial del dato
direccion_fisica_1 = 0x0000
dato = 1
maximo = 5000


# Abrir el archivo para escritura
with open('reads.trace', 'w') as archivo:
    # Generar líneas hasta que el valor del dato sea 2000
    while dato <= maximo:
        # Escribir la línea actual en el archivo
        archivo.write(f'0x{direccion_fisica_1:04x} READ {dato_1}\n')
        
        # Incrementar la dirección física y el valor del dato
        direccion_fisica_1 += 1
        dato_1 += 1

