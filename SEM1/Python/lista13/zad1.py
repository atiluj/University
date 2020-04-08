def wieza(N,D):
    szer = D - 8*(N-1)
    for i in range(N):
        print(" "*((D-szer)//2), end="")
        print("#"*szer)
        for j in range(2):
            print(" "*((D-szer)//2),end ="")
            print("#", end="")
            print(" "*(szer-2), end="")
            print("#")
        print(((D-szer)//2)*" ", end ="")
        print("#"*szer)
        szer += 8

wieza(4,40)