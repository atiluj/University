
def pierwiastek(n):
    sum = 0
    #print("rozpatrujemy pierwiastek z ", n)
    for i in range(1, n//2+1):
        sum += 2*i-1
        #print("suma = ", sum)
        if(sum > n):
            return i-1
    return i
        

# print(pierwiastek(2))   #oczeikwany wynik 1
# print(pierwiastek(4))   #oczeikwany wynik 2
# print(pierwiastek(16))  #oczeikwany wynik 4
# print(pierwiastek(20))  #oczeikwany wynik 4
# print(pierwiastek(220)) #oczeikwany wynik 14
# print(pierwiastek(225)) #oczeikwany wynik 15
# print(pierwiastek(227)) #oczeikwany wynik 15
# print(pierwiastek(8))   #oczeikwany wynik 2
# print(pierwiastek(5))   #oczeikwany wynik 2
# print(pierwiastek(13))  #oczeikwany wynik 3
# print(pierwiastek(1000))
# print(pierwiastek(99999999))
# print(pierwiastek(1000000000000000))

