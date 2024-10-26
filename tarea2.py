class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio
    
    def obtener_precio(self):
        return self._precio  
    
    def mostrar_info(self):
        return f"Producto: {self._nombre}, Precio: {self._precio}"

class Ropa(Producto):
    def __init__(self, nombre, precio, talla, color):
        super().__init__(nombre, precio)
        self.talla = talla
        self.color = color
    
    def mostrar_info(self):
        info = super().mostrar_info()
        return f"{info}, Talla: {self.talla}, Color: {self.color}"

class Blusa(Ropa):
    def __init__(self, precio, talla, color, tela):
        super().__init__("Blusa", precio, talla, color)
        self.tela = tela
    
    def mostrar_info(self):
        info = super().mostrar_info()
        return f"{info}, Tipo de Tela: {self.tela}"

class Falda(Ropa):
    def __init__(self, precio, talla, color, tela):
        super().__init__("Falda", precio, talla, color)
        self.tela = tela
    
    def mostrar_info(self):
        info = super().mostrar_info()
        return f"{info}, Tipo de Tela: {self.tela}"

class Zapato(Ropa):
    def __init__(self, precio, talla, color, tipo):
        super().__init__("Zapato", precio, talla, color)
        self.tipo = tipo
    
    def mostrar_info(self):
        info = super().mostrar_info()
        return f"{info}, Tipo de Zapato: {self.tipo}"

class Carrito:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_carrito(self):
        print("Productos adquiridos:")
        total = 0
        for producto in self.productos:
            print(producto.mostrar_info())
            total += producto.obtener_precio()
        print(f"Total a pagar: {total}")

class Tienda:
    def __init__(self):
        self.carrito = Carrito()
        self.productos_disponible = [
            Blusa(precio=22.00, talla="P", color="Rosado", tela="Algodon"),
            Falda(precio=28.00, talla="P", color="Blanco", tela="Algodon"),
            Zapato(precio=50.00, talla=36, color="Blanco", tipo="Deportivo")
        ]

    def mostrar_menu(self):
        print("Bienvenido a la Tienda de Ropa")
        while True:
            print("Productos disponibles:")
            for i, producto in enumerate(self.productos_disponible, start=1):
                print(f"{i}. {producto.mostrar_info()}")
            print(f"{len(self.productos_disponible) + 1}. Finalizar compra")
            
            try:
                opcion = int(input("Seleccione el número del producto que desea agregar al carrito: "))
                if opcion == len(self.productos_disponible) + 1:
                    break
                elif 1 <= opcion <= len(self.productos_disponible):
                    producto_seleccionado = self.productos_disponible[opcion - 1]
                    self.carrito.agregar_producto(producto_seleccionado)
                    print(f"{producto_seleccionado._nombre} agregado al carrito.")
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Por favor ingrese un número válido.")
        
        self.carrito.mostrar_carrito()



if __name__ == "__main__":
    tienda = Tienda()
    tienda.mostrar_menu()

  