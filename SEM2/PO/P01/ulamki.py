def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a%b)

def nww(a, b):
    return abs(a*b)/nwd(a,b)

#SKRACANIE UŁAMKA
def skroc_ulamek(ulamek):    
    dzielnik = nwd(ulamek[0], ulamek[1])
    licznik = ulamek[0] // dzielnik 
    mianownik = ulamek[1] // dzielnik 
    return [licznik, mianownik] 

#TWORZENIE UŁAMKA
def utworz_ulamek(licznik,  mianownik):
    if mianownik == 0:
        raise ZeroDivisionError #wyjątek bład ZeroDivisionError
    if mianownik < 0:
        licznik = -licznik
        mianownik = -mianownik 
    return [licznik, mianownik]

#UŁAMEK
def ulamek_wlasciwy(licznik, mianownik):
    ulamek = utworz_ulamek(licznik, mianownik)
    ulamek = skroc_ulamek(ulamek)
    return ulamek 

#OPERACJE
#DODAWANIE zwraca nowy ulamek
def dodaj(ulamek1, ulamek2):
    mianownik1 = ulamek1[1]
    mianownik2 = ulamek2[1]
    licznik1 = ulamek1[0]
    licznik2 = ulamek2[0]
    wspolny = nww(mianownik1, mianownik2)
    mnoznik1 = wspolny // mianownik1 
    mnoznik2 = wspolny // mianownik2 

    return [int(licznik1*mnoznik1+licznik2*mnoznik2), int(wspolny)]


#DODAWANIE zmieniaja drugi argument
def dodaj2(ulamek1, ulamek2):
    mianownik1 = ulamek1[1]
    mianownik2 = ulamek2[1]
    licznik1 = ulamek1[0]
    licznik2 = ulamek2[0]
    wspolny = nww(mianownik1, mianownik2)
    mnoznik1 = wspolny // mianownik1 
    mnoznik2 = wspolny // mianownik2

    ulamek2[0] = int(licznik1*mnoznik1+licznik2*mnoznik2)
    ulamek2[1] = int(wspolny)

#ODEJMOWANIE
def odejmij(ulamek1, ulamek2):
    ulamekDwa = [-ulamek2[0], ulamek2[1]]
    return dodaj(ulamek1, ulamekDwa)


def odejmij2(ulamek1, ulamek2):
    ulamekDwa = [-ulamek2[0], ulamek2[1]]
    d = dodaj(ulamek1, ulamekDwa)
    ulamek2[0] = d[0]
    ulamek2[1] = d[1]

#mnozenie
def pomnoz(ulamek1, ulamek2):
    licznik = ulamek1[0] * ulamek2[0]
    mianownik = ulamek1[1] * ulamek2[1]
    return ulamek_wlasciwy(licznik, mianownik)

def pomnoz2(ulamek1, ulamek2):
    ulamek2[0] = ulamek1[0] * ulamek2[0]
    ulamek2[1] = ulamek1[1] * ulamek2[1]

#dzielenie
def podziel(ulamek1, ulamek2):
    licznik2 = ulamek2[0]
    mianownik2 = ulamek2[1]
    if licznik2 == 0:
        return ZeroDivisionError
    
    licznik2, mianownik2 = mianownik2, licznik2
    return pomnoz(ulamek1, ulamek_wlasciwy(licznik2, mianownik2))

def podziel2(ulamek1, ulamek2):
    licznik2 = ulamek2[0]
    mianownik2 = ulamek2[1]
    if licznik2 == 0:
        return ZeroDivisionError
    
    licznik2, mianownik2 = mianownik2, licznik2
    p = pomnoz(ulamek1, ulamek_wlasciwy(licznik2, mianownik2))
    ulamek2[0] = p[0]
    ulamek2[1] = p[1]