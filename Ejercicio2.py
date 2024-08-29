def registrar_articulo():

    # Entrada del Tipo de Artículo: 
    tipo = input("Ingrese el tipo de artículo (cuaderno/lapiz): ").strip().lower()
    
    if tipo not in ["cuaderno", "lapiz"]:
        print("Tipo de artículo no válido. Intente de nuevo.")
        return None
     # Registro de Detalles Específicos:
    detalles = {}
    
    if tipo == "cuaderno":
        detalles['hojas'] = input("Número de hojas (50/100): ").strip()
        detalles['marca'] = "HOJITAS"
    elif tipo == "lapiz":
        detalles['tipo'] = input("Tipo de lápiz (grafito/colores): ").strip().lower()
        detalles['marca'] = "RAYAS"
    
    # Cálculo de Precios

    precio_compra = float(input("Ingrese el precio de compra: $"))
    precio_venta = round(precio_compra * 1.30, 2)

    # Devolución del Artículo Registrado

    return {
        'tipo': tipo,
        'detalles': detalles,
        'precio_compra': precio_compra,
        'precio_venta': precio_venta
    }

def mostrar_articulos(articulos):
    print("------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------")
    print("\nArtículos registrados:")
    for idx, articulo in enumerate(articulos, 1):
        print(f"Artículo {idx}:")
        print(f"Tipo: {articulo['tipo'].capitalize()}")
        if articulo['tipo'] == "cuaderno":
            print(f"Hojas: {articulo['detalles']['hojas']}")
        elif articulo['tipo'] == "lapiz":
            print(f"Tipo de lápiz: {articulo['detalles']['tipo']}")
        print(f"Marca: {articulo['detalles']['marca']}")
        print(f"Precio de Compra: ${articulo['precio_compra']}")
        print(f"Precio de Venta: ${articulo['precio_venta']}")
        print("-" * 30)

def main():
    # Inicialización y Registro de Artículos
    articulos = []
    
    while True:
        articulo = registrar_articulo()
        if articulo:
            articulos.append(articulo)
        
        continuar = input("¿Desea registrar otro artículo? (si/no): ").strip().lower()
        if continuar != 'si':
            break
    
    mostrar_articulos(articulos)

if __name__ == "__main__":
    main()
