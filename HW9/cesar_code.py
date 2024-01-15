def cesar_code(shift, ciphertext):
    decrypted_message = ""

    for char in ciphertext:
        if char.isalpha():
            # Визначення розшифрованого символу для букв
            if char.islower():
                decrypted_char = chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))

            decrypted_message += decrypted_char
        else:
            # Залишаємо неприналежні буквам символи без змін
            decrypted_message += char

    return decrypted_message
assert cesar_code(1,"az") == "zy"
assert cesar_code(3,"Wklv lv d whvw phvvdjh.") == "This is a test message."

def caesar_cipher_encrypt(shift):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            encrypted_result = ""
            for char in result:
                if char.isalpha():
                    if char.islower():
                        encrypted_char = chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
                    else:
                        encrypted_char = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
                    encrypted_result += encrypted_char
                else:
                    encrypted_result += char

            return encrypted_result

        return wrapper

    return decorator

@caesar_cipher_encrypt(shift=3)
def get_message(message):
    return message

# Отримання та виведення зашифрованого повідомлення
message = input('Type your message: ')
encrypted_message = get_message(message)
print(f'Yor message is encrypted: {encrypted_message}')

assert cesar_code(3, encrypted_message) == message
