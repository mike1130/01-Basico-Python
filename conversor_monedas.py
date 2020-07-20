def Inicio():
    """ Conversor de Monedas
    
        Este programa permite convertir una cantidad de dinero
        de una divisa a otra.
    """
    menu = """
    Bienvenido al conversor de monedas 💰

    1 - Pesos colombianos
    2 - Pesos argentinos
    3 - Pesos mexicanos

    Elige una opción: """

    opcion = int(input(menu))
    
    
    if opcion == 1:
        moneda = 'pesos colombianos'
        cambio = conversor(moneda)
        print(f"La cantidad de {cambio[1]} {moneda} en dólares es de {cambio[0]} USD")
    elif opcion == 2:
        moneda = 'pesos argentinos'
        cambio = conversor(moneda)
        print(f"La cantidad de {cambio[1]} {moneda} en dólares es de {cambio[0]} USD")
    elif opcion == 3:
        moneda = 'pesos mexicans'
        cambio = conversor(moneda)
        print(f"La cantidad de {cambio[1]} {moneda} en dólares es de {cambio[0]} USD")
    else:
        pass

def conversor (moneda):
    pesos = round(float(input(f'Cuánto dinero en {moneda} desea convertir a dólares: ')), 2)
    trm = round(float(input(f'Cuánto vale 1 USD en {moneda}: ')), 2)

    conversion = round(pesos / trm, 2)
    return conversion, pesos
   
if __name__ == '__main__':
    Inicio()
