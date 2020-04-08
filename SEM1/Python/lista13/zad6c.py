'''def czy_jest_tytulem(s):
    L = s.split(" ")
    for slowo in L:
        a = slowo[0]
        if a.islower() == True:
            return False
    return True'''

def czy_jest_tytulem(s):
    return all([a[0].isupper() for a in s.split()])

s = 'Czy To Tytuł?'
print(czy_jest_tytulem(s))
k = 'A czy to jest Tytuł?'
print(czy_jest_tytulem(k))