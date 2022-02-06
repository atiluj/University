class NieznanaZmienna(Exception):
    pass

class ZlyTyp(Exception):
    pass

class Formula:
    def __add__(self, w): #or
        return Or(self, w)

    def __mul__(self, w): #and
        return And(self, w)

    def uprosc(self):
        return self

    def wolneZmienne(self):
        if isinstance(self, And) or isinstance(self, Or):
            return self.w1.wolneZmienne() | self.w2.wolneZmienne()
        if isinstance(self, Not):
            return self.w1.wolneZmienne()
        if isinstance(self, Zmienna):
            return {self.nazwa}
        return set()
    
    @staticmethod
    def tautologia(w): 
        wartosci = [dict()]
        for zmienna in w.wolneZmienne():
            noweWartosci = []
            for wartosciowanie in wartosci:
                noweWartosci.append({**wartosciowanie, zmienna:True})
                noweWartosci.append({**wartosciowanie, zmienna:False})
            wartosci = noweWartosci
        for wartosc in wartosci:
            if not(w.oblicz(wartosc)):
                return False
        return True


class Zmienna(Formula): #p, q , t...
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __str__(self):
        return self.nazwa

    def oblicz(self, zmienne):
        if self.nazwa in zmienne:
            if isinstance(zmienne[self.nazwa], bool):
                return zmienne[self.nazwa]
            raise ZlyTyp("Zły typ")
        raise NieznanaZmienna("Nieznana zmienna")

class Stala(Formula): #true/false
    def __init__(self, wartosc):
        self.wartosc = wartosc

    def __str__(self):
        if self.wartosc:
            return "t"
        return "f"

    def oblicz(self, zmienne):
        if isinstance(self.wartosc, bool):
            return self.wartosc
        raise ZlyTyp("Zły typ")

class Not(Formula):
    def __init__(self, w1):
        self.w1 = w1

    def __str__(self):
        return f"¬{self.w1}"

    def oblicz(self, zmienne):
        return not(self.w1.oblicz(zmienne))

class Or(Formula):
    def __init__(self, w1, w2):
        self.w1 = w1
        self.w2 = w2
    
    def __str__(self):
        return f"({self.w1} ∨ {self.w2})"

    def oblicz(self, zmienne):
        return self.w1.oblicz(zmienne) or self.w2.oblicz(zmienne)

    def uprosc(self):
        if Formula.tautologia(self.w1):
            return Stala(True)
        if Formula.tautologia(self.w1):
            return Stala(True)
        if Formula.tautologia(self):
            return Stala(True)
        if Formula.tautologia(Not(self)):
            return Stala(False)
        if Formula.tautologia(Not(self.w1)):
            return self.w2.uprosc()
        if Formula.tautologia(Not(self.w2)):
            return self.w1.uprosc()
        return self.w1.uprosc() + self.w2.uprosc()


class And(Formula):
    def __init__(self, w1, w2):
        self.w1 = w1
        self.w2 = w2

    def __str__(self):
        return f"({self.w1} ∧ {self.w2})"

    def oblicz(self, zmienne):
        return self.w1.oblicz(zmienne) and self.w2.oblicz(zmienne)

    def uprosc(self):
        if Formula.tautologia(Not(self.w1)):
            return Stala(False)
        if Formula.tautologia(Not(self.w2)):
            return Stala(False)
        if Formula.tautologia(self):
            return Stala(True)
        if Formula.tautologia(Not(self)):
            return Stala(False)
        if Formula.tautologia(self.w1):
            return self.w2.uprosc()
        if Formula.tautologia(self.w2):
            return self.w1.uprosc()
        return self.w1.uprosc() * self.w2.uprosc()


# Wypisywanie
print("Przykłady")
print(Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True))), "dla: x=True, y=False   -> ", Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True))).oblicz({"x":True, "y":False}))
print(Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True))), "dla: x=False, y=False   -> ", Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True))).oblicz({"x":False, "y":False}))
print(Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True))), "dla: x=True, y=True   -> ", Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True))).oblicz({"x":True, "y":True}))
print(Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True))), "dla: x=False, y=True   -> ", Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True))).oblicz({"x":False, "y":True}))

try:
    print("\nWyjątki")
    # nie ma wartosci przypisanej pod y
    print("Nieznana wartość pod zmienną 'y'  -> ", Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True))).oblicz({"x":True}))
except (ZlyTyp, NieznanaZmienna) as e:
    print(str(e))

try:    
    # zły typ
    print("Stała nie jest typu bool   -> ", Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True))).oblicz({"x":True, "y":123}))
except (ZlyTyp, NieznanaZmienna) as e:
    print(str(e))


# tautologia
print("\nTautologie")
print(Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True)))," -> ", Formula.tautologia(Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True))))) 
print(Not(Zmienna("p")), " -> ", Formula.tautologia(Not(Zmienna("p")))) 
print(Or(Or(Zmienna("p"), Zmienna("q")), Not(Or(Zmienna("p"), Zmienna("q")))), " -> ", Formula.tautologia(Or(Or(Zmienna("p"), Zmienna("Q")), Not(Or(Zmienna("p"), Zmienna("Q")))))) 
print(Or(Stala(True), Zmienna("p")), " -> ", Formula.tautologia(Or(Stala(True), Zmienna("p"))))
print(Or(Zmienna("p"), Zmienna("p")), " -> ", Formula.tautologia(Or(Zmienna("p"), Zmienna("p"))))
print(Or(Not(Zmienna("x")), And(Zmienna("y"), Zmienna("q"))), " -> ", Formula.tautologia(Or(Not(Zmienna("x")), And(Zmienna("y"), Zmienna("q")))))


## uproszczenie
print("\nUproszczenia")
print(Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True)))," ----->  ", Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True))).uprosc())
print(Or(Not(Zmienna("x")), And(Zmienna("y"), Zmienna("q")))," ----->  ",Or(Not(Zmienna("x")), And(Zmienna("y"), Zmienna("q"))).uprosc())
print(Or(Stala(True), Stala(True))," ----->  ", Or(Stala(True), Stala(True)).uprosc())
print(Or(Zmienna("p"), Not(Zmienna("p")))," ----->  ", Or(Zmienna("p"), Not(Zmienna("p"))).uprosc())
print(And(Or(Zmienna("p"), Zmienna("q")), Or(Zmienna("t"), Not(Zmienna("t"))))," ----->  ", And(Or(Zmienna("p"), Zmienna("q")), Or(Zmienna("t"), Not(Zmienna("t")))).uprosc())