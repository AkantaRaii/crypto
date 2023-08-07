# Function to perform Vigenere encryption
def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(plain_text)):
        char = plain_text[i]
        key_char = key[i % key_length]
        if char.isalpha():
            shift = ord(key_char.upper()) - ord('A')
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Function to perform Vigenere decryption
def vigenere_decrypt(cipher_text, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        key_char = key[i % key_length]
        if char.isalpha():
            shift = ord(key_char.upper()) - ord('A')
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    # Input your full name and key
    full_name = input("Enter your full name: ")
    key = input("Enter the encryption key: ")

    # Encrypt the full name using Vigenere cipher
    encrypted_name = vigenere_encrypt(full_name, key)
    print("Encrypted Name:", encrypted_name)

    # Decrypt the encrypted name using Vigenere cipher
    decrypted_name = vigenere_decrypt(encrypted_name, key)
    print("Decrypted Name:", decrypted_name)

if __name__ == "__main__":
    main()
