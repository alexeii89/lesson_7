class Cell:
    def __init__(self, nucleus):
        self.nucl = nucleus

    def __add__(self, other):
        sum = self.nucl + other.nucl
        return Cell(sum)

    def __sub__(self, other):
        sub = self.nucl - other.nucl
        if sub>=0:
            return Cell(sub)
        else:
            return "Разность меньше 0"

    def __mul__(self, other):
        return Cell(self.nucl * other.nucl)

    def __truediv__(self, other):
        return Cell(self.nucl // other.nucl)

    def make_order(self, p_nucl):
        r = self.nucl // p_nucl
        en = self.nucl % p_nucl
        for i in range(r):
            for j in range(p_nucl):
                print('*', end='')
            print('')
        for n in range(en):
            print('*')

c_1 = Cell(9)
c_2 = Cell(3)

c_add = c_1 + c_2
print(c_add.nucl)

c_sub = c_1 - c_2
print(c_sub.nucl)

c_mul = c_1 * c_2
print(c_mul.nucl)

c_div = c_1 / c_2
print(c_div.nucl)

c_1.make_order(4)
