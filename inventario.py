def agregar_producto(inventario, nombre, precio, cantidad):
    """Si el producto no existe, lo agrega. Si ya existe, le suma la cantidad."""
    nombre = nombre.lower()
    if nombre in inventario:
        inventario[nombre]["cantidad"] += cantidad
    else:
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}

def eliminar_producto(inventario, nombre):
    """Elimina el producto. Si no existe, muestra un mensaje que lo indique."""
    nombre = nombre.lower()
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado exitosamente.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

def listar_productos(inventario):
    """Imprime todos los productos con su precio y cantidad."""
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\n--- LISTADO DE INVENTARIO ---")
        for nombre, datos in inventario.items():
            print(f"Producto: {nombre.capitalize()} | Precio: ${datos['precio']} | Cantidad: {datos['cantidad']}")
        print("-" * 30)

# Bloque de prueba independiente (solo se ejecuta al correr este archivo directamente)
if __name__ == "__main__":
    inventario_prueba = {
        "lapiz": {"precio": 1.5, "cantidad": 100},
        "cuaderno": {"precio": 4.0, "cantidad": 30}
    }
    
    print("Estado inicial:")
    listar_productos(inventario_prueba)
    
    print("\nAgregando existencia a 'lapiz' (+50):")
    agregar_producto(inventario_prueba, "lapiz", 1.5, 50)
    
    print("Agregando producto nuevo 'borrador':")
    agregar_producto(inventario_prueba, "borrador", 0.75, 40)
    
    listar_productos(inventario_prueba)
    
    print("\nEliminando producto 'regla' (inexistente):")
    eliminar_producto(inventario_prueba, "regla")
    
    print("\nEliminando producto 'cuaderno':")
    eliminar_producto(inventario_prueba, "cuaderno")
    
    listar_productos(inventario_prueba)
