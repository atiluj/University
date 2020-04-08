from collections import defaultdict as dd

alfabet = dd(lambda : 0)
licznik = 1
for element in "aąbcćdeęfghijklłmnńoóprstuwyzźż":
    alfabet[element] = licznik
    licznik += 1

litery = "aąbcćdeęfghijklłmnńoóprstuwyzźż"

def ceasar(slowo,k):
    wynik = ""
    for element in slowo:
        wartosc = alfabet[element]
        wynik += litery[(wartosc + k) % len(litery) - 1]
    return wynik

slowo = input("Podaj slowo:")
k = int(input("Podaj k: "))
print(ceasar(slowo,k))