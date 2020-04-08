from duze_cyfry import daj_cyfre

def zapis(lista):
    dl=len(lista)
    wynik=[]
    for i in range(dl):
        wynik=wynik + [daj_cyfre(lista[i])]
    return wynik

def wypisz(wynik):
    for i in range(5):
        for j in range(len(wynik)):
            print(wynik[j][i], end = " ")
        print()

liczba=input("Podaj liczbe: ")
lista=[int(n) for n in liczba]
wypisz(zapis(lista))