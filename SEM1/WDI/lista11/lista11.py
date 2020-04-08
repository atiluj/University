class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def wypisz(root):
    if root!=None:
        wypisz(root.left)
        print(root.val, end = ', ')
        wypisz(root.right)

def wypisz7(root):
    if root!=None:
        print(root.val, end = ', ')
        wypisz(root.left)
        wypisz(root.right)

def liczba_elementow(root): #zad2
    licznik = 1
    if root.left != None:
        licznik += liczba_elementow(root.left)
    if root.right != None:
        licznik += liczba_elementow(root.right)
    return licznik

def max_glebokosc(root): #zad3
    if root is None:
        return 0
    else:
        ldepth = max_glebokosc(root.left)
        rdepth = max_glebokosc(root.right)
        if ldepth > rdepth:
            return ldepth+1
        else:
            return rdepth+1

def dodatnie(root): #zad4
    if root!= None:
        dodatnie(root.left)
        if root.val > 0:
            print(root.val, end=", ")
        dodatnie(root.right)

def czy_dżewo(wierzcholek):
    if wierzcholek == None:
        return 0
    if wierzcholek.left==None and wierzcholek.right == None:
        return 1
    return (czy_dżewo(wierzcholek.left) and czy_dżewo(wierzcholek.right))

def czy_BST(t, left=None, right=None):  #zad5
    if (t == None):
        return True
    if t.left != None and t.left.val >= t.val:
        return False
    if t.right != None and t.right.val <= t.val:
        return False
    return (czy_BST(t.left, left, t) and czy_BST(t.right, t, right)) 

def czy_BST2(root, mini, maxi): 
    if root is None: 
        return True  
    if root.val < mini or root.val > maxi: 
        return False   
    return (czy_BST2(root.left, mini, root.val -1) and isBSTUtil(root.right, root.val +1, maxi)) 

def czy_BST3(t):  #zad5
    if (t == None):
        return True
    if t.left != None and t.left.val >= t.val:
        return False
    if t.right != None and t.right.val <= t.val:
        return False
    return (czy_BST(t.left) and czy_BST(t.right)) 

###ZADANIE 6 
#idziemy do najmniejszej wartosc, laczymy drzewa podobnie jak listy pythonowe
def polacz(t1, t2): #t1 < t2
    if t2 == None:
        return t1
    pom = t2
    while pom.left != None:
        pom = pom.left
    pom.left = t1
    return t2

root = Node(4)       #stworzenie drzewa
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
#root.left.left.left = Node(5)
#root.left.left.right = Node(3)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(8)
#root.right.right.right = Node(9)

wypisz(root)        #wypisanie drzewa
print("")
wypisz7(root)
print("")
print('zad.2')
print(liczba_elementow(root))
print('zad.3')
print(max_glebokosc(root))
print('zad.4')
dodatnie(root)
print("")
print("zad.5 - BST1")
if czy_BST(root, None, None):
    print('TAK')
else:
    print('NIE') 
print("zad.5 - BST2")
if czy_BST(root, None, None):
    print('TAK')
else:
    print('NIE')
print("zad.5 - BST3")
if czy_BST3(root) == 1:
    print('TAK')
else:
    print('NIE')