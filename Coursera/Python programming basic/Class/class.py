from sys import stdin
import copy


class Matrix:
    def __init__(self, listArr):
        self.listArr = copy.deepcopy(listArr)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, i)) for i in self.listArr])

    def size(self):
        return len(self.listArr), len(self.listArr[0])


exec(stdin.read())
