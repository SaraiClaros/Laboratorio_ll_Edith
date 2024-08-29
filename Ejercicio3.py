# Clase para representar un auto en el concesionario
class Auto:
    def __init__(self, marca, modelo, tipo, motor, año, puertas, ruedas, pasajeros, color, precio_compra):
        # Inicializa los atributos del auto
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.motor = motor
        self.año = año
        self.puertas = puertas
        self.ruedas = ruedas
        self.pasajeros = pasajeros
        self.precio_compra = precio_compra
        self.color = color
        # Calcula el precio de venta al momento de la creación
        self.precio_venta = self.calcular_precio_venta()
    
    def calcular_precio_venta(self):
        # Calcula el precio de venta con un margen del 40% sobre el precio de compra
        return self.precio_compra * 1.4
    
    def mostrar_informacion(self):
        # Imprime toda la información del auto
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Tipo: {self.tipo}")
        print(f"Motor: {self.motor}")
        print(f"Año: {self.año}")
        print(f"Puertas: {self.puertas}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Pasajeros: {self.pasajeros}")
        print(f"Color: {self.color}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")

# Función para registrar un nuevo auto
def registrar_auto():
    # Solicita datos del auto al usuario
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    tipo = input("Ingrese el tipo de auto (nacional/importado): ")
    motor = input("Ingrese el tipo de motor (gasolina/diésel/eléctrico): ")
    año = int(input("Ingrese el año del auto: "))
    puertas = int(input("Ingrese el número de puertas: "))
    ruedas = 4  # Todos los autos tienen 4 ruedas
    pasajeros = 5  # Todos los autos tienen capacidad para 5 pasajeros
    color = input("Ingrese el color del auto: ")
    precio_compra = float(input("Ingrese el precio de compra del auto: "))
    
    # Crea una instancia de Auto con los datos ingresados
    auto = Auto(marca, modelo, tipo, motor, año, puertas, ruedas, pasajeros, color, precio_compra)
    return auto

# Función principal que coordina el registro y visualización de autos
def main():
    print("Registro de autos en el concesionario")
    autos = []  # Lista para almacenar los autos registrados
    
    while True:
        auto = registrar_auto()  # Registra un nuevo auto
        autos.append(auto)  # Agrega el auto a la lista de autos

        # Pregunta al usuario si desea registrar otro auto
        continuar = input("¿Desea registrar otro auto? (s/n): ")
        if continuar.lower() != 's':
            break  # Sale del bucle si la respuesta no es 's'
    
    # Imprime encabezado y muestra información de todos los autos registrados
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("\nAutos registrados:")
    for auto in autos:
        auto.mostrar_informacion()  # Muestra la información de cada auto registrado
        print("-" * 30)

# Verifica si el script está siendo ejecutado directamente
if __name__ == "__main__":
    main()
