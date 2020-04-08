def lista(b):
    L=[]
    L = L + [0] + [0]
    for i in range(2,b+1):
        L= L + [i]
    return L
    

def sito(b):
    L=lista(b)
    for i in range(2,int((b+1)**0.5)+1):
        if(L[i]>0):
            for j in range(i+i,b+1,i):
                L[j]=0
    return L


def palindrom(a,b):
    L=sito(b)
    wynik=[]
    for i in range (a,b+1):
        if(L[i]!=0):
            s=str(L[i])
            if(s==s[::-1]):  #odwrócony string
                wynik=wynik+[L[i]]
    return wynik

a=int(input('Podaj a: '))
b=int(input('Podaj b: '))
print(palindrom(a,b))
#print (sito(b))