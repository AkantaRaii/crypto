def miller_rabin(n,a):
    
    if(n-1)%2==0:
        k=1
    else:
        return False
    if(n-1)%(2**k)==0:
        m=(n-1)/(2**k)
        t=(a**m)%n
        if(t==1 or t==n-1):
            return True
        for i in range(1,k-1):
            t=(t**2)%n
            if(t==1):
                return False
            elif(t==n-1):
                return True
    return False
num=int(input("enter a number to check prime or composite:"))
if(miller_rabin(num,2)):
    print ("prime")
else:
    print("composite")
    
                
