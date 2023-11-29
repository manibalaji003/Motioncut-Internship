import string
import random

def generate_strong_password(length):
    if length < 4:
        print("Password length should be at least 4")
        return

    all_chars = [random.choice(string.ascii_lowercase),
                 random.choice(string.ascii_uppercase),
                 random.choice(string.digits),
                 random.choice(string.punctuation)]

    if length > 4:
        all_chars += [random.choice(string.ascii_letters + string.digits + string.punctuation)
                      for _ in range(length-4)]

    random.shuffle(all_chars)
    password = ''.join(all_chars)
    return password

a = int(input("Enter the length of password: "))
print(generate_strong_password(a))
