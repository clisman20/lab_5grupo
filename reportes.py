# reportes.py
# Integrante B: reportes del inventario usando comprension de listas


def stock_bajo(inventario, limite):
    # lista con los nombres de los productos que tienen menos cantidad que el limite
    bajos = [nombre for nombre in inventario if inventario[nombre]["cantidad"] < limite]
    return bajos


def valor_total(inventario):
    # se calcula precio * cantidad de cada producto y luego se suman
    valores = [inventario[nombre]["precio"] * inventario[nombre]["cantidad"] for nombre in inventario]
    return sum(valores)


def nombres_en_mayuscula(inventario):
    # lista con los nombres en mayuscula, ordenada alfabeticamente
    nombres = [nombre.upper() for nombre in inventario]
    nombres.sort()
    return nombres


if __name__ == "__main__":
    prueba = {
        "lapiz": {"precio": 1.5, "cantidad": 100},
        "cuaderno": {"precio": 4.0, "cantidad": 30},
        "regla": {"precio": 2.0, "cantidad": 5},
    }

    print("Stock bajo:", stock_bajo(prueba, 10))
    print("Valor total:", valor_total(prueba))
    print("Nombres en mayuscula:", nombres_en_mayuscula(prueba))
