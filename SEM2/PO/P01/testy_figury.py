from figury import *

figura1 = kwadrat(1,1,4) #(x, y, bok)
figura2 = kolo(3, 4, 5) #(r, x, y)
figura3 = trojkat(1, 1, 1, 4, 5, 1) #(x1, y1, x2, y2, x3, y3)

print("Kwadrat: ", figura1)
przesun(figura1, 2, 2)
print("Przesuniety:", figura1)

print("Trojkat: ", figura3)
przesun(figura3, 2, 2)
print("Przesuniety:", figura3)

print("Kolo: ", figura2)
przesun(figura2, 2, 2)
print("Przesuniety:", figura2)

tablica_figur = [figura1, figura2, figura3]
il_ele = 3

for i in range(il_ele):
    print("Pole figury typu ", i, "to: ", pole(tablica_figur[i]))

print("Suma pol tablicy zawierajacej figury:", suma_pol(tablica_figur, il_ele))