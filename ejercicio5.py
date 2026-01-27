#Caso práctico 1: “El número entero mayor y menor de una lista”
lista = [1, 2, "árbol", 5, 1.5, 6, "a"]
numeros_enteros = []
for elemento in lista:
    if isinstance(elemento, int):
        numeros_enteros.append(elemento)
if numeros_enteros:
    mayor = max(numeros_enteros)
    menor = min(numeros_enteros)
    print(f"El número entero mayor es: {mayor}")
    print(f"El número entero menor es: {menor}")