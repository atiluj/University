class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
'''
class BTS:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self,val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if val <= currentNode.val:
            if currentNode.left:
                self.insertNode(currentNode.left, val)
            else:
                currentNode.left = Node()
        elif val > currentNode.val:
            if currentNode.right:
                self.insertNode(currentNode.right, val)
            else:
                currentNode.right = Node(val)'''

def insert(root, nkey):
    if root == None: return Node(nkey)
    if nkey < root.val:
        root.left = insert(root.left, nkey)
    else:
        if nkey > root.val:
            root.right = insert(root.right, nkey)
    return root

def insert2(root, nkey):
    if root == None: return Node(nkey)
    if nkey.val < root.val:
        root.left = insert(root.left, nkey)
    else:
        if nkey.val > root.val:
            root.right = insert(root.right, nkey)
    return root

def wypisz(t):
    if (t != None):
        print(t.val)
        wypisz(t.left)
        wypisz(t.right)

def wypisz2(t):
    if t!=None:
        wypisz(t.left)
        print(t.val)
        wypisz(t.right)

def liczbaelementow(t): #zad2
    licznik = 1
    if t.left != None:
        licznik += liczbaelementow(t.left)
    if t.right != None:
        licznik += liczbaelementow(t.right)
    return licznik

def maxdepth(t): #zad3
    if t is None:
        return 0
    else:
        ldepth = maxdepth(t.left)
        rdepth = maxdepth(t.right)
        if ldepth > rdepth:
            return ldepth+1
        else:
            return rdepth+1

def write(root): #zad4
    if root!= None:
        write(root.left)
        if root.val > 0:
            print(root.val)
        write(root.right)

def isBST(t):
    if t is None:
        return True

    if t.left != None and t.left.val > t.val:
        return False

    if t.right != None and t.right.val < t.val:
        return False
    if isBST(t.left) == False or isBST(t.right) == False:
        return False

    return True



drzewo = Node(8)

drzewo = insert(drzewo, 9)
drzewo = insert(drzewo, 7)
drzewo = insert(drzewo, 6)
drzewo = insert(drzewo, 5)
drzewo = insert(drzewo, 10)
drzewo = insert(drzewo, 22)
drzewo = insert(drzewo, 1)


wypisz(drzewo)
print('haha', liczbaelementow(drzewo))
print(maxdepth(drzewo))
write(drzewo)
print(isBST(drzewo))