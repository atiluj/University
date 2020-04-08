from losowanie_fragmentow import losuj_fragment

def losuj_haslo(n):
    wynik = ""
    while len(wynik) < n:
        slowo=losuj_fragment()
        if(len(wynik)+len(slowo) <= n) and (len(wynik)+len(slowo) != n-1):
            wynik+=slowo
    return wynik

print("Haslo o dlugosci 8: ")
for i in range(10):
    print(losuj_haslo(8))


print("Hasło o dlugosci 12: ")
for i in range(10):
    print(losuj_haslo(12))