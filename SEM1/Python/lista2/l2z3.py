from math import sqrt

def fragment_balwana(n,m):
    material="#"
    separator=" "
    for wiersz in range(n):
        dany_wiersz=(m-n)//2*" "
        for kolumna in range(n):
            r=n//2
            if(sqrt(((r - wiersz)*(r - wiersz)) + ((r - kolumna)*(r - kolumna)) )) <= n/2 :
                dany_wiersz=dany_wiersz+material
            else:
                dany_wiersz=dany_wiersz+separator
        print(dany_wiersz)


fragment_balwana(7,19)
fragment_balwana(9,19)
fragment_balwana(11,19)