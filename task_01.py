class Matrix:
    def __init__(self, list_arr):
        self.l = list(list_arr)

    def __add__(self, other):
        try:
            m_sum = []
            for i in range(len(self.l)):
                v_rez = []
                for j in range(len(self.l[i])):
                    z = int(m_1.l[i][j]) + int(m_2.l[i][j])
                    v_rez.append(z)
                m_sum.append(v_rez)
            return Matrix(m_sum)
        except IndexError:
            print("Error")

    def __str__(self):
        return "\n".join(['\t'.join(map(str, sublist)) for sublist in self.l])


m_1 = Matrix([[1, 2, 3], [3, 7, 9], [4, 2, 5]])
m_2 = Matrix([[3, 2, 1], [9, 5, 8], [3, 0, 7]])
m_sum = m_1 + m_2
print(m_sum)
