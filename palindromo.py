def palindromo(palabra):
    n_palabra = palabra.replace(' ','').upper()
    
    if n_palabra[::] == n_palabra[::-1]:
        return True
    else:
        return False

def main():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print(f'{palabra} es palíndromo')
    else:
        print(f'{palabra} NO es palíndromo')


if __name__ == '__main__':
    main()