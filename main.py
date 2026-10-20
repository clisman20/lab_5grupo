#Integrante C... "menu"

from inventario import agregar_producto, eliminar_producto, listar_productos
from reportes import ver_stock_bajo, ver_valor_total, ver_nombres_mayuscula

def mostrar_menu():
    print("\n--- MENÚ DE GESTIÓN DE INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Listar productos")
    print("4. Ver productos con stock bajo")
    print("5. Ver valor total")
    print("6. Ver nombres en mayúscula")
    print("7. Salir")

inventario = {
"lapiz": {"precio": 1.5, "cantidad": 100},
"cuaderno": {"precio": 4.0, "cantidad": 30},
"regla": {"precio": 2.0, "cantidad": 5},
}

# 3. Menú con ciclo while
while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-7): ").strip()

        if opcion == "1":
            inventario = agregar_producto(inventario)

        elif opcion == "2":
            inventario = eliminar_producto(inventario)

        elif opcion == "3":
            listar_productos(inventario)

        elif opcion == "4":
            ver_stock_bajo(inventario)

        elif opcion == "5":
            ver_valor_total(inventario)

        elif opcion == "6":
             ver_nombres_mayuscula(inventario)
            

        elif opcion == "7":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("opcion no valida bro")

if __name__ == "__main__":
    mostrar_menu()
     


           

