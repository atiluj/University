'''def maksymalny_zysk(L):
    max = 0
    for i in range(len(L)):
        koszt = L[i]
        for j in range(i+1, len(L)):
            zysk = L[j]
            zarobek = zysk - koszt
            if zarobek > max:
                max = zarobek
    return max'''

def maksymalny_zysk(L):
    return max([j - L[i] for i in range(len(L)-1) for j in L[i+1:]])

L = [100, 120, 40, 505, 13]
print(maksymalny_zysk(L))