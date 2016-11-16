a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
result = []

x = int(input("Give me a number: "))

for num in a:
    if num < x:
        result.append(num)

print(result)