# using code from 04
def find_divisor(num):
    result = []
    for i in range(1, num+1):
        if num%i == 0:
            result.append(i)
    return result

num = int(input("Give me a number: "))
if len(find_divisor(num)) <= 2:
    print("{} is a prime.".format(num))
else:
    print("{} is not a prime.".format(num))