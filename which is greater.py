x=int(input("enter first number:"))
y=int(input("enter second number:"))
z=int(input("enter third number:"))
if x>y and x>z:
    print("first number is greater:",x)
elif y>x and y>z:
    print("second number is greater:",y)
else:
    print("third number is greater:",z)
