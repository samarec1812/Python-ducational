import sys

arr = list(sys.stdin.read().split())
dictArr = dict()
listCountWords = list()

for w in arr:
    dictArr[w] = dictArr.get(w, -1)+1
    listCountWords.append(dictArr[w])
print(*listCountWords)
