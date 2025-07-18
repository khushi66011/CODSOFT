#---------------------------------------
#Task2: PAssword generator using python
#--------------------------------------
#Project Description:---
# Prompts the user for password length and complexity
# Uses a combination of character sets (uppercase, lowercase, digits, symbols)
# Randomly generates a strong password
# Displays the result clearly.

import random
import string

def generate_password(length, complexity):
    """Generate a password of given length and complexity."""

    if length < 4:
        return "Password length should be at least 4 characters."

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = '@#$%&*!?_<>./'

    required_chars = []
    all_chars = ""

    # Setup based on complexity level
    if complexity == "1":              # Simple: only letters
        all_chars = lowercase + uppercase
        required_chars = [random.choice(lowercase), random.choice(uppercase)]
    elif complexity == "2":            # Medium: letters + digits
        all_chars = lowercase + uppercase + digits
        required_chars = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits)
        ]
    elif complexity == "3":            # Strong: letters + digits + symbols
        all_chars = lowercase + uppercase + digits + symbols
        required_chars = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(symbols)
        ]
    else:
        return "Invalid complexity level. Choose 1, 2, or 3."

    # Fill the rest of the password
    remaining_length = length - len(required_chars)
    password_chars = required_chars + random.choices(all_chars, k=remaining_length)

    # Shuffle to avoid predictable pattern
    random.shuffle(password_chars)

    return ''.join(password_chars)


def main():
    print("Welcome to the Python Password Generator!\n")

    try:
        length = int(input("Enter password length (minimum 4): "))   # Input the prompt for password length and complexity

        print("\n Select complexity level:")     
        print("1 - Simple password")
        print("2 - Medium password")
        print("3 - Strong password")

        complexity = input("Enter choice (1/2/3): ")

        # Generate and display password
        password = generate_password(length, complexity)

        if password.startswith(" "):
            print(password)
        else:
            print(f"\nYour generated password is:\n{password}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
