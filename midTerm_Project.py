"""Mid term project to validate a Credit card number using a common algorithm."""

# Ben Batchelor
# CSIS 1300
# 2/25/2023


def validate_credit_card_number(credit_card_number):
    """This function carries out the validation of the card number."""
    # Double every other digit starting from the left.
    digits = [int(d) for d in str(credit_card_number)]
    for i in range(len(digits)-2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    # Add the digits and the odd ones from the credit card number.
    sum_new_digits = sum(digits)
    sum_odd_digits = sum(digits[1::2])
    # Check if the sum of the digits is divisible by 0.
    if (sum_new_digits + sum_odd_digits) % 10 == 0:
        return True
    else:
        return False


# Ask the user for a credit card number to validate.
CARD_NUMBER = input("Please enter a credit card number.")
# Loop to continue checking cards until user is done.
if validate_credit_card_number(CARD_NUMBER):
    print("Valid credit card number")
    check = input("Countinue? Y or N")
else:
    print("Invalid credit card number")
