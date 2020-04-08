def dzielniki(n):
    wynik=[]
    k=n
    i=2
    while(n!=1):
        if(n%i==0):
            wynik=wynik+[i]
            while(n%i==0):
                n=n/i
        i=i+1
    return wynik


n=int(input('Podaj liczbe: '))
wynik=dzielniki(n)
print(wynik)