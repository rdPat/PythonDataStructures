x=int(input("Enter no"))
s=0
while x>0:
    s=s+x%10
    x=x/10
print(int(s))