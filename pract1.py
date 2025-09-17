''''for i in range (0,5):
    for j in range (5,i,-1):
        print(j,end=" ")
    print()


ticket_no=int(input("enter a ticket no"))
n=5
ticket_price=500
ticket_total=0
    
if ticket_no<5:
    for i in range(1,ticket_no+1):
       if i <3:
          ticket_total=ticket_price
          print(ticket_total)
       else:
          ticket_total=ticket_price-(ticket_price)*n/100
          n=n+2
          print(ticket_total)
else:
   print("ticket is not allwed")


x="A012BC04"
y=""
z=""
for i in x:
    if i.isalpha():
        y+=i
    if i.isdigit():
        z+=i

print(y)
print(z)

class invalidAge(Exception):
    pass
try:
    age = int(input("enter the age"))
    if age<18:
        raise invalidAge
    else:
        print("you are eligible ")
except invalidAge:
    print("InvalidAge is occure")


class SalaryNorthRangeError(Exception):
    pass
try:
    salary = int(input("enter the salary"))
    name = input("enter name")
    if salary<20000 or salary>50000:
        raise SalaryNorthRangeError
    else:
        print(salary,end="")
        print("you are not in range")
except SalaryNorthRangeError:
    print("you are in range")

def avg(scores):
    assert len(scores)!=0,"the list is empty:"
    return sum(scores)/len(scores)
scores2=[4,5,10,1]
print("the average of scores2:",avg(scores2))

scores1=[8,9,15,6]
print("the average of scores1:",avg(scores1))


file1=open("mynew.txt","w")
file1.write("hello file")
file1.close()'''



'''class tas:
    def __init__(s,n1,n2):
        s.num1=n1
        s.num2=n2
    def tasadd(s):
        r1=s.num1+s.num2
        print("add is:",r1)
        r2=s.num1-s.num2
        print("subs is:",r2)
        r3=s.num1*s.num2
        print("multi is:",r3)
        r4=s.num1/s.num2
        print("divide is:",r4)
        r5=s.num1%s.num2
        print("remin is:",r5)
        r6=s.num1//s.num2
        print("floor is:",r6)
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
tas=tas(n1,n2)
tas.tasadd()




class tasleem:
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2
    def tasadd(self):
        r1=self.num1+self.num2
        print("add is:",r1)
    def tassub(self):
        r2=self.num1-self.num2
        print("subs is:",r2)
    def tasmul(self):
        r3=self.num1*self.num2
        print("multi is:",r3)
    def tasdiv(self):
        r4=self.num1/self.num2
        print("divide is:",r4)
    def tasremen(self):
        r5=self.num1%self.num2
        print("remin is:",r5)
    def tasfloor(self):
        r6=self.num1//self.num2
        print("floor is:",r6)
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
tasobj=tasleem(n1,n2)
tasobj.tasadd()
tasobj.tassub()
tasobj.tasmul()
tasobj.tasdiv()
tasobj.tasremen()
tasobj.tasfloor()



class chalk:
    def __init__(self):
        self.length=12
        self.radius=3.5
        self.color="white"
        self.shape="cylindricut"
        self.sur_area=2*3.14*3.5*12
        self.volume=3.14*3.5**2*12
        

    def write(self):
        print("wrote something")
        self.length=self.length-3
        self.sur_area=2*3.14*self.radius*self.length
        self.volume=3.14*self.radius**2*self.length
        
c1=chalk()
print(c1.__dict__)
c2=chalk()
c1.write()
c2.write()
print(c1.__dict__)



class student:
    def __init__(self):
        self.roll_number=2312584
        self.name="Tasleem Shah"
        self.branch="MCA"
        self.section="1c"
        

    def display(self,roll_number,name,branch,section):
        print("Student Detail")
        
c1=student()
print(c1.__dict__)


class T:
    def __init__(self,a,b):
        self.a=a
        self.__b=b
    def display(self):
        print(self.__b)
        
t1=T(2,3)
print(t1.a)
t1.display()
print(t1._T__b)


class student:
    def __init__(self,id1,name):
        self.__id1=id1
        self.name=name
    def get_id1(self):
        return self.__id1
    def set_id1(self,id1):
        self.__id1=id1
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
stu_obj=student(101,"Suji")
print("before update")
print(stu_obj.get_id1())
print(stu_obj.get_name())
print("after update")
stu_obj.set_id1(102)
stu_obj.set_name("Suji again")
print(stu_obj.get_id1())
print(stu_obj.get_name())
print("after update and update")
stu_obj.set_id1(103)
stu_obj.set_name("suji again and again")
print(stu_obj.get_id1())
print(stu_obj.get_name())


class customer:
    def __init__(self,Id,name,age,wallet_balance):
        self.Id=Id
        self.name=name
        self.age=age
        self.__wallet_balance=wallet_balance
    def get_wallet_balance(self):
        return self.__wallet_balance
    def set_wallet_balance(self,amount):
        if amount<1000 and amount>0:
            self.__wallet_balance+=amount
cust_obj=customer(101,"Suji",18,1000)
print("before update")
print(cust_obj.Id)
print(cust_obj.name)
print(cust_obj.age)
print(cust_obj.get_wallet_balance())
print("after update")
cust_obj.set_wallet_balance(800)
print(cust_obj.Id)
print(cust_obj.name)
print(cust_obj.age)
print(cust_obj.get_wallet_balance())


a=[]
n=int(input())
for i in range(0, n):
    b=int(input())
    a.append(b)
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[i]>=a[j]:
            k=a[i]
            a[i]=a[j]
            a[j]=k
print("after sort:",a)

a=[]
n=int(input())
for i in range (0, n):
    b=int(input())
    a.append(b)
for i in range (0, len(a)):
    for j in range (i+1, len(a)):
        if a[i]<=a[j]:
            k=a[i]
            a[i]=a[j]
            a[j]=k
print("array sort:",a)




class Demo:
    num=5
    def __init__(self,status):
        num=10
        print(status,num)
d=Demo('A')




n=(input())
s=0
for i in n:
    s+=int(i)
    print(s)


num = 12345
sum = 0
while num!=1:
	digit = int(num%10)
	sum += digit
	num = num/10
print(sum)'''




# graph = { '5':['3','7'], '3':['2','4'], '7':['8'], '2':[], '4':['8'], '8':[] }
# visited = set()
# def dfs(visited, graph, node):
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)
# print("Following is the Depth-First Search")
# dfs(visited, graph, '5')





























    
        
    

