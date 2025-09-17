'''class Priv_In:
    def __init__(self,abc):
        self.__abc=abc
    def get_abc(self):
        return self.__abc
    def set_abc(self,abc):
        self.__abc=abc
obj=Priv_In(23)
print(obj._Priv_In__abc)
print(obj.get_abc())


class Area:
    def __init__(self,len1,br):
        self.len1=len1
        self.br=br
class Cal_Area_Tri(Area):
    def Tri_area(self):
        area=0.5*self.len1*self.br
        print("Area of Triangle is",area)
obj=Cal_Area_Tri(4,6)
obj.Tri_area()

class Factorial:
    def __init__(self, num):
        self.num = num
    def calculate_factorial(self):
        factorial = 1
        if self.num < 0:
            return "Factorial undefined for negative numbers"
        elif self.num == 0:
            return 1
        else:
            for i in range(1, self.num + 1):
                factorial *= i
            return factorial
number = int(input("Enter a number to find its factorial: "))
factorial_obj = Factorial(number)
result = factorial_obj.calculate_factorial()
print(f"The factorial of {number} is {result}")


class Super:
    def __init__(self,num):
        self.num=num
class Fact(Super):
    def __init__(self):
        super().__init__(int(input("enter a number:")))
    def fact(self):
        f=1
        for i in range(1,self.num+1):
            f=f*i
        print("factorial of",self.num,"is",f)
obj=Fact()
obj.fact()


#function overloading
class Fn_Over:
    def display(self,a):
        print("First function")
    def display(self,a,b):
        print("Second Method")
obj=Fn_Over()
obj.display(3,5)


#function overriding
class Fn_Over:
    def display(self):
        print("super class method")
class sub(Fn_Over):
    def display(self):
        print("sub class method")
obj=sub()
obj.display()


class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
class SmartPhone(Phone):
    def check(self):
        print(self._Phone__price) 
s=SmartPhone(20000, "Apple", 13)
s.check()



class Parent():
    def __init__(self):
        self.value = "Inside Parent"
    def show(self):
        print(self.value)
class Child(Parent):
    def __init__(self):
        self.value = "Inside Child"
    def show(self):
        print(self.value)

obj1 = Parent()
obj2 = Child()
obj1.show()
obj2.show()


class Bank():
    def getRateofInterest(self,Amount):
        self.Amount = Amount
        Rate=(self.Amount*10)/100
        print("10% Rate of Interest is:",Rate)
class SBI(Bank):
    def getRateofInterest(self,Amount):
        self.Amount = Amount
        Rate=(self.Amount*8)/100
        print("8% Rate of Interest is:",Rate)
class ICICI(Bank):
    def getRateofInterest(self,Amount):
        self.Amount = Amount
        Rate=(self.Amount*7)/100
        print("7% Rate of Interest is:",Rate)
class AXIS(Bank):
    def getRateofInterest(self,Amount):
        self.Amount = Amount
        Rate=(self.Amount*9)/100
        print("9% Rate of Interest is:",Rate)
a=SBI()
a.getRateofInterest(int(input("enter a amount:")))
b=ICICI()
b.getRateofInterest(int(input("enter a amount:")))
c=AXIS()
c.getRateofInterest(int(input("enter a amount:")))



class Node():
    def __init__(self,info):
        self.info=info
        self.next=None
class Linklist():
    def __init__(self):
        self.head=None
    def add(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            current_node=head
            head=newNode
            newNode.next=current_node


#multilevel inheritance
class Grandfather:
    def __init__(self):
        self.name="Sujal Sahu"
        self.nickname="Suji"
    def f1(self):
        print("base class method")
class Father(Grandfather):
    def __init__(self):
        self.section="1c"
        super().__init__()
    def f2(self):
        print("first sub class method")
class Child(Father):
    def f3(self):
        print("second sub class method")
class More(Child):
    def f4(self):
        print("third sub class method")
obj=More()
obj.f1()
obj.f2()
obj.f3()
obj.f4()
print(obj.name)
print(obj.nickname)
print(obj.section)



#heirarchial inheritance
class Area:
    def __init__(self,l,b,r):
        self.len=l
        self.br=b
        self.r=r
    def display(self):
        print(self.len)
        print(self.br)
class AreaCircle(Area):
    def __init__(self,a,b,r):
        super().__init__(a,b,r)
    def calarea_circle(self):
        print(3.14*self.r*self.r)
class AreaTriangle(Area):
    def __init__(self,a,b,r):
        super().__init__(a,b,r)
    def calAreaTri(self):
        print(0.5*self.len*self.br)
obj1=AreaCircle(int(input("enter a length:")),int(input("enter a breadth:")),int(input("enter a radius:")))
print("Area of circle is:")
obj1.calarea_circle()
obj2=AreaTriangle(4,6,8)
print("Area of triangle is:")
obj2.calAreaTri()



#multiple inheritance
class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d=Derived()
print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))


class A:
    def tas(self):
        print(" In class A")
class B(A):
    def tas(self):
        print(" In class B")
class C(A):
    def tas(self):
        print("In class C")
class D(B, C):
    pass
r = D()
r.tas()


class A:
    def tas(self):
        print(" In class A")
class B:
    def tas(self):
        print(" In class B")
class C:
    def tas(self):
        print("In class C")
r = A()
r.tas()
r = B()
r.tas()
r = C()
r.tas()



class A:
    def method(self):
        print("A.method() called")
class B(A):
    def method(self):
        print("B.method() called")
b = B()
b.method()
print(B.mro())


#need of static variable
class Student:
    branch="MCA"  #static variable
    def __init__(self,name):
        self.name=name  #instance variable
obj=Student("Suyash Mishra")
print(obj.name)   #accessing of instance variable
print(Student.branch)   #accessing of static variable


class Student:
    college="PSIT"  
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def print_Detail(self):
        print("name=",self.name)
        print("Roll no=",self.roll_no)
        print("college=",Student.college)
obj1=Student("Suyash Mishra",123)
obj1.print_Detail()   
obj2=Student("Vaibhav Mota",205)
obj2.print_Detail()
obj3=Student("Sujal",190)
obj3.print_Detail()



#static method
class A:
    abc="I am good"
    @staticmethod
    def static_f1():
        print(A.abc)
    def instance_f2(self):
        print("Instance Method")
A.static_f1()
B=A()
B.instance_f2()


class Employee:
    counter=1001
    org="TCS"
    tot_emp=0
    def __init__(self,name,department):
        self.id=Employee.counter
        Employee.counter=Employee.counter+1
        self.name=name
        self.department=department
        Employee.tot_emp=Employee.tot_emp+1
    def display(self):
        print("ID =",self.id)
        print("Name =",self.name)
        print("Department =",self.department)
        print("Organization =",Employee.org)
        print("Total Instance =",Employee.tot_emp)
emp1=Employee("Suyash Uncle","IT")
emp1.display()
emp2=Employee("Ritesh","Business")
emp2.display()
emp3=Employee("Suji","Import & Export")
emp3.display()


class Passenger:
    Ticket_id=100
    source="Delhi"
    tot_passenger=0
    def __init__(self,passenger_name,destination):
        self.id=Passenger.Ticket_id
        Passenger.Ticket_id=Passenger.Ticket_id+1
        self.passenger_name=passenger_name
        self.destination=destination
        Passenger.tot_passenger=Passenger.tot_passenger+1
    def display(self):
        print("Ticket ID =",self.Ticket_id)
        print("Passenger Name =",self.passenger_name)
        print("Destination =",self.destination)
        print("Source =",Passenger.source)
        print("Total Instance =",Passenger.tot_passenger)
emp1=Passenger("Suyash Uncle","Mumbai")
emp1.display()
emp2=Passenger("Ritesh","Chennai")
emp2.display()
emp3=Passenger("Suji","pune")
emp3.display()
emp4=Passenger("Vaibhav","Kolkata")
emp4.display()


#lex_auth_012748317267525632347
#Start writing your code here
class Ticket:
    counter=0
    def __init__(self,passenger_name,source,destination):
        self.__passenger_name=passenger_name.lower()
        self.__source=source.lower()
        self.__destination=destination.lower()
        self.__ticket_id=None
    def get_passenger_name(self):
        return self.__passenger_name
    def get_source(self):
        return self.__source
    def get_destination(self):
        return self.__destination
    def get_ticket_id(self):
        return self.__ticket_id
    def validate_source_destination(self):
        if self.__source=="delhi":
            if self.__destination=="mumbai" or self.__destination=="kolkata" or self.__destination=="pune"or self.__destination=="chennai":
                return True
            else:
                return False
        else:
            return False
    def generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter+=1
            if Ticket.counter<10:
                self.__ticket_id=self.__source[0]+self.__destination[0]+str(0)+str(Ticket.counter)
            else:
                self.__ticket_id=self.__source[0]+self.__destination[0]+str(Ticket.counter)
            return self.__ticket_id.upper()
        else:
            self.__ticket_id=None
T1=Ticket("Mohan","Delhi","Mumbai")
T2=Ticket("Ram","Delhi","Pune")
print(T1.generate_ticket())
print(T2.generate_ticket())

a="Suyash mera bhai"
b=[]
for i in a:
    b.append(i)
    b.append(" ")
print(" ".join(b))

s="lvonsjwefjjaftgkll"
a=input()
for i in s:
    if i in a:
        print(a)
        break
    else:
        print("not")


a=[1,4,3,2]
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        a[i]>=a[j]
        k=a[i]
        a[i]=a[j]
        a[j]=k
print(a)


        
class Customer:
    def __init__(self,name,age,phone,address):
        self.name=name
        self.age=age
        self.phone=phone
        self.address=address #Aggregation
    def view_detail(self):
        print("Name=",self.name)
        print("Age=",self.age)
        print("Door no=",self.address.door_no)
        print("Street=",self.address.street)
        print("Area=",self.address.area)
        print("Pin code=",self.address.pin_code)
    def update_detail(self):
        pass
class Address:
    def __init__(self,door_no,street,area,pin_code):
        self.door_no=door_no
        self.street=street
        self.area=area
        self.pin_code=pin_code
    def update_address(self):
        pass
obj_add=Address(100,"b block street","yashoda nagar",209304)
obj_cust=Customer("suji",25,8736884781,obj_add)
obj_cust.view_detail()




class Car:
    def __init__(self,model,wheel,speed,colours):
        self.model=model
        self.wheel=wheel
        self.speed=speed
        self.colours=colours #Aggregation
    def view_detail(self):
        print("Model=",self.model)
        print("Speed=",self.speed)
        print("Color=",self.colours)
        print("Brand=",self.wheel.brand)
        print("Warrenty=",self.wheel.warrenty)
    def update_detail(self):
        pass
class Wheel:
    def __init__(self,brand,warrenty):
        self.brand=brand
        self.warrenty=warrenty
    def update_wheel(self):
        pass
obj_wh=Wheel("Tata","4 year")
obj_cr=Car("XL","400kmh","Black",obj_wh)
obj_cr.view_detail()


count=0
l={1,3,5,100,999,1000}
for n in l:
    if ((n+1)%3==0 or (n-1)%3==0)or count>=10:
        count=count+1
        print("first")
    else:
        print("second")


#Aggregation
class Salary:
    def __init__(self,pay):
        self.pay=pay
    def get_total(self):
        return (self.pay*12)
class Employee:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
        self.obj_salary=Salary(self.pay)
    def annual_salary(self):
        return "Total:" + str(self.obj_salary.get_total()+self.bonus)
obj_emp=Employee(10000,1000)
print(obj_emp.annual_salary())





#Composition
class Book:
    def __init__(self,bookname):
        self.bookname=bookname
    def getDetailBook(self):
        print("Book Name=",self.bookname)
        p1=Page("3","Chaper3 Association")
        p1.getDetailPage()
class Page:
    def __init__(self,pageno,title):
        self.pageno=pageno
        self.title=title
    def getDetailPage(self):
        print("page no.=",self.pageno,"Title=",self.title)

b1=Book("Python")
b1.getDetailBook()



class Trade:
    def __init__(self,obj):
        self.__trade_detail = obj

    def get_trade_detail(self):
        return self.__trade_detail

    def set_trade_detail(self, value):
        self.__trade_detail = value

class TradeDetail:
    def __init__(self):
        self.__trade_id = None
        self.__order_id = None

    def get_trade_id(self):
        return self.__trade_id

    def get_order_id(self):
        return self.__order_id

    def set_trade_id(self, value):
        self.__trade_id = value

    def set_order_id(self, value):
        self.__order_id = value
td=TradeDetail()
t=Trade(td)
print(t.get_trade_detail().get_order_id())


class A:
    def __init__(self,a):
        self.a=a
    def __pow__(self,other):
        return self.a**other.a
obj1=A(6)
obj2=A(5)
print(obj1**obj2)


class A:
    def __init__(self,a):
        self.a=a
    def __gt__(self,other):
        if(self.a>other.a):
            return True
        else:
            return False
obj1=A(int(input()))
obj2=A(int(input()))
if(obj1>obj2):
    print("obj1 is greater than obj2")
else:
    print("obj2 is greater than obj1")





from abc import ABC,abstractmethod
class MyFirstAbstractClass(ABC):
    @abstractmethod
    def MyfirstbstractMethod(self):
        pass
    def NonAbstractMethod(self):
        print("Hello Non Abstract Method")
class Normalclass(MyFirstAbstractClass):
    def MyfirstbstractMethod(self):
        print("this is deffination of abstract method")
obj1=Normalclass()
obj1.MyfirstbstractMethod()
obj1.NonAbstractMethod()




from abc import ABC,abstractmethod
class Area(ABC):
    @abstractmethod
    def area_result(self,x):
        pass
class Area1(Area):
    def area_result(self,x):
        result1=3.14*x*x
        print("Area of circle is :",result1)
class Area2(Area):
    def area_result(self,x):
        result2=x*x
        print("Area of square is :",result2)
obj1=Area1()
obj1.area_result(3)
obj2=Area2()
obj2.area_result(4)



class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

def change_price(mobile_obj):
    mobile_obj.price = 3000
    mobile_obj.brand = "xiomi"

mob1=Mobile(1000, "Apple")
print(mob1.price)
print(mob1.brand)
change_price(mob1)
print (mob1.price)
print (mob1.brand)




class Customer:
    def __init__(self, cust_id, age):
        self.cust_id = cust_id
        self.age = age

c1=Customer(100,20)

def change(c2):
    c2=Customer(100,21)

change(c1)
print(c1.age)
change(c2)
print(c2.cust_id)



class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

mob1=Mobile("Apple", 1000)
mob2=Mobile("Samsung", 2000)
mob3=Mobile("Apple", 3000)
mob4=Mobile("Samsung", 4000)
mob5=Mobile("Apple", 5000)
mob6=Mobile("xiomi", 6000)
mob7=Mobile("realme", 7000)
mob8=Mobile("sujal", 50)

l=[mob1, mob2, mob3, mob4, mob5, mob6, mob7, mob8]

for i in l:
    print (i.brand,i.price)




class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
mob1=Mobile("Apple", 1000)
mob2=Mobile("Samsung", 5000)
mob3=Mobile("Apple", 3000)
mob_dict={
          "m1":mob1,
          "m2":mob2,
          "m3":mob3
          }
for key,value in mob_dict.items():
    if value.price > 3000:
        print (value.brand,value.price)




class Customer:
    def __init__(self, cust_id, cust_name, location):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.location = location

list_of_customers = [Customer(101, 'Mark', 'US'),
                     Customer(102, 'Jane', 'Japan'),
                     Customer(103, 'Kumar', 'India')]

dict_of_customer = {}
for customer in list_of_customers:
    dict_of_customer[customer.location] = customer

print ("Customer name in India is "+dict_of_customer["India"].cust_name)

for key,value in dict_of_customer.items():
    print ("Location: "+key+", Name: "+value.cust_name+", Id: "+(str(value.cust_id)))



class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
obj1=Student("Suyash",100,85)
obj2=Student("Sujal",101,90)
obj3=Student("Ritesh",102,95)
obj4=Student("Tasleem",103,90)
obj5=Student("Vaibhav",104,85)
l=[obj1,obj2,obj3,obj4,obj5]
for i in l:
    if i.marks<90:
        print(i.name,i.roll_no,i.marks)


class Mobile:
    def __init__(self,company,price):
        self.company = company
        self.price = price
mob1=Mobile("ACME", 45.23)
mob2=Mobile("AAPL", 612.78)
mob3=Mobile("IBM", 205.55)
mob4=Mobile("HPQ", 37.20)
mob5=Mobile("FB", 10.75)
create_new_dict={
          "m1":mob1,
          "m2":mob2,
          "m3":mob3,
          "m4":mob4,
          "m5":mob5
          }
for key,value in create_new_dict.items():
    if value.price > 200:
        print (value.company,value.price)






add_3=lambda x,y:x*x*x+y*y*y
print(add_3(int(input()),int(input())))






add_cube=lambda num1,num2:num1**3+num2**3
print(add_cube(2,3))




def myfun1(n):
    return lambda a:a*n
def myfun2(n):
    return lambda a:a*n
mydoubler=myfun1(2)
mytripler=myfun2(3)
print(mydoubler(11))
print(mytripler(11))

               
                                         
                                                                          

x=map(lambda x:x*x,(1,2,3,4,5,6))
print(list(x))




tup=(5,7,22,21,10)
x=map(lambda x:(x+3)*5*(x/5),(tup))
print(set(x))




y=filter(lambda x:x>=3,(1,4,3,4))
print(tuple(y))



from functools import reduce
result=reduce(lambda a,b:a**3*b**3,[23,21,45,95])
print(result)



y=filter(lambda x:(x%2==0),(1,4,9,12,15,21,24,3,4))
print(tuple(y))



l1=[5,8,6,1]
l2=[]
for i in l1:
    l2.append(i**3)
print(l2)




l2=[i**3 for i in [4,5,6,7]]
print(l2)




l1=[1,2,3,4,5,6]
l2=[]
for i in l1:
    if i%2==0:
        l2.append(i)
print(l2)




l1=[1,2,3,4,5,6]
l2=[i for i in l1 if i%2==0]
print(l2)




square_dict=dict()
for num in range(1,9):
    square_dict[num]=num*num
print(square_dict)




d1={i:i*i for i in range(1,11)}
print(d1)'''





f=["Apple","Banana", "Papaya"]
c=["Red","Green","Yellow"]
a={f[i]:c[i] for i in range(0,len(f))}
print(a)



