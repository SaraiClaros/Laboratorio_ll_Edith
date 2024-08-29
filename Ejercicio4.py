# Clase para representar un dispositivo electrónico
class DispositivoElectronico:
    def __init__(self, tipo, modelo, almacenamiento, ram, procesador, precio_compra):
        self.marca = "PHR"  # Todos los dispositivos son de la marca PHR
        self.tipo = tipo
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.ram = ram
        self.procesador = procesador
        self.precio_compra = precio_compra
        # Calcula el precio de venta al momento de la creación
        self.precio_venta = self.calcular_precio_venta()
    
    def calcular_precio_venta(self):
        # Calcula el precio de venta con un margen del 70% sobre el precio de compra
        return self.precio_compra * 1.7
    
    def mostrar_informacion(self):
        # Imprime toda la información del dispositivo
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Modelo: {self.modelo}")
        print(f"Almacenamiento: {self.almacenamiento} GB")
        print(f"RAM: {self.ram} GB")
        print(f"Procesador: {self.procesador}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")

# Función para registrar un nuevo dispositivo
def registrar_dispositivo():
    tipo = input("Ingrese el tipo de dispositivo (celular/tablet/portátil): ")
    modelo = input("Ingrese el modelo del dispositivo: ")
    almacenamiento = int(input("Ingrese el almacenamiento del dispositivo (en GB): "))
    ram = int(input("Ingrese la RAM del dispositivo (en GB): "))
    procesador = input("Ingrese el tipo de procesador del dispositivo: ")
    precio_compra = float(input("Ingrese el precio de compra del dispositivo: "))

    # Crea una instancia de DispositivoElectronico con los datos ingresados
    dispositivo = DispositivoElectronico(tipo, modelo, almacenamiento, ram, procesador, precio_compra)
    return dispositivo

# Función principal que coordina el registro y visualización de dispositivos
def main():
    print("Registro de dispositivos electrónicos en el almacén")
    dispositivos = []  # Lista para almacenar los dispositivos registrados
    
    while True:
        dispositivo = registrar_dispositivo()  # Registra un nuevo dispositivo
        dispositivos.append(dispositivo)  # Agrega el dispositivo a la lista de dispositivos

        # Pregunta al usuario si desea registrar otro dispositivo
        continuar = input("¿Desea registrar otro dispositivo? (s/n): ")
        if continuar.lower() != 's':
            break  # Sale del bucle si la respuesta no es 's'
    
    # Imprime encabezado y muestra información de todos los dispositivos registrados
    print("\n_________________________________________________________________________")
    print("_________________________________________________________________________")
    print("_________________________________________________________________________")

    print("\nDispositivos registrados:")
    for dispositivo in dispositivos:
        dispositivo.mostrar_informacion()  # Muestra la información de cada dispositivo registrado
        print("-" * 30)

# Verifica si el script está siendo ejecutado directamente
if __name__ == "__main__":
    main()
