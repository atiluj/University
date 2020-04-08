from collections import defaultdict as dd

file = open('grzyby.txt')   #zad4a
ranking = dd(list)
for line in file:
    linijka = line.split(" ")
    for i in range(1, len(linijka)-1):
        waga = linijka[i]
        ranking[linijka[0]].append(waga)

raport = dict()          #zad4b
for osoba in ranking:
    suma = 0
    for grzyb in ranking[osoba]:
        suma += float(grzyb)
    raport[osoba] = suma

wynik = []
for i in raport:
    wynik.append((raport[i],i))
wynik.sort(reverse=True)


oszust = dict()          #zad4c
for osoba in ranking:
    oszust[osoba] = len(ranking[osoba]) - len(set(ranking[osoba]))


print('zad4a')
print(ranking)
print('zad4b')
print(wynik)
print('zad4c')
print(oszust)
for i in oszust:
    if oszust[i] == max(oszust.values()):
        print(i)
        