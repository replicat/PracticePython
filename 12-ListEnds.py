import random

def list_ends(list_):
    return list_[::len(list_)-1]

a = random.sample(range(0, 32), random.randrange(8, 16))
print(a)
print(list_ends(a))