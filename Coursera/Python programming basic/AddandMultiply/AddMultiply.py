from sys import stdin
import copy


class Matrix:
    def __init__(self, listArr):
        self.listArr = copy.deepcopy(listArr)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, i)) for i in self.listArr])

    def size(self):
        return len(self.listArr), len(self.listArr[0])

    def __add__(self, other):
        result = []
        for i in range(len(self.listArr)):
            tmp = []
            for j in range(len(self.listArr[0])):
                tmp.append(self.listArr[i][j] + other.listArr[i][j])
            result.append(tmp)
        return Matrix(result)

    def __mul__(self, other):
        result = []
        for i in range(len(self.listArr)):
            tmp = []
            for j in range(len(self.listArr[0])):
                tmp.append(self.listArr[i][j] * other)
            result.append(tmp)
        return Matrix(result)

    __rmul__ = __mul__


exec(stdin.read())
