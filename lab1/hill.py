# Function to generate key matrix
def generate_key_matrix(key_str, n):
    key_matrix = [[0] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            key_matrix[i][j] = ord(key_str[index]) % 65
        index += 1
    return key_matrix

# Function to calculate the determinant of a 2x2 matrix
def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

# Function to calculate the inverse of a matrix modulo 26
def inverse_matrix(matrix):
    det = determinant(matrix)
    det_inv = pow(det, -1, 26)
    if det_inv == 0:
        raise ValueError("Matrix is not invertible")
    
    inv_matrix = [[0] * len(matrix) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            cofactor = ((-1) ** (i + j)) * det_inv * determinant(minor(matrix, i, j))
            inv_matrix[i][j] = int(cofactor) % 26
    
    return inv_matrix

# Function to perform encryption
def encrypt(plain_text, key_matrix):
    n = len(key_matrix)
    cipher_text = ""
    for i in range(0, len(plain_text), n):
        chunk = [ord(c) - 65 for c in plain_text[i:i + n]]
        result = [0] * n
        for row in range(n):
            for col in range(n):
                result[row] += key_matrix[row][col] * chunk[col]
            result[row] %= 26
        cipher_text += ''.join(chr(c + 65) for c in result)
    return cipher_text

# Function to perform decryption
def decrypt(cipher_text, key_matrix):
    n = len(key_matrix)
    key_matrix_inv = inverse_matrix(key_matrix)
    plain_text = ""
    for i in range(0, len(cipher_text), n):
        chunk = [ord(c) - 65 for c in cipher_text[i:i + n]]
        result = [0] * n
        for row in range(n):
            for col in range(n):
                result[row] += key_matrix_inv[row][col] * chunk[col]
            result[row] %= 26
        plain_text += ''.join(chr(c + 65) for c in result)
    return plain_text

# Function to calculate the minor of a matrix
def minor(matrix, row, col):
    return [[matrix[i][j] for j in range(len(matrix[i])) if j != col] for i in range(len(matrix)) if i != row]

def main():
    # Set the key and matrix size
    key = "HILLKEY"
    matrix_size = 3  # You can adjust this for different matrix sizes

    # Generate the key matrix
    key_matrix = generate_key_matrix(key, matrix_size)

    # Input your full name
    full_name = input("Enter your full name: ")

    # Ensure the full name can be mapped onto the matrix
    full_name = full_name.upper().replace(" ", "")[:matrix_size**2]

    # Encryption
    encrypted_name = encrypt(full_name, key_matrix)
    print("Encrypted Name:", encrypted_name)

    # Decryption
    decrypted_name = decrypt(encrypted_name, key_matrix)
    print("Decrypted Name:", decrypted_name)

if __name__ == "__main__":
    main()
