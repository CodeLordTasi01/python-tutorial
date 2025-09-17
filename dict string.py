dict={'a':'rahul','b':'shahid','c':'rohit'}
z={}
for i in dict:
     for j in dict:
        if dict[i]==dict[i+1]:
            z.append(dict[i])
print(z)
               
               
