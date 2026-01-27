#Definimos una funcion 
def suma(a, b):
    resultado = a + b
    return resultado

numero1 = 5
numero2 = 10

print(f"La suma de {numero1} y {numero2} es: {suma(numero1, numero2)}")

def sum_mul(num1, num2):
    return num1+num2, num1*num2

sum, mul = sum_mul(3,4)

print(sum)
print(mul)