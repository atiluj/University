def pierwiastek(n):
    sum = 0
    #print("rozpatrujemy pierwiastek z ", n)
    for i in range(1, n//2+1):
        sum += 2*i-1
        #print("suma = ", sum)
        if(sum > n):
            return i-1
    return i
        

print(pierwiastek(2))   #oczekiwany wynik 1
print(pierwiastek(4))   #oczekiwany wynik 2
print(pierwiastek(16))  #oczekiwany wynik 4
print(pierwiastek(20))  #oczekiwany wynik 4
print(pierwiastek(220)) #oczekiwany wynik 14
print(pierwiastek(225)) #oczekiwany wynik 15
print(pierwiastek(227)) #oczekiwany wynik 15
print(pierwiastek(8))   #oczekiwany wynik 2
print(pierwiastek(5))   #oczekiwany wynik 2
print(pierwiastek(13))  #oczekiwany wynik 3
