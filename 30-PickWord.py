import random
with open("30-sowpods.txt", "r") as f:
    print(random.choice(f.readlines()).strip())