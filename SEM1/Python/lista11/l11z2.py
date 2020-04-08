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

print(ppn('tak'))
print(ppn('nie'))
print(ppn('mama'))
print(ppn('python'))