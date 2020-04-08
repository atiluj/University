def silnia(n):
    wynik = 1
    for i in range(1,n+1):
        wynik *= i
    return wynik


for i in range(4,101):
    dl = len(str(silnia(i)))
    print(i, "! ma", dl, end=" ")
    if dl==1:
        print("cyfra")
    elif dl%100==12 or dl%100==13 or dl%100==14:
        print("cyfr")
    elif dl%10==2 or dl%10==3 or dl%10==4:
        print("cyfry")
    else: print("cyfr")