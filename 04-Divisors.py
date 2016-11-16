num = int(input("Give me a number: "))
result = []

for i in range(1, num+1):
    if num%i == 0:
        result.append(i)

print("The divisors of " + str(num) + " are " + str(result))
