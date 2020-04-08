import copy
kolejka = []

class gra():

    def __init__(self, jeden_brzeg, drugi_brzeg, gracz, stany):
        self.stany = stany
        self.jeden_brzeg = jeden_brzeg
        self.drugi_brzeg = drugi_brzeg
        self.gracz = gracz

    def __str__(self):
        return (str(self.jeden_brzeg) + "  ||  " + str(self.drugi_brzeg) + "  ||  " +str(self.gracz))

    def zwyciestwo(self):
        if 1 in self.drugi_brzeg and 2 in self.drugi_brzeg and 3 in self.drugi_brzeg:
            return 1
        return 0

    def przegrana(self):
        if 2 in self.drugi_brzeg and 3 in self.drugi_brzeg and self.gracz == 1:
            return 1
        if 1 in self.drugi_brzeg and 2 in self.drugi_brzeg and self.gracz == 1:
            return 1
        if 2 in self.jeden_brzeg and 3 in self.jeden_brzeg and self.gracz == 0:
            return 1
        if 1 in self.jeden_brzeg and 2 in self.jeden_brzeg and self.gracz == 0:
            return 1
        return 0

    def graj(self):
        if self.zwyciestwo() == 1:
            print(self.stany)
            return 1
        else:
            if self.przegrana() == 0:
                if self.gracz == 1:
                    nowy_brzeg_1 = copy.deepcopy(self.jeden_brzeg)
                    nowy_brzeg_2 = copy.deepcopy(self.drugi_brzeg)
                    nowy_stan = copy.deepcopy(self.stany)
                    nowy_brzeg_1 = sorted(nowy_brzeg_1)
                    nowy_brzeg_2 = sorted(nowy_brzeg_2)
                    if [nowy_brzeg_1,nowy_brzeg_2, self.gracz] not in self.stany:
                        nowy_stan.append([nowy_brzeg_1,nowy_brzeg_2, copy.deepcopy(self.gracz)])
                        nastepna_tura = gra(nowy_brzeg_1, nowy_brzeg_2, (copy.deepcopy(self.gracz)+1)%2, nowy_stan)
                        kolejka.append(nastepna_tura)           

                    for i in self.jeden_brzeg:
                        nowy_brzeg_1 = copy.deepcopy(self.jeden_brzeg)
                        nowy_brzeg_2 = copy.deepcopy(self.drugi_brzeg)
                        nowy_stan = copy.deepcopy(self.stany)
                        nowy_brzeg_2.append(i)
                        nowy_brzeg_1.remove(i)
                        nowy_brzeg_1 = sorted(nowy_brzeg_1)
                        nowy_brzeg_2 = sorted(nowy_brzeg_2)
                        if [nowy_brzeg_1,nowy_brzeg_2, self.gracz] not in self.stany:
                            nowy_stan.append([nowy_brzeg_1,nowy_brzeg_2, copy.deepcopy(self.gracz)])
                            nastepna_tura = gra(nowy_brzeg_1, nowy_brzeg_2, (copy.deepcopy(self.gracz)+1)%2, nowy_stan)
                            kolejka.append(nastepna_tura)
                else:
                    nowy_brzeg_1 = copy.deepcopy(self.jeden_brzeg)
                    nowy_brzeg_2 = copy.deepcopy(self.drugi_brzeg)
                    nowy_stan = copy.deepcopy(self.stany)
                    nowy_brzeg_1 = sorted(nowy_brzeg_1)
                    nowy_brzeg_2 = sorted(nowy_brzeg_2)
                    if [nowy_brzeg_1,nowy_brzeg_2, self.gracz] not in self.stany:
                        nowy_stan.append([nowy_brzeg_1,nowy_brzeg_2, copy.deepcopy(self.gracz)])
                        nastepna_tura = gra(nowy_brzeg_1, nowy_brzeg_2, (copy.deepcopy(self.gracz)+1)%2, nowy_stan)
                        kolejka.append(nastepna_tura)    
                    for i in self.drugi_brzeg:
                        nowy_brzeg_1 = copy.deepcopy(self.jeden_brzeg)
                        nowy_brzeg_2 = copy.deepcopy(self.drugi_brzeg)
                        nowy_stan = copy.deepcopy(self.stany)
                        nowy_brzeg_1.append(i)
                        nowy_brzeg_2.remove(i)
                        nowy_brzeg_1 = sorted(nowy_brzeg_1)
                        nowy_brzeg_2 = sorted(nowy_brzeg_2)
                        if [nowy_brzeg_1,nowy_brzeg_2, self.gracz] not in self.stany:
                            nowy_stan.append([nowy_brzeg_1,nowy_brzeg_2, copy.deepcopy(self.gracz)])
                            nastepna_tura = gra(nowy_brzeg_1, nowy_brzeg_2, (copy.deepcopy(self.gracz)+1)%2, nowy_stan)
                            kolejka.append(nastepna_tura)
                kolejka.pop().graj()
            else:
                kolejka.pop().graj()

kolejka.append(gra([1,2,3],[],1,[]))
kolejka[0].graj()