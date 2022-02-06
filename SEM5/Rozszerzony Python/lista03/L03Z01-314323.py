import timeit

def pierwsze_imperatywne(n):
    result = []
    for i in range(2, n):
        flag = 1 
        for j in range(2,i):
            if i % j == 0:
                flag = 0
        if flag == 1:
            result.append(i)
    return result


def pierwsze_skladana(n):
    result = [i for i in range(2,n+1) if all(i%j != 0 for j in range(2, i))]
    return result


def pierwsze_funkcyjna(n):
    result = list(filter(lambda x: 0 not in [x % i for i in range(2, x)], [i for i in range(2, n+1)]))
    return result


print("Wyniki dla przykładowych testów - WERSJA IMPERATYWNA")
print("Dla 10: ", pierwsze_imperatywne(10), "---- CZAS - ", timeit.timeit(lambda: pierwsze_imperatywne(10), number=100))
print("Dla 15: ", pierwsze_imperatywne(15), "---- CZAS - ", timeit.timeit(lambda: pierwsze_imperatywne(15), number=100))
print("Dla 41: ", pierwsze_imperatywne(41), "---- CZAS - ", timeit.timeit(lambda: pierwsze_imperatywne(41), number=100))
print("Dla 100: ", pierwsze_imperatywne(100), "---- CZAS - ", timeit.timeit(lambda: pierwsze_imperatywne(100), number=100))
print("Dla 1000: ", pierwsze_imperatywne(1000), "---- CZAS - ", timeit.timeit(lambda: pierwsze_imperatywne(1000), number=100))
# print("Dla 9999: ", pierwsze_imperatywne(9999), "---- CZAS - ", timeit.timeit(lambda: pierwsze_imperatywne(9999), number=100))
print("----------------------")
print("Wyniki dla przykładowych testów - WERSJA LISTY SKŁADANE")
print("Dla 10: ", pierwsze_skladana(10), "---- CZAS - ", timeit.timeit(lambda: pierwsze_skladana(10), number=100))
print("Dla 15: ", pierwsze_skladana(15), "---- CZAS - ", timeit.timeit(lambda: pierwsze_skladana(15), number=100))
print("Dla 41: ", pierwsze_skladana(41), "---- CZAS - ", timeit.timeit(lambda: pierwsze_skladana(41), number=100))
print("Dla 100: ", pierwsze_skladana(100), "---- CZAS - ", timeit.timeit(lambda: pierwsze_skladana(100), number=100))
print("Dla 1000: ", pierwsze_skladana(1000), "---- CZAS - ", timeit.timeit(lambda: pierwsze_skladana(1000), number=100))
# print("Dla 9999: ", pierwsze_skladana(9999), "---- CZAS - ", timeit.timeit(lambda: pierwsze_skladana(9999), number=100))
print("----------------------")
print("Wyniki dla przykładowych testów - WERSJA IMPLEMENATCJA FUNKCYJNA")
print("Dla 10: ", pierwsze_funkcyjna(10), "---- CZAS - ", timeit.timeit(lambda: pierwsze_funkcyjna(10), number=100))
print("Dla 15: ", pierwsze_funkcyjna(15), "---- CZAS - ", timeit.timeit(lambda: pierwsze_funkcyjna(15), number=100))
print("Dla 41: ", pierwsze_funkcyjna(41), "---- CZAS - ", timeit.timeit(lambda: pierwsze_funkcyjna(41), number=100))
print("Dla 100: ", pierwsze_funkcyjna(100), "---- CZAS - ", timeit.timeit(lambda: pierwsze_funkcyjna(100), number=100))
print("Dla 1000: ", pierwsze_funkcyjna(1000), "---- CZAS - ", timeit.timeit(lambda: pierwsze_funkcyjna(1000), number=100))
# print("Dla 9999: ", pierwsze_funkcyjna(9999), "---- CZAS - ", timeit.timeit(lambda: pierwsze_funkcyjna(9999), number=100))

