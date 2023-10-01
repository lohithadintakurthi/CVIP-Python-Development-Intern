import random
import string

def generate_password(length, uppercase, lowercase, digits, special_chars):
    characters = ""
    
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not any([uppercase, lowercase, digits, special_chars]):
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")

    length = int(input("Enter the desired password length: "))
    uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    digits = input("Include digits? (yes/no): ").lower() == 'yes'
    special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, uppercase, lowercase, digits, special_chars)

    if password:
        print(f"\nGenerated Password: {password}")
    else:
        print("Password generation failed. Please try again.")

if __name__ == "__main__":
    main()