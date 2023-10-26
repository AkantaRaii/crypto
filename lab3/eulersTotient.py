li = []
phii = []
count = 0

def gcd(num1, num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)




n = int(input("Enter a number:"))
li = [i for i in range(n)]
for i in li:
    if gcd(i, n) == 1:
        count += 1
        phii.append(i)
print("Count of numbers relatively prime to", n, "is", count)
print("Numbers relatively prime to", n, "are:", phii)
