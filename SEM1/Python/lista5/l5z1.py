import statistics
def F(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def collatz(i):
    licznik=0
    while(i!=1):
        i=F(i)
        licznik += 1
    return licznik
    

def analiza(a,b):
    wynik=[]
    for i in range(a,b+1):
        wynik=wynik + [collatz(i)]   
    print('srednia energia; ', statistics.mean(wynik))
    print('mediana energii; ', statistics.median(wynik))
    print('max energia; ', max(wynik))
    print('min energia; ', min(wynik))
    print('energia; ', wynik)
    

a=int(input('podaj a: '))
b=int(input('podaj b: '))
analiza(a,b)