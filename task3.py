import string
import random

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for i in range(length))
    return password
a=int(input("Enter the length of password: "))
print(generate_password(a))