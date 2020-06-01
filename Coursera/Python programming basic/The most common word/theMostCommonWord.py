import sys

arr = list(sys.stdin.read().split())
dictArr = dict()

for w in arr:
    dictArr[w] = dictArr.get(w, 0) + 1
sumWord = 0
s = ''
for key in sorted(dictArr):
    if dictArr[key] > sumWord:
        sumWord = dictArr[key]
        s = key
print(s)
