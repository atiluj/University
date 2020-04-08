def koperta(n):
    for i in range(2*n+1):
        if i==0 or i==2*n:
            print((2*n)*"*",end="")
        else:
            print("*",end="")
            for j in range(1,2*n):
                if j==i or j==(2*n-i):
                    print("*",end="")
                else:
                    print(" ",end="")
        print("*")

n=int(input("Podaj n: "))
koperta(n)