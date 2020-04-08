def szachownica(n,k):
    for i in range(2*n):
        if i%2==0:
            for j in range(k):
                print(n*(k*" "+k*"#"))
        else: 
            for i in range(k):
                print(n*(k*"#"+k*" "))


n=int(input("Podaj n:"))
k=int(input("Podaj k:"))
szachownica(n,k)
