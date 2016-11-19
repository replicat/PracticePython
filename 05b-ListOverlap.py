from random import randint

def genList(x, min, max):
    """Generate a list of x random numbers within the range of [min, max)]"""
    returnList = []
    for i in range(x):
        returnList.append(randint(min, max))
    return returnList

a = genList(randint(8, 16), 0, 64)
b = genList(randint(8, 16), 0, 64)
print("First list: " + str(a))
print("Second list: " + str(b))

#The one-liner
print("Overlap: " + str(list(set([i for i in a if i in b]))))