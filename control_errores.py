try:
    #instrucciones (10/0) ("a"*2) (2+2) ("a"+2)
    ("a"+2) 
except ArithmeticError as error:
    print("Se ha producido un error aritmetico", str(error))

except Exception as error:
    #captura cualquier otro error
    print("Se ha producido un error", str(error))

else:
    #entra aqui si no se ha producido ningun error
    print("El bloque de instrucciones se ha ejecutado correctamente")