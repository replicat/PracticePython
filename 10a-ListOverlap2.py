import random

a = [random.randint(1, 64) for i in range(16)]
b = [random.randint(1, 64) for i in range(16)]
print("List a:\t\t{}".format(a))
print("List b:\t\t{}".format(b))

# Convert to set to remove duplicates, then convert back to list.
print("Overlap:\t{}".format(list(set(num for num in a if num in b))))