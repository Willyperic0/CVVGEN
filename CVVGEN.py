#!/usr/bin/env python3
print("\033[36m" +r"""
  ______     ____     ______ _____ _   _ 
 / ___\ \   / /\ \   / / ___| ____| \ | |
| |    \ \ / /  \ \ / / |  _|  _| |  \| |
| |___  \ V /    \ V /| |_| | |___| |\  |
 \____|  \_/      \_/  \____|_____|_| \_|
""""\033[0m")


# Solicitamos los valores al usuario, asegurándonos de que solo contengan números
xx = input("Ingresa el valor para XXXXXXXXXXXXXXXX (16 dígitos numéricos): ")
while len(xx) != 16 or not xx.isdigit():  # Verificamos que sea de 16 dígitos y numérico
    print("El valor de XXXXXXXXXXXXXXXX debe tener exactamente 16 dígitos y ser numérico.")
    xx = input("Ingresa el valor para XXXXXXXXXXXXXXXX (16 dígitos numéricos): ")

dd = input("Ingresa el valor para DD (números): ")
while not dd.isdigit():  # Verificamos que dd sea numérico
    print("El valor de DD debe ser numérico.")
    dd = input("Ingresa el valor para DD (números): ")

yy = input("Ingresa el valor para YY (números): ")
while not yy.isdigit():  # Verificamos que yy sea numérico
    print("El valor de YY debe ser numérico.")
    yy = input("Ingresa el valor para YY (números): ")

# Creamos el archivo con las 1000 líneas
with open("archivo_generado.txt", "w") as file:
    for i in range(1000):
        # Escribimos cada línea con el formato proporcionado
        file.write(f"{xx}|{dd}|{yy}|{i:03}\n")

print("Archivo generado exitosamente.")