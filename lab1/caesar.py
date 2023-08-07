num_code=[]
cipher=""
plain=""
option=int(input("1.encryption\n2.decrypthion\n"))
if(option==1):
    plain=str(input("enter message:"))
    for i in plain:
        if(ord(i)<96):
            num_code.append(ord(i)-65)
        else:
            num_code.append(ord(i)-97)
    key=int(input("ener a key:"))
    print("cipher text is:")
    for i in num_code:
        if(i==-33):
            continue
        cipher=cipher+chr((i+key)%26+97)
    print(cipher)
elif(option==2):
    cipher=str(input("enter message:"))
    for i in cipher:
        if(ord(i)<96):
            num_code.append(ord(i)-65)
        else:
            num_code.append(ord(i)-97)
    key=int(input("ener a key:"))
    print("cipher text is:")
    for i in num_code:
        if(i==-33):
            continue
        plain=plain+chr((i-key)%26+97)
    print(plain)