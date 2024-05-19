def buitenste_functie(boodschap):
    def binnenste_functie():
        print('Binnenste functie gestart')
        print(boodschap)
        print('Binnenste functie gestopt')
    return binnenste_functie()

hallo_func = buitenste_functie('Wazza')

hallo_func()