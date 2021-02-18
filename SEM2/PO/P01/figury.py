from math import pi #ponieważ potrzbujemy pi do policzenia pola koła

class Enum:
    One, Two, Three = range(1, 4)

#kwadrat
def kwadrat(x1,y1,bok):
    if bok <= 0:
        print("Długość boku kadratu musi być liczbą wiekszą od 1")
    
    typ = Enum.One

    x2 = x1
    y2 = y1 + bok

    x3 = x1 + bok
    y3 = y2

    x4 = x3
    y4 = x1

    return [typ, x1, y1, x2, y2, x3, y3, x4, y4]

#trojkat    
def dl_boku(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1 / 2)

def trojkat(x1, y1, x2, y2, x3, y3):
    a = dl_boku(x1, y1, x2, y2)
    b = dl_boku(x1,y1, x3, y3)
    c = dl_boku(x2, y2, x3, y3)

    if not(a + b > c and a + c > b and b + c > a):
        print("Taki trojkat nie istnieje")

    typ = Enum.Two

    return [typ, x1, y1, x2, y2, x3, y3]

#kolo
def kolo(r, x, y):
    if r <= 0:
        print("Promien kola nie moze być ujemny!")
 
    typ = Enum.Three
    
    return [typ, r, x, y]

def pole(figura):

    if figura[0] == Enum.One: #gdy figura jest kwadratem
        bok = figura[4] - figura[2]
        return bok*bok

    elif figura[0] == Enum.Two: #gdy figura to trojkat
        a = dl_boku(figura[1], figura[2], figura[3], figura[4])
        b = dl_boku(figura[1], figura[2], figura[5], figura[6])
        c = dl_boku(figura[3], figura[4], figura[5], figura[6])
        p = (a + b + c) / 2  #wzor Herona
        pole_tr = (p * (p - a)*(p - b)*(p - c)**(1 / 2))   #wzór Herona
        return pole_tr

    elif figura[0] == Enum.Three: #gdy figura to koło
        return figura[1] ** 2 * pi

#####działania
def przesun(figura, x, y):
    if figura[0] == Enum.One:
        for i in range(1, 8, 2):
            figura[i] += x
        for i in range(2, 9, 2):
            figura[i] += y 
    elif figura[0] == Enum.Two:
        for i in range(1,6,2):
            figura[i] += x 
        for i in range(2, 7, 2):
            figura[i] += y 
    elif figura[0] == Enum.Three:
        figura[2] += x 
        figura[3] += y 

def suma_pol(tablica_figur, il_ele):
    suma = 0
    for i in range(il_ele):
        pole_i = pole(tablica_figur[i])
        suma += pole_i
    return suma
