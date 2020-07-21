
def es_primo(numero):
    # contador = 0

    # for i in range(1, numero + 1):
    #     if i == 1 or i == numero:
    #         continue
    #     elif numero % i == 0:
    #         contador += 1
    # if contador == 0:
    #     return True
    # else:
    #     return False

    if numero % 2 == 0 or numero % 3 == 0:
        return False
    else: 
        return True
        

def main():
    numero = int(input('Escribe un número: '))
    if es_primo(numero): #si es True entonces no requiere == True
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    main()