def add_to_tree(tree, e):
    if tree == []:
        tree += [e, [], []]
    a, left, right = tree
    if e < a:  
        add_to_tree(left, e)
    if e > a:  
        add_to_tree(right, e)

def in_tree(e, tree):  #czy jest element w drzewie
    if tree == []:
        return False
    a, left, right = tree    
    if a == e:
        return True
    if e < a:
        return in_tree(e, left)
    return in_tree(e, right)
    
    
def list_to_tree(L):   #lista na drzewo
    tree = []
    for e in L:
        add_to_tree(tree, e)
    return tree

def tree_to_list(tree):   #z drzewa liste  A B.... C...
    if tree == []:
        return []
    a, left, right = tree  
    return tree_to_list(left) + [a] + tree_to_list(right)

def nasz_iterator(tree):   #aby przeglądąc
    if tree == []:
        return
    a, left, right = tree  
    for e in nasz_iterator(left):
        yield e  #generuje wartosci
    yield a
    
    for e in nasz_iterator(right):
        yield e

def tree_set_sort(L):       
    t = list_to_tree(L)
    return tree_to_list(t)

class Set:
    def __init__(self, *args):
        self.tree = []
        for e in args:
            self.add(e)
        
    def add(self, e):
       add_to_tree(self.tree, e)
       
    def __contains__(self, e):  #czy zawiera
        return in_tree(e, self.tree)   
    
    def __or__(self, other):  #or and żeby wiedział co oznaczają znaczki
        wynik = Set()
        for e in self:
            wynik.add(e)
        for e in other:
            wynik.add(e)
        return wynik
    
    def __iter__(self):
        return nasz_iterator(self.tree)
               
    def __str__(self):
        lista = tree_to_list(self.tree)
        
        return '{' + ','.join([str(x) for x in lista]) + '}' 

    ############################################ zad1

    def __len__(self): #na liscie bo na liscie zwroci len na drzwie nie
        x = tree_to_list(self.tree)
        if self.tree == []: #jak jest pusty to ma długośc 0
            return 0
        return len(x)

    def __and__(self,second):
        new = Set()
        for e in self:
            if e in second:
                new.add(e)
        return new

    def __sub__(self,second):
        new = Set()
        for e in self:
            if e not in second:
                new.add(e)
        return new

#############
        
zbior = Set()

for e in [3,5,6,7,3,88,1,2,0,99]:
    zbior.add(e)

for i in range(10):
    print (i, i in zbior)

print (zbior)        

print (Set(4,7,2,3)) 
print (Set(1,2) | Set(2,3,4))  # (1,2,3,4)
   
############
print('zad 1 lista 12 przykladu')
print('len')
print(len(Set(1,2,3,4,5,6)))
print('and')
print(Set(1,2,5,6,3) & Set(1,2,3))
print('sub')
print(Set(1,4,2,5,9) - Set(1,5,9))