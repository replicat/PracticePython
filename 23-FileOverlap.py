with open("23-primenumbers.txt", "r") as f:
    prime = [int(line) for line in f]

with open("23-happynumbers.txt", "r") as f:
    happy = [int(line) for line in f]

print([i for i in prime if i in happy])