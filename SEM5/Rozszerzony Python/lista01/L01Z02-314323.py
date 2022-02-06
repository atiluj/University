def is_palindrom(text):
    text = text.lower()
    length = len(text)
    lista = [' ', '.', ',', ':', ';', '-', '\"', '?', '!', '\'']
    
    for i in range(length):
        k = length - i - 1

        if text[k] in lista and length-1 != k:
            text = text[0:k:]+text[k+1::]
        elif text[k] in lista and length-1 == k:
            text = text[:-1] 
    
    length = len(text)
    i = 0

    while i <= length//2:
        if text[i] == text[length - 1]:
            i = i + 1
            length = length - 1
        else:
            return False

    return True
        

text1 = 'Kobyła ma mały bok'
text2 = 'Eine gulden, gute Tugend: Luge nie!'
text3 = 'oko'
text4 = 'rotor' 

print(is_palindrom(text1))
print(is_palindrom(text2))
print(is_palindrom(text3))
print(is_palindrom(text4))
