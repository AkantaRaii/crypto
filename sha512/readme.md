# SHA-512 Implementation in Python

## Description

This repository contains a straightforward Python implementation of SHA-512.

## What is SHA-512

SHA-512 is a cryptographic hash function that generates a 512-bit (64-byte) hash value. It operates on 1024 bits per block and goes through 80 rounds of processing.

---

## Algorithm

1. Request user input for the message.
2. Encode the input message using `UTF-8`.
3. Apply the necessary padding to the message.
4. Divide the message into `N * 1024` blocks if the message length is greater than or equal to 896 bits.
5. Initialize constants K and HASH_VALUE.
6. For each input block, apply the `compression_function()`.
7. The final hash value is stored in the HASH_VALUE constant, which serves as the seed for hashing another message.

---

## Functions Used

### Ch(e, f, g)

```python
return (e & f) ^ (~e & g)
```

The `Ch` function is a bitwise operation used in the SHA-512 compression function, working on three 64-bit inputs (e, f, and g) and producing a 64-bit result.

### Maj(a, b, c)

```python
return (a & b) ^ (a & c) ^ (b & c)
```

The `Maj` function is another bitwise operation used in the SHA-512 compression function, operating on three 64-bit inputs (a, b, and c) and returning a 64-bit result.

### rotr(x, n)

```python
return (x >> n) | (x << (64 - n))
```

The `rotr()` function performs a bitwise right rotation of a 64-bit value "x" by "n" bits.

### summation_a(a)

```python
return rotr(a, 28) ^ rotr(a, 34) ^ rotr(a, 39)
```

The `summation_a()` function combines right rotations and XOR operations on a 64-bit input "a," resulting in a 64-bit output.

### summation_e(e)

```python
return rotr(e, 14) ^ rotr(e, 18) ^ rotr(e, 41)
```

The `summation_e()` function combines right rotations and XOR operations on a 64-bit input "e," producing a 64-bit result.

### sigma_0(word)

```python
return rotr(word, 1) ^ rotr(word, 8) ^ (word >> 7)
```

The `sigma_0()` function calculates a value based on right rotations and XOR operations on a 64-bit word.

### sigma_1(word)

```python
return rotr(word, 19) ^ rotr(word, 61) ^ (word >> 6)
```

The `sigma_1` function calculates another value based on right rotations and XOR operations on a 64-bit word.

### addition_modulo_2_64(value)

```python
return value % (2**64)
```

The `addition_modulo_2_64()` function performs modular addition of a 64-bit value, ensuring that the result doesn't exceed 64 bits.

### pad_message(message)

```python
message += b"\x80"  # Adding 1 byte (10000000)
while len(message) % 128 != 112:
    message += b"\x00"
message += (len(message) * 8).to_bytes(16, "big")
return message
```

The `pad_message()` function adds padding to the input message, making its length a multiple of 128 bytes. It also appends the message length in bits at the end.

### divide_to_blocks(message)

```python
blocks = []
for i in range(0, len(message), 128):
    blocks.append(message[i: i + 128])

return blocks
```

The `divide_to_blocks` function splits a padded message into 128-byte blocks, which are processed by the SHA-512 compression function.

### SHA-512 Compression Function

#### compression_function(message)

```python
for t in range(16):
    W[t] = int.from_bytes(message[t * 8: (t + 1) * 8], byteorder="big")

for t in range(16, 80):
    W[t] = sigma_1(W[t - 2] + W[t - 7]) + sigma_0(W[t - 15] + W[t - 16])
```

The first loop calculates W<sub>0</sub> - W<sub>15</sub, and the second loop computes W<sub>16</sub> - W<sub>79</sub.

```python
for t in range(80):
    T1 = h + (Ch(e, f, g) + (rotr(e, 14) ^ rotr(e, 18) ^ rotr(e, 41)) + K[t] + W[t])
    T2 = (rotr(a, 28) ^ rotr(a, 34) ^ rotr(a, 39)) + Maj(a, b, c)

    h = g
    g = f
    f = e
    e = addition_modulo_2_64(d + T1)
    d = c
    c = b
    b = a
    a = addition_modulo_2_64(T1 + T2)

# Intermediate Hash values
HASH_VALUE[0] = addition_modulo_2_64(HASH_VALUE[0] + a)
HASH_VALUE[1] = addition_modulo_2_64(HASH_VALUE[1] + b)
HASH_VALUE[2] = addition_modulo_2_64(HASH_VALUE[2] + c)
HASH_VALUE[3] = addition_modulo_2_64(HASH_VALUE[3] + d)
HASH_VALUE[4] = addition_modulo_2_64(HASH_VALUE[4] + e)
HASH_VALUE[5] = addition_modulo_2_64(HASH_VALUE[5] + f)
HASH_VALUE[6] = addition_modulo_2_64(HASH_VALUE[6] + g)
HASH_VALUE[7] = addition_modulo_2_64(HASH_VALUE[7] + h)
```

The `compression_function` is the core of the SHA-512 hashing process, taking a 128-byte message block as input and updating the `HASH_VALUE` accordingly.

## Usage

1. Run the program and input a message.
2. The code pads the message, divides it into blocks, and initiates the SHA-512 hashing process.
3. The final 512-bit (64-byte) hash value is printed as a hexadecimal string.# SHA-512 Implementation in Python

## Description

This repository contains a straightforward Python implementation of SHA-512.

## What is SHA-512

SHA-512 is a cryptographic hash function that generates a 512-bit (64-byte) hash value. It operates on 1024 bits per block and goes through 80 rounds of processing.

---

## Algorithm

1. Request user input for the message.
2. Encode the input message using `UTF-8`.
3. Apply the necessary padding to the message.
4. Divide the message into `N * 1024` blocks if the message length is greater than or equal to 896 bits.
5. Initialize constants K and HASH_VALUE.
6. For each input block, apply the `compression_function()`.
7. The final hash value is stored in the HASH_VALUE constant, which serves as the seed for hashing another message.

---

## Functions Used

### Ch(e, f, g)

```python
return (e & f) ^ (~e & g)
```

The `Ch` function is a bitwise operation used in the SHA-512 compression function, working on three 64-bit inputs (e, f, and g) and producing a 64-bit result.

### Maj(a, b, c)

```python
return (a & b) ^ (a & c) ^ (b & c)
```

The `Maj` function is another bitwise operation used in the SHA-512 compression function, operating on three 64-bit inputs (a, b, and c) and returning a 64-bit result.

### rotr(x, n)

```python
return (x >> n) | (x << (64 - n))
```

The `rotr()` function performs a bitwise right rotation of a 64-bit value "x" by "n" bits.

### summation_a(a)

```python
return rotr(a, 28) ^ rotr(a, 34) ^ rotr(a, 39)
```

The `summation_a()` function combines right rotations and XOR operations on a 64-bit input "a," resulting in a 64-bit output.

### summation_e(e)

```python
return rotr(e, 14) ^ rotr(e, 18) ^ rotr(e, 41)
```

The `summation_e()` function combines right rotations and XOR operations on a 64-bit input "e," producing a 64-bit result.

### sigma_0(word)

```python
return rotr(word, 1) ^ rotr(word, 8) ^ (word >> 7)
```

The `sigma_0()` function calculates a value based on right rotations and XOR operations on a 64-bit word.

### sigma_1(word)

```python
return rotr(word, 19) ^ rotr(word, 61) ^ (word >> 6)
```

The `sigma_1` function calculates another value based on right rotations and XOR operations on a 64-bit word.

### addition_modulo_2_64(value)

```python
return value % (2**64)
```

The `addition_modulo_2_64()` function performs modular addition of a 64-bit value, ensuring that the result doesn't exceed 64 bits.

### pad_message(message)

```python
message += b"\x80"  # Adding 1 byte (10000000)
while len(message) % 128 != 112:
    message += b"\x00"
message += (len(message) * 8).to_bytes(16, "big")
return message
```

The `pad_message()` function adds padding to the input message, making its length a multiple of 128 bytes. It also appends the message length in bits at the end.

### divide_to_blocks(message)

```python
blocks = []
for i in range(0, len(message), 128):
    blocks.append(message[i: i + 128])

return blocks
```

The `divide_to_blocks` function splits a padded message into 128-byte blocks, which are processed by the SHA-512 compression function.

### SHA-512 Compression Function

#### compression_function(message)

```python
for t in range(16):
    W[t] = int.from_bytes(message[t * 8: (t + 1) * 8], byteorder="big")

for t in range(16, 80):
    W[t] = sigma_1(W[t - 2] + W[t - 7]) + sigma_0(W[t - 15] + W[t - 16])
```

The first loop calculates W<sub>0</sub> - W<sub>15</sub, and the second loop computes W<sub>16</sub> - W<sub>79</sub.

```python
for t in range(80):
    T1 = h + (Ch(e, f, g) + (rotr(e, 14) ^ rotr(e, 18) ^ rotr(e, 41)) + K[t] + W[t])
    T2 = (rotr(a, 28) ^ rotr(a, 34) ^ rotr(a, 39)) + Maj(a, b, c)

    h = g
    g = f
    f = e
    e = addition_modulo_2_64(d + T1)
    d = c
    c = b
    b = a
    a = addition_modulo_2_64(T1 + T2)

# Intermediate Hash values
HASH_VALUE[0] = addition_modulo_2_64(HASH_VALUE[0] + a)
HASH_VALUE[1] = addition_modulo_2_64(HASH_VALUE[1] + b)
HASH_VALUE[2] = addition_modulo_2_64(HASH_VALUE[2] + c)
HASH_VALUE[3] = addition_modulo_2_64(HASH_VALUE[3] + d)
HASH_VALUE[4] = addition_modulo_2_64(HASH_VALUE[4] + e)
HASH_VALUE[5] = addition_modulo_2_64(HASH_VALUE[5] + f)
HASH_VALUE[6] = addition_modulo_2_64(HASH_VALUE[6] + g)
HASH_VALUE[7] = addition_modulo_2_64(HASH_VALUE[7] + h)
```

The `compression_function` is the core of the SHA-512 hashing process, taking a 128-byte message block as input and updating the `HASH_VALUE` accordingly.

## Usage

1. Run the program and input a message.
2. The code pads the message, divides it into blocks, and initiates the SHA-512 hashing process.
3. The final 512-bit (64-byte) hash value is printed as a hexadecimal string.