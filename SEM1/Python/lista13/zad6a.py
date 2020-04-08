'''def srednia_liczba_cyfr(L):
    suma = 0
    dl = len(L)
    for i in range(dl):
        liczba = L[i]
        suma = suma + len(str(liczba))
    return suma/dl'''

def srednia_liczba_cyfr(L):
#    return(sum(for i in range(len(i)))/len(L))
    return sum([len(str(a)) for a in L])/len(L)

def 

L = [0, 12, 13, 4]
print('6a', end = '  -  ')
print(srednia_liczba_cyfr(L))

