# Function to perform Rail Fence encryption
def rail_fence_encrypt(plain_text, key):
    encrypted_text = ""
    rail = [['\n' for _ in range(len(plain_text))] for _ in range(key)]
    direction = False
    row, col = 0, 0
    
    for char in plain_text:
        if row == 0 or row == key - 1:
            direction = not direction
        rail[row][col] = char
        col += 1
        
        if direction:
            row += 1
        else:
            row -= 1
    
    for i in range(key):
        for j in range(len(plain_text)):
            if rail[i][j] != '\n':
                encrypted_text += rail[i][j]
    
    return encrypted_text

# Function to perform Rail Fence decryption
def rail_fence_decrypt(cipher_text, key):
    decrypted_text = ""
    rail = [['\n' for _ in range(len(cipher_text))] for _ in range(key)]
    direction = False
    row, col = 0, 0
    
    for _ in range(len(cipher_text)):
        if row == 0 or row == key - 1:
            direction = not direction
        rail[row][col] = '*'
        col += 1
        
        if direction:
            row += 1
        else:
            row -= 1
    
    index = 0
    for i in range(key):
        for j in range(len(cipher_text)):
            if rail[i][j] == '*' and index < len(cipher_text):
                rail[i][j] = cipher_text[index]
                index += 1
    
    row, col = 0, 0
    for _ in range(len(cipher_text)):
        if row == 0 or row == key - 1:
            direction = not direction
        if rail[row][col] != '\n':
            decrypted_text += rail[row][col]
        col += 1
        
        if direction:
            row += 1
        else:
            row -= 1
    
    return decrypted_text

def main():
    # Input your full name and key
    full_name = input("Enter your full name: ")
    key = int(input("Enter the encryption key: "))

    # Encrypt the full name using Rail Fence cipher
    encrypted_name = rail_fence_encrypt(full_name, key)
    print("Encrypted Name:", encrypted_name)

    # Decrypt the encrypted name using Rail Fence cipher
    decrypted_name = rail_fence_decrypt(encrypted_name, key)
    print("Decrypted Name:", decrypted_name)

if __name__ == "__main__":
    main()
