sum1=0
n = int(input("Enter the number where you find the entered number is armstrong or not : " ))
len
s = n
while n!=0:
    r=n%10
    sum1=sum1+(r**3)
    n=n//10
if s==sum1:
    print("the given number",s,"is armstrong number")
else:
    print("the given number",s,"is not armstrong number")
