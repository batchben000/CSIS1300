"""Program to check if a given string is a palindrome."""

# Ben Batchelor
# CSIS 1300
# 2/25/2023

def is_palindrome(string):
    """This function checks if the reverse string is the same as the regular string."""
    # This converts the string to lower case and then removes all non alphabet characters
    string = ''.join(e for e in string if e.isalnum()).lower()
    # Check if the string is the same as its reverse
    return string == string[::-1]


# Checks if the user_input is a palindrome using the is_palindrome function.
while True:
    # Ask the user for a string to check
    user_input = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

# Here we check if they would like to try again and enter another string
# if they do then y for continue or anything else for break.
    check = input("Do you want to continue? Yes(y) or No(n)")
    if str(check) == "y":
        continue
    else:
        break
