import string

_encryption_key_list = [each for each in (string.ascii_lowercase + string.ascii_uppercase)]


def message_encryptor(message: str = "") -> str:
    encryption_map = {each: ord(each) for each in _encryption_key_list}
    return "".join([f"{int(encryption_map.get(each, '000')):03}" for each in message])


def message_decryptor(encrypted_message: str = "") -> str:
    decryption_map = {ord(each): each for each in _encryption_key_list}
    return "".join([" " if each == "000" else decryption_map.get(int(each), "000") for each in
                    [encrypted_message[i:i + 3] for i in range(0, len(encrypted_message), 3)]])


if __name__ == '__main__':
    message_to_encrypt = "This is Simple Encryption Message"
    print(f"Message to encrypt: {message_to_encrypt}")
    encrypted_msg = message_encryptor(message=message_to_encrypt)
    print(f"Encrypted Message: {encrypted_msg}")
    decrypted_msg = message_decryptor(encrypted_message=encrypted_msg)
    print(f"Decrypted Message: {decrypted_msg}")
