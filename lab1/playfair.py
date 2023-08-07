# Function to generate a Playfair matrix from the key
def generate_playfair_matrix(key):
    key = key.replace("J", "I")
    key = key.upper()
    key = key.replace(" ", "")
    key_set = set(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = [[0] * 5 for _ in range(5)]
    
    i, j = 0, 0
    for char in key_set:
        matrix[i][j] = char
        j += 1
        if j == 5:
            i += 1
            j = 0
    
    for char in alphabet:
        if char not in key_set:
            matrix[i][j] = char
            j += 1
            if j == 5:
                i += 1
                j = 0
    
    return matrix

# Function to find the position of a character in the Playfair matrix
def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

# Function to perform Playfair encryption
def playfair_encrypt(plain_text, key):
    matrix = generate_playfair_matrix(key)
    encrypted_text = ""
    plain_text = plain_text.replace("J", "I").upper().replace(" ", "")
    i = 0
    while i < len(plain_text):
        char1 = plain_text[i]
        i += 1
        if i == len(plain_text):
            char2 = 'X'
        else:
            char2 = plain_text[i]
            i += 1
        
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        
        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]
    
    return encrypted_text

# Function to perform Playfair decryption
def playfair_decrypt(cipher_text, key):
    matrix = generate_playfair_matrix(key)
    decrypted_text = ""
    i = 0
    while i < len(cipher_text):
        char1 = cipher_text[i]
        i += 1
        char2 = cipher_text[i]
        i += 1
        
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        
        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]
    
    return decrypted_text

def main():
    # Input your full name and key
    full_name = input("Enter your full name: ")
    key = input("Enter the encryption key: ")

    # Encrypt the full name using Playfair cipher
    encrypted_name = playfair_encrypt(full_name, key)
    print("Encrypted Name:", encrypted_name)

    # Decrypt the encrypted name using Playfair cipher
    decrypted_name = playfair_decrypt(encrypted_name, key)
    print("Decrypted Name:", decrypted_name)

if __name__ == "__main__":
    main()
