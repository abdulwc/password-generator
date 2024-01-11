import random
import string

def generate_password(length, use_special_chars=True):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''

    # Ensuring the password contains at least one character of each type
    password = random.choice(lower) + random.choice(upper) + random.choice(digits)
    password += random.choice(special_chars) if use_special_chars else random.choice(lower + upper + digits)

    # Filling the rest of the password length with a mix of all characters
    all_chars = lower + upper + digits + special_chars
    password += ''.join(random.choice(all_chars) for _ in range(length - 4))

    # Shuffling the password to ensure randomness
    password = ''.join(random.sample(password, len(password)))

    return password

# Directly asking the user for the password length and character inclusion
try:
    password_length = int(input("Enter desired password length: "))
    include_special_chars = input("Include special characters? (Yes/No): ").lower() == 'yes'
    new_password = generate_password(password_length, include_special_chars)
    print("Generated Password:", new_password)
except ValueError:
    print("Please enter a valid number.")
