
def gcd(num1, num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)
    
p=int(input("enter p:"))
q=int(input("enter q:"))
x=int(input(f"Enter a number below {max(p,q)}: "))
n=p*q
phi=(p-1)*(q-1)
for i in range(1,phi):
    if gcd(i,phi)==1:
        e=i 
d=1
while True:
    if (e*d)%phi==1:
        break
    d+=1
y=(x**e)%n
print("encrypted text:",y)
xbob=(y**d)%n
print("decrypted text:",xbob)

