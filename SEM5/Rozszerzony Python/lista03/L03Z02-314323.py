import timeit

def doskonale_imperatywna(n):
    result = []
    for i in range(1, n):
        sum = 0
        for j in range(1, i):
            if i % j == 0:
                sum += j
        if sum == i:        
            result.append(i)
    return result


def doskonale_skladana(n):
    result = [i for i in range(2,n+1) if sum([j for j in range(2, i//2+1) if i%j == 0]) + 1 == i]
    return result


def doskonale_funkcyjna(n):
    result = list(i for i in range(2, n) if sum(filter(lambda x: i%x==0 ,[j for j in range(2, i)]))+1 == i)
    return result


print("Wyniki dla przykładowych testów - WERSJA IMPERATYWNA")
print("Dla 10: ", doskonale_imperatywna(10), "----- CZAS - ", timeit.timeit(lambda: doskonale_imperatywna(10), number=100))
print("Dla 15: ", doskonale_imperatywna(15), "----- CZAS - ", timeit.timeit(lambda: doskonale_imperatywna(15), number=100))
print("Dla 41: ", doskonale_imperatywna(41), "----- CZAS - ", timeit.timeit(lambda: doskonale_imperatywna(41), number=100))
print("Dla 100: ", doskonale_imperatywna(100), "----- CZAS - ", timeit.timeit(lambda: doskonale_imperatywna(100), number=100))
print("Dla 1000: ", doskonale_imperatywna(1000), "----- CZAS - ", timeit.timeit(lambda: doskonale_imperatywna(1000), number=100))
print("Dla 1500: ", doskonale_imperatywna(1500), "----- CZAS - ", timeit.timeit(lambda: doskonale_imperatywna(1500), number=100))
print("----------------------")
print("Wyniki dla przykładowych testów - WERSJA LISTY SKŁADANE")
print("Dla 10: ", doskonale_skladana(10), "----- CZAS - ", timeit.timeit(lambda: doskonale_skladana(10), number=100))
print("Dla 15: ", doskonale_skladana(15), "----- CZAS - ", timeit.timeit(lambda: doskonale_skladana(15), number=100))
print("Dla 41: ", doskonale_skladana(41), "----- CZAS - ", timeit.timeit(lambda: doskonale_skladana(41), number=100))
print("Dla 100: ", doskonale_skladana(100), "----- CZAS - ", timeit.timeit(lambda: doskonale_skladana(100), number=100))
print("Dla 1000: ", doskonale_skladana(1000), "----- CZAS - ", timeit.timeit(lambda: doskonale_skladana(1000), number=100))
print("Dla 1500: ", doskonale_skladana(1500), "----- CZAS - ", timeit.timeit(lambda: doskonale_skladana(1500), number=100))
print("----------------------")
print("Wyniki dla przykładowych testów - WERSJA IMPLEMENATCJA FUNKCYJNA")
print("Dla 10: ", doskonale_funkcyjna(10), "----- CZAS - ", print(timeit.timeit(lambda: doskonale_funkcyjna(10), number=100)))
print("Dla 15: ", doskonale_funkcyjna(15), "----- CZAS - ", timeit.timeit(lambda: doskonale_funkcyjna(15), number=100))
print("Dla 41: ", doskonale_funkcyjna(41), "----- CZAS - ", timeit.timeit(lambda: doskonale_funkcyjna(41), number=100))
print("Dla 100: ", doskonale_funkcyjna(100), "----- CZAS - ", timeit.timeit(lambda: doskonale_funkcyjna(100), number=100))
print("Dla 1000: ", doskonale_funkcyjna(1000), "----- CZAS - ", timeit.timeit(lambda: doskonale_funkcyjna(1000), number=100))
print("Dla 1500: ", doskonale_funkcyjna(1500), "----- CZAS - ", timeit.timeit(lambda: doskonale_funkcyjna(1500), number=100))

