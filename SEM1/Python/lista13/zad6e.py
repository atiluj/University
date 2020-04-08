'''def posortowanie_leksykograficzne(L):
    for liczba in L:
        liczba = str(liczba)
    L.sort()
    for liczba in L:
        liczba = int(liczba)
    return L'''

def posortowanie_leksykograficzne(L):
    return [int(numer) for numer in sorted(str(liczba) for liczba in L)]

L = [12, 0, 13, 22, 54]
print(posortowanie_leksykograficzne(L))