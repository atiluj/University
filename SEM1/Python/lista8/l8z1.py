import random
from collections import defaultdict as dd #przypisanie do czegos wartosci

pol_ang = {} 

#
czestotliwosc = [] #dziennik dla kazdego wiersza do slowa przypisuje ilosc wystpaien
for wiersz in open('korpus.txt'):
    czestotliwosc += wiersz.split()

zliczacz = dd(lambda:0) #liczy ilosc wystapień

for a in czestotliwosc:
    zliczacz[a] += 1
       
def najczestrzy(lista):
    maksimum = 0
    for wyraz in lista:
        if maksimum < zliczacz[wyraz]:
            maksimum = zliczacz[wyraz]
            slowo = wyraz
    return slowo

def tlumacz(zdanie):
    wynik = []
    for w in zdanie:
        if w in pol_ang:
            wynik.append(najczestrzy(pol_ang[w])) #pola_ang[w] zwraca liste slow po ang i najczestrze zwraca najczestsze
        else:
            wynik.append('[?]')
    return ' '.join(wynik)
    
for wiersz in open('pol_ang.txt'):
    wiersz = wiersz.strip() #strip - usuwa pusty znak
    if '=' not in wiersz:
        continue
    pola = wiersz.split('=')
    if len(pola) != 2:
        continue
    p, a = pola
    if p in pol_ang:
        pol_ang[p].append(a)
    else:
        pol_ang[p] = [a]    
    
zdanie = input("podaj zdanie: ")
zdanie = zdanie.split()
print (tlumacz(zdanie))