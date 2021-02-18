from ulamki import *

#testowanie funkcji zwracajacych ulamki 

licznik = 2
mian1 = 4
mian2 = 6

ulamek = ulamek_wlasciwy(licznik, mian1)
ulamek2 = ulamek_wlasciwy(licznik, mian2)

dod = dodaj(ulamek, ulamek2)
od = odejmij(ulamek, ulamek2)
pomn = pomnoz(ulamek, ulamek2)
pod = podziel(ulamek, ulamek2) 

print("Wprowadzone ulamki {0}/{1} i {0}/{2} ".format(licznik, mian1, mian2))
print("Ulamki wygladaja teraz tak: ", ulamek, " i ", ulamek2 )
print("dodaj: \t", dod)
print("odejmij: \t", od)
print("pomnoz: \t", pomn)
print("podziel: \t", pod)

#testowanie funkcji modyfikujacych ulamek drugi

u1 = ulamek_wlasciwy(licznik, mian2)
u2 = ulamek_wlasciwy(licznik, mian2)
u3 = ulamek_wlasciwy(licznik, mian2)
u4 = ulamek_wlasciwy(licznik, mian2)

dodaj2(ulamek, u1)
odejmij2(ulamek, u2)
pomnoz2(ulamek, u3)
podziel2(ulamek, u4)
print("\nDruga wersja funkcji: ")
print("dodaj: \t", u1)
print("odejmij: \t", u2)
print("pomnoz: \t", u3)
print("podziel: \t", u4)