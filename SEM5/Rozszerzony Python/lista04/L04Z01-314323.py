#PLAN
# wyłonić operator
# zrobić liste słów z których składa się cały string
# zrobić liste wszystkich liter z których składaja się słowa (bez powtórzeń)
# zrobic słownik wszystkich mozliwych kombinacji przypisania liczb do każdej z liter
# dla każdej takiej permutacji sprawdzić czy nie daje akurat ona dobrego wyniku

import itertools

def findOperator(text):
    listOfOperators = ['-','+','/','*']
    i = 0
    while text[i] not in listOfOperators:
        i += 1
    operator = text[i]
    return operator

def getWords(text):
    listOfOperators = ['-','+','/','*','=', ' ']
    words = []
    i = 0
    start = 0
    end = -1
    while i < len(text):
        if text[i] not in listOfOperators:
            i += 1
        else:
            if text[i-1] in listOfOperators: 
                i += 1
                start += 1
                continue #gdyby komuś się wpisały więcej niz jedna spacja pod rząd
            end = i
            newWord = text[start:end]
            words.append(newWord.upper())
            start = i+1
            i += 1
    end = i+1
    newWord = text[start:end]
    words.append(newWord.upper())   

    return words

def permutations(letters):
    numbers = list(i for i in range(0,10))
    for i in list(itertools.permutations(numbers)):
        perDict = dict(list(zip(letters, i))) 
        yield perDict

def changeString(word, dict):
    chars = list(word)
    for i in range(0, len(word)):
        chars[i] = str(dict[chars[i]])
    return ''.join(chars)
    

def cryptarithm(text):
    operator = findOperator(text)
    words = getWords(text)
    letters = list(set(''.join(words)))

    for per in permutations(letters):
        propostion = []
        for word in words:
            propostion.append(str(int(changeString(word, per)))) 
        if operator == '/' and propostion[1] == '0':
            continue
        else:
            if eval(propostion[0] + operator + propostion[1]) == int(propostion[2]):
                print(propostion[0] + ' ' + operator + ' ' + propostion[1] + ' = ' + propostion[2])
                return per

    return text


# #przykładowe testy
print("kioto + osaka = tokio           ", cryptarithm("kioto + osaka = tokio"), "\n")
print("KTK +  zlkTk = ZLTZT           ", cryptarithm("KTK +  zlkTk = ZLTZT"), "\n")
print("puru / u = rpk           ", cryptarithm("puru / u = rpk"), "\n") 
print("eeee - iiii = aaaa           ", cryptarithm("eeee - iiii = aaaa"), "\n")
print("labt*i=zkrc           ", cryptarithm("labt *   i = zkrc"), "\n")

#przykładowy test - przykład bez rozwiązania
print("labt - i = xzkrc           ", cryptarithm("labt -   i = xzkrc"), "\n")

