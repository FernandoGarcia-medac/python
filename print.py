# PRINT
#print(<obj>,...<obj>) si algun elemento no es string lo convierte automaticamente
nombre = "Fernando"
apellido = "Garcia"
edad = 21

print("Nombre: " + nombre, apellido)
print("Edad: ", 25)

#parametros sep, end
print("Hola ","adios", sep="---", end="---\n")

#Formato
#Desde python 3.6 se introdujo lo que informalmente se llama f-strings
#Permite usar expresiones directamente dentro del string
#cada trozo del string que este dentro de llaves {} sera trataado como una expresion

cantidad = 4
fruta = "manzanas"
precio = 2.9

print(f"El coste de {cantidad} {fruta} es {precio}€", 
      f"por lo que {int(cantidad/2)} costarian {precio/2}€")

print(type(fruta), type(precio))

op1 = int(input("Operando 1: "))
op2 = int(input("Operando 2: "))
print(op1 + op2)
#print(op1 * op2)