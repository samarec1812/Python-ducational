n = int(input())

synonyms = dict()
for i in range(n):
    s = input().split()
    synonyms[s[0]] = s[1]
    synonyms[s[1]] = s[0]
s1 = input()
print(synonyms[s1])
