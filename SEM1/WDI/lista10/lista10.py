class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None

def wypisz(lis):
    while lis != None:
        print(lis.val, end=" ")
        lis = lis.next
    print(" ")

#Zadanie 1
'''def wypisz_dodatnie(lis):
    while lis != None:
        if lis.val > 0:
            print(lis.val)
        lis = lis.next'''

#Zadanie 2
def dodac_na_koniec(lis, wartosc):
    first = lis
    if lis == None:
        first = ListItem(wartosc)
    else:
        while lis.next != None:
            lis = lis.next
        lis.next = ListItem(wartosc)
    return first

lis = ListItem(2)
lis = dodac_na_koniec(lis, 1)
lis = dodac_na_koniec(lis, 3)
wypisz(lis)
print("\n")

#Zadanie 3
'''
def usunac_koniec(lis):
    pom = lis
    #if pom.next == None:
        #pom = None
        #return pom
    while pom.next != None:
        poprz = pom
        pom = pom.next
    poprz.next = None
    return lis

print('zadanie 3')
usunac_koniec(lis)
#usunac_koniec(lis)
wypisz_dodatnie(lis)

#Zadanie 4
def polaczenie_list(lis1,lis2):
    pom = lis1
    while pom.next != None:
        pom = pom.next
    pom.next = lis2
    return lis1

print('zadanie 4')
lis1 = ListItem(2)
lis2 = ListItem(5)
dodac_na_koniec(lis1 , 2)
dodac_na_koniec(lis2, 5) 
polaczenie_list(lis1,lis2)
wypisz_dodatnie(lis1)

#zadanie 5
def usun(lis, wartosc):
    temp = lis
    while temp.val == wartosc:
        temp = temp.next
    lis = temp
    nowa = ListItem(temp.val)
    while temp.next != None:
        pom = temp.next
        if pom.val == wartosc:
            temp.next = pom.next
            if(temp.next.val != wartosc):
                dodac_na_koniec(nowa, temp.next.val)
        if temp.next == None:
            return nowa
        temp = temp.next
    return nowa

print('zadanie 5')
lis2 = ListItem(6)
dodac_na_koniec(lis2, 5)
dodac_na_koniec(lis2, 6)
dodac_na_koniec(lis2, 6)
wypisz_dodatnie(lis2)
print('usuniecie')
nowa = usun(lis2, 6)
wypisz_dodatnie(nowa)

#Zadanie 6
def wypisz_odwrotnie(lis):
    if lis != None:
        wypisz_odwrotnie(lis.next)
        print(lis.val)

print('zadanie 6')
dodac_na_koniec(lis, 1)
dodac_na_koniec(lis, 7)
dodac_na_koniec(lis, 2)
wypisz_dodatnie(lis)
print('')
wypisz_odwrotnie(lis)
        
#Zadanie 7
def odwroc(lis):
    licznik = 1
    pom = lis
    while pom.next != None:
        licznik += 1
        pom = pom.next
    nowa = ListItem(pom.val)
    usunac_koniec(lis)
    for i in range(licznik-1):
        temp = lis
        while temp.next != None:
            temp = temp.next
        dodac_na_koniec(nowa, temp.val)
        if i == licznik - 2:
            return nowa
        usunac_koniec(lis)   
    return nowa     

print('Zadanie 7')
wypisz_dodatnie(lis)
print(',,,')
nowa = odwroc(lis)
wypisz_dodatnie(nowa)

#Zadanie 8
def podlisty(lis0):
    dodatnie = None
    ujemne = None
    while lis0 != None:
        if lis0.val >= 0:
            if dodatnie == None:
                dodatnie = ListItem(lis0.val)
            else:
                dodac_na_koniec(dodatnie, lis0.val)
        else:
            if ujemne == None:
                ujemne = ListItem(lis0.val)
            else:
                dodac_na_koniec(ujemne, lis0.val)
        lis0 = lis0.next
    return dodatnie, ujemne

print('zad 8')
lis0 = ListItem(2)
dodac_na_koniec(lis0, -1)
dodac_na_koniec(lis0, -2)
dodac_na_koniec(lis0, 3)
dodac_na_koniec(lis0, 4)

wypisz(lis0)
dod, uj = podlisty(lis0)
wypisz(dod)
wypisz(uj)'''



