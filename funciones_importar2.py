# importar funciones especificas directamente
from testeo import holamundofichero, sum_mulfichero

# uso de funciones sin prefijar el nombre del modulo
holamundofichero()

suma, multiplicacion = sum_mulfichero(8, 9)
print(f"Suma: {suma}, Multiplicación: {multiplicacion}")