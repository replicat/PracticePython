# Usable even with more than three numbers.
def fake_max(list_):
    current_max = None
    for i in list_:
        current_max = i if current_max == None or i > current_max else current_max
    return current_max

print(fake_max(int(i) for i in input("Give me some numbers, each seperated by a comma(,): ").split(",")))