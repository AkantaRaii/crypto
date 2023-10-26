def if_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def primitive(n):
    p_roots=[]
    temp_mod=[]
    for num in range(2,n):
        status=True
        for power in range(1,n):
            mod=(num**power)%n
            if mod not in temp_mod:
                temp_mod.append(mod)
            else:
                status=False
                break
        if status:
            p_roots.append(num)
        temp_mod.clear()
    return p_roots
num=int(input("number to find primitive roots:"))
print(primitive(num))
        
       