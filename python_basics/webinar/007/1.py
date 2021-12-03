class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < len(self.matrix):
            return self.matrix[self.current]
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.matrix[index]

    def __len__(self):
        return len(self.matrix)

    def __str__(self):
        result = ''
        for line in self.matrix:
            for num in line:
                result += '{:>6}'.format(num)
            result += '\n'
        return result

    def __add__(self, other):
        sum_list = list()
        for i in range(len(self)):
            tmp_list = [sum(tup) for tup in zip(self[i], other[i])]
            sum_list.append(tmp_list)
        return Matrix(sum_list)


m_1 = Matrix([
    [3, 5, 8],
    [8, 3, 7],
    [3, 3, -100]
])

m_2 = Matrix([
    [4, 3, 3],
    [-2, 4, 5],
    [5, 20, -200]
])

print(m_1)
print(m_2)
print(m_1 + m_2)
