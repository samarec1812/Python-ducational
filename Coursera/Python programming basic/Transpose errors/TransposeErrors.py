from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, listArr):
        self.listArr = copy.deepcopy(listArr)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, i)) for i in self.listArr])

    def size(self):
        return len(self.listArr), len(self.listArr[0])

    def __add__(self, other):
        if len(self.listArr) != len(other.listArr) or \
                len(self.listArr[0]) != len(other.listArr[0]):
            raise MatrixError(self, other)
        result = []
        for i in range(len(self.listArr)):
            tmp = []
            for j in range(len(self.listArr[0])):
                tmp.append(self.listArr[i][j] + other.listArr[i][j])
                result.append(tmp)
            return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = []
            for i in range(len(self.listArr)):
                tmp = []
                for j in range(len(self.listArr[0])):
                    tmp.append(self.listArr[i][j] * other)
                result.append(tmp)
        elif isinstance(other, Matrix):
            # ru.wikipedia.org/wiki/Умножение_матриц - Определение
            if len(self.listArr[0]) != len(other.listArr):
                raise MatrixError(self, other)
            m = len(self.listArr[0])
            l = len(self.listArr)
            n = len(other.listArr[0])
            result = [[None for j in range(n)] for i in range(l)]
            for i in range(l):
                for j in range(n):
                    sum = 0
                    for r in range(m):
                        sum += self.listArr[i][r] * other.listArr[r][j]
                    result[i][j] = sum
        else:
            raise MatrixError(self, other)
        return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        result = [[None for j in self.listArr]
                  for i in self.listArr[0]]
        for i in range(len(self.listArr)):
            for j in range(len(self.listArr[0])):
                result[j][i] = self.listArr[i][j]
        self.listArr = result
        return Matrix(self.listArr)

    @staticmethod
    def transposed(instance):
        result = [[None for j in instance.listArr]
                  for i in instance.listArr[0]]
        for i in range(len(instance.listArr)):
            for j in range(len(instance.listArr[0])):
                result[j][i] = instance.listArr[i][j]
        return Matrix(result)


exec(stdin.read())
