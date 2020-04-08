from collections import defaultdict as dd #biblioteka do dziennika
import random

def ile_liter(slowo):
    zliczacz = dd(lambda:0) #liczy ile dan litera występuje razy na początku dla kazdej litery 0
    for e in slowo:
        zliczacz[e] += 1
    return zliczacz

def czy_ukladalne(slowo1, slowo2):
    zliczacz1 = ile_liter(slowo1)
    zliczacz2 = ile_liter(slowo2)
    for e in slowo1:
        if e not in slowo2 or zliczacz1[e] > zliczacz2[e]:
            return False
    return True

def slowa_ukladalne(slowo):
    wynik = []
    for e in open('popularne_slowa.txt'):
        e = e[:-1] #odcina ostatni znak tutaj enter
        if czy_ukladalne(e, slowo):
            wynik += [e]
    return wynik

def doklejenie(slowo, lista):
    wynik=[]
    slowo = sorted(slowo)
    for e in lista:
        if sorted(e) == slowo:
            wynik += [e]
    return wynik

def pary_wyrazow(slowo, lista):
    wynik=[]
    for poczatek in lista:
        slowo2 = slowo
        for e in poczatek:
            slowo2 = slowo2.replace(e, "", 1) #usuwa pierwsza literke w slowie
        lista2 = slowa_ukladalne(slowo2)
        poczatek2 = poczatek + " " + random.choice(lista2)
        koniec = doklejenie(slowo2, lista)
        if len(koniec) > 0 and len(poczatek) > 0:
            lista.remove(poczatek)
            for a in koniec:
                wynik +=[poczatek2 + " " + a]
    return wynik

imie_nazwisko = input("Podaj imie i nazwisko: ")
imie_nazwisko = imie_nazwisko.replace(" ","") 
lista = slowa_ukladalne(imie_nazwisko) #lista slow ktore sie nadaja
pary = pary_wyrazow(imie_nazwisko, lista)

for para in pary:
    print(para)