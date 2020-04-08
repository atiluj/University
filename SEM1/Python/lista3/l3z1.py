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

def siedem(n):
    n=str(n)
    if "777" in n:
        return True
    else: return False


ile =0
for n in range(1,100001):
    if czy_pierwsza(n) and siedem(n):
        print(n)
        ile=ile+1

print(ile)