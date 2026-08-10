import string
import secrets

def get_password_length():
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            if length < 8:
                print("⚠️ For security, please choose at least 8 characters.")
                continue
            return length
        except ValueError:
            print("⚠️ Please enter a valid number.")

def generate_password(length):
    # Character pool: letters + digits (as required by the task)
    characters = string.ascii_letters + string.digits

    # Efficient string building using list + join(), not +=
    password_chars = [secrets.choice(characters) for _ in range(length)]
    password = ''.join(password_chars)
    return password

def main():
    print("🔐 RANDOM PASSWORD GENERATOR 🔐")
    length = get_password_length()
    password = generate_password(length)
    print(f"\n✅ Your secure password: {password}")

if __name__ == "__main__":
    main()