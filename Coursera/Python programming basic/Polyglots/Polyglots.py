countPeople = int(input())
famousLanguage = set()
allLanguages = set()
for counter, i in enumerate(range(countPeople)):
    thinkLanguage = int(input())
    includeLanguage = set()
    for j in range(thinkLanguage):
        includeLanguage.add(input())
    if counter == 0:
        famousLanguage = includeLanguage
    famousLanguage &= includeLanguage
    allLanguages |= includeLanguage
print(len(famousLanguage), *sorted(famousLanguage), sep="\n")
print(len(allLanguages), *sorted(allLanguages), sep="\n")
