def buitenste_functie(functie):
    def binnenste_functie():
        print('Binnenste functie gestart')
        result = functie()
        print('buitenste functie gestopt')
        return result
    return binnenste_functie

@buitenste_functie
def toon_hallo():
    print('hallo')

# hallo_func = buitenste_functie(toon_hallo)
toon_hallo()