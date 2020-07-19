def Inicio():
    """ Conversor de Monedas
    
        Este programa permite convertir una cantidad de dinero
        de una divisa a otra.
    """
    opcion = 0

    while opcion == 0:
        print(f'1. Convertir COP a USD')
        print(f'2. Convertir USD a COP')
        opcion = int(input('Escoge el método para conversión de moneda: '))

        if opcion == 1:
            dinero = round(float(input('Cuánto dinero en COP desea convertir: ')), 2)
            trm = round(float(input('Cuánto vale 1 COP en USD: ')), 2)
            cambio = round(conversor(dinero, trm), 2)
            print(f"La cantidad de {dinero} COP en dolares es de {cambio} USD")
        elif opcion == 2:
            dinero = round(float(input('Cuánto dinero en USD desea convertir: ')), 2)
            trm = round(float(input('Cuánto vale 1 USD en COP: ')), 2)
            cambio = round(conversor(dinero, trm), 2)
            print(f"La cantidad de {dinero} USD en dolares es de {cambio} COP") 
        else:
            opcion = 0

def conversor (dinero, trm):
    
    conversion = dinero / trm
    return conversion
   
if __name__ == '__main__':
    Inicio()
