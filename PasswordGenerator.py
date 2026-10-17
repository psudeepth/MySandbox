import string
import random

def generate_password(password_length:int=0)->str:
    password_keys = f"{string.digits}{string.punctuation}{string.ascii_uppercase}{string.ascii_lowercase}"
    return "".join(random.choices(password_keys, k=password_length))

if __name__ == '__main__':
    password_len = 16
    generated_password = generate_password(password_length=password_len)
    print(generated_password)