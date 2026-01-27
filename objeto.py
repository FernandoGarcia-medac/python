# definicion de la clase

class DatosUsuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def escribir_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
    
#crear un objeto de la clase
usuario = DatosUsuario("Ana", 30)

#llamar al metodo para escribir los datos
usuario.escribir_datos()