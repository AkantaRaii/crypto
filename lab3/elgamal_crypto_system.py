import random as r
p=int(input("entera large prime number p:"))
alpha=int(input("enter a ptimitive rootof p:"))
kprivate=r.randint(2,p-2)
kpublic=(alpha**kprivate)%p

i=r.randint(2,p-2)
kepheneral=(alpha**i)%p
kmasking=(kpublic**i)%p
x=int(input("enter number as text"))
y=(x*kmasking)%p
print("encrypted:",y)
kmasking_bob=(kepheneral**kprivate)%p
inverse_kmasking_bob=1
while True:
    if (kmasking_bob*inverse_kmasking_bob)%p==1:
        break
    inverse_kmasking_bob+=1
x_bob=(y*inverse_kmasking_bob)%p
print("decrypted",x_bob)