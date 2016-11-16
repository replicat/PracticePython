from random import randint

def genList(x, min, max):
    """Generate a list of x random numbers within the range of [min, max)]"""
    returnList = []
    for i in range(x):
        returnList.append(randint(min, max))
    return returnList

a = genList(randint(8, 16), 0, 64)
b = genList(randint(8, 16), 0, 64)
resultList = []

for i in a:
    if i in b and i not in resultList:
        resultList.append(i)

print("First list: " + str(a))
print("Second list: " + str(b))
print("Overlap: " + str(resultList))