# Definir la dirección física inicial y el valor inicial del dato
direccion_fisica_1 = 0x0000
direccion_fisica_2 = 0xa000
direccion_fisica_3 = 0x10000
direccion_fisica_4 = 0x1a000
direccion_fisica_5 = 0x20000
direccion_fisica_6 = 0x2a000
direccion_fisica_7 = 0x30000
direccion_fisica_8 = 0x3a000
dato = 1


# Abrir el archivo para escritura
with open('reads_8.trace', 'w') as archivo:
    # Generar líneas hasta que el valor del dato sea 2000
    while dato <= 5000:
        # Escribir la línea actual en el archivo
        archivo.write(f'0x{direccion_fisica_1:04x} READ {dato}\n')
        
        # Incrementar la dirección física y el valor del dato
        direccion_fisica_1 += 1
        dato += 1
    
    dato = 1
    while dato <= 5000:
        # Escribir la línea actual en el archivo
        archivo.write(f'0x{direccion_fisica_2:04x} READ {dato}\n')
        
        # Incrementar la dirección física y el valor del dato
        direccion_fisica_2 += 1
        dato += 1
    
    dato = 1
    while dato <= 5000:
        # Escribir la línea actual en el archivo
        archivo.write(f'0x{direccion_fisica_3:04x} READ {dato}\n')
        
        # Incrementar la dirección física y el valor del dato
        direccion_fisica_3 += 1
        dato += 1
    
    dato = 1
    while dato <= 5000:
        # Escribir la línea actual en el archivo
        archivo.write(f'0x{direccion_fisica_4:04x} READ {dato}\n')
        
        # Incrementar la dirección física y el valor del dato
        direccion_fisica_4 += 1
        dato += 1
    
    dato = 1
    while dato <= 5000:
        # Escribir la línea actual en el archivo
        archivo.write(f'0x{direccion_fisica_5:04x} READ {dato}\n')
        
        # Incrementar la dirección física y el valor del dato
        direccion_fisica_5 += 1
        dato += 1
    
    dato = 1
    while dato <= 5000:
        # Escribir la línea actual en el archivo
        archivo.write(f'0x{direccion_fisica_6:04x} READ {dato}\n')
        
        # Incrementar la dirección física y el valor del dato
        direccion_fisica_6 += 1
        dato += 1
    
    dato = 1
    while dato <= 5000:
        # Escribir la línea actual en el archivo
        archivo.write(f'0x{direccion_fisica_7:04x} READ {dato}\n')
        
        # Incrementar la dirección física y el valor del dato
        direccion_fisica_7 += 1
        dato += 1
    
    dato = 1
    while dato <= 5000:
        # Escribir la línea actual en el archivo
        archivo.write(f'0x{direccion_fisica_8:04x} READ {dato}\n')
        
        # Incrementar la dirección física y el valor del dato
        direccion_fisica_8 += 1
        dato += 1

