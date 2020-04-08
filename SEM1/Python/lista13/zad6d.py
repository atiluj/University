'''def maksymalny_skok(D):
    maks = 0 
    lista_kluczy = D.keys()
    for klucz in lista_kluczy:
        roznica = klucz -D[klucz]
        if abs(roznica > maks):
            maks = abs(roznica)
            odp = klucz
    return odp'''

def pomocnicza(D):
    return max([abs(x -D[x]) for x in D.keys()])
def maksymalny_skok(D):
    return [x for x in D.keys() if abs(x - D[x]) == pomocnicza(D)]#[0]

D = {1:3, 5:-5, 3:7, 15:-10}
print(maksymalny_skok(D))


