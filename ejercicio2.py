#Escribe un programa en Python que imprima todos
#  los números del 0 al 100 que sean divisibles por 5.
for numero in range(0, 101):
    if numero % 5 == 0:
        print(numero)
