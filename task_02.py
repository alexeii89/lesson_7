from abc import abstractmethod


class Cloves:
    cloves_all = []

    @abstractmethod
    def tissue_consumption(self):
        pass

    def sum(self):
        self.rez = sum((self.cloves_all))
        return self.rez


class Coat(Cloves):
    def __init__(self, V):
        super(Cloves, self).__init__()
        self.v = V
        self.cloves_all.append(self.tissue_consumption)

    @property
    def tissue_consumption(self):
        return self.v / 6.5 + 0.5


class Costume(Cloves):
    def __init__(self, H):
        super(Cloves, self).__init__()
        self.h = H
        self.cloves_all.append(self.tissue_consumption)

    @property
    def tissue_consumption(self):
        return 2 * self.h + 0.3


cos_1 = Costume(50)
cos_2 = Costume(48)
coat_1 = Coat(180)
coat_1 = Coat(165)

print(cos_1.tissue_consumption)
print(coat_1.tissue_consumption)

sum_all = Cloves()
print(sum_all.sum())
