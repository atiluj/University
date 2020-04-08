####################################
# Program:  linked_list.py
####################################

class ListItem:
    def __init__(self, e):
        self.e = e
        self.n = None
        
    def __str__(self):
        return str(self.e)    

class LinkedList:
    def __init__(self, elems):
        self.first = None
        self.last = None
        self.length = 0
        
        for e in elems:
            self.append(e)  
            
    def append(self, e):
        new = ListItem(e)
        if self.first == None:
            self.first = new
            self.last = new
        else:
            self.last.n = new
            self.last = new
        self.length += 1  
        
    def __len__(self):
        return self.length    
        
    def __iter__(self):
        elem = self.first
        while elem:
            yield elem.e
            elem = elem.n   

    def iterator_li(self):
        elem = self.first
        while elem:
            yield elem
            elem = elem.n   
            
    def __getitem__(self, i):
        pos = 0
        for e in self:
            if pos == i:
                return e
            pos += 1
        raise IndexError 
        
    def __setitem__(self, i, a):     
        pos = 0
        for li in self.iterator_li():
            if pos == i:
                li.e = a
                return
            pos += 1
        raise IndexError 
        
    def __str__(self):
        elems = [str(e) for e in list(self)]
        # elems = map(str, list(elems))
        return '-[' + ', '.join(elems) + ']-'    
    
    def __delitem__(self, i):
        if i != 0:
            raise IndexError
        if len(self) == 0:
            raise IndexError
        if len(self) == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.n
        self.length -= 1
                          
L = LinkedList([2,3,4,5,5,6,7])        
L[2] = 44
print (L)

N = 100000
#L2 = list(range(N))
L2 = LinkedList(range(N))

"""
for e in L:
    print (e)

for i in range(len(L)):
    print (L[i])
"""

while len(L2) > 0:
    del L2[0]
    #print (L)

print ('done')
        
            
            
            
                
####################################
# Program:  inny_string.py
####################################

tekst = 'ala ma kota i dwa kanarki i napisała w elementarzu ala ma kota i psa i dwa kanarki'

class Substring:
    def __init__(self, txt, a=None, b=None):
        self.txt = txt
        if a != None:
            self.a = a
        else:
            self.a = 0
        if b != None:        
            self.b = b
        else:
            self.b = len(txt)    
        
    def __str__(self):
        return self.txt[self.a:self.b]
    
    def __getitem__(self, i):
        return self.txt[self.a + i]
            
    def __len__(self):
        return self.b - self.a
        
    def __lt__(self, other):
        m = min(len(self), len(other))
        for i in range(m):
            if self[i] != other[i]:
                return self[i] < other[i]
        return len(self) < len(other)            
            
sufiksy = [Substring(tekst, i, len(tekst)) for i in range(len(tekst))]

sufiksy.sort()

for s in sufiksy:
    print (s)
####################################
# Program:  rlist.py
####################################

class RList(list):
    def __init__(self):
        super().__init__()
        
    def __getitem__(self, i):
        if i >= len(self):
            return None
        return super().__getitem__(i)
    
    def __setitem__(self, i, a):
        if i >= len(self):
            self += (i - len(self) + 1) * [None]
        super().__setitem__(i, a)
        
L = RList()
L += [0,1,2]
L[10] = 999
print (L)                    