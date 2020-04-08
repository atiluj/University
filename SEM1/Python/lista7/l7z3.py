def zle_slowo(slowo):
    return any(znak in slowo for znak in '/-.:;!?') #dla kazdego znaku w slowie jesli nie zawiera !/-;:,. to zwróć |all

def waga(slowo):
    liczba_wystapien = lista.count(slowo)
    dlugosc = len(slowo)
    return liczba_wystapien * (dlugosc**alfa)

plik = open('Lalka.txt').read()
alfa = 3
lista = [slowo for slowo in plik.split() if not zle_slowo(slowo)]
slowa = set(lista)
slowa = sorted(slowa, key = waga) #najwieksza waga jest teraz na samym koncu
for i in range(len(slowa)-1,len(slowa)-11,-1):
    print(slowa[i])
