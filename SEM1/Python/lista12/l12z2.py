from collections import defaultdict as dd

def ppn(slowo):
    slownik = {}
    wynik = ''
    licznik = 0
    for litera in slowo:
        if litera not in slownik.keys():
            licznik += 1
            slownik[litera] = str(licznik)
            wynik = wynik + str(licznik) + '-'
        else:
            wynik = wynik + slownik[litera] + '-'
    return wynik[:-1]

plik = open('slowa.txt')
slowa = dd(set)
zaszyfrowane = dd(set)

for slowo in plik:
    slowo = slowo[:-1] #usuwam ostatnia znak czyli tabulator  [:-1]
    slowa[len(slowo)].add(slowo)

szyfr = dict()

for klucz in slowa:
    for wyraz in slowa[klucz]:
        zaszyfrowane[klucz].add(ppn(wyraz))
        szyfr[ppn(wyraz)] = wyraz


zdanie1 = "fulfolfu ćtąśśótą tlźlźltą"
zdanie2 = "udhufńfd ąuąuęąę yrrożdśś śdśsdtsć"

zdanie1 = zdanie1.split()
haslo=''
for slowo in zdanie1:
    dl = len(slowo)
    slowo = ppn(slowo)
    if slowo in zaszyfrowane[dl]:
        haslo = haslo + szyfr[slowo]
        haslo += ' '

print(haslo)


