# Initial permutation choice table (PC-1)
pc1_table = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4,
]

# Key permutation choice table (PC-2)
pc2_table = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32,
]

# The initial 56-bit key
key = "1100110100000000110011001111111111110001101010101111000010101010"

# Initial permutation (PC-1)
permuted_key = ''.join(key[i - 1] for i in pc1_table)

# Split the key into C0 and D0
C0 = permuted_key[:28]
D0 = permuted_key[28:]

# Perform key generation for 16 rounds
round_keys = [] 
C, D = C0, D0
for round in range(1, 17):
    # Perform left circular shift on C and D
    if(round==1 or round==2 or round==9 or round==16):
        C = C[1:] + C[0]
        D = D[1:] + D[0]
    else:
        C = C[2:] + C[0]+C[1]
        D = D[2:] + D[0]+D[1]

    # Combine C and D
    combined_cd = C + D

    # Perform key permutation (PC-2) to generate the round key
    round_key = ''.join(combined_cd[i - 1] for i in pc2_table)
    round_keys.append(round_key)

# Display the 16 round keys
for i, round_key in enumerate(round_keys, start=1):
    print(f"Round {i} Key: {round_key}")
