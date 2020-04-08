def suma_podzbiorow(lista):
    if lista == []:
        return [0]
    x = suma_podzbiorow(lista[1:])
    print(x + [lista[0] + y for y in x])
    return x + [lista[0] + y for y in x]

print(sorted(list(set(suma_podzbiorow([1,2,3,100])))))