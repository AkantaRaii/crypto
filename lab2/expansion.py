import random as r
expansion_p_box = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1]
def generateInput():
    input_block = ""
    for j in range(32):
        input_block += str(r.randint(0,1))
    return input_block
def expansion(data,p_box):
    result=""
    for i in p_box:
        result+=data[i-1]
    return result

data=generateInput()
print("data:",data)
expand_data=expansion(data,expansion_p_box)
print("expanded data:",expand_data)
print(len(expand_data))