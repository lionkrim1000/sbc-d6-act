def palindrome(input_string):
    input_string = input_string.replace(" ", "").lower()
    length = len(input_string)
    for i in range(length // 2):
        if input_string[i] != input_string[length - i - 1]:
            return False
    return True

string = input("Enter string: ")

if palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
