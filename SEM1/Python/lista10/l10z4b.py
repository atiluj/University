def tworzenie_listy(a,b):
    wynik = []
    for i in range (a,b+1):
        wynik.append(i)
    return wynik

def ciagi_niemalejace(lista):
    if lista == []:
        return [[]]
    x = ciagi_niemalejace(lista[1:])
    print(x + [[lista[0]] + y for y in x])
    return x + [[lista[0]] + y for y in x]

dlugosc = 3
a = 2
b = 5
lista = tworzenie_listy(a,b)
wszystkie_ciagi = ciagi_niemalejace(lista)
for e in wszystkie_ciagi:
    if len(e) == dlugosc:
        print(e, end = ", ")
