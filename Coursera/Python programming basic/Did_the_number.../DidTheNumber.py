arr = list(map(int, input().split()))
setArr = set()
for w in arr:
    if w not in setArr:
        print('NO')
        setArr.add(w)
    else:
        print('YES')
