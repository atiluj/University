def krzyz(n):
    for i in range(n):
        print((n-1)*" ",n*"*")
    for i in range(n):
        print((n*3)*"*")
    for i in range(n):
        print((n-1)*" ",n*"*")

n=int(input("Podaj dlugosc boku: "))
krzyz(n)
