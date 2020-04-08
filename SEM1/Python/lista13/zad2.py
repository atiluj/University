import random

def wieza(N,D):
    L = ['o', '*', '@', '0']
    szer = D - 8*(N-1)
    for i in range(N):
        print(" "*((D-szer)//2), end="")
        print("#"*szer)
        for j in range(2):
            print(" "*((D-szer)//2),end ="")
            print("#", end="")
            for k in range(szer-2):
                los = random.randint(0,3)
                print(L[los], end="")
            print("#")
        print(((D-szer)//2)*" ", end ="")
        print("#"*szer)
        szer += 8

wieza(4,40)