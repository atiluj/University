import math

def czy_pierwsza(n):
    if n<=1:
        return False
    if n==2:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True


def tworzenie():
    liczby= []                                #zbior nie przechowuje duplikatow set()  set.add()
    siodemki="7777777"
    for i in range(100,1000):
        liczba=str(i)+siodemki
        if czy_pierwsza(int(liczba)):
            liczby=liczby+[liczba]
    for i in range(1,1000,2):                    #zeby szybciej działał to nieparzyste
        if i<10:
            liczba=siodemki+"00"+str(i)
        elif i<100:
            liczba=siodemki+"0"+str(i)
        else: 
            liczba=siodemki+str(i)
        if czy_pierwsza(int(liczba)):
            liczby=liczby+[liczba]
    for i in range(1,10):#1 z porzdu 2 z tyłu
        liczba=str(i)+siodemki
        for j in range(1,100,2):
            if j<10:
                liczba2=liczba+"0"+str(j)
            else: 
                liczba2=liczba+str(j)
            if czy_pierwsza(int(liczba2)):
                liczby=liczby+[liczba2]
    for i in range(1,10,2):#1 z tyłu 2 z przodu
        liczba=siodemki+str(i)
        for j in range(10,100):
            liczba2=str(j)+liczba
            if czy_pierwsza(int(liczba2)):
                liczby=liczby+[liczba2]
    return liczby

def filtr(liczby):#usowa duplikaty
    wynik=[]
    for i in range(len(liczby)):
        if(liczby[i] in wynik) == False:
            wynik = wynik + [liczby[i]]
    return wynik

liczby = tworzenie()
liczby = filtr(liczby)
print(len(liczby))


