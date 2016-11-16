def isPalindrome(a):
    return a == a[::-1]

print("The string is a palindrome." if isPalindrome(input("Give me a string: ")) else "The string is not a palindrome.")
