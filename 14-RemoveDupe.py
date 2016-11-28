import random

def rmv_dupe_1(list_):
    """Remove duplicates from a list using loop method."""
    result = []
    for i in list_:
        if i not in result:
            result.append(i)
    return result

def rmv_dupe_2(list_):
    """Remove duplicates from a list using set method."""
    return list(set(list_))

a = [random.randrange(0, 16) for i in range(random.randrange(16, 32))]
print(a)
print(rmv_dupe_1(a))
print(rmv_dupe_2(a))