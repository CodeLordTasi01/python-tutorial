data="Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
x=data.split()
print(x)
z={}
for i in x:
  if i in z:
     z[i]=z[i]+1
  else:
      z[i]=1
print(z)
