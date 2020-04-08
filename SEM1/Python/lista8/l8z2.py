from collections import defaultdict as dd #przypisanie do czegos wartosci

def wystapienie_liter(slowo):
    zliczacz = dd(lambda:0)
    for e in slowo:
        zliczacz[e] +=1
    return zliczacz

def ukladalne(slowo1,slowo2):
    zliczacz1 = wystapienie_liter(slowo1)
    zliczacz2 = wystapienie_liter(slowo2)
    for e in slowo1:
        if e not in slowo2 or zliczacz1[e] > zliczacz2[e]:
            return "nie jest ukladalne"
    return "jest ukladalne"

slowo1 = input('Podaj slowo1: ')
slowo2 = input('Podaj slowo2: ')

print(ukladalne(slowo1,slowo2))