def saludo():
    print('---------------------------')
    print('Conoce que año es bisiesto')
    print('---------------------------')
    return

def datos():
    year = int(input('Introduzca el año que desea consultar: '))
    return year

def algBisiesto(year):
    if year/4 == int(year/4):
        if year/100 == int(year/100):                        #numeros para testear salidas
            if year/400 == int(year/400):                    #2000, 2100, 2020, 2025
                print(f'---> El año {year} es bisiesto')
            else:
                print(f'---> El año {year} NO es bisiesto')
        else:
            print(f'---> El año {year} es bisiesto')
    else:
        print(f'---> El año {year} NO es bisiesto')

    return 

# main section
saludo()
year = datos()
algBisiesto(year)