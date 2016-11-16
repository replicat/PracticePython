num = int(input("Give me a number to check: "))
check = int(input("Give me a number to divide by: "))
if num%check == 0:
    print(str(num) + " is divisible by " + str(check) + "!")
else:
    print(str(num) + " is not divisible by " + str(check) + "!")