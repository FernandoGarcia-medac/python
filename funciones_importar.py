# importar el modulo creado
import testeo

# llamar a la funcion del modulo
testeo.holamundofichero()

# llamar a la funcion en sum_mulfichero
suma, multiplicacion = testeo.sum_mulfichero(6, 7)
print(f"Suma: {suma}, Multiplicación: {multiplicacion}")