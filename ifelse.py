x=int(input("enter int x"))
y=int(input("enter int y"))
z=int(input("enter int z"))

if(x>y):
    if(x>z):
        print("x is big")
elif(y>x and y>z):
    print("y is big")
elif(x==y and y==z):
    print("all same")
else:
    print("z is big")